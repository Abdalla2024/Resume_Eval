# Resume Evaluator - Full Version

Advanced Resume Evaluator with spaCy integration for sophisticated NLP analysis.

## Features

- **Advanced NLP Processing**: Uses spaCy for named entity recognition
- **Noun Phrase Extraction**: Identifies complex technical terms and concepts
- **Enhanced Text Analysis**: More sophisticated linguistic processing
- **PDF Text Extraction**: Uses PyPDF2 to extract text from PDF resumes
- **Smart Scoring Algorithm**: Multi-factor scoring system
- **Actionable Suggestions**: Specific improvement recommendations

## Quick Start

### 1. Install Dependencies

```bash
cd full
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 2. Run the Application

```bash
python3 app.py
```

### 3. Access the Web Interface

Open your browser to: `http://localhost:5001`

## Running Tests

```bash
cd full
python3 test_app.py
```

## Dependencies

- Flask 2.3.3 - Web framework
- PyPDF2 3.0.1 - PDF text extraction
- Flask-CORS 4.0.0 - Cross-origin support
- Werkzeug 2.3.7 - WSGI utilities
- Requests 2.31.0 - HTTP testing
- spaCy 3.6.1 - Advanced NLP processing

## Files

- `app.py` - Main application with spaCy integration
- `requirements.txt` - Python dependencies including spaCy
- `setup.py` - Automated setup script with spaCy model download
- `test_app.py` - Functionality tests

## Setup Notes

The full version requires spaCy compilation which may require additional setup:

- **macOS**: May need Xcode command line tools
- **Linux**: May need build-essential package
- **Windows**: May need Visual Studio Build Tools

For easier installation, consider using the simple version instead.

## Port Configuration

The application runs on port 5001 to avoid conflicts with macOS AirPlay Receiver (port 5000).
