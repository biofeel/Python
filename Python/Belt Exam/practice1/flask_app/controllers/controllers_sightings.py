from flask_app import app
from types import MethodType
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_sightings, models_users

@app.route('/create/sighting',methods=['POST'])
def create_sighting():
    if not models_sightings.Sighting.validate_sighting(request.form):
        return redirect('/create')
    data = {
        "location": request.form["location"],
        "what_happened": request.form["what_happened"],
        "date_of_siting": request.form["date_of_siting"],
        "number_of_sasquatches": request.form["number_of_sasquatches"],
        "user_id": session["user_id"]
    }
    models_sightings.Sighting.save(data)
    return redirect('/dashboard')

@app.route('/delete/sighting/<int:id>')
def delete_sighting(id):
    models_sightings.Sighting.delete({'id':id})
    return redirect('/dashboard')

@app.route('/edit/sighting/<int:id>')
def edit_one_sighting(id):
    data = {
        "id": id
    }
    sighting = models_sightings.Sighting.get_one_sighting(data)
    return render_template("edit.html", sighting = sighting)

@app.route('/update_one/<int:id>', methods=['post'])
def update_one_sighting(id):
    data = {
        "location": request.form["location"],
        "what_happened": request.form["what_happened"],
        "date_of_siting": request.form["date_of_siting"],
        "number_of_sasquatches": request.form["number_of_sasquatches"],
        "id": id
    }
    if not models_sightings.Sighting.validate_sighting(data):
        return redirect(f"/edit/sighting/{id}")
    models_sightings.Sighting.update_one_sighting(data)
    return redirect("/dashboard")
