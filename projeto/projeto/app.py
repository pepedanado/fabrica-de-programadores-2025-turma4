from flask import Flask, request, jsonify, render_template, redirect, url_for
from main import criar_novo_usuario_e_pet, ler_dados, remover_usuario
import json
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
    
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        try:
            data = request.get_data()
            usuario = json.loads(data)
            print(usuario)
            return jsonify({"sucess": True, "data": data}), 200
        except Exception as e:
            return jsonify({"sucess": False, "error": "Erro de servidor: " + str(e)})
    else:
        return render_template('login.html')
    
@app.route("/remover/usuarios/<id_usuario>", methods=['GET', 'DELETE'])
def remover_usuarios(id_usuario):
    if request.method == "DELETE":
        try:
            data = request.get_data()
            usuario_removido = json.loads(data)
            remover_usuario(id_usuario=usuario_removido['id_usuario'])
            print("Usuário : %s foi removido com sucesso!" % usuario_removido)
            return redirect(url_for('index'))
        except Exception as e:
            return jsonify({"sucess": False, "error": "Erro ao remover usuário "+ str(e)}), 500
    else:
        return render_template('remover_usuario.html')
    
if __name__ == "__main__":
    app.run()
        