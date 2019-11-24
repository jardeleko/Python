from collections import deque

lista = ['abacaxi', 'melancia', 'abacate']
lista2 = [1, 2, 3, 4, 5, 6, 78]
print(lista)
print(lista2)

lista = lista + lista2

print(lista)
print(lista[2])
 
lista.append("limao")
lista.pop()

for item in lista:
	print(item)

lista.append(32)

del lista[8:]

del lista[:] #apaga toda lista free(lista)

print(lista)

newlista = []

