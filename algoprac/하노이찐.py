def hanoi(n, start , end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, 6 - start - end)# 1에서 2로 큰원판 빼고 넘기는 단계
    print(start, end) # 1에서 3으로 원판 옮기는 단계
    hanoi(n-1, 6-start-end, end) # 2에서 3으로 남은 원판 옮기는단계

n = int(input())
print(2**n-1)
hanoi(n,1,3)


def hanoi(n, start , end):
    if n == 1:
        print(start, end)
        return

    hanoi(n-1, start, 6 - start - end)# 1에서 2로 큰원판 빼고 넘기는 단계
    print(start, end) # 1에서 3으로 원판 옮기는 단계
    hanoi(n-1, 6-start-end, end) # 2에서 3으로 남은 원판 옮기는단계

n = int(input())
print(2**n-1)
hanoi(n,1,3)