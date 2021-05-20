#while문 추가, 카운팅 뭐는 되고 뭐는 안되는거 수정하기 
# 
import math
n=int(input())
cnt=0
array=[True for n in range(2*n+1)] #처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
#에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(2*n))+1): #2부터 n의 제곱근까지의 모든 수를 확인하며
    if array[i]==True: #i가 소수인 경우(남은 수인 경우)
        #i를 제외한 i의 모든 배수를 지우기
       j=2
       while i*j<=2*n:
           array[i*j]=False
           j+=1 
#모든 소수 출력
for i in range(n+1,2*n):
    if array[i]:
        cnt+=1
        # print(i,end=' ')  

print(cnt)