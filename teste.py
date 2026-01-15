import flask 
app = flask.Flask(__name__)    

@app.route('/')
def saudacao():
    return {'Olá, Mundo!'