import random 

def sllist_insert(list, x):
	return lista.append(x)

def sllist_sort(list):
	return lista.sort()

def sllist_reverse(list):
	return lista.reverse()

def sllist_remove(list, x):
	return lista.remove(x)

def sllist_print(list):
	for x in range(0,10):
		print(lista[x])


lista = []

for x in range(0,10):
	x = input("key:\n")
	sllist_insert(lista, x);

print(lista)

sllist_sort(lista)
print(lista)

sllist_reverse(lista)
print(lista)

sllist_print(lista)

x = input()
sllist_remove(lista, x)

print(lista)