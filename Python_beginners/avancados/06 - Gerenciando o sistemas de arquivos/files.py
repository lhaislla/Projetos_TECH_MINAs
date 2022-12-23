from pathlib import Path
cwd = Path.cwd()

demo_file = Path(Path.joinpath(cwd, 'demo.txt'))

# Pega o nome do arquivo
print('\nfile name: ' + demo_file.name)
# Pega a extensão
print('\nfile suffix: ' + demo_file.suffix)

# Pegue a pasta
print('\nfile folder: ' + demo_file.parent.name)
# Obter o tamanho
print('\nfile size: ' + str(demo_file.stat().st_size) + '\n')