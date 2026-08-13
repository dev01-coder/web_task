from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime
import logging

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'your-secret-key-change-in-production')
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.context_processor
def inject_year():
    return {'now': datetime.now()}

# Sample projects data - Updated with Ozair Ilyas's projects
PROJECTS = [
    {
        'id': 1,
        'title': 'Resume Analyzer AI',
        'description': 'AI-powered resume analysis tool using Groq\'s LLM API (Llama 3.3 70B). Provides ATS match scoring, keyword gap analysis, skill gap prioritization, and actionable improvement tips.',
        'tech': ['Python', 'FastAPI', 'Streamlit', 'Groq', 'SQLite', 'Plotly'],
        'image': 'https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=800&h=500&fit=crop',
        'github_url': 'https://github.com/dev01-coder/Resume-Analyzer-AI',
        'live_url': '',
        'category': 'ai,ml',
        'highlights': [
            'LLM-powered ATS scoring with Llama 3.3 70B via Groq API',
            'Real-time keyword gap analysis and skill prioritization',
            'PDF and DOCX resume parsing with structured output',
            'Analytics dashboard with score trends and history tracking',
            'Full REST API with SQLite persistence and export capabilities'
        ]
    },
    {
        'id': 2,
        'title': 'MediAssist: Healthcare RAG Chatbot',
        'description': 'Production-ready healthcare RAG chatbot combining ChromaDB vector search with BM25 keyword matching across 27,000+ medical documents from NIH\'s MedQuAD dataset. Supports 4 LLM providers with real-time SSE streaming.',
        'tech': ['Python', 'FastAPI', 'React', 'ChromaDB', 'RAG', 'Groq', 'Gemini', 'Tailwind CSS'],
        'image': 'https://raw.githubusercontent.com/dev01-coder/Healthcare-Chatbot/main/screenshot.png',
        'github_url': 'https://github.com/dev01-coder/Healthcare-Chatbot',
        'live_url': '',
        'category': 'ai,healthcare',
        'highlights': [
            'Hybrid retrieval: ChromaDB vector search + BM25 keyword matching with Reciprocal Rank Fusion',
            '27,000+ medical documents from NIH MedQuAD dataset indexed and searchable',
            '4 LLM providers: Groq (free), Gemini, Ollama (local), Anthropic with SSE streaming',
            'Emergency detection for 7 life-threatening categories with instant response',
            'React + Tailwind UI with source citations, medical disclaimers, and rate limiting'
        ]
    },
    {
        'id': 3,
        'title': 'AI Invoice Processor',
        'description': 'Full-stack AI invoice processing system with OCR extraction, NLP-based field parsing, ML classification, and anomaly detection.',
        'tech': ['Python', 'FastAPI', 'Streamlit', 'Tesseract', 'scikit-learn', 'Docker'],
        'image': 'https://images.unsplash.com/photo-1554224155-6726b3ff858f?w=800&h=500&fit=crop',
        'github_url': 'https://github.com/dev01-coder/ai-invoice-processor',
        'live_url': '',
        'category': 'ai,ml',
        'highlights': [
            'Tesseract OCR for PDF and image text extraction',
            'NLP-based field parsing with fallback vendor extraction',
            'TF-IDF + Random Forest invoice classification pipeline',
            'Isolation Forest anomaly detection for suspicious invoices',
            'Docker-ready deployment with async SQLAlchemy database'
        ]
    },
    {
        'id': 4,
        'title': 'ArticleBot: Article Research Tool',
        'description': 'Intelligent document analysis and Q&A application using LLMs and vector embeddings. Provide any article URL, ask natural language questions, and get accurate answers with source citations.',
        'tech': ['Python', 'LangChain', 'OpenAI', 'FAISS', 'Streamlit', 'Selenium'],
        'image': 'https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800&h=500&fit=crop',
        'github_url': 'https://github.com/dev01-coder/article-bot',
        'live_url': '',
        'category': 'ai,nlp',
        'highlights': [
            'Selenium-based web scraping for dynamic article content',
            'OpenAI embeddings with FAISS vector similarity search',
            'LangChain orchestration for intelligent Q&A workflows',
            'Source attribution with citations for every answer',
            'Persistent vector storage to avoid re-processing costs'
        ]
    },
    {
        'id': 5,
        'title': 'AI-Powered HCFA OCR',
        'description': 'Web application to automate data extraction from HCFA forms using OCR technology, extracting billing details and eliminating manual data entry.',
        'tech': ['Python', 'Gemini', 'Flask', 'Google Vision', 'Azure'],
        'image': 'https://images.unsplash.com/photo-1576091160399-112ba8d25d1d?w=800&h=500&fit=crop',
        'github_url': 'https://github.com/dev01-coder',
        'live_url': '',
        'category': 'ai,healthcare',
        'highlights': [
            'Google Vision API for high-accuracy OCR extraction',
            'Automated billing field parsing from HCFA forms',
            'Eliminates manual data entry with 95%+ accuracy',
            'Cloud deployment on Azure for scalability',
            'Real-world healthcare billing automation'
        ]
    },
    {
        'id': 6,
        'title': 'AI Medical Coding Assistant',
        'description': 'LLM-powered system for predicting ICD, CPT, and Modifier codes from medical records using RAG and OCR for processing medical documents.',
        'tech': ['Python', 'Flask', 'Langchain', 'MySQL', 'Docker', 'Azure'],
        'image': 'https://images.unsplash.com/photo-1538108149393-fbbd81895907?w=800&h=500&fit=crop',
        'github_url': 'https://github.com/dev01-coder',
        'live_url': '',
        'category': 'ai,healthcare',
        'highlights': [
            'RAG-based retrieval for accurate medical code prediction',
            'Multi-code output: ICD, CPT, and Modifier codes',
            'OCR integration for processing scanned medical records',
            'Docker containerized deployment with MySQL backend',
            'Reduces coding time from hours to minutes'
        ]
    },
    {
        'id': 7,
        'title': 'Claim Denial Prediction System',
        'description': 'Machine learning system to forecast acceptance or rejection of claims based on 837 data using Random Forest, Neural Networks, and Decision Trees.',
        'tech': ['Python', 'Gemini', 'Flask', 'Google Vision', 'Azure', 'ML'],
        'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=500&fit=crop',
        'github_url': 'https://github.com/dev01-coder',
        'live_url': '',
        'category': 'ai,ml',
        'highlights': [
            'Multi-model comparison: Random Forest, Neural Networks, Decision Trees',
            '837 data parsing for claims feature engineering',
            'Proactive denial prediction before claim submission',
            'Azure cloud deployment for production scalability',
            'Reduces claim denial rates with data-driven insights'
        ]
    }
]

