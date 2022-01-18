from types import MethodType
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_ninja, models_dojo

@app.route('/new_ninja')
def alls_dojos():
    all_dojos = models_dojo.Dojo.get_all_dojos()
    return render_template('new_ninja.html', all_dojos = all_dojos)

@app.route('/new_ninja')
def add_ninja():
    return render_template('new_ninja.html')

@app.route('/add_new_ninja', methods=['post'])
def add_a_new_ninja():
    data = {
        "first_name" : request.form["first_name"],
        "last_name" : request.form["last_name"],
        "age" : request.form["age"],
        "dojo_id" : request.form["dojo_id"],
    }
    models_ninja.Ninja.create_new_ninja(data)
    return redirect(f"/{data['dojo_id']}/show")