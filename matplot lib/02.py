import matplotlib.pyplot as plt

#comparando o consumo de água no inicio de 2 meses seguidos 

x = [1, 3, 5, 7, 9]
y = [2, 3, 7, 1, 4]

x1 = [2, 4, 6, 8, 10]
y1 = [4, 6, 2, 8, 10]

#title graph
plt.title('Graphics')

#Ox 
plt.xlabel("DIA")

#Oy
plt.ylabel("Consumo m³")

plt.bar(x, y, label="fev")
plt.bar(x1, y1, label="mar")
plt.legend()
plt.show()