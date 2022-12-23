# Este código retornará um erro porque o método sort não sabe
# qual campo do apresentador usar ao classificar
apresentadores = [
    {'name': 'Susan', 'age': 50},
    {'name': 'Christopher', 'age': 47}
]

apresentadores.sort()
print(apresentadores)
