from classDiagnostico import *
from classPerguntas import *

#Inferência
se = Diagnostico()
pergunta = Pergunta()


while se.probabilidade() != 100:
	string = pergunta.texto()
	se.pergunta(string[0], string[1])
	print('probabilidade é %d' %(se.probabilidade()))
	print(se.resultado)
	if se.probabilidade() == 100:
		print('Arte mais indicado para você é: ',se.resultado[0])
		if(se.resultado[0] == 'surrealista'):
			print("Pintores relacionados:\n Vicente Van Gogh \n Salvador Dalí \n Pablo Picasso \n")
		elif(se.resultado[0] == 'renascentista'):
			print("Pintores relacionados:\n Michelangelo \n Leonardo da Vinci \n Rafael \n")
		elif(se.resultado[0] == 'minimalista'):
			print("Pintores relacionados:\n Donald Judd \n Yayoi kusama \n Frank Stella \n")
		elif(se.resultado[0] == 'artdigital'):
			print("Pintores relacionados:\n Mike Winkelmann \n Banksy \n Giselle Beiguelman \n")
