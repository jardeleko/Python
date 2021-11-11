import matplotlib.pyplot as plt

#dispersão de pontos

x = [1, 3, 5, 7, 9]
y = [2.21, 3.31, 7.10, 1.21, 4.1230]

#title graph
plt.title('Scatterplot')

#Ox 
plt.xlabel("Ox")
#Oy
plt.ylabel("amostra")

plt.plot(x, y, color="k", linestyle="--")
plt.scatter(x, y, label="Points", color='purple', marker="h", s=100)
#colocando arestas nos pontos
plt.legend()
plt.show()

plt.savefig("figura1.png", dpi="144")