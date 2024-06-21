from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

produtos = []

@app.route('/')
def listar_produtos():
    produtos_ordenados = sorted(produtos, key=lambda x: x['valor'])
    return render_template('lista_produtos.html', produtos=produtos_ordenados)

@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrar_produto():
    if request.method == 'POST':
        nome = request.form['nome']
        descricao = request.form['descricao']
        valor = float(request.form['valor'])
        disponivel = request.form['disponivel'] == 'sim'
        
        produto = {
            'nome': nome,
            'descricao': descricao,
            'valor': valor,
            'disponivel': disponivel
        }
        produtos.append(produto)
        return redirect(url_for('listar_produtos'))
    return render_template('cadastrar_produto.html')

if __name__ == '__main__':
    app.run(debug=True)