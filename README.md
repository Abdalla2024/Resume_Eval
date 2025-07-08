# Resume Evaluator

A comprehensive Resume Evaluator application that analyzes PDF resumes, compares them against job descriptions, and provides detailed scores and improvement suggestions.

## 🚀 Quick Start

Choose between two versions:

### 📦 Simple Version (Recommended)

- **No complex dependencies** - easy to install and run
- **Fast setup** - works out of the box
- **Advanced pattern matching** - 100+ technical skills

```bash
cd simple
pip install -r requirements_simple.txt
python3 app_simple.py
```

### 🧠 Full Version (Advanced)

- **spaCy integration** - sophisticated NLP analysis
- **Enhanced processing** - named entity recognition
- **More complex setup** - requires compilation

```bash
cd full
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python3 app.py
```

## 📁 Project Structure

```
Resume_Eval/
├── README.md                 # This file
├── .gitignore               # Git ignore rules
├── simple/                  # Simple version (recommended)
│   ├── README.md           # Simple version documentation
│   ├── app_simple.py       # Main application
│   ├── requirements_simple.txt  # Dependencies
│   ├── setup_simple.py     # Automated setup
│   └── test_simple.py      # Functionality tests
├── full/                    # Full version (advanced)
│   ├── README.md           # Full version documentation
│   ├── app.py              # Main application with spaCy
│   ├── requirements.txt    # Dependencies including spaCy
│   ├── setup.py           # Automated setup with spaCy
│   └── test_app.py        # Functionality tests
├── templates/              # Shared web interface
│   └── index.html         # Modern responsive frontend
├── uploads/               # PDF upload directory
└── venv/                 # Virtual environment
```

## ✨ Key Features

### 📄 PDF Processing

- Extracts text from PDF resumes using PyPDF2
- Handles multiple page documents
- Robust error handling for corrupted files

### 🔍 Advanced Analysis

- **100+ Technical Skills**: Programming languages, frameworks, tools
- **Multi-word Phrase Detection**: "machine learning", "full stack", etc.
- **Experience Extraction**: Years of experience patterns
- **Education Detection**: Degree and certification recognition
- **Company Information**: Email domain analysis

### 📊 Intelligent Scoring

- **Keyword Matching**: Direct alignment with job requirements
- **Resume Length Optimization**: Ideal length scoring
- **Keyword Density**: Relevance factor calculation
- **Overall Score**: Weighted combination of all factors

### 💡 Actionable Suggestions

- **Missing Keywords**: Specific skills to add
- **Content Improvement**: Length and detail recommendations
- **Structure Enhancement**: Organization suggestions
- **Industry Alignment**: Sector-specific advice

### 🎨 Modern Web Interface

- **Drag & Drop Upload**: Intuitive file handling
- **Real-time Analysis**: Instant feedback
- **Responsive Design**: Mobile and desktop optimized
- **Beautiful UI**: Professional gradient design
- **Interactive Results**: Color-coded keyword highlighting

## 🛠️ Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Virtual environment (recommended)

### Virtual Environment Setup

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate  # On macOS/Linux
# or
venv\Scripts\activate     # On Windows
```

### Choose Your Version

#### Simple Version (Recommended)

```bash
cd simple
pip install -r requirements_simple.txt
python3 app_simple.py
```

#### Full Version (Advanced)

```bash
cd full
pip install -r requirements.txt
python -m spacy download en_core_web_sm
python3 app.py
```

## 🌐 Usage

1. **Start the application** using the commands above
2. **Open your browser** to `http://localhost:5001`
3. **Upload a PDF resume** using the drag-and-drop interface
4. **Enter a job description** in the text area
5. **Click "Evaluate Resume"** to get instant analysis
6. **Review the results** including scores and suggestions

## 🧪 Testing

### Simple Version

```bash
cd simple
python3 test_simple.py
```

### Full Version

```bash
cd full
python3 test_app.py
```

## 📡 API Endpoints

- **GET** `/` - Web interface
- **POST** `/evaluate` - Resume evaluation API
- **GET** `/health` - Health check endpoint

## 🔧 Configuration

- **Port**: 5001 (avoids macOS AirPlay conflicts)
- **Upload Size**: 16MB maximum
- **Supported Formats**: PDF only
- **Upload Directory**: `uploads/` (auto-created)

## 🐛 Troubleshooting

### Common Issues

1. **Port 5000 already in use**

   - The app uses port 5001 by default
   - On macOS, disable AirPlay Receiver in System Preferences

2. **spaCy installation fails (Full Version)**

   - Use Simple Version instead
   - Ensure you have build tools installed
   - Try using conda instead of pip

3. **Virtual environment issues**

   - Ensure virtual environment is activated
   - Use `which python` to verify correct Python path

4. **PDF processing errors**
   - Ensure PDF is not password protected
   - Check file size (16MB limit)
   - Verify PDF is text-based, not image-based

## 🔄 Version Comparison

| Feature                | Simple Version   | Full Version   |
| ---------------------- | ---------------- | -------------- |
| **Dependencies**       | Minimal          | Heavy (spaCy)  |
| **Setup Time**         | < 1 minute       | 5-10 minutes   |
| **Keyword Extraction** | Pattern matching | NLP + Patterns |
| **Entity Recognition** | Basic            | Advanced       |
| **Performance**        | Fast             | Moderate       |
| **Accuracy**           | Good             | Excellent      |
| **Installation**       | Easy             | Complex        |

## 📊 Technical Details

### Simple Version

- **Pure Python**: No external NLP dependencies
- **Pattern Matching**: Regular expressions and string operations
- **Fast Performance**: Instant processing
- **Reliability**: Consistent results across platforms

### Full Version

- **spaCy Integration**: Advanced natural language processing
- **Named Entity Recognition**: Identifies organizations, skills, etc.
- **Noun Phrase Extraction**: Complex technical terms
- **Linguistic Analysis**: Part-of-speech tagging, dependency parsing

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests to ensure functionality
5. Submit a pull request

## 📝 License

This project is available for educational and personal use.

## 🎯 Future Enhancements

- [ ] Support for Word documents
- [ ] Batch processing capabilities
- [ ] Resume template suggestions
- [ ] Industry-specific analysis
- [ ] Integration with job boards
- [ ] Machine learning model training
- [ ] Real-time collaborative editing
- [ ] Export results to PDF/Excel

---

**Ready to analyze resumes?** Choose your version and get started! 🚀
