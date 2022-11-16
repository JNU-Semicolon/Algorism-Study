n, k = map(int, input().split())
coin = []
coinNum = 0

for i in range(n):
    x = int(input())
    coin.append(x)

coin.reverse() 

for i in coin:
    if (k//i) != 0:
        coinNum += (k//i)
        k %= i
        
print(coinNum)
