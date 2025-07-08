from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import os
import PyPDF2
import re
from collections import Counter
from werkzeug.utils import secure_filename
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Configuration
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Create upload directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

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
    """Extract skills and keywords from text using simple pattern matching"""
    text = text.lower()
    
    # Extended list of technical skills and keywords
    technical_skills = {
        # Programming Languages
        'python', 'java', 'javascript', 'typescript', 'c++', 'c#', 'c', 'php', 'ruby', 'go', 'rust',
        'swift', 'kotlin', 'scala', 'r', 'matlab', 'perl', 'shell', 'bash', 'powershell',
        
        # Web Technologies
        'html', 'css', 'html5', 'css3', 'sass', 'scss', 'less', 'bootstrap', 'tailwind',
        'react', 'angular', 'vue', 'vue.js', 'react.js', 'angular.js', 'svelte', 'ember',
        'jquery', 'ajax', 'json', 'xml', 'rest', 'api', 'graphql', 'websocket',
        
        # Backend & Frameworks
        'nodejs', 'node.js', 'express', 'flask', 'django', 'fastapi', 'spring', 'spring boot',
        'laravel', 'symfony', 'rails', 'ruby on rails', 'asp.net', '.net', 'core',
        
        # Databases
        'sql', 'mysql', 'postgresql', 'postgres', 'sqlite', 'mongodb', 'redis', 'elasticsearch',
        'oracle', 'sql server', 'mariadb', 'dynamodb', 'cassandra', 'couchdb', 'neo4j',
        
        # Cloud & DevOps
        'aws', 'azure', 'gcp', 'google cloud', 'docker', 'kubernetes', 'jenkins', 'gitlab',
        'github', 'bitbucket', 'ci/cd', 'devops', 'terraform', 'ansible', 'puppet', 'chef',
        'vagrant', 'helm', 'istio', 'prometheus', 'grafana', 'elk', 'nginx', 'apache',
        
        # Data Science & ML
        'machine learning', 'deep learning', 'artificial intelligence', 'data science',
        'pandas', 'numpy', 'scikit-learn', 'tensorflow', 'pytorch', 'keras', 'opencv',
        'matplotlib', 'seaborn', 'plotly', 'jupyter', 'tableau', 'power bi', 'spark',
        'hadoop', 'kafka', 'airflow', 'mlflow', 'kubeflow',
        
        # Tools & Technologies
        'git', 'github', 'gitlab', 'jira', 'confluence', 'slack', 'teams', 'zoom',
        'visual studio', 'vscode', 'intellij', 'eclipse', 'sublime', 'vim', 'emacs',
        'postman', 'swagger', 'figma', 'sketch', 'adobe', 'photoshop', 'illustrator',
        
        # Methodologies
        'agile', 'scrum', 'kanban', 'lean', 'waterfall', 'tdd', 'bdd', 'pair programming',
        'code review', 'unit testing', 'integration testing', 'automation testing',
        'continuous integration', 'continuous deployment', 'microservices', 'serverless',
        
        # Operating Systems
        'linux', 'ubuntu', 'centos', 'redhat', 'debian', 'windows', 'macos', 'unix',
        
        # Mobile Development
        'android', 'ios', 'flutter', 'react native', 'xamarin', 'ionic', 'cordova',
        
        # Blockchain & Crypto
        'blockchain', 'ethereum', 'bitcoin', 'solidity', 'web3', 'smart contracts', 'defi',
        
        # Security
        'cybersecurity', 'penetration testing', 'vulnerability assessment', 'owasp',
        'ssl', 'tls', 'encryption', 'authentication', 'authorization', 'oauth', 'jwt',
        
        # Soft Skills
        'leadership', 'communication', 'teamwork', 'project management', 'problem solving',
        'analytical thinking', 'creative thinking', 'time management', 'collaboration'
    }
    
    # Find all words in the text
    words = re.findall(r'\b\w+\b', text)
    
    # Multi-word skills
    multi_word_skills = [
        'machine learning', 'deep learning', 'artificial intelligence', 'data science',
        'computer science', 'software engineering', 'web development', 'mobile development',
        'full stack', 'front end', 'back end', 'database design', 'system design',
        'project management', 'agile methodology', 'scrum master', 'product owner',
        'business analyst', 'data analyst', 'quality assurance', 'user experience',
        'user interface', 'responsive design', 'cross platform', 'real time',
        'cloud computing', 'edge computing', 'big data', 'data mining', 'data visualization',
        'version control', 'code review', 'unit testing', 'integration testing',
        'performance optimization', 'scalability', 'load balancing', 'fault tolerance'
    ]
    
    found_keywords = set()
    
    # Check for single-word skills
    for word in words:
        if word.lower() in technical_skills:
            found_keywords.add(word.lower())
    
    # Check for multi-word skills
    for skill in multi_word_skills:
        if skill in text:
            found_keywords.add(skill)
    
    # Also extract common patterns
    # Email domains (companies)
    email_domains = re.findall(r'@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', text)
    for domain in email_domains:
        # Extract company name from domain
        company = domain.split('.')[0]
        if len(company) > 2:
            found_keywords.add(company.lower())
    
    # Years of experience patterns
    experience_patterns = re.findall(r'(\d+)\s*(?:years?|yrs?)\s*(?:of\s*)?(?:experience|exp)', text)
    for years in experience_patterns:
        if int(years) > 0:
            found_keywords.add(f"{years} years experience")
    
    # Degree patterns
    degree_patterns = re.findall(r'\b(bachelor|master|phd|doctorate|associate|diploma)\b', text)
    found_keywords.update(degree_patterns)
    
    # Programming language version patterns
    version_patterns = re.findall(r'\b(python\s*[23]\.?\d*|java\s*\d+|c\+\+\d+|\.net\s*\d+)\b', text)
    found_keywords.update([v.lower() for v in version_patterns])
    
    return list(found_keywords)

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
    resume_length = len(resume_text.split())
    resume_length_score = min(resume_length / 300, 1) * 10  # Optimal around 300 words
    
    # Bonus for having many relevant keywords
    keyword_density = len(common_keywords) / max(len(resume_keywords), 1)
    keyword_density_score = min(keyword_density * 100, 20)
    
    # Calculate overall score
    overall_score = min(keyword_score * 0.7 + resume_length_score * 0.2 + keyword_density_score * 0.1, 100)
    
    return {
        'overall_score': round(overall_score, 1),
        'keyword_score': round(keyword_score, 1),
        'keyword_density_score': round(keyword_density_score, 1),
        'resume_length_score': round(resume_length_score, 1),
        'common_keywords': list(common_keywords),
        'missing_keywords': list(job_keywords - resume_keywords)[:10],  # Top 10 missing
        'resume_keywords': list(resume_keywords),
        'job_keywords': list(job_keywords),
        'stats': {
            'resume_word_count': resume_length,
            'resume_keyword_count': len(resume_keywords),
            'job_keyword_count': len(job_keywords),
            'common_keyword_count': len(common_keywords)
        }
    }

