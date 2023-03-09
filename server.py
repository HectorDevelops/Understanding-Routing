from flask import Flask

app = Flask(__name__)

# home page output
@app.route('/')
def hello_world():
    return 'Hello World!'

# dojo route that returns 'Dojo!' 
@app.route('/dojo')
def dojo():
    return 'Dojo!'

# route that greets input variable name
@app.route('/say/<name>')
def say(name):
    print(name)
    # adding the built-in function title() to capitalize the first character of the name
    return 'Hi ' + name.title(), '!'

# route will display the name variable number times in our page
@app.route('/repeat/<int:number>/<name>')
def repeat(number, name):
    return f'{name} ' * number

if __name__=="__main__":
    app.run(debug=True)
