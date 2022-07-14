from flask import Flask, redirect, render_template, request, session
app = Flask(__name__)
app.secret_key = 'hola'

@app.route('/')
def inicio():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    print(request.form)
    session['nombre'] = request.form['nombre']
    session['ubicacion'] = request.form['ubicación']
    session['lenguaje'] = request.form['lenguaje']
    session['comentarios'] = request.form['comentarios']
    return redirect('resultado')

@app.route('/resultado')
def resultado():
    return render_template('resultado.html')

if __name__=="__main__":
    app.run(debug=True)