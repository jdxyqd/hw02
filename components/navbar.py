from flask import Blueprint, render_template, url_for

navbar = Blueprint('navbar', __name__)

@navbar.route('/')
def home():
    return render_template('home.html')

@navbar.route('/about')
def about():
    return render_template('about.html')

@navbar.route('/projects')
def projects():
    return render_template('projects.html')

@navbar.route('/contact')
def contact():
    return render_template('contact.html')