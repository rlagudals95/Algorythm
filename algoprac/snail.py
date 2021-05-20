import math

a,b,v = map(int,input().split())

# a올라가는 거 b 는 미끄러지는거 v는 높이
# >> 결국 (a-b)n + a = v 가 되야한다 
# >> n = (v-a)(a-b) 이렇게 되겠다

n = (v-a)/(a-b) 

print(math.ceil(n)+1) #아직도 왜 1을 더해야 하는지는 모르겠다.....ㅜㅠ
