# Dev Portfolio Website

A beautiful, responsive portfolio website built with Flask and Bootstrap.

## Features

- **Home Page**: Eye-catching hero section with featured skills
- **About Page**: Personal introduction and qualifications
- **Projects Page**: Showcase of sample projects with technologies used
- **Contact Page**: Fully functional contact form with AJAX submission
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Modern UI**: Clean and professional design with smooth animations

## Project Structure

```
web_task/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/            # HTML templates
│   ├── base.html        # Base template with navigation
│   ├── index.html       # Home page
│   ├── about.html       # About page
│   ├── projects.html    # Projects showcase
│   ├── contact.html     # Contact form
│   └── 404.html         # 404 error page
└── static/
    ├── css/
    │   └── style.css    # Custom styles
    └── js/
        └── script.js    # JavaScript functionality
```

## Installation

1. Clone or download this project
2. Navigate to the project directory
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Website

```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

## Pages

- **Home** (`/`) - Hero section with skills overview
- **About** (`/about`) - Personal bio and qualifications
- **Projects** (`/projects`) - Project showcase
- **Contact** (`/contact`) - Contact form for visitors to reach out

## Technologies Used

- **Backend**: Python, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Bootstrap 5
- **Animations**: CSS animations and transitions

## Customization

Feel free to customize:
- Edit `app.py` to add more routes or modify data
- Update HTML templates in the `templates/` folder
- Modify styles in `static/css/style.css`
- Add more JavaScript functionality in `static/js/script.js`

## Future Enhancements

- Add database to store contact messages
- Implement email notifications for form submissions
- Add dark mode toggle
- Deploy to a live server (Heroku, PythonAnywhere, etc.)
- Add blog section
- Implement authentication for admin panel

## License

MIT License - Feel free to use this for your portfolio!
