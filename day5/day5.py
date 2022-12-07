import re

f = open("input.txt", "r")

for x in f:
    numbers = re.findall(r'\w+',x)
    print(numbers)

f.close()