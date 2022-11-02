import time
start_time = time.time();

n, k = map(int,input().split())
ctr = 0
while(n>1):
    if (n%k) != 0:
        ctr = (n - n//k)
    n = n//k
    ctr += 1

end_time = time.time()
print(ctr)
print("소요 시간: " , (end_time - start_time))
    


    
