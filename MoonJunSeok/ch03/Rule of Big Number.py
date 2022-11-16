import time


n,m,k = map(int,input().split())
data = list(map(int,input().split()))
beginning_time = time.time()

data.sort()
big_number = data[n-1]
secondbig_number = data[n-2]

i = 0
data_sum = 0
ctr = 1
while i<m:  
    if ctr<k: 
        data_sum += big_number
        ctr += 1
        
    else:
        data_sum += secondbig_number
        ctr = 1
        
    i += 1
    

print(data_sum)
ending_time = time.time()
print(ending_time-beginning_time)
