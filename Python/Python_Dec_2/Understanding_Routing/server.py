from flask import Flask  
app = Flask(__name__)    
@app.route('/')          
def hello_world():
    return 'Hello World!'  

@app.route('/success')
def success():
    return "success"

# 1.
@app.route('/hello')
def hello():
    return "hello"

# 2.
@app.route('/dojo')
def dojo():
    return "dojo!"

# 3.
@app.route('/say/flask')
def sayflask():
    return "Hi flask"

@app.route('/say/michael')
def saymichael():
    return "Hi michael"

@app.route('/say/john')
def sayjohn():
    return "Hi john"  

# 4.
@app.route('/repeat/<int:num>/<string:word>')
def repeat_word(num, word):
    output = ''

    for i in range(0,num):
        output += f"<p>{word}</p>"

    return output

if __name__=="__main__":    
    app.run(debug=True)