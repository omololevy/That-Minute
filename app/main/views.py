from flask import render_template,request,redirect,url_for,request,redirect,url_for,abort
from . import main
from flask_login import login_required,current_user
from ..models import Pitch,Comment,User,Upvote,Downvote
from .. import db,photos
from .forms import UpdateProfile,PitchForm,CommentsForm


@main.route('/')
def index():
    pitches_list= Pitch.query.all()
    
    return render_template('index.html',pitches_list=pitches_list)

@main.route('/filter/<int:pitch_query>')
def filter(pitch_query):  
    categories = {"1":"Interview","2":"Advertisement","3":"Humour","4":"Pickup_lines"}
    
        
    filtered_pitches_list = Pitch.get_pitches(categories.get(str(pitch_query)))
    print(filtered_pitches_list)
      
    return render_template('filter_pitch.html',pitches_list=filtered_pitches_list)


