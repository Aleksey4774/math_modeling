import numpy as np 
import Lab_3_task1
x0 = 0
y0 = 0
v0x = 0
g = Lab_3_task1.gravity_constant

t = np.arange(0.5, 0.1)
x = x0 + v0x*t 
y = x0 + v0x*t - g * t ** 2 / 2

a = [t, x, y]
b = np.array(a)

print(type(a))
print(type(b))














