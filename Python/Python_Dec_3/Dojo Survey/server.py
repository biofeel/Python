from flask import Flask, render_template, session, redirect, request, flash
from config.mysqlconnection import connectToMySQL

app = Flask(__name__)
app.secret_key="spiderman."

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    if len(request.form["name"])<1:
        flash("Name field can not be empty")
        return redirect("/")
    else:
        name = request.form["name"]
        location = request.form["dojo_location"]
        language = request.form["favlanguage"]
        comment = request.form["comments"]
        return render_template("result.html", name = name, location = location, language = language, comment = comment)
class Dojo:

    @staticmethod
    def validate_dojo(dojos):
        is_valid = True
        if len(dojos['name']) <3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(dojos['location']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        if len(dojos['language']) < 2:
            flash("language must be 2 or greater.")
            is_valid = False
        if len(dojos['comment']) < 3:
            flash("comment must be at least 3 characters.")
            is_valid = False
        return is_valid

if __name__=="__main__":
    app.run(debug=True)