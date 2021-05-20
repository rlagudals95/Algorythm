
# arr= [0 for i in range(101)]

# arr[1] = 1
# arr[2] = 1
# arr[3] = 1

# for i in range(0,98): #또 반복문을 돌려줘야 i가 증가하는 상황을 만들어 줄 수 있음
#   arr[i+3] = arr[i]+arr[i+1] 
# T = int(input())

# for i in range(T):
#     n = int(input())
#     print(arr[n])




s = [0 for i in range(101)]  # s = 0,0,0,0,0,0,0 .............

s[1] = 1 
s[2] = 1
s[3] = 1 # s = [0,1,1,1,00000000000000000]


for i in range(0,98): # 0,1,2,3,4.....97
    s[i+3] = s[i]+s[i+1] # 1,1,1,2,2,3,4,5,7,9  규칙
# s[3]/1 = s[0]/0 +  s[1]/1 , ................
T = int(input())

for _ in range(T): # 2번의 테스트 케이스
    n = int(input()) #
    print(s[n]) # n을 넣으면 s의 몇번째 정렬일까?


