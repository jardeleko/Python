import matplotlib.pyplot as plt
import random as rd
 
arr = []

for i in range(100):
    x = rd.randint(0, 150)
    arr.append(x)

plt.title("Boxplot")
plt.boxplot(arr)
plt.show()