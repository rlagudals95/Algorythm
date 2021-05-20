kg = int(input())

가방 = 0

while kg >= 0:
    if kg % 5 == 0: #5의 배수면 실행
        가방 = 가방 + (kg // 5) #5의 배수니까 나머지 없이 나뉜다
        print(가방)
        break
    elif kg % 3 == 0: kg = kg - 3
    가방 = 가방 +1 # 5의 배수가 될때까지 3kg씩 빼준다
    
else:
    print(-1)


 