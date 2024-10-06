import numpy
import pandas as pd
from matplotlib import pyplot as plt
df = pd.read_csv('titanic.csv')
ages = df['Age']
l = []
for i in ages:
    l.append(int(i))
ages_list = sorted(l)
plt.hist(ages_list, bins=len(ages_list)//11, edgecolor = 'black')

plt.xlabel('Возраст')
plt.ylabel('Количество пассажиров')
mean = sum(ages_list)/len(ages_list)
mean = round(mean, 3)
sm = 0
for x in ages_list:
    sm += (x - mean)**2
std = round(numpy.sqrt(sm/len(ages_list)-1), 3)
median = numpy.median(ages_list)

plt.title('Распределение пассажиров Титаника по возрасту\n(mean = {mean}, median = {median}, std = {std})'.format(mean=mean, std=std, median=median))

print('mean =', mean, '\nstd =', std, '\nmedian =', median)

plt.show()