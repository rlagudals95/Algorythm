h, m = map(int, input().split())

if m > 45:
    print(h , 45 -m)
elif m < 45:
    print(h-1, m + 15)
else:
    print(23, h+15)

