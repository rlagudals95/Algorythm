import sys
from collections import Counter

N = int(input())
numbers=[]
for _ in range(N):
    numbers.append(int(sys.stdin.readline()))

#산술평균

def avg(nums):
    return sum(nums)//len(nums)

#중앙값

def mid(nums):
    nums.sort() # 정렬을 오름차순으로 
    mid = nums[len(nums)//2] #nums 가 홀수
    return mid

def often(nums):
    if N == 1 :return nums[0]
    c=Counter(nums).most_common(2) #nums 정렬안의 개수가 많은 순서로 정렬
                                   #Counter('hello world').most_common() # [('l', 3), ('o', 2), ('h', 1), ('e', 1), (' ', 1), ('w', 1), ('r', 1), ('d', 1)]
    return (c[1][0] if c[0][1] == c[1][1] else c[0][0])

def site(nums):
    answer = max(nums) - min(nums)

    return answer

print(avg(numbers))
print(mid(numbers))
print(often(numbers))
print(site(numbers))

# import sys
# from collections import Counter

# N = int(input())
# numbers=[]
# for _ in range(N):
#     numbers.append(int(sys.stdin.readline()))

# #산술평균
# def am(nums):
#     return round((sum(nums)/N))
# #중앙값
# def median(nums):
#     mid = nums[len(nums)//2] # nums의 개수는 홀수
#     return mid
# #최빈값 
# def mode(nums):  
#     if N == 1:return nums[0]
#     c=Counter(nums).most_common(2)
#     return (c[1][0] if c[0][1] == c[1][1] else c[0][0])
# #범위
# def r(nums):return nums[N-1]-nums[0]

# numbers.sort()
# print(am(numbers))
# print(median(numbers))
# print(mode(numbers))
# print(r(numbers))