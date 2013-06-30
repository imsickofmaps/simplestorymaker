"""
views imports app but not import views
"""

from app import app


@app.route('/')
def homepage():
    return "homepage"
