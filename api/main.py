from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def homePage():
    return render_template('index.html')


@app.route('/saque')
def saque():
    return render_template('saque.html')


@app.route('/maquinas')
def maquinas():
    return render_template('maquinas.html')


@app.route('/conta')
def conta():
    return render_template('conta.html')

@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')



@app.route('/login')
def login():
    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
