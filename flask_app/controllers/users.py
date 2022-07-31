from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.user import User
from flask_app.models.post import Post
from flask_app.models.comment import Comment
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/wall/')
def wall():
    data = {
        'user_id':session['user_id']
        }
    user = User.get_by_id(data)
    return render_template('wall.html',user=user)

@app.route('/register/',methods=['POST'])
def register():
    if not User.validate(request.form):
        session['first_name']=request.form['first_name']
        session['last_name']=request.form['last_name']
        session['email']=request.form['email']
        session['password']=request.form['password']
        session['confirm_password']=request.form['confirm_password']
        return redirect('/')
    session.clear()
    password_hash = bcrypt.generate_password_hash(request.form['password'])
    data = {
        'first_name' : request.form['first_name'],
        'last_name' : request.form['last_name'],
        'email' : request.form['email'],
        'password' : password_hash
    }
    session['user_id'] = User.save(data)
    return redirect('/wall/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')