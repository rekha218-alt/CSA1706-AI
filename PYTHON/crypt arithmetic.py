from itertools import permutations

letters = ('S','E','N','D','M','O','R','Y')

digits = (0,1,2,3,4,5,6,7,8,9)

for p in permutations(digits, 8):

    S,E,N,D,M,O,R,Y = p

    if S == 0 or M == 0:
        continue

    SEND = S*1000 + E*100 + N*10 + D
    MORE = M*1000 + O*100 + R*10 + E
    MONEY = M*10000 + O*1000 + N*100 + E*10 + Y

    if SEND + MORE == MONEY:

        print("SEND =", SEND)
        print("MORE =", MORE)
        print("MONEY =", MONEY)
        break
