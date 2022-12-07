
f = open("input.txt", "r")

su = 0
highest = 0
list = []
for x in f:
    if x == '\n':
        if su > highest:
            highest = su
        list.append(su)
        su = 0
    else:
        su = su + int(x)  
f.close
list.sort()
xx = list[-3:]

print(sum(list[-3:]))

