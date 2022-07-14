from flask import Flask, redirect, render_template, session
app = Flask(__name__)
app.secret_key = '1234'


@app.route('/')
def contador():
    if 'visitas' in session:
        print('la llave existe!')
        session['visitas'] +=1
    else:
        print("la llave 'key_name' NO existe")
        session['visitas'] = 1

    return render_template('index.html')

@app.route('/count')
def suma2():
    session['visitas'] += 1
    return redirect('/')


@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)