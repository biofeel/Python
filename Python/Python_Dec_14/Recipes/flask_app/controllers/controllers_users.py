from flask_app import app
from types import MethodType
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_users, models_recipes
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

# ******* Home Page *******
@app.route('/')
def homepage():
    return render_template('register_login.html')


# ******* Route to welome page ********
@app.route('/welcome')
def welcome():
    if 'user_id' not in session:
        return redirect ('/')
    user = models_users.User.get_user({'id':session['user_id']})
    one_recipe = models_recipes.Recipe.get_all_recipes()
    return render_template('welcome.html', user = user, one_recipe = one_recipe)

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
    return redirect("/welcome")

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
    return redirect("/welcome")

# ******** Logout *********
@app.route('/logout')
def logout_user():
    del session['user_id']
    return redirect('/')

# ******** Show Recipes ********
@app.route('/show')
def recipes_in_user():
    one_recipe = models_recipes.Recipe.get_all_recipes()
    return render_template('welcome.html', one_recipe = one_recipe)

@app.route('/recipe/<int:id>')
def show_recipe(id):
    user = models_users.User.get_user({'id': session['user_id']})
    show_recipe = models_recipes.Recipe.get_one_recipe({'id':id})
    return render_template('recipe.html', user = user, show_recipe = show_recipe )



@app.route('/create')
def create():
    return render_template('new_recipe.html')