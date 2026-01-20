from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-here'

# Sample projects data
PROJECTS = [
    {
        'id': 1,
        'title': 'Portfolio Website',
        'description': 'A beautiful responsive portfolio built with Flask and Bootstrap',
        'tech': ['Flask', 'Python', 'HTML', 'CSS'],
        'image': 'https://via.placeholder.com/300x200?text=Portfolio'
    },
    {
        'id': 2,
        'title': 'Task Manager App',
        'description': 'Simple task management application with local storage',
        'tech': ['JavaScript', 'HTML', 'CSS'],
        'image': 'https://via.placeholder.com/300x200?text=Task+Manager'
    },
    {
        'id': 3,
        'title': 'Weather App',
        'description': 'Real-time weather information using public APIs',
        'tech': ['Python', 'Flask', 'API'],
        'image': 'https://via.placeholder.com/300x200?text=Weather'
    },
    {
        'id': 4,
        'title': 'E-commerce Platform',
        'description': 'Full-featured e-commerce site with payment integration',
        'tech': ['Django', 'PostgreSQL', 'Stripe', 'React'],
        'image': 'https://via.placeholder.com/300x200?text=E-commerce'
    },
    {
        'id': 5,
        'title': 'Chat Application',
        'description': 'Real-time messaging app with WebSocket support',
        'tech': ['Node.js', 'WebSocket', 'MongoDB'],
        'image': 'https://via.placeholder.com/300x200?text=Chat+App'
    },
    {
        'id': 6,
        'title': 'Data Visualization Dashboard',
        'description': 'Interactive analytics dashboard with real-time data',
        'tech': ['Python', 'D3.js', 'Flask', 'PostgreSQL'],
        'image': 'https://via.placeholder.com/300x200?text=Dashboard'
    }
]

# Skills data
SKILLS = [
    {'name': 'Python', 'level': 95},
    {'name': 'JavaScript', 'level': 88},
    {'name': 'Flask/Django', 'level': 90},
    {'name': 'React', 'level': 85},
    {'name': 'SQL', 'level': 92},
    {'name': 'HTML/CSS', 'level': 95},
    {'name': 'Docker', 'level': 80},
    {'name': 'Git', 'level': 93}
]

# Blog posts data
BLOG_POSTS = [
    {
        'id': 1,
        'title': 'Getting Started with Flask',
        'author': 'John Doe',
        'date': 'Jan 15, 2026',
        'excerpt': 'Learn the basics of Flask web framework and build your first web application.',
        'content': 'Flask is a lightweight WSGI web application framework written in Python. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. In this post, we will explore the fundamentals of Flask...',
        'image': 'https://via.placeholder.com/600x400?text=Flask+Tutorial'
    },
    {
        'id': 2,
        'title': 'Modern JavaScript ES6 Features',
        'author': 'Jane Smith',
        'date': 'Jan 12, 2026',
        'excerpt': 'Explore the latest ES6 features that make JavaScript development more efficient and enjoyable.',
        'content': 'ES6 introduced many new features that have revolutionized JavaScript development. From arrow functions to classes, destructuring to async/await, these features make code more readable and maintainable...',
        'image': 'https://via.placeholder.com/600x400?text=JavaScript+ES6'
    },
    {
        'id': 3,
        'title': 'Database Design Best Practices',
        'author': 'Mike Johnson',
        'date': 'Jan 10, 2026',
        'excerpt': 'Master the art of designing efficient and scalable database schemas.',
        'content': 'Proper database design is crucial for application performance. In this comprehensive guide, we will cover normalization, indexing strategies, and optimization techniques...',
        'image': 'https://via.placeholder.com/600x400?text=Database+Design'
    },
    {
        'id': 4,
        'title': 'REST API Design Principles',
        'author': 'Sarah Williams',
        'date': 'Jan 8, 2026',
        'excerpt': 'Build scalable and maintainable REST APIs following industry best practices.',
        'content': 'REST APIs are the backbone of modern web applications. Learn how to design APIs that are easy to understand, use, and maintain...',
        'image': 'https://via.placeholder.com/600x400?text=REST+API'
    }
]

# Testimonials data
TESTIMONIALS = [
    {
        'name': 'Alice Johnson',
        'company': 'Tech Startup Inc.',
        'text': 'Excellent work! The portfolio website exceeded our expectations. Very professional and responsive.',
        'rating': 5,
        'image': 'https://via.placeholder.com/100x100?text=Alice'
    },
    {
        'name': 'Bob Martinez',
        'company': 'Digital Solutions Ltd.',
        'text': 'Great developer with strong technical skills. Delivered on time and within budget.',
        'rating': 5,
        'image': 'https://via.placeholder.com/100x100?text=Bob'
    },
    {
        'name': 'Carol Davis',
        'company': 'Creative Agency Co.',
        'text': 'Professional, reliable, and easy to work with. Would definitely hire again!',
        'rating': 5,
        'image': 'https://via.placeholder.com/100x100?text=Carol'
    }
]

# Services data
SERVICES = [
    {
        'id': 1,
        'title': 'Web Development',
        'description': 'Full-stack web development using modern technologies and frameworks',
        'icon': '🌐'
    },
    {
        'id': 2,
        'title': 'Mobile App Development',
        'description': 'Native and cross-platform mobile applications for iOS and Android',
        'icon': '📱'
    },
    {
        'id': 3,
        'title': 'API Development',
        'description': 'RESTful and GraphQL API design and development',
        'icon': '⚙️'
    },
    {
        'id': 4,
        'title': 'Database Design',
        'description': 'Efficient database schema design and optimization',
        'icon': '🗄️'
    },
    {
        'id': 5,
        'title': 'Cloud Deployment',
        'description': 'Deploy applications to AWS, Google Cloud, or Azure',
        'icon': '☁️'
    },
    {
        'id': 6,
        'title': 'Consulting',
        'description': 'Technical consulting and architecture guidance',
        'icon': '💡'
    }
]

# Store messages from contact form
MESSAGES = []

@app.route('/favicon.ico')
def favicon():
    return '', 204

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html', skills=SKILLS)

@app.route('/projects')
def projects():
    return render_template('projects.html', projects=PROJECTS)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if project is None:
        return render_template('404.html'), 404
    return render_template('project_detail.html', project=project)

@app.route('/services')
def services():
    return render_template('services.html', services=SERVICES)

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=BLOG_POSTS)

@app.route('/blog/<int:post_id>')
def blog_detail(post_id):
    post = next((p for p in BLOG_POSTS if p['id'] == post_id), None)
    if post is None:
        return render_template('404.html'), 404
    return render_template('blog_detail.html', post=post)

@app.route('/testimonials')
def testimonials():
    return render_template('testimonials.html', testimonials=TESTIMONIALS)

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.get_json()
        message = {
            'name': data.get('name'),
            'email': data.get('email'),
            'message': data.get('message'),
            'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        MESSAGES.append(message)
        return jsonify({'status': 'success', 'message': 'Message sent successfully!'})
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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
