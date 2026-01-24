# Ozair Ilyas - AI Engineer Portfolio Website

A professional, production-ready portfolio website showcasing AI engineering expertise, healthcare AI solutions, and technical projects. Built with Flask, Bootstrap 5, and deployed to production standards.

## ✨ Features

- **Home Page**: Eye-catching hero section highlighting AI/ML expertise
- **About Page**: Professional bio, timeline, and technical skills showcase
- **Projects Page**: 4 professional projects with full tech stacks (Medical Coding AI, HCFA OCR, Call Auditor, Claim Prediction)
- **Services Page**: 6 core services aligned with expertise (AI & ML, Healthcare AI, Document Processing, API Dev, Cloud, Analytics)
- **Blog Page**: Technical blog posts with proper formatting
- **Contact Page**: Fully functional contact form with validation and error handling
- **API Endpoints**: JSON APIs for projects, services, skills, and blog data
- **Production Ready**: Environment-based configuration, error handling, logging, and security
- **Responsive Design**: Mobile-first design, works on all devices
- **Modern UI**: Clean professional design with smooth animations and FontAwesome icons

## Project Structure

```
web_task/
├── app.py                      # Main Flask application (260+ lines)
├── requirements.txt            # Python dependencies
├── Procfile                    # Heroku deployment configuration
├── .env.example               # Environment variables template
├── .gitignore                 # Git ignore rules
├── README.md                  # Project documentation (this file)
├── DEPLOYMENT.md              # Deployment guide
├── PRODUCTION_CHECKLIST.md    # Production readiness checklist
│
├── templates/                 # HTML templates
│   ├── base.html             # Base template with navbar & footer
│   ├── index.html            # Home page (hero + featured content)
│   ├── about.html            # About page (bio, skills, timeline)
│   ├── projects.html         # Projects showcase
│   ├── project_detail.html   # Individual project detail
│   ├── services.html         # Services offering
│   ├── blog.html             # Blog listing
│   ├── blog_detail.html      # Individual blog post
│   ├── contact.html          # Contact form page
│   └── 404.html              # Error page
│
└── static/
    ├── css/
    │   └── style.css         # Custom CSS with animations
    ├── js/
    │   └── script.js         # Navigation & interaction logic
    └── images/
        └── profile.jpg       # Profile image (circular, 400px)
```

## Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for version control)

### Installation

1. **Clone or download this project**
   ```bash
   git clone <repository-url>
   cd web_task
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings (optional for development)
   ```

## Running the Application

### Development Mode
```bash
python app.py
```
Then open: `http://localhost:5000`

### Production Mode (with Gunicorn)
```bash
gunicorn app:app --bind 0.0.0.0:5000
```

### Environment Variables
Create a `.env` file with these variables:
```
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secure-key-here
PORT=5000
HOST=0.0.0.0
```

## Features in Detail

### Backend (Flask)
- **4 Professional Projects**: AI Medical Coding, HCFA OCR, Call Auditor, Claim Prediction
- **10 Technical Skills**: Python, SQL, LLM, Docker, Flask, Azure, etc.
- **4 Blog Posts**: AI/ML related technical content
- **6 Services**: AI & ML, Healthcare AI, Document Processing, API Development, Cloud Architecture, Data Analytics
- **Contact Form**: Full validation, error handling, and logging
- **API Endpoints**: `/api/projects`, `/api/services`, `/api/skills`, `/api/blog`
- **Error Handlers**: 404 and 500 with custom error pages
- **Logging**: INFO level logging for important events
- **Security**: Environment-based configuration, input validation

### Frontend
- **Bootstrap 5.1.3**: Responsive grid system
- **FontAwesome 6.0.0**: Professional icons
- **Custom CSS**: Animations, gradients, hover effects
- **Mobile Responsive**: Tested on mobile, tablet, and desktop
- **Accessibility**: Semantic HTML, ARIA labels

## Deployment

### Supported Platforms
- **Heroku** (Recommended - see DEPLOYMENT.md)
- **Railway**
- **Render**
- **Fly.io**
- **PythonAnywhere**
- **AWS Elastic Beanstalk**

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions.

## Routes & Pages

| Route | Method | Purpose |
|-------|--------|---------|
| `/` | GET | Home page with hero section |
| `/about` | GET | About page with bio and skills |
| `/projects` | GET | Projects showcase |
| `/project/<id>` | GET | Individual project detail |
| `/services` | GET | Services offered |
| `/blog` | GET | Blog listing |
| `/blog/<id>` | GET | Individual blog post |
| `/contact` | GET, POST | Contact form page |
| `/api/projects` | GET | JSON API for projects |
| `/api/services` | GET | JSON API for services |
| `/api/skills` | GET | JSON API for skills |
| `/api/blog` | GET | JSON API for blog posts |
| `/download-cv` | GET | CV download endpoint |
| `*` (invalid) | GET | 404 error page |

## Technologies Used

