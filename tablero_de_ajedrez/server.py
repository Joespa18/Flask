from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def tablero():
    return render_template('index.html')

@app.route('/<int:x>')
def tablero_2(x):
    return render_template('index_1.html', x=x)

@app.route('/<int:x>/<int:y>')
def tablero_3(x,y):
    return render_template('index_2.html', x=x, y=y)

if __name__=="__main__":
    app.run(debug=True)