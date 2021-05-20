# 팩토리얼은 1부터 어느 양의정수 n 까지의 정수를 모두 곱한것
#


def factorial(n): #n=5
    if n == 1:    #n == 1 x 그러면 밑으로 내려가서 
        return 1 # 결국 1씩줄고 줄어 1이되면 1을 리턴

    return n * factorial(n-1) #5 곱하기 n-1 = 4 >> 5곱하기 4가 된다 이제다시 위로가서 1이 될때까지 로직 반복


print(factorial(5))

