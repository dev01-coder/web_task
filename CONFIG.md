# Configuration Guide

This guide explains all configuration options for the portfolio application.

## Environment Variables

The application uses environment variables for configuration. Create a `.env` file in the root directory with the following variables:

### Development Environment

```bash
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=dev-key-not-secure-change-in-production
PORT=5000
HOST=localhost
```

### Production Environment

```bash
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=<randomly-generated-secure-key>
PORT=5000
HOST=0.0.0.0
```

## Configuration Details

### FLASK_ENV
- **Type**: String
- **Default**: `production`
- **Options**: `development`, `production`
- **Purpose**: Sets Flask's environment mode
- **Note**: Automatically enables/disables debug features

### FLASK_DEBUG
- **Type**: Boolean (set as string: "True" or "False")
- **Default**: `False`
- **Purpose**: Enables Flask's debugger and auto-reloader
- **Warning**: NEVER set to True in production!

### SECRET_KEY
- **Type**: String
- **Default**: `'your-secret-key-change-in-production'`
- **Purpose**: Encrypts session data and secure cookies
- **How to generate**: 
  ```bash
  python -c "import secrets; print(secrets.token_hex(32))"
  ```
- **Important**: Change this for each environment!

### PORT
- **Type**: Integer
- **Default**: `5000`
- **Purpose**: Port the Flask server listens on
- **Example**: `8000`, `3000`, `5000`

### HOST
- **Type**: String
- **Default**: `0.0.0.0`
- **Options**:
  - `localhost` - Only accessible from your machine
  - `127.0.0.1` - Same as localhost
  - `0.0.0.0` - Accessible from any IP (for cloud deployment)
- **Purpose**: Determines which interfaces the server binds to

## Configuration Methods

### Method 1: Environment File (.env) - Recommended

1. Create `.env` file in project root:
   ```bash
   cp .env.example .env
   ```

2. Edit `.env` with your values:
   ```bash
   FLASK_ENV=production
   SECRET_KEY=your-secret-key-here
   ```

3. Load automatically (python-dotenv handles this)

### Method 2: Command Line

```bash
# Set individual variables
export FLASK_ENV=production
export SECRET_KEY=your-secret-key-here

# Windows PowerShell
$env:FLASK_ENV = "production"
$env:SECRET_KEY = "your-secret-key-here"

# Then run
python app.py
```

### Method 3: Docker/Container Environment

Set environment variables when running the container:

```bash
docker run -e FLASK_ENV=production \
           -e SECRET_KEY=your-key \
           -p 5000:5000 \
           your-image
```

### Method 4: Cloud Platform Dashboard

For Heroku:
```bash
heroku config:set FLASK_ENV=production
heroku config:set SECRET_KEY=your-secret-key
```

For Railway/Render: Use the dashboard UI to set variables

## Generating Secure Secret Keys

### Python
```python
import secrets
key = secrets.token_hex(32)
print(key)
```

### Command Line
```bash
python -c "import secrets; print(secrets.token_hex(32))"
```

### Online Generator (for reference)
Visit: https://www.random.org/bytes/ and generate 32 bytes (hex)

## Flask Configuration Objects

The application supports different configuration profiles. Edit `app.py` to customize:

### Currently Configured
```python
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback-key')
app.config['JSON_SORT_KEYS'] = False  # Don't sort JSON keys (faster)
```

### Optional Configurations
```python
# Session timeout (in seconds)
app.config['PERMANENT_SESSION_LIFETIME'] = 1800

# Maximum content length (10 MB)
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024

# Compression
app.config['COMPRESS_LEVEL'] = 6
```

## Platform-Specific Configuration

### Heroku Deployment

Create `runtime.txt`:
```
python-3.13.3
```

The `Procfile` is already configured:
```
web: gunicorn app:app
```

Gunicorn configuration in `Procfile`:
```
web: gunicorn --workers 4 --bind 0.0.0.0:$PORT app:app
```

### PythonAnywhere Configuration

