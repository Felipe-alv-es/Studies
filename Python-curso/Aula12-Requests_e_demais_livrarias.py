import requests

#C:\Users\Felipe\PycharmProjects\Python-curso>pip install requests - para instalar o requests

#O site http://viacep.com.br/ws/05729110/json/ mostra os demais dados referentes ao cep

def consulta_cep():
    cep = input('Insira um CEP a para ser consultado: ')
    response = requests.get('http://viacep.com.br/ws/{}/json/' .format(cep))  #Com esse get, ele pega a função do via cep de calcular o cep
    print(response.status_code)  #Quando restorna o status code 200, significa que deu certo, caso retorne 400, de errado
    print(response.text)
    dados_cep = response.json()
    #print(dados_cep['logradouro']) #Quando você atribui o response.jason pra uma variavel, é possível exibir apenas um valor dela, conforme o codigo informado

def consulta_response():
    url = input('Informe um site para consultar seus codigos: ')
    response = requests.get(url)
    print(response.text)

if __name__ == '__main__':
    #consulta_cep()
    consulta_response()