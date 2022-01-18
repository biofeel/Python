from flask_app import app
from types import MethodType
from flask import render_template, redirect, request, session
from flask_app.models import models_users, models_bands
from flask_bcrypt import Bcrypt        
bcrypt = Bcrypt(app)

@app.route('/create/band',methods=['POST'])
def create_band():
    if not models_bands.Band.validate_band(request.form):
        return redirect('/create')
    data = {
        "band_name": request.form["band_name"],
        "music_genre": request.form["music_genre"],
        "home_city": request.form["home_city"],
        "user_id": session["user_id"]
    }
    models_bands.Band.save(data)
    return redirect('/dashboard')

@app.route('/delete/band/<int:id>')
def delete_band(id):
    models_bands.Band.delete({'id':id})
    return redirect('/dashboard')

@app.route('/edit/band/<int:id>')
def edit_one_band(id):
    data = {
        "id": id
    }
    band = models_bands.Band.get_one_band(data)
    user = models_users.User.get_user({'id': session['user_id']})
    return render_template("edit.html", band = band, user=user)

@app.route('/update_one/<int:id>', methods=['post'])
def update_one_band(id):
    data = {
        "band_name": request.form["band_name"],
        "music_genre": request.form["music_genre"],
        "home_city": request.form["home_city"],
        "id": id
    }
    if not models_bands.Band.validate_band(data):
        return redirect(f"/edit/band/{id}")
    models_bands.Band.update_one_band(data)
    return redirect("/dashboard")
