from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():

    return render_template("index.html")

@app.route("/cadastro")
def cadastro():
    return render_template("cadastro.html")  # Aqui deve estar o formulário de cadastro de alunos

@app.route("/cadastro", methods=['GET', 'POST'])
def validar_produto():
    nome = request.form["nome_aluno"]

    nota1 = float(request.form["nota1"])  
    nota2 = float(request.form["nota2"])  
    nota3 = float(request.form["nota3"])  

    media = (nota1 + nota2 + nota3) /3

    if media >= 7:
        status = "Aprovado"
    elif media >= 3:
        status = "Recuperação"
    else:
        status 
    caminho_arquivo = 'models/notas.txt'  # Mudança para notas.txt

    with open(caminho_arquivo, 'a') as arquivo:
        arquivo.write(f"{nome};{nota1};{nota2};{nota3};{media};{status}\n")

    return redirect("/cadastro")

@app.route("/notas")
def consulta_notas():
    notas = []
    caminho_arquivo = 'models/notas.txt'

    with open(caminho_arquivo, 'r') as arquivo:
        for linha in arquivo:
            item = linha.strip().split(';')
            if len(item) == 6:  # Verifica se a linha contém 5 elementos
                notas.append({
                    'nome': item[0],
                    'nota1': item[1],
                    'nota2': item[2],
                    'nota3': item[3],
                    'media': item[4],
                    'status': item[5]
                })

    return render_template("media_aluno.html", prod=notas)

@app.route("/excluir_produto", methods=['GET'])
def excluir_produto():
    linha_para_excluir = int(request.args.get('linha')) 
    caminho_arquivo = 'models/notas.txt'  # Mudança para notas.txt
    
    with open(caminho_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
    
    del linhas[linha_para_excluir]  

    with open(caminho_arquivo, 'w') as arquivo:
        arquivo.writelines(linhas)

    return redirect("/notas")

if __name__ == "__main__":

    app.run(host='127.0.0.1', port=80, debug=True)
