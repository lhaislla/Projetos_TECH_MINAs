# Abra o arquivo manage.txt para escrever o texto
stream = open('manage.txt', 'wt')

#Escreva a palavra demo no fluxo de arquivo
stream.write('demo!')

# Volte para o início do fluxo de arquivo
stream.seek(0)

#escreva a palavra legal no fluxo de arquivo
stream.write('cool')

#Esvazie o conteúdo do fluxo de arquivo para o buffer de arquivo
stream.flush()

# Libere o fluxo de arquivo e feche o arquivo
stream.close()
