from flask import Flask
app = Flask(__name__)

@app.route('/0')
def index():
    return '<h1Hello World!</h1>'

@app.route('/pepe')
def pepe():
    return '<h1>Vambora negão!</h1>'

@app.route('/home')
def home():
    return '<h1>Nois é zika memo!</h1>'



if __name__ == '__main__':
    app.run()

app.add_url_rule('/', 'index', index)