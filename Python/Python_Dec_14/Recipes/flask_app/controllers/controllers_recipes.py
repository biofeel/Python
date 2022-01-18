from flask_app import app
from types import MethodType
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_users, models_recipes
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/create/recipe',methods=['POST'])
def create_recipe():
    if not models_recipes.Recipe.validate_recipe(request.form):
        return redirect('/create')
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "cook_time": request.form["cook_time"],
        "date_made": request.form["date_made"],
        "user_id": session["user_id"]
    }
    models_recipes.Recipe.save(data)
    return redirect('/welcome')

@app.route('/delete/recipe/<int:id>')
def delete_recipe(id):
    models_recipes.Recipe.delete({'id':id})
    return redirect('/welcome')

@app.route('/edit/recipe/<int:id>')
def edit_one_recipe(id):
    data = {
        "id": id
    }
    recipe = models_recipes.Recipe.get_one_recipe(data)
    return render_template("edit.html", recipe = recipe)

@app.route('/update_one/<int:id>', methods=['post'])
def update_one_recipe(id):
    data = {
        "name": request.form["name"],
        "description": request.form["description"],
        "instruction": request.form["instruction"],
        "cook_time": request.form["cook_time"],
        "date_made": request.form["date_made"],
        "id": id
    }
    if not models_recipes.Recipe.validate_recipe(data):
        return redirect(f"/edit/recipe/{id}")
    models_recipes.Recipe.update_one_recipe(data)
    return redirect("/welcome")
