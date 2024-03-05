import matplotlib.pyplot
import numpy as np

def cicloida (a=3):
    t= np.arange (0, 8, 0.1)
    
    x= a * (t - np.sin(t))
    y = a * (1 - np.cos(t))
    
    plt. plot (x, y, 1s='--', Iw=3)
    plt. axis( 'equal')
    plt.savefig('fig_task1.png')

if__name__ == ' _main__':
    cicloida ()

def astroida (r = 4):
    t = np.arange (0, 10, 0.1)
    x= r * (np.sin(t))**3
    y= r * (np.cos (t)) **3
    
    plt. plot(x, y, 1s='--', 1w=3)
    plt.axis ('equal')
    plt.savefig('fig_task1.png')

if __name__ == "__main__":
    astroida ()