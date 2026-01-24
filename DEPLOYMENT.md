# Portfolio Website - Deployment Guide

## Local Development Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd web_task
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   ```
   
   Edit `.env` and set:
   - `FLASK_ENV=development`
   - `FLASK_DEBUG=True` (for development only)
   - `SECRET_KEY=your-secure-random-key` (generate with: `python -c "import secrets; print(secrets.token_hex(32))"`)

5. **Add profile image**
   - Save your profile photo as `profile.jpg`
   - Place it in `static/images/` folder

6. **Run the development server**
   ```bash
   python app.py
   ```
   
   Visit `http://localhost:5000` in your browser.

## Production Deployment

### Heroku Deployment

1. **Create Heroku account** - Visit [heroku.com](https://www.heroku.com)

2. **Install Heroku CLI**
   ```bash
   # Download from: https://devcenter.heroku.com/articles/heroku-cli
   ```

3. **Initialize git repository** (if not already done)
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

4. **Create Heroku app**
   ```bash
   heroku create your-app-name
   ```

5. **Set environment variables on Heroku**
   ```bash
   heroku config:set FLASK_ENV=production
   heroku config:set FLASK_DEBUG=False
   heroku config:set SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
   ```

6. **Deploy to Heroku**
   ```bash
   git push heroku main
   ```

7. **View logs**
   ```bash
   heroku logs --tail
   ```

### Other Cloud Platforms

#### PythonAnywhere
1. Upload files to PythonAnywhere
2. Create a virtual environment
3. Set SECRET_KEY in web app configuration
4. Configure WSGI file to use Gunicorn

#### AWS Elastic Beanstalk
1. Install EB CLI
2. Run `eb init` and `eb create`
3. Configure environment variables in `.ebextensions/`
4. Deploy with `eb deploy`

#### Railway, Render, or Fly.io
All support Python Flask apps with Procfile-based deployment. Follow their specific documentation.

## Configuration for Production

### Environment Variables (Required)
```
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-very-secure-random-key-here
PORT=5000
HOST=0.0.0.0
```

### Security Checklist
- ✅ SECRET_KEY is cryptographically secure (use `secrets` module)
- ✅ FLASK_DEBUG=False in production
- ✅ All user input is validated
- ✅ HTTPS is enforced (handled by cloud provider)
- ✅ Profile image exists and is optimized
- ✅ No hardcoded secrets in code

### Performance Optimization
- Static files are cached with appropriate headers
- Images are served with correct MIME types
- JSON responses are minified when deployed
- Gunicorn is configured with multiple workers

## Monitoring & Maintenance

### Logging
- Application logs are written to stdout
- Check `heroku logs --tail` for production issues
- Log level is set to INFO for relevant information

### Contact Form
- Currently stores messages in memory (resets on restart)
- For persistence, implement:
  - SQLite database
  - PostgreSQL on Heroku
  - Email notifications (SendGrid, mailgun)

### Updates & Maintenance
1. Test locally before deploying
2. Use `git` for version control
3. Set up CI/CD pipeline (GitHub Actions, etc.)
4. Monitor application performance

## Troubleshooting

### Images not loading
- Check that profile.jpg exists in `static/images/`
- Verify image file permissions
- Use dev tools (F12) to check image URLs

### Form not submitting
- Check browser console for JavaScript errors
- Verify Flask is running (`python app.py`)
- Check email format validation on backend

### 500 errors
- Check `heroku logs --tail` for error details
- Verify all environment variables are set
- Ensure database/external services are accessible

## Support

For issues or questions, check the app logs and enable debug mode locally to identify the problem.
