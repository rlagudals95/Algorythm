# n = int(input())

# s = str(666)

# print(int(str(n-1) +str(666)) )

# n = int(input()) # 7

# name = 666
# cnt=0
# while(True):
#     if "666" in str(name) : 
#         cnt+=1
#         if cnt == n : print(name) ; break # n , name 이 붙은 str으로 출력
    
#     name+=1

# N = int(input()) # 3 / 2 / 1 / 0
# first = 666#처음 666인 수

# while N != 0:# N 이 0이 아니면 계속 반복
#     if '666' in str(first): # 만약 666이란 문자열이 문자열(first)안에 있으면
#         N = N-1# N을 1 감소시키고
#         if N == 0:# 만약 N 이 0이면
#             break# 반복문을 탈출한다.
#     first = first + 1#first의 값을 1 증가시킨다.
# print(first)


# # 원동균 / 27조 / 1436
# # 브루트포스 - 쉽게 말하면 싹다 뒤지는 알고리즘
# # 브루트포스 문제라서 정말로 무식하게 풀었습니다.
# # 이 문제는 6이 3개 이상 붙어있어야 합니다. 딱 666만 찾는 문제가 아닙니다.
# # 일단 첫번째 666은 무조건 666이란 수이기 때문에 arr에 담았습니다.
# # 그리고 두번째 666은 1666이기 때문에 1665부터 시작했습니다.
# # 그래서 find문으로 '666'이란 수가 존재하면 반복문을 돌면서 카운트 값을 증가시킵니다.
# # 만약 카운트 값이 3보다 크거나 같으면 배열에 담아줍니다.


# import sys

# n = int(sys.stdin.readline().split()[0])
# arr = [666]
# point = 1665

# if n == 1 :
#     print(arr[0])
# else :
#     while True :
#         point += 1
#         cnt = 1
#         if str(point).find('666') != -1 :
#             numArr = list(str(point))
#             for i in range(len(numArr)) :
#                 if i > 0 :
#                     if numArr[i] == '6' :
#                         if numArr[i-1] == '6' :
#                             cnt += 1
#         if cnt >= 3:
#             arr.append(int(''.join(numArr)))
#         if len(arr) == n :
#             print(arr[-1])
#             break


N = int(input()) # 1
M = 666 # 667
while(N): # 브루탈포스 완전 탐색
    if '666' in str(M): #          
        N -= 1 #  
    M += 1 # 667, 668 , 1000 , 1666 ,1667 # M 은 if 문의 영향을 받지 않는다 
    
print(M-1) # 1667 - 1


# # 예제 입력에서 N을 2라고 넣었을 때, M의 값은 while문에서 666부터 증가를 합니다. 
# # M이 666이니 N은 -1이 줄어 1이 될 것이고, M은 667부터 1씩 증가하여 1666일 때, 
# # str(M)에 666이 있어 N은 0이 되어 while문은 종료되고, 결과가 출력됩니다.

# #20조 김연재
# n = int(input())  
# count = 0
# six_n = 666
# while True:
#     if '666' in str(six_n):  # if in 은 string만 비교
#         count += 1  # 아래 if 하위 수준이 아닌 이유:
#         # 하위수준일 경우, 1번 조건이 무한반복되기 때문에 하위로 안내려옴
#         # and를 쓸 경우, 둘 다 만족해야해서 count=n인 경우가 0제외하고 충족안됨
#         # or쓸 경우, 계속 666이 있기 때문에 무한반복됨
#         # 그래서 if문을 동일수준으로 두개 만들어야함.
#     if count == n:
#         print(six_n)
#         break  #브레이크없으면 무한반복
#     else:
#         six_n = six_n + 1  # 666,667,668,669,...1666,1667,1668...