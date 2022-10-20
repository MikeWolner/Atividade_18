# Importar a classe Flask e o objeto request:
from flask import Flask, request
# Criar o objeto Flask app:
app = Flask(__name__)
# http://127.0.0.1:5000/teste/1
# Aceita requisições com o método POST.
# O corpo da requisição deve conter um objeto JSON
# como o apresentado abaixo:
# {
# "x" : 3,
# "y" : 4,
# "z" : 5
# }
@app.route('/teste/1', methods=['POST'])
def teste_triangulo():
    objeto_json = request.get_json()
    
    
    # EXERCÍCIO NUMERO 1
    
    
    # Verificar se o ojeto no formato JSON é NULL.
    '''if objeto_json is not None:
        if 'x' in objeto_json:
            x = objeto_json['x']
        if 'y' in objeto_json:
            y = objeto_json['y']
        if 'z' in objeto_json:
            z = objeto_json['z']
    
    resp = 'triangulo invalido'
    
    # Testando se é triângulo
    if (x + y > z) and (x + z > y) and (y + z > x):
        if (abs(x - y) < z) and (abs(x - z) < y) and (abs(y - z) < x):
            resp = 'triangulo valido'     

    return resp
            
if __name__ == '__main__':
    # Executar app no modo debug (default) na porta 5000 (default):
    app.run(debug = True, port = 5000)'''
    
    
    #EXecício Número 2
    
   ''' apagar = 0
while True:
    código = int(input("Código da mercadoria (0 para sair): "))
    preço = 0
    if código == 0:
        break
    elif código == 1:
        preço = 99.99
    elif código == 2:
        preço = 103.89
    elif código == 3:
        preço = 49.98
    elif código == 4:
        preço = 89.72
    elif código == 5:
        preço = 97.35
    else:
        print("Código inválido!")
    if preço != 0:
        quantidade = int(input("Quantidade: "))
        apagar = apagar + (preço * quantidade)
print(f"Total a pagar R${apagar:8.2f}")'''
    
    
