import math
#1
a = input()
a = int(a)
if a > 17 : print("maior")
else: print("menor")
print("\n")

#2
a = int(input())
b = int(input())

mean = 0
mean = (a+b)/2

if mean >= 6: print("A")
else: print("R")

print(mean)
print("\n")

#3
#math.sqrt(var)

a = int(input())
b = int(input())
c = int(input())

delta = ((b*b)-4*(a*c))

delta = math.sqrt(delta)

x1 = -b+delta/(2*a)
x2 = -b-delta/(2*a)

print(x1)
print(x2)

#4

def ol(lista):
	return lista.sort()


lista = [2, 25, 43]
ol(lista)

print(lista)

#5

def operation(a, b, op):
	if(op == "*"): return a*b 
	elif(op == "/"): return a/b
	elif(op == "+"): return a+b
	else: return a-b

a = int(input())
b = int(input())

op = input()

aux = operation(a, b, op)
print(aux)