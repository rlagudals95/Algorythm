# N, K = map(int, input().split())

# arr = []

# cnt = 0

# for i in range(N):
#     c = int(input())
#     arr.append(c)


# for coin in arr:
#     if K % 10 == 0: #10의 자릿수가 있을때
#         coin = 10
#         cnt += (K % 100)//coin
#         K %= coin

#     elif K % 100 == 0:
#         coin = 100
#         cnt += (K % 1000)//coin
#         K %= coin
#     else:
#         coin = 1000
#         cnt += K//coin
#         K %= coin

# print(cnt)

# n, k = map(int, input().split())
# m = []
# num = 0
# for i in range(n):
#     m.append(int(input()))
    
# for i in range(n - 1, -1, -1): #  10 - 1에서 -1까지 반복하는데 -1 을 계속하면서 반복
#     if k == 0:
#         break
#     if m[i] > k: # 
#         continue
#     num += k // m[i]
#     k %= m[i]
# print(num)



#동전과 값 입력받기
n,k=map(int,input().split())
#동전을 입력받을 리스트 초기화하기 # 4200
coin=[1,5,10,50,100,500,1000,10000,50000]

#동전 종류 입력받기
for i in range(n):
  coin.append(int(input()))

#동전개수 셀 변수 초기화
result=0

#동전 내림차순으로 정렬하기
coin.sort(reverse=True) #  50000, 10000, 5000, 1000, 500, 100, 50 ,10, 5, 1

# k = 4200 // 1000 코인개수에 4 >>> k = 200

#동전 개수 구하기
for i in coin:
  if k==0: break
  result+=k//i # 50000으로 나누면 몫은 0 > 10000도 0 > 5000도 0 > 1000은 4 / 4더해주고 > 
  k %= i # 4 더해주고 4로 k나눈 나머지 +해줌 (이게 동전 갯수니까)
  

print(result)# 4 , 2