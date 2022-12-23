# Python 3.6 ou superior
# Pegue a biblioteca
from pathlib import Path

# Qual é o diretório de trabalho atual?
cwd = Path.cwd()
print('\nCurrent working directory:\n' + str(cwd))

# Crie um nome de caminho completo juntando caminho e nome de arquivo
new_file = Path.joinpath(cwd, 'new_file.txt')
print('\nFull path:\n' + str(new_file))

# Verifica se o arquivo existe
print('\nDoes that file exist? ' + str(new_file.exists()) + '\n')