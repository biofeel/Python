from flask_app import app
from types import MethodType
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_users, models_sightings
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

# ******* Home Page *******
@app.route('/')
def homepage():
    return render_template('index.html')


# ******* Route to welome page ********
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect ('/')
    user = models_users.User.get_user({'id':session['user_id']})
    one_sighting = models_sightings.Sighting.get_all_sightings()
    return render_template('dashboard.html', user = user, one_sighting = one_sighting)

# ******** Create new user ********
@app.route('/create', methods=['POST'])
def create_user():
    if not models_users.User.validate_user(request.form):
        return redirect('/')
    
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # put the pw_hash into the data dictionary
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
        'password' : pw_hash
    }
    user_id = models_users.User.save(data)
    session['user_id'] = user_id
    return redirect("/dashboard")

# ******** Login *********
@app.route('/login', methods=['POST'])
def validate_login():
    # see if the username provided exists in the database
    data = { "email" : request.form["email"] }
    user_in_db = models_users.User.get_by_email(data)
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
    return redirect("/dashboard")

# ******** Logout *********
@app.route('/logout')
def logout_user():
    del session['user_id']
    return redirect('/')

# ******** Show sightings ********
@app.route('/show')
def sightings_in_user():
    one_sighting = models_sightings.Sighting.get_all_sightings()
    return render_template('dashboard.html', one_sighting = one_sighting)

@app.route('/sighting/<int:id>')
def show_sighting(id):
    user = models_users.User.get_user({'id': session['user_id']})
    show_sighting = models_sightings.Sighting.get_one_sighting({'id':id})
    return render_template('sighting.html', user = user, show_sighting = show_sighting )

@app.route('/create')
def create():
    user = models_users.User.get_user({'id': session['user_id']})
    return render_template('new_sighting.html', user = user)