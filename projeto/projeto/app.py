from flask import Flask, request, jsonify, render_template
from main import criar_novo_usuario_e_pet, ler_dados

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/usuarios", methods=["GET"])
def usuarios():
    return render_template("usuarios.html")

@app.route("/api/create", methods=["POST"])
def api_create():
    try:
        usuario = request.form.get("usuario")
        pet = request.form.get("pet")
        porte = request.form.get("porte")
        email = request.form.get("email")
        senha = request.form.get("senha")

    
        usuario = request.form.get("usuario")
        pet = request.form.get("pet")

        if not usuario:
            return jsonify({'success': False, 'error': 'Campo usuário obrigatório'}), 400
        
        resultado = criar_novo_usuario_e_pet(nome_usuario=usuario, nome_pet=pet, email=email, senha_hash=senha, porte=porte)
        
        return jsonify({'success': True, 'result': resultado}), 200
    except Exception as e:
        return jsonify({'success': False, 'result': str(e)}), 500
    

@app.route("/api/users", methods=["GET"])
def api_users():
    try:
        data = ler_dados()
        return jsonify({'success': True, 'result': data}), 200
    except Exception as e:
        return jsonify({'success': False, 'result': str(e)}), 500
    
if __name__ == "__main__":
    app.run()
        