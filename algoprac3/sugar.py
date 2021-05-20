n = int(input())

cnt = 0


while True:
    if n % 5 == 0:
       five_bag = n//5
       cnt = cnt + five_bag
       n = n - (five_bag*5)
       
    elif n%3 ==0:
        n = n-3
        cnt = cnt +1
    else:
        n = 0
        cnt = -1

    if n == 0:
        break

print(cnt)

        
    