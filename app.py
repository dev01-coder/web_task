from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
app.config['JSON_SORT_KEYS'] = False

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Sample projects data - Updated with Ozair's projects
PROJECTS = [
    {
        'id': 1,
        'title': 'AI Medical Coding Assistant',
        'description': 'Developed an AI Medical Coding Assistant using LLM to predict ICD, CPT, and Modifier codes with RAG and OCR for processing medical documents',
        'tech': ['Python', 'Flask', 'Langchain', 'MySQL', 'Docker', 'Azure'],
        'image': 'https://loremflickr.com/600/400/healthcare'
    },
    {
        'id': 2,
        'title': 'AI-Powered HCFA OCR',
        'description': 'Web application to automate data extraction from HCFA forms using OCR technology, extracting billing details and eliminating manual data entry',
        'tech': ['Python', 'Gemini', 'Flask', 'Google Vision', 'Azure'],
        'image': 'https://loremflickr.com/600/400/ocr'
    },
    {
        'id': 3,
        'title': 'AI Call Quality Auditor',
        'description': 'System for transcribing speech to text and evaluating calls for grammar, tone, and communication standards using LLMs',
        'tech': ['Python', 'Gemini', 'Flask', 'Whisper', 'Azure'],
        'image': 'https://loremflickr.com/600/400/audio'
    },
    {
        'id': 4,
        'title': 'Claim Denial Prediction System',
        'description': 'Machine learning system to forecast acceptance or rejection of claims based on 837 data using Random Forest, Neural Networks, and Decision Trees',
        'tech': ['Python', 'Gemini', 'Flask', 'Google Vision', 'Azure', 'ML'],
        'image': 'https://loremflickr.com/600/400/machine,learning'
    }
]

# Skills data - Updated with Ozair's skills
SKILLS = [
    {'name': 'Python', 'level': 95},
    {'name': 'SQL', 'level': 90},
    {'name': 'Large Language Models (LLM)', 'level': 92},
    {'name': 'Flask/FastAPI', 'level': 88},
    {'name': 'Machine Learning', 'level': 85},
    {'name': 'OCR & Computer Vision', 'level': 87},
    {'name': 'RAG & Prompt Engineering', 'level': 90},
    {'name': 'Azure Cloud', 'level': 85},
    {'name': 'Git & DevOps', 'level': 88},
    {'name': 'NLP & Classification', 'level': 86}
]

# Blog posts data - Updated with AI/ML topics
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Getting Started with Large Language Models',
        'author': 'Ozair Ilyas',
        'date': 'Jan 20, 2026',
        'excerpt': 'Learn the fundamentals of LLMs, RAG, and how to integrate them into your applications.',
        'content': 'Large Language Models have revolutionized AI development. In this comprehensive guide, we explore LLM basics, Retrieval-Augmented Generation (RAG), prompt engineering, and practical integration patterns...',
        'image': 'https://loremflickr.com/600/400/ai'
    },
    {
        'id': 2,
        'title': 'Building Healthcare AI Solutions',
        'author': 'Ozair Ilyas',
        'date': 'Jan 18, 2026',
        'excerpt': 'Insights into developing AI solutions for medical coding, claims processing, and healthcare automation.',
        'content': 'Healthcare AI presents unique challenges and opportunities. This post covers medical data handling, HIPAA considerations, and building robust healthcare AI systems using Python and cloud services...',
        'image': 'https://loremflickr.com/600/400/health'
    },
    {
        'id': 3,
        'title': 'OCR and Computer Vision for Document Processing',
        'author': 'Ozair Ilyas',
        'date': 'Jan 15, 2026',
        'excerpt': 'Mastering document extraction and data recognition using OCR and Google Vision API.',
        'content': 'Automating document processing is crucial for many industries. Learn how to use Google Vision, OpenCV, and modern OCR techniques to extract and validate data from medical forms, receipts, and documents...',
        'image': 'https://loremflickr.com/600/400/document'
    },
    {
        'id': 4,
        'title': 'Machine Learning for Predictive Analytics',
        'author': 'Ozair Ilyas',
        'date': 'Jan 12, 2026',
        'excerpt': 'Using Random Forest, Neural Networks, and Decision Trees for claims prediction and business intelligence.',
        'content': 'Predictive analytics can significantly impact business outcomes. Explore machine learning algorithms, feature engineering, model evaluation, and deployment strategies for production systems...',
        'image': 'https://loremflickr.com/600/400/data'
    }
]

