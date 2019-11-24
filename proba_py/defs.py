import random 

def create_list(n):
	lista = []
	for i in range(n):
		lista.append(random.randint(0, n))

	return lista

