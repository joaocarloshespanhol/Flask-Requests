from flask import Flask, render_template, request, redirect
app = Flask(__name__)

produto = [
    ['Refrigerante', 4.50],
    ['Pizza', 2.50],
    ['Suco', 24.90],
    ['Salgado', 5.50],
    ['Lanche', 18.50]
    ] 

@app.route('/')
def index():  
    return render_template('index.html', titulo = 'Produtos', produto = produto)

@app.route('/prod/<int:id>')
def produtos(id):
    prod = produto[id]
    return render_template('produtos.html', produto = prod,id=id)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/store', methods=['POST', 'GET'])
def store():
    nome = request.form['nome']
    val = request.form['val']
    produto.append([nome, val])
    
    return redirect('/')

@app.route('/delete/<int:id>')
 def delete(id):
      del produto[id]
      return redirect('/')

if __name__ == '__main__':
    app.run()