# Testimonials data
TESTIMONIALS = []

# Services data - Updated with AI services
SERVICES = [
    {
        'id': 1,
        'title': 'AI & Machine Learning',
        'description': 'Develop intelligent systems using LLMs, RAG, classification, and predictive analytics',
        'icon': '<i class="fas fa-brain"></i>'
    },
    {
        'id': 2,
        'title': 'Healthcare AI Solutions',
        'description': 'Medical coding assistance, claim prediction, and healthcare automation using AI',
        'icon': '<i class="fas fa-hospital"></i>'
    },
    {
        'id': 3,
        'title': 'Document Processing & OCR',
        'description': 'Automated document extraction, data recognition, and processing using OCR and Vision APIs',
        'icon': '<i class="fas fa-file-pdf"></i>'
    },
    {
        'id': 4,
        'title': 'API Development',
        'description': 'RESTful and GraphQL API design using Python Flask, FastAPI with Azure cloud integration',
        'icon': '<i class="fas fa-cog"></i>'
    },
    {
        'id': 5,
        'title': 'Cloud Deployment',
        'description': 'Deploy AI/ML applications to Azure, Google Cloud, and optimize for production',
        'icon': '<i class="fas fa-cloud"></i>'
    },
    {
        'id': 6,
        'title': 'Data Analytics & Insights',
        'description': 'Extract actionable insights from healthcare and business data using ML algorithms',
        'icon': '<i class="fas fa-chart-bar"></i>'
    }
]

# Store messages from contact form
MESSAGES = []

@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('favicon.ico') if os.path.exists(os.path.join(app.static_folder, 'favicon.ico')) else ('', 204)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about/')
def about():
    return render_template('about.html', skills=SKILLS)

@app.route('/projects/')
def projects():
    return render_template('projects.html', projects=PROJECTS)

@app.route('/project/<int:project_id>/')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if project is None:
        return render_template('404.html'), 404
    return render_template('project_detail.html', project=project)

@app.route('/services/')
def services():
    return render_template('services.html', services=SERVICES)

@app.route('/blog/')
def blog():
    return render_template('blog.html', posts=BLOG_POSTS)

@app.route('/blog/<int:post_id>/')
def blog_detail(post_id):
    post = next((p for p in BLOG_POSTS if p['id'] == post_id), None)
    if post is None:
        return render_template('404.html'), 404
    return render_template('blog_detail.html', post=post)

@app.route('/contact/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        try:
            data = request.get_json()
            
            # Validate required fields
            if not data or not data.get('name') or not data.get('email') or not data.get('message'):
                return jsonify({'status': 'error', 'message': 'Missing required fields'}), 400
            
            # Validate email format
            if '@' not in data.get('email', ''):
                return jsonify({'status': 'error', 'message': 'Invalid email format'}), 400
            
            message = {
                'name': data.get('name'),
                'email': data.get('email'),
                'message': data.get('message'),
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            MESSAGES.append(message)
            logger.info(f"New contact message from {data.get('name')} ({data.get('email')})")
            return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
        except Exception as e:
            logger.error(f"Error processing contact form: {str(e)}")
            return jsonify({'status': 'error', 'message': 'Server error'}), 500
    return render_template('contact.html')

@app.route('/api/messages')
def get_messages():
    return jsonify(MESSAGES)

@app.route('/api/projects')
def api_projects():
    return jsonify(PROJECTS)

@app.route('/api/blog')
def api_blog():
    return jsonify(BLOG_POSTS)

@app.route('/download-cv')
def download_cv():
    return jsonify({'status': 'success', 'message': 'CV download link prepared', 'link': '#'})

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    logger.error(f"Server error: {str(error)}")
    return render_template('404.html'), 500

if __name__ == '__main__':
    # Production: Use environment variable to set debug mode
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=debug_mode, port=port, host='0.0.0.0')
