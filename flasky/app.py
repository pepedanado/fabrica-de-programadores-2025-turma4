from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

@app.route('/example', methods=['GET', 'POST'])
def example():
    if request.method == 'GET':
        return jsonify({"message": "Este é um copo (body) de uma requisição GET"})
    elif request.method == 'POST':
        data = request.json
        return jsonify({"message": "Esta é uma requisição POST!", "data": data})

@app.route('/pepe')
def pepe():
    return '<h1>Vambora negão!</h1>'

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)


@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
    # the code below is executed if the request method
    # was GET or the credentials were invalid
        return render_template('login.html', error=error)
print(['username1', 'password'])


        