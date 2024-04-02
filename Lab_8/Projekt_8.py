import matplotlib. pyplot as plt 
import numpy as np 
from matplotlib. animation import FuncAnimation
import warnings
import matplotlib
warnings.filterwarnings("ignore", category=matplotlib.MatplotlibDeprecationWarning)

def planet(R, angle_vel, time):
    alpha = angle_vel * np.pi / 180 * time
    x = R * np.cos(alpha)
    y = R * np.sin(alpha) * 0.8
    return x, y

def animate(i):
    ball.set_data(planet(R=10, angle_vel=1, time=i))

    ax.set_title("Движение вокруг солнца")

if __name__ == '__main__':
    fig, ax = plt.subplots()
    plt.grid()
    plt.plot([0], [0], "o", color = "orange", ms = 10)
    ball, = plt.plot([], [], 'o', color='blue', label='Ball')

    edge = 12

    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    ani = FuncAnimation(fig,
                        animate,
                        frames=360,
                        interval=30)
    
    ani.save('project.gif') 