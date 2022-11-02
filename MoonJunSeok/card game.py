n,m = map(int,input().split())
max_list = []
for i in range(n):
        data = list(map(int,input().split()))
        min_number = 10001
        for j in data:
            min_number = min(min_number,j)
        max_list.append(min_number)

max_list.sort()
print(max_list[-1])
        
