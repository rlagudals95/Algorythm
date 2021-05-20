C = int(input())

for _ in range(C):
    s = list(map(int, input().split()))
    students = s[0]
    scores = s[1:]
    cnt = 0
    avg = sum(scores)/students
    
    for num in scores:
        if num < avg:
            cnt += 1 # 평균보다 높은 학생의 수

        rate = cnt/students*100
print(f'{rate:.3f}%')   #소숫점 3째 자리까지 표기


