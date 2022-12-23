try:
	stream = open('output.txt', 'wt')
	stream.write('Lorem ipsum dolar')
finally:
	stream.close() # ISSO É MUITO IMPORTANTE!!

# com open('output.txt', 'wt') como stream:
# stream.write('Lorem ipsum dolar')
