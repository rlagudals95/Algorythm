n = int(input())


a=[]

for i in range(n+1,n*2):
    for j in range(2,i):
        if n <= 1:
            break
        elif i%j == 0:
            break
    else:
        a.append(i)

# print(len(a))
print(len(a))



