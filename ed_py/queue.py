from collections import deque

def insert_queue(lista, x):
	return lista.append(x)

def remove_dequeue(lista):
	return lista.popleft()

lista = deque(['maggie', 'cxh', ':B', 'hesawjoys'])
x = input()

insert_queue(lista, x)
print(lista)
remove_dequeue(lista)
print(lista)