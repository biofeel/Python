from flask_app import app
from types import MethodType
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_user
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

@app.route('/')
def homepage():
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect ('/')
    user = models_user.User.get_user({'id':session['user_id']})
    return render_template('welcome.html', user = user)

@app.route('/create', methods=['POST'])
def create_user():
    if not models_user.User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # put the pw_hash into the data dictionary
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password' : pw_hash
    }
    user_id = models_user.User.save(data)
    session['user_id'] = user_id
    return redirect("/welcome")

@app.route('/login', methods=['POST'])
def validate_login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = models_user.User.get_by_email(data)
    # user is not registered in the db
    if not user_in_db:
        flash("Invalid Email/Password", "login")
        return redirect("/")
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password", "login")
        return redirect('/')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    # never render on a post!!!
    return redirect("/welcome")

@app.route('/logout')
def logout_user():
    del session['user_id']
    return redirect('/')