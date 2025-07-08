# Resume Evaluator - Simple Version

A streamlined Resume Evaluator using pure Python pattern matching without external NLP dependencies.

## Features

- **PDF Text Extraction**: Uses PyPDF2 to extract text from PDF resumes
- **Advanced Keyword Matching**: 100+ technical skills and keywords
- **Smart Scoring Algorithm**: Multi-factor scoring system
- **Actionable Suggestions**: Specific improvement recommendations
- **No Complex Dependencies**: Works without spaCy or other heavy NLP libraries

## Quick Start

### 1. Install Dependencies

```bash
cd simple
pip install -r requirements_simple.txt
```

### 2. Run the Application

```bash
python3 app_simple.py
```

### 3. Access the Web Interface

Open your browser to: `http://localhost:5001`

## Running Tests

```bash
cd simple
python3 test_simple.py
```

## Dependencies

- Flask 2.3.3 - Web framework
- PyPDF2 3.0.1 - PDF text extraction
- Flask-CORS 4.0.0 - Cross-origin support
- Werkzeug 2.3.7 - WSGI utilities
- Requests 2.31.0 - HTTP testing

## Files

- `app_simple.py` - Main application
- `requirements_simple.txt` - Python dependencies
- `setup_simple.py` - Automated setup script
- `test_simple.py` - Functionality tests

## Port Configuration

The application runs on port 5001 to avoid conflicts with macOS AirPlay Receiver (port 5000).
