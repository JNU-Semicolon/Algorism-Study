n = int(input())
P = list(map(int,input().split()))
atmTime = 0
P.sort()

for i in range(n+1):
    for j in range(i):
        atmTime += P[j]
        
print(atmTime)
