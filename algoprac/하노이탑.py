
# def hanoi(n , a , b):
#     if n > 1:
#         hanoi(n-1, a , 6-a-b) #기둥이 1개 이상이면 그룹으로 묶인 n-1개의 원판을 중간으로 먼저 다 옮긴다

#     print(a,b)                # n 번째 기둥이 a -> b 로 옮겨짐
                              
#     if n > 1:
#         hanoi(n-1, 6-a-b, b)  # 기둥이 한개 이상이면 남은 기둥 (n-1)개를 중간에서 b로 옮기겠다
    
# n = int(input()) # 원반이 몇갠지 입력을 받는다

# print(2**n-1) #총 이동해야 하는 횟수
# hanoi(n, 1, 3) #3개 원판을 기둥 1에서 3으로 옮기겠다

# # 하노이 3, 1 ,3 을 호출 했을때를 가정해보자 
# # 함수 프린터 밑의 하노이를 보면 

# # 

def hanoi_tower(n, start, end) :
    if n == 1 :
        print(start, end)
        return
       
    hanoi_tower(n-1, start, 6-start-end) # 1단계
    print(start, end) # 2단계
    hanoi_tower(n-1, 6-start-end, end) # 3단계
    
n = int(input())
print(2**n-1)
hanoi_tower(n, 1, 3)