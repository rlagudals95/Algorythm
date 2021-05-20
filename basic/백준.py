# alpha = ['c=','c-','dz=','d-','lj','nj','s=','z=']

# string = input()


# for i in alpha:
#     string = string.replace(i,' ')

# print(len(string))

# # 달팽이는 올라간다 

# A,B,V = map(int, input().split())

# count = 0

# while True:
#     A = A + 2 # 2 4 8 10 
#     B = A - 1 # 1 3 6 9
#     count += 1
#     if B >= V:
#         break

# print(count)

# import math

# a,b,v = map(int, input().split())

# day = math.ceil((v-a)/(a-b))+1
# print(day)
# # a = 올라가는 길이 , b = 떨어지는길이, v = 나무높이

# 호텔 방배정

# h = 층수 , w = 가로 방순서, n 손님 순서
# 가로방 순서가 작은 호수를 가장선호, 그 다음르로 층수가 낮을 수록 선호
# 



# t = int(input())

# for i in range(t):
#     h, w, n = map(int, input().split())
#     num = n//h + 1
#     floor = n % h
#     if n % h == 0:  # h의 배수이면,
#         num = n//h
#         floor = h
#     print(f'{floor*100+num}')

m,n = map(int, input().split())

i = 1

print(3)
print(5)

for i in range(m, n-1):
    i = i + 2
    if i % 3 != 0 and i % 5 != 0 and i % 2 != 0:
        
        print(i)
  
    

          

        