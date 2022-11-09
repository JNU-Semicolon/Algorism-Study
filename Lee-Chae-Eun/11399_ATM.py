### [문제 분석]
# 목적 : 각 사람이 돈을 인출하는데 필요한 시간의 합의 최솟값 구하기 (!주의 ATM은 1개밖에 없음!)
# -> 각 손님의 대기시간의 총합 줄이기

### [문제 풀이]
# 1단계 : 손님의 수(n)와, 각 손님의 대기시간 리스트를 입력받는다. 
# 2단계 : 대기시간 리스트를 오름차순으로 정렬한다.
# 3단계 : 각 손님의 대기 시간의 총합을 구한다.

# 손님의 수 입력한다.(5)
n = int(input())

# 각 손님의 대기시간을 입력한다. (3 1 4 3 2)
times = list(map(int, input().split()))

# 오름차순 정렬한다.
times.sort()

# 만약 내림차순 정렬하고 싶다면?
# times.sort(reverse = True)

time = 0
sum = 0

# n만큼(5명만큼) 반복하면서 
for i in range(n):
    time = time + times[i]
    sum = time + sum
    
print(sum)