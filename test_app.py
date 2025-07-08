#!/usr/bin/env python3
"""
Test script for Resume Evaluator
"""
import requests
import json
import os
import sys

def test_health_endpoint():
    """Test the health check endpoint"""
    try:
        response = requests.get('http://localhost:5000/health')
        data = response.json()
        print(f"✓ Health check: {data['status']}")
        print(f"✓ spaCy model loaded: {data['spacy_loaded']}")
        return True
    except Exception as e:
        print(f"❌ Health check failed: {e}")
        return False

def test_text_analysis():
    """Test text analysis functionality"""
    try:
        # Import the app functions to test them directly
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from app import extract_skills_and_keywords, calculate_match_score, generate_suggestions
        
        # Test data
        sample_resume = """
        John Doe
        Software Engineer
        
        Skills: Python, JavaScript, React, Node.js, SQL, Docker, AWS
        Experience: 3 years developing web applications using Flask and React
        Education: Computer Science degree
        """
        
        sample_job_description = """
        We are looking for a Software Engineer with experience in:
        - Python programming
        - React development
        - AWS cloud services
        - Docker containerization
        - SQL databases
        - Node.js backend development
        """
        
        # Test keyword extraction
        resume_keywords = extract_skills_and_keywords(sample_resume)
        job_keywords = extract_skills_and_keywords(sample_job_description)
        
        print(f"✓ Resume keywords extracted: {len(resume_keywords)} keywords")
        print(f"✓ Job keywords extracted: {len(job_keywords)} keywords")
        
        # Test scoring
        analysis = calculate_match_score(sample_resume, sample_job_description)
        print(f"✓ Analysis completed - Overall score: {analysis['overall_score']}%")
        
        # Test suggestions
        suggestions = generate_suggestions(analysis)
        print(f"✓ Generated {len(suggestions)} suggestions")
        
        return True
        
    except Exception as e:
        print(f"❌ Text analysis test failed: {e}")
        return False

def main():
    """Main test function"""
    print("🧪 Testing Resume Evaluator Application...")
    
    # Test 1: Health endpoint
    print("\n1. Testing health endpoint...")
    if not test_health_endpoint():
        print("❌ Please make sure the application is running (python app.py)")
        return
    
    # Test 2: Text analysis
    print("\n2. Testing text analysis...")
    if not test_text_analysis():
        return
    
    print("\n✅ All tests passed! The application is working correctly.")
    print("\nTo use the application:")
    print("1. Open your browser and go to http://localhost:5000")
    print("2. Upload a PDF resume")
    print("3. Paste a job description")
    print("4. Click 'Evaluate Resume' to get your analysis")

if __name__ == "__main__":
    main() 