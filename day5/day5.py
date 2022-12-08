import re
import numpy as np

f = open("input.txt", "r")

readData = 0

data =[]

for x in f:
    if readData < 8:
        data.append([x[1],x[5],x[9],x[13],x[17],x[21],x[25],x[29],x[33]])
        readData =readData + 1
    else:
        break
data_t = [list(x) for x in zip(*data)]
data_t[0].remove(' ')
print(data_t[0])

list1 = [ele for ele in data_t[0] if ele not in {' '}]
list1.reverse()
print(list1.pop())

for x in f:
    numbers = re.findall(r'\d+',x)
    #print(numbers)
f.close()