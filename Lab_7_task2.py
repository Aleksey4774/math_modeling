import matplotlib. pyplot as plt 
import numpy as np 
from matplotlib. animation import FuncAnimation

def circle(a, t):
    R = a * t
    alpha = np. arange (0, 2*np.pi, 0.01)
    x = R*np. cos (alpha)
    y = R*p. sin (alpha)
    return x, y

def animate (1):
    ball.set_data(circle(a = 0.1, t=i))


if __name__ == ' _main__':
    plt.axis ('equal')
    fig, ax = plt. subplots ()
    ball, = plt. plot([], [], '-', color=
    
    ax. set_xlim (-6, 6) 
    ax. set_ylim (-6, 6)

    ani = FuncAnimation(fig,
                        animate, 
                        frames=20, 
                        interval=50
    ani save( 'Lab_7_task_2.gif')