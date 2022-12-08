import re
import numpy as np

f = open("/home/markussigurbjornsson/Documents/adventOfCode2022/day5/input.txt", "r")

readData = 0
res=""
data =[]
lists = []
for x in f:
    if readData < 8:
        data.append([x[1],x[5],x[9],x[13],x[17],x[21],x[25],x[29],x[33]])
        readData =readData + 1
    else:
        break
data_t = [list(x) for x in zip(*data)]

for i in range(len(data_t)):
    lists.append([ele for ele in data_t[i] if ele not in {' '}])
    lists[i].reverse()


for x in f:break
for x in f:
    numbers = re.findall(r'\d+',x)
    tmp = []
    for i in range(int(numbers[0])):
        print(i)
        p = lists[int(numbers[1])-1].pop()
        print(p)
        tmp.append(p)
    tmp.reverse()
    lists[int(numbers[2])-1].extend(tmp)
    print(lists)
f.close()

#print(lists)
for i in range(len(lists)):
    res = res + lists[i].pop()

print(res)