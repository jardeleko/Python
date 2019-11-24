#from statistics import *
""" Bibliotecas nativas do python statistics
mean(lista)
median(lista)
mode(lista):"""

def _mean(lista):
	mean = sum(lista)/float(len(lista))
	return mean

def median(lista):
	ol = sorted(lista)
	t = len(ol)

	if t % 2 == 0:
		median = (ol[int(t/2)]+ol[int(t/2)-1])/2
	elif	 t % 2 == 1:
		median = ol[int(t/2)+0.5]

	return median

def mode(lista):
	glossary = {}
	for x in lista:
		if(x not in glossary):
			glossary[x] = 1
		else:
			glossary[x] +=1

	count = max(glossary.values())

	for i in glossary:
		if(glossary[i] == count): return i