# num = 3

# if num % 2 == 0:
#     result = '짝수'
# else:
#     result = '홀수'

# print(f'{num}은 {result}입니다')

#위의 조건문을 삼항연산자로 간단하게 표현해보기

num = 3

result = '짝수' if num%2 == 0 else '홀수'

print(f'{num}은 홀수다!')