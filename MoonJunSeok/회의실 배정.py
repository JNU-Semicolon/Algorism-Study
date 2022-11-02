N = int(input())
conlist = []
availList = []
for i in range(N):
    tmpList = list(map(int,input().split()))
    conlist.append(tmpList)

print(conlist)
conlist.sort(key = lambda x:x[1])
print(conlist)
availList.append(conlist[0])

for con in conlist:
    if(availList[-1][1]<=con[0]):
        availList.append(con)
        
        
print(len(availList))
print(availList)
