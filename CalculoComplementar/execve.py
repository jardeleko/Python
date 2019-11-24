import csv
import numpy as np 
import pylab as plt 
from scipy import integrate

#x = np.linspace(0, 10, 21)


# fig, axes = plt.subplots(1,2, figsize=(12,4))
# axes[0].plot(x, y)
# axes[0].set_xlabel('X')
# axes[0].set_ylabel('F(X)')
# axes[1].fill_between(x,y)
# axes[1].set_xlabel('X')
# axes[1].set_ylabel('F(X)')

# plt.show()

# Trapezoidal 
# def y(x):
# 	return x**2-5*x+6
# N = 10000
# a = 0.0
# b = 10.0
# h = (b-a)/N

# constante = 0.5*((y(a)+y(b)))
# soma = 0
# for k in range(1, N):
# 	soma +=y(a+k*h)
# I = h*(constante+soma)

# print(I)

# print(np.trapz([1,2,3]))
# print(np.trapz([1,2,3]))

# #Lista 4
# # Exercicio 1 

# x = np.linspace(0, 10, 10000)
# y = x**2-5*x+6
# N = 10000
# a = 0.0
# b = 10.0
# h = ((b-a)/N)
# result = np.trapz(y, dx=h)
# print(result)

# Exercicio 2

# Data = []

# with open('04-Integral/Queda-livre.csv', 'r') as entrada:
# 	ler = csv.reader(entrada)
# 	next(ler)

# 	for linha in ler:
# 		for i in range(len(linha)):
# 			linha[i] = float(linha[i])
# 		Data.append(linha)
# tempo = []
# acelaracao = []

# for i in Data:
# 	t, a = i
# 	tempo.append(t)
# 	acelaracao.append(a)

# N = len(tempo)
# a = tempo[0]
# b = tempo[N-1]
# h = ((b-a)/N)

# velocidade = np.empty(N)
# velocidade[0] = 0
# varMax = velocidade[N-1]

# for k in range(1, N):
# 	velocidade[k] = velocidade[k-1]+(acelaracao[k-1]+acelaracao[k])*(h/2)

# print(velocidade[k])
# print(velocidade[N-1])

#Exercicio 3
tempo,velocidade = np.loadtxt('04-Integral/velocities.txt',unpack=True)

x = np.linspace(0,10,11)
y=x**2-5*x+6

N = len(tempo)
a = tempo[0]
b = tempo[N-1]
h = (b-a)/N

#USANDO NUMPY
distancia2=np.trapz(velocidade,dx=h)
print(distancia2)

I2 = integrate.simps(y,dx=h) 
print(I2)