import  json

# Cria um objeto de dicionário
pessoa_dict  = { 'primeiro' : 'Lhaislla' , 'ultimo' : 'Cavalcanti' }
# Adicione pares de chaves adicionais ao dicionário conforme necessário
pessoa_dict [ 'Estado' ] = 'Pernambuco'

# Cria um objeto de lista de linguagens de programação
idiomas_list  = [ 'CSharp' , 'Python' , 'JavaScript' ]

# Adicionar objeto de lista ao dicionário para a chave de idiomas
pessoa_dict [ 'idiomas' ] =  idiomas_list

# Converter dicionário para objeto JSON
pessoa_json  =  json.dumps(pessoa_dict)

print(pessoa_json)