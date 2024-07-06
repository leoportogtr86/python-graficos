import matplotlib.animation as animation

fig, ax = plt.subplots()
x = [0]
y = [0]

def update(frame):
    x.append(frame)
    y.append(frame**2)
    ax.clear()
    ax.plot(x, y)

ani = animation.FuncAnimation(fig, update, frames=range(10), repeat=False)
plt.show()
