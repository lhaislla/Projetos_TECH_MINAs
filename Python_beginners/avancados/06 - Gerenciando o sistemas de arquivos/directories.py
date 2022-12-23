from pathlib import Path
cwd = Path.cwd()
# Obtém o diretório pai
parent = cwd.parent

# Isso é um diretório?
print('\nIs Isto é um  directorio? ' + str(parent.is_dir()))

# Isso é um arquivo?
print('\nIs isto é um arquivo? ' + str(parent.is_file()))

# Listar diretórios filhos
print('\n-----Conteúdo dos diretórios-----')
for child in parent.iterdir():
    if child.is_dir():
        print(child)
