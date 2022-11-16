T = int(input())
for i in range(T):
    n = int(input())
    ctr = 0
    while n != 0:
        if n % 2 == 1 : 
            print(ctr, end = " ")
        n //= 2
        ctr += 1