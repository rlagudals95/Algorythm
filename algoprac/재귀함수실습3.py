
# def power (b,m):
#     if m == 0:
#         return 1 
#     else:
#         return b*power(b, m - 1)
# # a의 n승을 구하는 함수

# a, n = input().split()
# a = int(a)
# n = int(n)

# ans = power(a, n)

# print(ans)

# 재귀함수를 이용해 별을 출력하는 법

def make_castle(m):
    if m == 0: #밑의 else가 계속 실행되다가 m이 0이 되면 다시 별이 늘어난다 
        return
    else:
        print('*'*m)
        make_castle(m - 1)
        print('*'*m) #리턴은 아래 숨어있다 생각해라 리턴을 만난순간 함수는 종료됨

n = int(input())

make_castle(n)