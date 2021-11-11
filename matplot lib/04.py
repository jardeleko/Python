import matplotlib.pyplot as plt

#crescimento da população brasileira 1980-2016
#DataSUS

dados = open("populacao_brasileira.csv").readlines()

x = []
y = []

for i in range(len(dados)):
    if i != 0:
        line = dados[i].split(";")
        x.append(int(line[0]))
        y.append(int(line[1]))

plt.title("Crescimento populacional brasileiro")
#Ox 
plt.xlabel("Ano")
#Oy
plt.ylabel("População")

plt.plot(x, y, color="k")
plt.scatter(x, y)
plt.show()