N = int(input())
conlist = []
for i in range(N):
    tmpList = list(map(int,input().split()))
    conlist.append(tmpList)

conlist.sort(key = lambda x:x[0])
conlist.sort(key = lambda x:x[1])

ctr = 0
end_time = 0
for st, ed in conlist:
    if(st>=end_time):
        end_time = ed
        ctr+=1
        
        
print(ctr)
