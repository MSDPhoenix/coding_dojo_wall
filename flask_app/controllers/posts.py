from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/wall/')
def wall():
    if 'user_id' not in session:
        print("A")
        print("user_id not in session")
        return redirect('/')
    print("A")
    print("user_id = ",session['user_id'])
    data = {
        'user_id':session['user_id']
        }
    user = User.get_by_id(data)
    posts = Post.get_all()
    return render_template('wall.html',user=user,posts=posts)

@app.route('/post/',methods=['POST'])
def post():
    if not Post.validate(request.form):
        return redirect('/wall/')
    data = {
        'content' : request.form['content'],
        'user_id' : session['user_id']
    }
    Post.save(data)
    return redirect('/wall/')