### Backend
- **Python 3.13.3**
- **Flask 2.3.2** - Web framework
- **Werkzeug 2.3.6** - WSGI utility library
- **Gunicorn 21.2.0** - Production WSGI server
- **python-dotenv 1.0.0** - Environment variable management

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Custom styling with animations
- **JavaScript (Vanilla)** - Interaction and form handling
- **Bootstrap 5.1.3** - Responsive grid and components
- **FontAwesome 6.0.0** - Icon library

### Hosting & Deployment
- **Procfile** - For cloud deployment
- **Environment variables** - Secure configuration
- **WSGI server** - Production-grade application server

## Customization

### Adding New Projects
Edit `app.py` and add to the `PROJECTS` list:
```python
{
    'id': 5,
    'title': 'Your Project Title',
    'description': 'Project description',
    'tech': ['Python', 'Flask', 'AI'],
    'image': 'https://loremflickr.com/600/400/category'
}
```

### Editing Skills
Modify the `SKILLS` list in `app.py`:
```python
{'name': 'Skill Name', 'level': 90},
```

### Updating Content
- **Homepage**: Edit `templates/index.html`
- **About page**: Edit `templates/about.html`
- **Services**: Edit `templates/services.html`
- **Styles**: Edit `static/css/style.css`
- **Navigation**: Edit `templates/base.html`

### Profile Image
1. Replace `static/images/profile.jpg` with your profile photo
2. Recommended size: 400x400px (square)
3. Supported formats: JPG, PNG, WebP

## Validation & Quality Assurance

### Form Validation
- ✅ Name field - Required, non-empty
- ✅ Email field - Required, valid format (contains @)
- ✅ Message field - Required, non-empty
- ✅ Terms checkbox - Must be checked

### Error Handling
- ✅ 404 errors - Custom error page
- ✅ 500 errors - Logged and reported
- ✅ Invalid form data - Validation error messages
- ✅ API errors - Proper JSON responses with status codes

### Security
- ✅ No hardcoded secrets (uses environment variables)
- ✅ Input validation on all forms
- ✅ Error messages don't expose sensitive info
- ✅ HTTPS ready (handled by deployment platform)
- ✅ No SQL injection vulnerabilities

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution**: Install dependencies
```bash
pip install -r requirements.txt
```

### Issue: Port already in use
**Solution**: Change the port in app.py or environment variable
```bash
export PORT=8000
python app.py
```

### Issue: Profile image not showing
**Solution**: Ensure `profile.jpg` exists in `static/images/` folder

### Issue: Form not submitting
**Solution**: Check browser console (F12) for JavaScript errors, ensure Flask is running

### Issue: 404 errors for images
**Solution**: Images use LoremFlickr API; check internet connection

## API Documentation

### GET /api/projects
Returns list of all projects
```json
[
  {
    "id": 1,
    "title": "Project Name",
    "description": "...",
    "tech": ["Python", "Flask"],
    "image": "..."
  }
]
```

### GET /api/skills
Returns list of all skills with proficiency levels
```json
[
  {"name": "Python", "level": 95},
  {"name": "SQL", "level": 90}
]
```

### POST /contact
Submit contact form
**Request body**:
```json
{
  "name": "Your Name",
  "email": "your@email.com",
  "message": "Your message"
}
```
**Response**:
```json
{
  "status": "success",
  "message": "Message sent successfully!"
}
```

## Future Enhancements

- [ ] Database integration (SQLite/PostgreSQL)
- [ ] Email notifications for contact submissions
- [ ] Dark mode toggle
- [ ] Admin dashboard for managing projects/blog
- [ ] Blog comment system
- [ ] Newsletter signup
- [ ] Analytics integration
- [ ] Performance optimization (caching, compression)

## Production Checklist

Before deploying to production:
- [ ] Set unique SECRET_KEY in .env file
- [ ] Add profile.jpg to static/images/ folder
- [ ] Update GitHub URL if needed
- [ ] Test all forms locally
- [ ] Review error handling logs
- [ ] Check responsive design on mobile
- [ ] Verify all images load correctly
- [ ] Set FLASK_DEBUG=False in production

See [PRODUCTION_CHECKLIST.md](PRODUCTION_CHECKLIST.md) for detailed checklist.

## License

MIT License - Feel free to use this template for your portfolio!

## Author

**Ozair Ilyas**
- Jr. AI Engineer
- Healthcare AI Solutions Specialist
- Email: sardarozair13@gmail.com
- LinkedIn: [pk.linkedin.com/in/ozair-ilyas](https://pk.linkedin.com/in/ozair-ilyas)
- GitHub: [github.com/ozairilyas](https://github.com)

## Support

For issues, questions, or suggestions:
1. Check [DEPLOYMENT.md](DEPLOYMENT.md) for deployment help
2. Review [PRODUCTION_CHECKLIST.md](PRODUCTION_CHECKLIST.md) for setup issues
3. Check Flask documentation: https://flask.palletsprojects.com
4. Check Bootstrap documentation: https://getbootstrap.com

---

**Last Updated**: January 2026
**Version**: 1.0.0 (Production Ready)
