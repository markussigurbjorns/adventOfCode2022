

f = open("input.txt", "r")

sum = 0
rucksackind = 0
rucksacks = []
for x in f:

    if rucksackind == 3:
        a = set(rucksacks[0])
        a.remove('\n')
        b = set(rucksacks[1])
        b.remove('\n')
        c = set(rucksacks[2])
        c.remove('\n')                
        union = a.intersection(b,c).pop()
        if union.islower():
            sum = sum + ord(union) - 96
        else:
            sum = sum + ord(union) - 64 + 26
        rucksacks = []
        rucksackind = 0
    rucksacks.append(x)
    rucksackind = rucksackind + 1


a = set("QTTcqJZJhHSpShhFpFzjDDwwsFzpdg")
b = set("NBMnBvmBPvwrqvgvvqgD")
c = set("bNNGmWmbbClQTQRqchhQbf")
union = a.intersection(b,c).pop()
if union.islower():
            sum = sum + ord(union) - 96
else:
            sum = sum + ord(union) - 64 + 26


    #union = set(first).intersection(set(second)).pop()
    #if union.islower():
    #    sum = sum + ord(union) - 96
    #else:
    #    sum = sum + ord(union) - 64 + 26

print(sum)

f.close()