"""
Build script for generating static files using Frozen-Flask.
This converts the Flask application into a static site for Netlify deployment.
"""
from flask_frozen import Freezer
from app import app, PROJECTS, BLOG_POSTS

# Configure Frozen-Flask
app.config['FREEZER_DESTINATION'] = 'build'
app.config['FREEZER_RELATIVE_URLS'] = True
app.config['FREEZER_IGNORE_MIMETYPE_WARNINGS'] = True
app.config['FREEZER_STATIC_IGNORE'] = ['*.pyc']
app.config['FREEZER_DEFAULT_MIMETYPE'] = 'text/html'

freezer = Freezer(app, with_no_argument_rules=False, log_url_for=False)


@freezer.register_generator
def home():
    yield {}


@freezer.register_generator
def about():
    yield {}


@freezer.register_generator
def projects():
    yield {}


@freezer.register_generator
def services():
    yield {}


@freezer.register_generator
def contact():
    yield {}


@freezer.register_generator
def thank_you():
    yield {}


@freezer.register_generator
def privacy_policy():
    yield {}


@freezer.register_generator
def project_detail():
    """Generate URLs for all project detail pages."""
    for project in PROJECTS:
        yield {'project_id': project['id']}


@freezer.register_generator
def blog():
    yield {}


@freezer.register_generator
def blog_detail():
    """Generate URLs for all blog detail pages."""
    for post in BLOG_POSTS:
        yield {'post_id': post['id']}


if __name__ == '__main__':
    import os
    import shutil

    build_dir = os.path.join(os.path.dirname(__file__), 'build')

    # Clean build directory
    if os.path.exists(build_dir):
        shutil.rmtree(build_dir)

    print("Building static site...")
    freezer.freeze()

    # Generate 404 page manually since it's not a route
    with app.test_client() as client:
        resp = client.get('/nonexistent-page-for-404')
        with open(os.path.join(build_dir, '404.html'), 'wb') as f:
            f.write(resp.data)

    # Copy robots.txt and sitemap.xml to build root
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    for filename in ['robots.txt', 'sitemap.xml']:
        src = os.path.join(static_dir, filename)
        dst = os.path.join(build_dir, filename)
        if os.path.exists(src):
            shutil.copy2(src, dst)
            print(f"Copied {filename} to build directory")

    print("Static site built successfully in 'build' directory!")