In your WSGI file:
```python
import os
import sys

path = '/home/yourusername/web_task'
sys.path.append(path)
os.chdir(path)

os.environ['FLASK_ENV'] = 'production'
os.environ['SECRET_KEY'] = 'your-secret-key'

from app import app as application
```

### AWS Elastic Beanstalk

Create `.ebextensions/app.config`:
```yaml
option_settings:
  aws:elasticbeanstalk:container:python:
    WSGIPath: app:app
  aws:elasticbeanstalk:application:environment:
    FLASK_ENV: production
    SECRET_KEY: your-secret-key
```

### Docker Configuration

Create `Dockerfile`:
```dockerfile
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_ENV=production
ENV FLASK_DEBUG=False
ENV HOST=0.0.0.0
ENV PORT=5000

EXPOSE 5000

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
```

Create `docker-compose.yml`:
```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
      - SECRET_KEY=your-secret-key
```

## Development vs Production

### Development Settings
```bash
FLASK_ENV=development
FLASK_DEBUG=True
SECRET_KEY=dev-insecure-key-fine-for-local-use
```

### Production Settings
```bash
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=<use-secrets.token_hex(32)-output>
```

## Security Considerations

### Do's ✅
- ✅ Use environment variables for secrets
- ✅ Generate unique SECRET_KEY for each deployment
- ✅ Never commit .env to version control
- ✅ Use HTTPS in production (handled by cloud provider)
- ✅ Rotate SECRET_KEY regularly
- ✅ Keep dependencies updated

### Don'ts ❌
- ❌ Don't hardcode secrets in code
- ❌ Don't use weak/simple keys
- ❌ Don't set FLASK_DEBUG=True in production
- ❌ Don't commit .env file to git
- ❌ Don't share SECRET_KEY across environments
- ❌ Don't use default/example values

## Validating Configuration

Check your configuration:

```bash
# View current environment variables
python -c "import os; print('FLASK_ENV:', os.environ.get('FLASK_ENV')); print('SECRET_KEY:', os.environ.get('SECRET_KEY')[:20] + '...' if os.environ.get('SECRET_KEY') else 'Not set')"
```

## Troubleshooting Configuration Issues

### Issue: "SECRET_KEY not set in app config"
**Solution**: Ensure .env file exists and FLASK_ENV variable is properly set

### Issue: "Port already in use"
**Solution**: Change PORT variable or kill process using that port
```bash
# Find process
lsof -i :5000
# Kill process
kill -9 <PID>
```

### Issue: "Cannot access from other machines"
**Solution**: Set HOST=0.0.0.0 and ensure firewall allows the port

### Issue: Environment variables not loading
**Solution**: 
1. Verify .env file exists in root directory
2. Restart Python process
3. Check file permissions

## Advanced Configuration

### Multiple Environments

Create separate files:
- `.env.local` - Local development
- `.env.staging` - Staging environment  
- `.env.production` - Production

Load with:
```bash
export ENV_FILE=.env.production
python -c "from dotenv import load_dotenv; load_dotenv('.env.' + os.environ['ENV_FILE'])"
python app.py
```

### Configuration Classes

Extend `app.py` with configuration classes:

```python
import os

class Config:
    """Base configuration"""
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JSON_SORT_KEYS = False

class DevelopmentConfig(Config):
    """Development configuration"""
    FLASK_ENV = 'development'
    FLASK_DEBUG = True

class ProductionConfig(Config):
    """Production configuration"""
    FLASK_ENV = 'production'
    FLASK_DEBUG = False

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

# In app.py:
config_name = os.environ.get('FLASK_ENV', 'development')
app.config.from_object(config[config_name])
```

## Reference

- Flask Configuration: https://flask.palletsprojects.com/config
- Python-dotenv: https://pypi.org/project/python-dotenv/
- Gunicorn Configuration: https://docs.gunicorn.org/

---

**Last Updated**: January 2026
**Version**: 1.0.0
