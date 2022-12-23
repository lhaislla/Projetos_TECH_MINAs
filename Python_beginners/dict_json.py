import  json

# Cria um objeto de dicionário
pessoa_dict = { 'primeiro' : 'Lhaislla' , 'ultimo' : 'Cavalcanti' }
# Adicione pares de chaves adicionais ao dicionário conforme necessário
pessoa_dict[ 'Estado' ] = 'Pernambuco'
# Converter dicionário para objeto JSON
pessoa_json  =  json.dumps(pessoa_dict)
# Imprime o objeto JSON
print(pessoa_json)