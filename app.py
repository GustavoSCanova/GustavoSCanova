from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/sobre')
def sobre():
    return "<h1>Sobre Nós</h1><p>A empresa Contra Tempo atende ao público de transporte, se comprometendo com a melhoria contínua e a satisfação dos seus usuários, está implementando uma nova funcionalidade em seu aplicativo: a opção para envio de feedbacks. Essa iniciativa visa estabelecer uma comunicação direta com os passageiros, permitindo que compartilhem sugestões, elogios ou críticas sobre o serviço. Com essas informações, a empresa poderá identificar áreas de melhoria, adaptar-se melhor às necessidades do público e aprimorar a qualidade do atendimento, garantindo uma experiência de transporte mais eficiente, segura e confortável para todos os usuários.</p>"

if __name__ == '__main__':
    app.run(debug=True)
