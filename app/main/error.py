from flask import render_template
from . import main

@main.app_errorhandler(404)
def errors(error):
    '''
    Function to render the 404 error page
    '''
    return render_template('errors.html'),404
