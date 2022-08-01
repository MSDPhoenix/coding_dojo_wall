from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/post_a_comment/<int:post_id>/',methods=['POST'])
def post_a_comment(post_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'content' : request.form['content'],
        'post_id' : post_id,
        'user_id' : session['user_id'],
    }
    Comment.save(data)
    return redirect('/wall/')

@app.route('/delete_comment/<comment_id>/')
def delete_comment(comment_id):
    if 'user_id' not in session:
        return redirect('/')
    Comment.delete({'comment_id':comment_id})
    return redirect('/wall/')
