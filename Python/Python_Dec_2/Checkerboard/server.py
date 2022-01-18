from flask import Flask, render_template
app = Flask(__name__) 

@app.route('/')
def checker_board():
    return render_template("index.html")

@app.route('/<int:x>')
def row(x):
    return render_template("index.html",row=x,col=8,color1='color1',color2='color2')

@app.route('/<int:x>/<int:y>')
def rowandcol(x,y):
    return render_template("index.html",row=x,col=y,color1='color1',color2='color2')


if __name__=="__main__":
    app.run(debug=True)