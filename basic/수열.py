# #  수열이란 어떤 규칙에 따라 수를 순서대로 나열한 것 ex) 1234//2468//3 6 9 12

# a, d , n = map(int, input().split())

# # a는 시작값 , d는 등차값, n은 몇번째 수인지 알아보는 값
# # d가 더해지는건 n-1이 반복되는것 > 첫번째 수는 제외해야하니

# print(a + d*(n-1)) # >> 식을 이용한 방법


# #for문을 사용한 방법
# a, d , n = map(int, input().split())

# for i in range(n-1):
#     a = a + d

# print(a)


# 곱하기 수열

#바로 계산 하는 방법

# a는 시작값 , r은 등곱?값, n은 몇번째 수인지 알아보는 값

# a, r, n = map(int, input().split())

# print(a*(r**(n-1)))

# for문 이용해서 알아내기

# for i in range(n-1):
#     a = a*r
# print(a)


# 조건이 더 붙은 수열
# 1부터 시작해 이전에 만든 수에 -2를 곱한 다음 1을 더해 만든 수열

#시작값 a , 곱할 값 m , 더할 값 d, 몇번째인지 나타낼 정수 n
a, m, d, n = map(int, input().split())

for i in range(n-1):
    a = a*m+d

print(a)