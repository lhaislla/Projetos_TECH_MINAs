import  json

# Cria um objeto de dicionário
pessoa_dict  = { 'primeiro' : 'Lhaislla' , 'ultimo' : 'Cavalcanti' }
# Adicione pares de chaves adicionais ao dicionário conforme necessário
pessoa_dict [ 'Estado' ] = 'Pernambuco'

# criar um dicionário de pessoal
# designar uma pessoa para um cargo de gerente de programa
staff_dict  = {}
staff_dict [ 'Gerente de Programa' ] = pessoa_dict
# Converter dicionário para objeto JSON
staff_json  =  json.dumps(staff_dict)

# Imprime o objeto JSON
print(staff_json) 