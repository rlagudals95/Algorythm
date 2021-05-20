def fact(m):
    if m == 1:
        return 1
    else:
        return m*fact(m-1)

n = int(input())

ans = fact(n)

print(ans)