from flask import Flask, render_template, request, redirect
import os

IMG_FOLDER = os.path.join('static', 'img')
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = IMG_FOLDER

@app.route('/')         
def index():
    return render_template("index.html")

@app.route('/checkout', methods=['POST'])         
def checkout():
    print(request.form)
    strawberry_quantity = request.form['strawberry']
    raspberry_quantity = request.form['raspberry']
    apple_quantity = request.form['apple']
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    student_id = request.form['student_id']
    total_fruits = int(strawberry_quantity) + int(raspberry_quantity) + int(apple_quantity)
    print(f"Charging {first_name} {last_name} for {total_fruits} fruits")
    return render_template("checkout.html", firstname_template = first_name, lastname_template = last_name, student_id = student_id, strawberry_quantity = strawberry_quantity, apple_quantity = apple_quantity, raspberry_quantity = raspberry_quantity)

@app.route('/fruits')         
def fruits():
    fruitPic = os.path.join(app.config['UPLOAD_FOLDER'], 'apple.png')

    imageList = os.listdir('static/img')
    imageList = ['img/' + image for image in imageList]
    return render_template("fruits.html", imageList = imageList)



if __name__=="__main__":   
    app.run(debug=True)    