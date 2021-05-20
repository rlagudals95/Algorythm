inp = tmp = int(input())

count = 0

while True:
    ten = tmp//10
    one = tmp%10
    res = ten + one
    tmp = int(str(tmp%10)+ str(res%10))
    count += 1
    if inp == tmp:
        break

print(count)

