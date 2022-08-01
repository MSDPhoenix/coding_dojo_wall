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

@app.route('/login/',methods=['POST'])
def login():
    data = {
        'email' : request.form['email']
    }
    user_in_db = User.get_by_email(data)
    if not user_in_db:
        flash('Invalid email/password','login')
        session['email']=request.form['email']
        session['password']=request.form['password']
        return redirect('/')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        flash('Invalid email/password','login')
        session['email']=request.form['email']
        session['password']=request.form['password']
        return redirect('/')
    session['user_id'] = user_in_db.id
    return redirect('/wall/')

@app.route('/logout/')
def logout():
    session.clear()
    return redirect('/')