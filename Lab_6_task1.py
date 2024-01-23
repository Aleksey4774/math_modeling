import matplotlib.pyplot as plt
 
plt.plot([1, 1, 1], [1, 1, 5])
plt.plot([1, 1, 5], [5, 5, 5])
plt.plot([5, 5, 1], [5, 1, 1])

plt.axis('equal')

plt.savefig('fig_task1.png')