def generate_suggestions(analysis_result):
    """Generate improvement suggestions based on analysis"""
    suggestions = []
    
    score = analysis_result['overall_score']
    missing_keywords = analysis_result['missing_keywords']
    stats = analysis_result['stats']
    
    # Overall score feedback
    if score < 30:
        suggestions.append("🔴 Your resume has low alignment with the job description. Consider significant revisions to better match the requirements.")
    elif score < 50:
        suggestions.append("🟡 Your resume has moderate alignment with the job description. There's good room for improvement.")
    elif score < 70:
        suggestions.append("🟢 Your resume shows good alignment with the job description. Small improvements could make it even stronger.")
    else:
        suggestions.append("🟢 Excellent! Your resume shows strong alignment with the job description.")
    
    # Missing keywords suggestions
    if missing_keywords:
        top_missing = missing_keywords[:5]
        suggestions.append(f"💡 Consider adding these key skills/terms: {', '.join(top_missing)}")
    
    # Resume length suggestions
    word_count = stats['resume_word_count']
    if word_count < 200:
        suggestions.append("📝 Your resume might be too brief. Consider adding more details about your experience and achievements.")
    elif word_count > 600:
        suggestions.append("✂️ Your resume might be too long. Consider condensing to the most relevant information.")
    
    # Keyword density suggestions
    if stats['resume_keyword_count'] < 5:
        suggestions.append("🔍 Your resume has few technical keywords. Add more specific skills and technologies you've worked with.")
    elif stats['resume_keyword_count'] > 50:
        suggestions.append("📊 Your resume has many keywords. Ensure they're all relevant and not just keyword stuffing.")
    
    # General improvement suggestions
    suggestions.extend([
        "🎯 Tailor your resume to match the specific job requirements more closely.",
        "📈 Use action verbs and quantifiable achievements (e.g., 'Improved performance by 25%').",
        "🔧 Include specific technologies, tools, and methodologies mentioned in the job description.",
        "💼 Highlight relevant work experience and projects that align with the role.",
        "🎓 Ensure your educational background and certifications are clearly mentioned if relevant.",
        "📋 Use a clean, professional format that's easy to read and ATS-friendly."
    ])
    
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
    return jsonify({
        'status': 'healthy',
        'version': '1.0.0',
        'features': ['PDF parsing', 'keyword extraction', 'scoring algorithm']
    })

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001) 