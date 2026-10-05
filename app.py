from flask import Flask, jsonify

app = Flask(__name__)

# Dados mockados dos cursos técnicos
cursos = [
    {
        "id": 1,
        "nome": "Técnico em Administração",
        "instituicao": "Escola Técnica Estadual",
        "cidade": "Dourados",
        "modalidade": "Presencial",
        "duracao": "3 semestres"
    },
    {
        "id": 2,
        "nome": "Técnico em Desenvolvimento de Sistemas",
        "instituicao": "Centro Estadual de Educação Profissional",
        "cidade": "Campo Grande",
        "modalidade": "Presencial",
        "duracao": "4 semestres"
    },
    {
        "id": 3,
        "nome": "Técnico em Enfermagem",
        "instituicao": "Escola Técnica Estadual",
        "cidade": "Três Lagoas",
        "modalidade": "Presencial",
        "duracao": "4 semestres"
    },
    {
        "id": 4,
        "nome": "Técnico em Meio Ambiente",
        "instituicao": "Centro Estadual de Educação Profissional",
        "cidade": "Corumbá",
        "modalidade": "Presencial",
        "duracao": "3 semestres"
    },
    {
        "id": 5,
        "nome": "Técnico em Ciência de Dados",
        "instituicao": "Centro Estadual de Educação Profissional",
        "cidade": "Dourados",
        "modalidade": "Presencial",
        "duracao": "4 semestres"
    }
]

@app.route("/", methods=["GET"])
def inicio():
    return jsonify({
        "mensagem": "API de Cursos Técnicos funcionando",
        "endpoints": [
            "GET /cursos",
            "GET /cursos/<id>"
        ]
    })

@app.route("/cursos", methods=["GET"])
def listar_cursos():
    """Retorna todos os cursos técnicos cadastrados."""
    return jsonify(cursos)


@app.route("/cursos/<int:curso_id>", methods=["GET"])
def buscar_curso(curso_id):
    """Retorna um curso específico pelo ID."""
    curso = next((curso for curso in cursos if curso["id"] == curso_id), None)

    if curso is None:
        return jsonify({
            "erro": "Curso não encontrado",
            "id_consultado": curso_id
        }), 404

    return jsonify(curso)


if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
