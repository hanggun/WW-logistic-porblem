# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 11:17:56 2020

@author: s1925253
"""

import numpy as np
import csv
import matplotlib.pyplot as plt

np.random.seed(3)
#plant location
pl = np.array([10,10])

num_of_seed = 6
num_of_order = 100
four_points = [(35,40),(60,80),(80,45)]
num_of_points = [40, 30, 30]
points = []
for i,j in zip(four_points,num_of_points):
    a = np.c_[np.repeat(i[0], j , axis=0),
          np.repeat(i[1], j , axis=0)]
    a = a + np.column_stack([(np.random.randn(j)*10).reshape(-1,1), 
                        (np.random.randn(j)*10).reshape(-1,1)])
    points.append(a)
points = np.row_stack(points)
#randomly generate 3 center points
x = np.random.rand(num_of_seed) * 80 + 20
y = np.random.rand(num_of_seed) * 80 + 20

#generate 4 seed location points
x_seed = np.random.rand(num_of_seed) * 50 + 10
y_seed = np.random.rand(num_of_seed) * 50 + 10
#generate 9 random points
x1 = np.random.rand(num_of_order) * 80 + 20
y1 = np.random.rand(num_of_order) * 80 + 20

#calculate the distance
seed_location = np.c_[x,y]
order_location = points
seed_location1 = np.array([[30,20], [20,50], [60,40], [40,70], [60,80],[80,45]])
#container_location = np.c_[x2,y2]

dist = np.ones([num_of_order, num_of_seed])
#d_kj = np.ones([num_of_container_seed, num_of_order])
d_0i = np.ones([num_of_seed,1])
d_0j = np.ones([num_of_order,1])
for i in range(num_of_seed):
    for j in range(num_of_order):
        dist[j,i] = np.sqrt((order_location[j,0] - seed_location1[i,0])**2 +
            (order_location[j,1] - seed_location1[i,1])**2)

for i in range(num_of_seed):
    d_0i[i] = np.sqrt((pl[0] - seed_location1[i,0])**2 +
            (pl[1] - seed_location1[i,1])**2)
    
for i in range(num_of_order):
    d_0j[i] = np.sqrt((pl[0] - order_location[i,0])**2 +
            (pl[1] - order_location[i,1])**2)

seed_index = list(range(4))
container_index = list(range(4,6))
plt.scatter(seed_location1[seed_index,0], seed_location1[seed_index,1], c = 'pink', label = 'Seed Location')
plt.scatter(seed_location1[container_index,0], seed_location1[container_index,1], c = 'black', alpha = 1, label = 'Container Location')
plt.scatter(points[:,0], points[:,1], alpha = 0.2, label = 'Order Location')
plt.scatter(10,10, c = 'red', label = 'Plant Location')
plt.xlabel('Distance',fontdict = {'fontsize': 10})
plt.ylabel('Distance',fontdict = {'fontsize': 10})
#plt.title('Scatter plot of seed location, order location and plant location',
#          fontdict = {'fontsize': 10})
plt.legend(loc = 'upper left', fontsize = 'small')

#plt.scatter(a[:,0], a[:,1])
plt.ylim([0,110])
plt.xlim([0,110])
#plt.show()
plt.savefig('location_plot.png', dpi=300)
np.savetxt('dist.csv', dist, delimiter=',')
np.savetxt('d_0i.csv', d_0i, delimiter=',')
np.savetxt('d_0j.csv', d_0j, delimiter=',')
np.savetxt('d_ij.csv', dist.T, delimiter=',')