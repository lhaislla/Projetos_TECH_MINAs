def sorter(item):
    return item['name']


apresentadores = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]
apresentadores.sort(key=sorter)
print(apresentadores)
