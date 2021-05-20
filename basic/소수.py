import math

start_num, last_num = map(int, input().split())
nums = {x for x in range(start_num, last_num+1) if x == 2 or x % 2 ==1} # nums = 2와 홀수로 이루어진 집합

for odd_num in range(3, int(math.sqrt(last_num))+1, 2):  # 3부터 last_num제곱근의 범위에서 홀수만
    nums -= {i for i in range(2 * odd_num, last_num + 1, odd_num)}
    # for문이 반복되는 동안 홀수의 배수로 이루어진 집합을 빼줌
    
for sosu in sorted(nums) :  
    if sosu > 1 :
        print(sosu)  # 오름차순으로 정렬해서 하나씩 출력