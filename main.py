from flask import Flask, render_template, request

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html', resultado='')
@app.route('/verificar', methods=['POST'])
def verificar():
    fatorial = int(request.form["fatorial"])
    fator = 2
    fatorando = 0
    fatorial_ = fatorial
    while fatorial_ != fator:
        if fatorial == -1:
            break
        fatorando = fator * fatorial
        fatorial = fatorando
        fator = fator + 1

    return render_template('index.html', resultado=f'O resultado é {fatorando}')
if __name__ == '__main__':
    app.run(debug=True)