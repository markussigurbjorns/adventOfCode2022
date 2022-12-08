import re
f = open("input.txt", "r")
sets = 0 
for x in f:
    numbers = re.findall(r'\d+',x)
    first_set = set(list(range(int(numbers[0]), int(numbers[1])+1)))
    second_set = set(list(range(int(numbers[2]), int(numbers[3])+1)))
    #if first_set.issubset(second_set) or second_set.issubset(first_set):
    #    sets = sets +1
    if any(first_set.intersection(second_set)):
        sets = sets +1
print(sets)
f.close()