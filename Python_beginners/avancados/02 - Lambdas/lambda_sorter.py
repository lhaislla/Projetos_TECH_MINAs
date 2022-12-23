# Ordenar alfabeticamente
apresentadores = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

apresentadores.sort(key=lambda item: item['name'])
print('-- alphabetically --')
print(apresentadores)

# Ordena pelo tamanho do nome (do menor para o maior)
apresentadores.sort(key=lambda item: len(item['name']))
print('-- length --')
print(apresentadores)
