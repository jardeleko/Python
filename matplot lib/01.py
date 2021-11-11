import matplotlib.pyplot as plt

x = [1, 2, 4]
y = [2, 3, 6]
plt.title("Graphics")

plt.xlabel("T(ts)")
plt.ylabel("V(m/s)")

plt.plot(x, y)
plt.show()