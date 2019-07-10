def f(x):
	return x % 2 != 0 and x % 3 != 0 

def cubo(x):	 	
	return x * x * x

def soma(x, y):	return x+y

filter(f, range(2, 25)) 

map(cubo, range(1,11)) # aplica a função a todos os valores da sequencia
seq = range(8)
map(soma, seq, seq)
#[0, 2, 4, 8, 10, 12,14]
map(Nome, range(5))
#[0, 1, 2, 3, 4]
map(None, range(5), range(3))
#[(0,0), (1, 1), (2, 2), (3, None),(4, None)]
zip(range(5), range(3))
#[(0,0), (1, 1), (2, 2)]
reduce(soma, range(1,11))
#55
