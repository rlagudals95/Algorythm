a = int(input()) # 테스트 케이스
for i in range(a):

    b = input() # 
    s = list(b) #괄호 입력값
    
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
