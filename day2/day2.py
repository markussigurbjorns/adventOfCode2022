
def summ(him):
    if him == 'A':return 1 
    if him == 'B':return 2
    if him == 'C':return 3

def summm(him):
    if him == 'A':return 2
    if him == 'B':return 3
    if him == 'C':return 1

def lose(him):
    if him == 'A':return 3
    if him == 'B':return 1
    if him == 'C':return 2

def winwin(him, me):
    if me == 'X':
        return lose(him)
    if me == 'Y':
        return 3 + summ(him)
    if me == 'Z':
        return 6 + summm(him)

def win (him, me):
    if him == 'A' and me == 'Z' or him == 'B' and me == 'X' or him == 'C' and me == 'Y':
        return 0
    if him == 'A' and me == 'Y' or him == 'B' and me == 'Z' or him == 'C' and me == 'X':
        return 6
    else: return 3
        
f = open("input.txt", "r")
score = 0
for x in f:
    print('him: ', x[0], 'me: ', x[2])
    him = x[0]
    me = x[2]
    #if me == 'X':score = score + 1 
    #if me == 'Y':score = score + 2
    #if me == 'Z':score = score + 3
    score = score + winwin(him,me)
f.close()
print(score)


