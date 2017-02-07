#!/usr/bin/python3

import sys

_, operacion, operando1, operando2 = sys.argv

if len(sys.argv) != 4:
	sys.exit('Numero de argumentos no valido')
try:
	if operacion == 'suma':
		result = float(sys.argv[2]) + float(sys.argv[3])
	elif operacion == 'resta':
		result = float(sys.argv[2]) - float(sys.argv[3])
	elif opercion == 'multiplicacion':
		result = float(sys.argv[2]) * float(sys.argv[3])
	elif opercion == 'division':
		try:
			result = int(sys.argv[2]) / int(sys.argv[3])
		except ZeroDivisionError:
			print('Can not divide by 0')
			result = 'Not exist'
	print(result)
except NameError:
	print('Operation name not valid')
except IndexError:
	print('Insert parameters')


#otra forma de declarar la lista:  
#	_, operacion, operando1, operando2 = sys.argv
