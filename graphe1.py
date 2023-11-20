# coding: utf-8
import matplotlib.pyplot as plt

plt.title("Fig 1")

plt.subplot(211)
plt.plot([50,100,150,200], [1,2,3,4], "r--", linewidth=1, marker="*", label="trajet 1")
plt.plot([50,100,150,200], [2,3,7,10], "b", linewidth=1, marker="+", label="trajet 2")
plt.plot([50,100,150,200], [2,7,9,10], "g", linewidth=1, marker="o", label="trajet 3")
plt.text(150,6.5,r'Danger')
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.axis([80, 180, 1, 10])
plt.legend()

plt.subplot(212)
plt.plot([50,100,150,200], [1,2,3,15], "r--", linewidth=1, marker="*", label="trajet 1")
plt.plot([50,100,150,200], [2,3,7,10], "b", linewidth=1, marker="+", label="trajet 2")
plt.plot([50,100,150,200], [2,7,9,10], "g", linewidth=1, marker="o", label="trajet 3")
plt.xlabel('Vitesse')
plt.ylabel('Temps')
plt.axis([80, 180, 1, 10])
plt.annotate('limite', xy=(150, 7), xytext=(165, 5.5), arrowprops={'facecolor': 'black', 'shrink': 0.05})
plt.legend(loc='upper right', fontsize='x-small')

plt.show()