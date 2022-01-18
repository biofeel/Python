from typing import Counter
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'AllSecret'
app.counter = 0

@app.route('/')         
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    return render_template("index.html")

@app.route('/addcount', methods=['POST'])
def add_count_two():
    session['counter'] += 1
    return redirect('/')

@app.route('/reset', methods=['POST'])
def clear():
    session['counter'] = 0
    return redirect('/')

@app.route('/destroy_session', methods=['POST'])
def destory_session():
    session.clear()
    return redirect('/')


if __name__=="__main__":   
    app.run(debug=True)    