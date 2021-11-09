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

@main.route('/new_pitch',methods= ['GET','POST'])
@login_required
def new_pitch():
    form = PitchForm()
    
    if form.validate_on_submit():
        title = form.title.data
        pitch = form.pitch.data
        category = form.category.data
        user_id = current_user
        new_pitch_object = Pitch(pitch=pitch,user_id=current_user._get_current_object().id,category=category,title=title)
        new_pitch_object.save_pitch()
       
        return redirect(url_for('main.index'))
    
    return render_template('new_pitch.html',form=form)


@main.route('/comment/<int:pitch_id>',methods = ['GET','POST'])
@login_required
def add_comment(pitch_id):
    form = CommentsForm()
    pitch = Pitch.query.get(pitch_id)
    
    comments_list = Comment.get_comments(pitch_id)
    if form.validate_on_submit():
        comment = form.comment.data 
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        new_comment = Comment(comment = comment,user_id = user_id,pitch_id = pitch_id)
        new_comment.save_comment()
        return redirect(url_for('.add_comment', pitch_id = pitch_id))
    return render_template('comments.html',form=form,comments_list=comments_list,pitch=pitch)


@main.route('/upvote_pitch/<int:user_id>/<int:pitch_id>')
@login_required
def upvote_pitch(pitch_id,user_id):
    upvote = Upvote.query.filter_by(user_id =current_user._get_current_object().id).first()
   
    print(pitch_id)
    if upvote:
        pitch_id = pitch_id
       
        if upvote.user_id == current_user._get_current_object().id and upvote.pitch_id == pitch_id :         
            print("upvote already exists")
            return redirect(url_for("main.index"))
        elif  upvote.pitch_id == pitch_id  and db.session.query(Upvote.id).filter_by(user_id=current_user._get_current_object().id) is not None   :
            print("upvote already exists")
            return redirect(url_for("main.index")) 
        else:
            print(pitch_id)
            pitch_id = pitch_id
            user_id = current_user._get_current_object().id
            upvote_count = 1
            new_upvote = Upvote(upvote_count=upvote_count,user_id = user_id,pitch_id = pitch_id)
            new_upvote.add_upvote()
            print("Added new upvote")
            return redirect(url_for("main.index"))

    else:
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        upvote_count = 1
        new_upvote = Upvote(upvote_count=upvote_count,user_id = user_id,pitch_id = pitch_id)
        new_upvote.add_upvote()
        print("Added new upvote")
       
    return redirect(url_for("main.index"))

@main.route('/downvote_pitch/<int:user_id>/<int:pitch_id>')
@login_required
def downvote_pitch(pitch_id,user_id):
    downvote = Downvote.query.filter_by(user_id =current_user._get_current_object().id).first()
   
    print(pitch_id)
    if downvote:
        pitch_id = pitch_id
      
        if downvote.user_id == current_user._get_current_object().id and downvote.pitch_id == pitch_id :         
            print("downvote already exists")
            return redirect(url_for("main.index"))
        elif  downvote.pitch_id == pitch_id  and db.session.query(Downvote.id).filter_by(user_id=current_user._get_current_object().id) is not None   :
            print("downvote already exists")
            return redirect(url_for("main.index")) 
        else:
            print(pitch_id)
            pitch_id = pitch_id
            user_id = current_user._get_current_object().id
            downvote_count = 1
            new_downvote = Downvote(downvote_count=downvote_count,user_id = user_id,pitch_id = pitch_id)
            new_downvote.add_downvote()
            print("Added new downvote")
            return redirect(url_for("main.index"))
   
    else:
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id
        downvote_count = 1
        new_downvote = Downvote(downvote_count=downvote_count,user_id = user_id,pitch_id = pitch_id)
        new_downvote.add_downvote()
        print("Added new downvote")
       
    return redirect(url_for("main.index"))
        
      
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()
    posts = Pitch.query.filter_by(user_id =current_user._get_current_object().id ).all()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user,posts=posts)