# Skills data - Updated with Ozair Ilyas's skills
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
        'content': 'Large Language Models have revolutionized AI development. In this comprehensive guide, we explore LLM basics, Retrieval-Augmented Generation (RAG), prompt engineering, and practical integration patterns.',
        'key_takeaways': [
            'LLMs like GPT and Llama process text using transformer architecture with attention mechanisms',
            'RAG combines retrieval systems with generative models to ground responses in real data',
            'Prompt engineering is the skill of crafting inputs that guide LLMs toward accurate outputs',
            'Fine-tuning on domain-specific data dramatically improves model performance for specialized tasks'
        ],
        'conclusion': 'LLMs are powerful tools when used correctly. Start with prompt engineering, graduate to RAG for knowledge-heavy tasks, and fine-tune only when necessary. The key is understanding trade-offs between cost, latency, and accuracy.',
        'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800&h=400&fit=crop'
    },
    {
        'id': 2,
        'title': 'Building Healthcare AI Solutions',
        'author': 'Ozair Ilyas',
        'date': 'Jan 18, 2026',
        'excerpt': 'Insights into developing AI solutions for medical coding, claims processing, and healthcare automation.',
        'content': 'Healthcare AI presents unique challenges and opportunities. This post covers medical data handling, HIPAA considerations, and building robust healthcare AI systems using Python and cloud services.',
        'key_takeaways': [
            'Healthcare data requires strict HIPAA compliance with encryption at rest and in transit',
            'Medical coding automation using LLMs can reduce coding time from hours to minutes',
            'Claims prediction models help healthcare providers proactively manage revenue cycles',
            'OCR + NLP pipelines extract structured data from unstructured medical documents'
        ],
        'conclusion': 'Healthcare AI is not just about technology — it is about understanding clinical workflows, regulatory requirements, and the real impact on patient outcomes. Start with high-value, low-risk automation tasks.',
        'image': 'https://images.unsplash.com/photo-1576091160550-2173dba999ef?w=800&h=400&fit=crop'
    },
    {
        'id': 3,
        'title': 'OCR and Computer Vision for Document Processing',
        'author': 'Ozair Ilyas',
        'date': 'Jan 15, 2026',
        'excerpt': 'Mastering document extraction and data recognition using OCR and Google Vision API.',
        'content': 'Automating document processing is crucial for many industries. Learn how to use Google Vision, OpenCV, and modern OCR techniques to extract and validate data from medical forms, receipts, and documents.',
        'key_takeaways': [
            'Google Vision API achieves 95%+ accuracy on printed text extraction from scanned documents',
            'Pre-processing steps like deskewing, denoising, and binarization significantly improve OCR results',
            'Combining OCR with NLP enables intelligent field extraction from unstructured documents',
            'Confidence scoring helps identify low-quality extractions that need manual review'
        ],
        'conclusion': 'OCR technology has matured significantly. The real value comes from combining it with NLP for intelligent document understanding, not just text extraction. Focus on the end-to-end pipeline.',
        'image': 'https://images.unsplash.com/photo-1555949963-ff9fe0c870eb?w=800&h=400&fit=crop'
    },
    {
        'id': 4,
        'title': 'Machine Learning for Predictive Analytics',
        'author': 'Ozair Ilyas',
        'date': 'Jan 12, 2026',
        'excerpt': 'Using Random Forest, Neural Networks, and Decision Trees for claims prediction and business intelligence.',
        'content': 'Predictive analytics can significantly impact business outcomes. Explore machine learning algorithms, feature engineering, model evaluation, and deployment strategies for production systems.',
        'key_takeaways': [
            'Random Forest and XGBoost consistently outperform deep learning on structured/tabular data',
            'Feature engineering is more important than model selection for most real-world problems',
            'Cross-validation and proper train/test splits prevent overfitting and give honest performance estimates',
            'Model explainability with SHAP values builds trust with non-technical stakeholders'
        ],
        'conclusion': 'Start simple, validate rigorously, and only increase complexity when justified by data. The best model is the one that solves the business problem, not necessarily the most sophisticated one.',
        'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800&h=400&fit=crop'
    }
]

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
    return render_template('index.html', projects=PROJECTS, posts=BLOG_POSTS)

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

@app.route('/download-cv')
def download_cv():
    cv_path = os.path.join(app.static_folder, 'files', 'Ozair_Ilyas_CV.pdf')
    if os.path.exists(cv_path):
        from flask import send_file
        return send_file(cv_path, as_attachment=True, download_name='Ozair_Ilyas_CV.pdf')
    return jsonify({'status': 'error', 'message': 'CV file not found'}), 404

@app.route('/thank-you/')
def thank_you():
    return render_template('thank-you.html')

@app.route('/privacy-policy/')
def privacy_policy():
    return render_template('privacy-policy.html')

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
