from types import MethodType
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import model_users

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def users_show():
    return render_template("users.html", users=model_users.User.get_all())

@app.route('/users/new_user')
def new_user():
    return render_template("new_user.html")

@app.route('/users/create', methods=['post'])
def create():
    print(request.form)
    model_users.User.create_one(request.form)
    return redirect('/users')

@app.route('/<int:id>/read_one')
def read_one(id):
    user = model_users.User.get_one({'id':id})
    return render_template("read.html", user=user)  


@app.route('/<int:id>/delete_one')
def delete_one(id):
    model_users.User.delete_one({'id':id})
    return redirect("/users")
    
@app.route('/<int:id>/edit_user')
def edit_one(id):
    data = {
        'id': id
    }
    user = model_users.User.get_one(data)
    return render_template("edit_user.html", user=user) 

@app.route('/update_one', methods=['post'])
def update_one():
    model_users.User.update_one(request.form)
    return redirect("/users")