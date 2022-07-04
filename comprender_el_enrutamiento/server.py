from flask import Flask
app = Flask(__name__)

# Crea una ruta raíz ("/") que responda con "¡Hola Mundo!"
@app.route('/')
def hola_mundo():
    return 'Hola mundo!'

# Crea una ruta que responda con "¡Dojo!"
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# Crea una ruta que responda con "Hola" y el nombre que esté en la URL después de /say/
@app.route('/say/<string:name>')
def say_name(name):
    return f"Hola {name.capitalize()}!"

# Crea una ruta que responda con la palabra dada repetida tantas veces como se especifique en la URL
@app.route('/repetir/<string:toto>/<int:num>')
def repetir(toto, num):
    return f"{toto * num}"

if __name__=="__main__":
    app.run(debug=True)