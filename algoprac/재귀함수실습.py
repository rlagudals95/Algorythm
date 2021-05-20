
def fibo(m): 
    if m == 1 or m == 2: #기본적으로 피보나치는 (n-1)+(n-2)이기 때문
        return 1
    else:
        return fibo(m-1) + fibo(m-2)


n = int(input()) #피보 함수에 넣는 값을 n 이라지정

ans = fibo(n)  # n을 넣었을 때 값을 ans라 지정


print(ans)