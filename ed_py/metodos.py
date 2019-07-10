""" metodos disponiveis em python
para listas dinamicas 
"""
lista = []
lista2 = [12, "a", 64]
lista.insert(0, 12)
x = input()
lista.append(x) #insere novo elemento 
print(lista)
lista.extend(lista2) #concatena
print(lista)
y = input()
lista.remove(y) #percorre e remove
print(lista)
lista.pop() #remove da pilha /ou ultimo inserido 
print(lista)
z = input() 
print(lista.index(z))#pega o indice caso o dado exista no array 
print(lista.count(12))
