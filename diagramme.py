# coding: utf-8
import matplotlib.pyplot as plt
import random
print(matplotlib.__version__)
plt.title("Fig 1")

name = ['-18', '18-25','25-50','50+']
data = [5000, 26000, 21400, 12000]
explode = (0, 0.15, 0, 0)
plt.pie(data, explode= explode, labels=name, autopct='%1.1f%%', startangle=90, shadow=True)
plt.axis('equal')
plt.show()