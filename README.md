# Resume Evaluator

A web application that analyzes how well your resume matches a job description and provides suggestions for improvement.

## Features

- **PDF Resume Upload**: Upload your resume in PDF format
- **Job Description Analysis**: Paste any job description for comparison
- **Intelligent Scoring**: Get an overall match score based on keyword alignment
- **Detailed Analysis**: See which keywords match and which are missing
- **Improvement Suggestions**: Get actionable recommendations to improve your resume
- **Modern UI**: Clean, responsive design that works on all devices

## How It Works

1. **Upload** your resume (PDF format)
2. **Paste** the job description you're targeting
3. **Get** instant analysis including:
   - Overall match score (0-100%)
   - Keyword alignment analysis
   - Missing keywords from your resume
   - Specific improvement suggestions

## Quick Start

### ✅ Working Version (Recommended)

```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
python3 setup_simple.py

# Run the application
python3 app_simple.py
```

### Alternative: Manual Setup

```bash
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements_simple.txt

# Run the application
python3 app_simple.py
```

## Usage

1. Open your browser and go to `http://localhost:5001`
2. Upload your resume (PDF format)
3. Paste the job description in the text area
4. Click "Evaluate Resume"
5. Review your results and suggestions

**Note**: Using port 5001 because port 5000 is often occupied by macOS AirPlay service.

## Technical Details

### Backend

- **Flask**: Web framework
- **Pattern Matching**: Advanced keyword extraction using regex and predefined skill lists
- **PyPDF2**: PDF text extraction
- **Flask-CORS**: Cross-origin resource sharing support

**Note**: Currently using a simplified version without spaCy to avoid compilation issues on macOS. The pattern-matching approach still provides excellent keyword extraction and analysis.

### Frontend

- **HTML5/CSS3**: Modern, responsive design
- **JavaScript**: Interactive UI and API communication
- **No external libraries**: Pure vanilla JavaScript

### Analysis Algorithm

The application uses a sophisticated scoring system that:

- Extracts keywords and skills from both resume and job description
- Matches technical skills, tools, and relevant terminology
- Calculates alignment percentage based on keyword overlap
- Provides weighted scoring for different factors
- Generates contextual suggestions based on the analysis

## File Structure

```
Resume_Eval/
├── app_simple.py          # Main Flask application (working version)
├── requirements_simple.txt # Python dependencies (simplified)
├── setup_simple.py       # Automatic setup script
├── templates/
│   └── index.html        # Frontend template
├── uploads/              # Temporary file storage (auto-created)
├── README.md             # This file
├── app.py                # Full version with spaCy (needs setup)
├── requirements.txt      # Full dependencies (includes spaCy)
└── setup.py              # Setup for full version
```

## Requirements

- Python 3.7+
- 50MB+ available disk space
- Internet connection (for initial setup)

## Features in Detail

### Smart Keyword Extraction

- Identifies technical skills, programming languages, frameworks
- Recognizes industry-standard tools and methodologies
- Extracts relevant entities and noun phrases
- Filters out common words and irrelevant terms

### Comprehensive Scoring

- **Keyword Match Score**: Percentage of job requirements found in resume
- **Overall Score**: Weighted combination of multiple factors
- **Missing Keywords**: Specific terms to add to your resume
- **Matching Keywords**: Skills already well-represented

### Actionable Suggestions

- Targeted recommendations based on your specific score
- Keyword suggestions from the job description
- General resume improvement tips
- Industry best practices

## Troubleshooting

### Common Issues

**"spaCy model not found"**

```bash
python -m spacy download en_core_web_sm
```

**"Permission denied" when installing**

```bash
pip install --user -r requirements.txt
```

**"Port already in use"**

- Change the port in `app.py` (line 175): `app.run(debug=True, host='0.0.0.0', port=5001)`

### System Requirements

- **macOS**: Tested on macOS 10.14+
- **Windows**: Tested on Windows 10+
- **Linux**: Tested on Ubuntu 18.04+

## Security Notes

- Files are temporarily stored and automatically deleted after processing
- No data is permanently stored or transmitted to external servers
- Application runs locally on your machine

## Contributing

Feel free to submit issues and enhancement requests!

## License

This project is open source and available under the [MIT License](LICENSE).

---

**Made with ❤️ for job seekers everywhere**
