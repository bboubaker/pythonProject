# coding: utf-8
import matplotlib.pyplot as plt
import random
print(matplotlib.__version__)
plt.title("Fig 1")

x = [random.randint(0,150) for i in range(1000)]
n, bins, patches = plt.hist(x, 50, density=True, facecolor='b', alpha=0.5)
plt.xlabel('Mise')
plt.ylabel(u'probabilité')
plt.axis([0, 150, 0, 0.02])
plt.grid(True)

plt.show()