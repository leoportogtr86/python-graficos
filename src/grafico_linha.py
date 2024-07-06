import matplotlib.pyplot as plt

x = ["1°", "2°", "3°", "4°"]
y = [7, 8.5, 9.1, 10]

plt.plot(x, y, color="blue", linestyle="--", marker="o")
plt.xlabel("Trimestre")
plt.ylabel("Nota")
plt.grid(True)
plt.savefig("grafico.png")
plt.title("Notas Por Trimestre")
plt.show()
