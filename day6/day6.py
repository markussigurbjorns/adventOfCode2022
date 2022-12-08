

f = open("input.txt", "r")
x = f.read()
f.close()
d = dict()
for i in range(len(x)):
    d.clear()
    slice= (x[i:i+14])
    for c in slice:
        d[c] = c
    if len(d) == 14:
        print(i+14)
        break

