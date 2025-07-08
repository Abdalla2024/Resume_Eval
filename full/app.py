from flask import Flask, request, jsonify, render_template, send_from_directory
from flask_cors import CORS
import os
import PyPDF2
import spacy
import re
from collections import Counter
from werkzeug.utils import secure_filename
import json
from datetime import datetime

app = Flask(__name__, template_folder='../templates')
CORS(app)

# Configuration
UPLOAD_FOLDER = '../uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load spaCy model for text processing
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Please install spaCy English model: python -m spacy download en_core_web_sm")
    nlp = None

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file"""
    try:
        with open(pdf_path, 'rb') as file:
            pdf_reader = PyPDF2.PdfReader(file)
            text = ""
            for page in pdf_reader.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        return f"Error extracting text from PDF: {str(e)}"

def extract_skills_and_keywords(text):
    """Extract skills and keywords from text"""
    if not nlp:
        return []
    
    doc = nlp(text.lower())
    
    # Common technical skills and keywords
    technical_skills = {
        'python', 'java', 'javascript', 'html', 'css', 'sql', 'react', 'angular', 'vue',
        'nodejs', 'express', 'flask', 'django', 'spring', 'docker', 'kubernetes',
        'aws', 'azure', 'gcp', 'git', 'github', 'ci/cd', 'jenkins', 'mongodb',
        'postgresql', 'mysql', 'redis', 'elasticsearch', 'tensorflow', 'pytorch',
        'machine learning', 'data science', 'artificial intelligence', 'blockchain',
        'microservices', 'agile', 'scrum', 'devops', 'linux', 'windows', 'macos'
    }
    
    # Extract entities and noun phrases
    entities = [ent.text.lower() for ent in doc.ents if ent.label_ in ['ORG', 'PRODUCT', 'SKILL']]
    noun_phrases = [chunk.text.lower() for chunk in doc.noun_chunks if len(chunk.text.split()) <= 3]
    
    # Combine all potential keywords
    all_keywords = set()
    
    # Add technical skills found in text
    words = set(re.findall(r'\b\w+\b', text.lower()))
    for skill in technical_skills:
        if skill in text.lower():
            all_keywords.add(skill)
    
    # Add entities and noun phrases
    all_keywords.update(entities)
    all_keywords.update(noun_phrases)
    
    # Filter out common words
    common_words = {'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'a', 'an'}
    filtered_keywords = [kw for kw in all_keywords if kw not in common_words and len(kw) > 2]
    
    return filtered_keywords

def calculate_match_score(resume_text, job_description):
    """Calculate alignment score between resume and job description"""
    
    # Extract keywords from both texts
    resume_keywords = set(extract_skills_and_keywords(resume_text))
    job_keywords = set(extract_skills_and_keywords(job_description))
    
    # Calculate overlap
    common_keywords = resume_keywords.intersection(job_keywords)
    
    # Calculate scores
    if len(job_keywords) == 0:
        keyword_score = 0
    else:
        keyword_score = len(common_keywords) / len(job_keywords) * 100
    
    # Additional scoring factors
    resume_length_score = min(len(resume_text.split()) / 300, 1) * 10  # Optimal around 300 words
    
    # Calculate overall score
    overall_score = min(keyword_score * 0.8 + resume_length_score * 0.2, 100)
    
    return {
        'overall_score': round(overall_score, 1),
        'keyword_score': round(keyword_score, 1),
        'common_keywords': list(common_keywords),
        'missing_keywords': list(job_keywords - resume_keywords),
        'resume_keywords': list(resume_keywords),
        'job_keywords': list(job_keywords)
    }

def generate_suggestions(analysis_result):
    """Generate improvement suggestions based on analysis"""
    suggestions = []
    
    score = analysis_result['overall_score']
    missing_keywords = analysis_result['missing_keywords']
    
    if score < 30:
        suggestions.append("Your resume has low alignment with the job description. Consider significant revisions.")
    elif score < 60:
        suggestions.append("Your resume has moderate alignment. There's room for improvement.")
    else:
        suggestions.append("Great! Your resume shows good alignment with the job description.")
    
    if missing_keywords:
        top_missing = missing_keywords[:5]  # Top 5 missing keywords
        suggestions.append(f"Consider adding these relevant keywords: {', '.join(top_missing)}")
    
    if len(analysis_result['resume_keywords']) < 10:
        suggestions.append("Your resume might benefit from more specific technical skills and keywords.")
    
    suggestions.append("Tailor your resume to match the job description more closely.")
    suggestions.append("Use action verbs and quantifiable achievements in your experience section.")
    suggestions.append("Ensure your resume is well-formatted and easy to read.")
    
    return suggestions

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/evaluate', methods=['POST'])
def evaluate_resume():
    try:
        # Check if files were uploaded
        if 'resume' not in request.files:
            return jsonify({'error': 'No resume file provided'}), 400
        
        resume_file = request.files['resume']
        job_description = request.form.get('job_description', '')
        
        if resume_file.filename == '':
            return jsonify({'error': 'No resume file selected'}), 400
        
        if not job_description.strip():
            return jsonify({'error': 'Job description is required'}), 400
        
        if not allowed_file(resume_file.filename):
            return jsonify({'error': 'Invalid file type. Please upload a PDF file.'}), 400
        
        # Save uploaded file
        filename = secure_filename(resume_file.filename)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        unique_filename = f"{timestamp}_{filename}"
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], unique_filename)
        resume_file.save(file_path)
        
        # Extract text from PDF
        resume_text = extract_text_from_pdf(file_path)
        
        # Clean up uploaded file
        os.remove(file_path)
        
        if resume_text.startswith("Error"):
            return jsonify({'error': resume_text}), 400
        
        # Analyze resume against job description
        analysis_result = calculate_match_score(resume_text, job_description)
        suggestions = generate_suggestions(analysis_result)
        
        return jsonify({
            'success': True,
            'analysis': analysis_result,
            'suggestions': suggestions,
            'resume_preview': resume_text[:500] + "..." if len(resume_text) > 500 else resume_text
        })
        
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

@app.route('/health')
def health_check():
    return jsonify({'status': 'healthy', 'spacy_loaded': nlp is not None})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 