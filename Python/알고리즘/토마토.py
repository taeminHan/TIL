import numpy as np

col, row = input().split(" ")
box = []
for i in range(int(row)):
    box.append(input().split(" "))

npbox = np.array(box)

a = np.where(npbox == '1')
coordinate = []
for i in range(0, len(a[0]) + 1):
    a[i]