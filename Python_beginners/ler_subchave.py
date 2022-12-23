# Este código mostrará como chamar a API de Visão Computacional do Python
# Você pode encontrar documentação sobre o método Computer Vision Analyze Image aqui
# https://westus.dev.cognitive.microsoft.com/docs/services/5adf991815e1060e6355ad44/operations/56f91f2e778daf14a499e1fa

# Use a biblioteca de solicitações para simplificar a chamada da API REST do Python
import requests


# Vamos precisar da biblioteca json para ler os dados passados
# pelo serviço web
import json

# Precisamos do endereço do nosso serviço de Visão Computacional
vision_service_address = "https://canadacentral.api.cognitive.microsoft.com/vision/v2.0/"
# Adicione o nome da função que queremos chamar ao endereço
address = vision_service_address + "analyze"

# De acordo com a documentação para a função de análise de imagem
# Existem três parâmetros opcionais: idioma, detalhes e recursos visuais
parameters  = {'visualFeatures':'Description,Color',
               'language':'en'}

# Precisamos da chave para acessar nosso Serviço de Visão Computacional
subscription_key = "xxxxxxxxxxxxxxxxxxxxxxx"

# Abra o arquivo de imagem para obter um objeto de arquivo contendo a imagem para analisar
image_path  =  "./TestImages/PolarBear.jpg"
image_path = "./TestImages/PolarBear.jpg"
image_data = open(image_path, 'rb').read()

# De acordo com a documentação para a função de análise de imagem
# precisamos especificar a chave de assinatura e o tipo de conteúdo
# no cabeçalho HTTP. Content-Type é application/octet-stream quando você passa uma imagem diretamente
headers    = {'Content-Type': 'application/octet-stream',
              'Ocp-Apim-Subscription-Key': subscription_key}

# De acordo com a documentação para a função de análise de imagem
# usamos HTTP POST para chamar esta função
response = requests.post(address, headers=headers, params=parameters, data=image_data)


# Gera uma exceção se a chamada retornar um código de erro
response.raise_for_status()

# Exibe os resultados JSON brutos retornados
results = response.json()
print(json.dumps(results))

# Imprima o valor para dominanteColorBackground das chaves de cor
print()
print('dominantColorBackground')
print(results['color']['dominantColorBackground'])