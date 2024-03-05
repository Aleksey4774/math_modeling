import matplotlib. pyplot as plt 
import numpy as np 
from matplotlib. animation import FuncAnimation

def circle(a, t):
    R = a * t
    alpha = np. arange (0, 2*np.pi, 0.01)
    x = R*np. cos (alpha)
    y = R*np. sin (alpha)
    return x, y

def animate (i):
    ball.set_data(circle(a = 0.1, t=i))


if __name__ == ' _main__':
    fig, ax = plt. subplots ()
    ball, = plt. plot([], [], 'o', color = 'b')
    plt.axis ('equal')
    
    ax. set_xlim (-10, 10) 
    ax. set_ylim (-10, 10)

    ani = FuncAnimation(fig,
                        animate, 
                        frames=20, 
                        interval=50
                        )
    
    ani.save('fig_task2.gif')