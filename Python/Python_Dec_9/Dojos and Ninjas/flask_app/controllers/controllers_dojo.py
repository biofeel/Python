from types import MethodType
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import models_dojo

@app.route('/')
def all_dojos():
    all_dojos = models_dojo.Dojo.get_all_dojos()
    return render_template('dojos.html', all_dojos = all_dojos)

@app.route('/create_dojo', methods=['post'])
def create_dojo():
    print(request.form)
    models_dojo.Dojo.create_dojo(request.form)
    return redirect ('/')

@app.route('/<int:id>/show')
def ninjas_in_dojo(id):
    one_dojo = models_dojo.Dojo.get_dojos_with_ninjas({'id':id})
    return render_template('dojo_show.html', one_dojo = one_dojo)

