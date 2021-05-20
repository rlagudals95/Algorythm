from collections import deque

# max_num, target_num = map(int, input().split()) #큐의 크기, 뽑아내려는 수의개수

# target_list = list(map(int, input().split()))
# que = deque([i for i in range( 1, max_num + 1 )])
# # 리스트에 요소를 넣고 빼는 것이 매우 자유로워짐
# result = 0

# for num in target_list: #리스트 요소 꺼낼때 마다 실행?
#     if num == que[0]: # 리스트의 숫자가 큐의 첫번째와 같을 때 p p p! 1, 2, 3이기 때문에 여기서 다 걸러짐
#         que.popleft() # 큐의 맨 왼쪽 숫자를 팝! 해줘라 // 
#         continue # 전체를 해당하기 위해서! 123만 있는게 아니니 # break를 쓰면 1만뽑고 실행이 멈춤
#     left_move = que.index(num) # 왼쪽으로 이동 = 1,2,3 // 0, 1, 2
#     right_move = len(que) - left_move # 오른쪽 으로 이동 = 큐의 길이 // 10 - 0, 1, 2

#     if left_move <= right_move: # 같거나 클때 // 0, 1, 2 != 10, 9, 8
#         que.rotate(-left_move) # 값을 큐 맨뒤로 보냄 
#         que.popleft()
#         result += left_move
#     else:
#         que.rotate(right_move) # 값을 큐 맨뒤로 보냄 라이트 무브는 > 10, 9 ,8 
#         que.popleft()          # 보내고 지워버림 => 1,2,3은 인덱스 값이 항상 0
#         result += right_move # 이게 0이 되야하는데..

# print(result)

# max_num, target_num = map(int, input().split()) #  10 개 중에서 3개를 찾고싶다

# target_list = list(map(int, input().split())) # 그 3개는 2 9 5
# que = deque([i for i in range(1, max_num +1 )])

# result = 0

# for num in target_list: # 반복문으로 2 9 5 넣어보자
#     if num == que[0]: # 2 != 1 통과
#         que.popleft()
#         continue
#     left_move = que.index(num) # 큐 인덱스 2는 큐 정렬의 1 , 2 ,3번째 2를 가르키겠다! 9 / 5
#     right_move = len(que) - left_move # 10 - 2 = 8 / 10 - 9 = 1 / 10 - 5 = 5

#     if left_move <= right_move: # 레프트 무브는 3 < 7 / 5 = 5
#         que.rotate(-left_move) # =(-3) 큐값을 맨뒤로 보냄 1을 보냈겠죠? 양수면 뒤엣걸 맨앞으로 음수면 맨앞엣걸 뒤로
#         que.popleft() # 1을 뒤로 보낸후 구하려는 값 2가 나온다 pop!
#         result += left_move # + 2 + 5
#     else: # 9 > 1 / 
#         que.rotate(right_move) # 10을 맨 앞으로
#         que.popleft() 
#         result += 1 # + 1

# print(result)
# print(que)

max_num, target_num = map(int, input().split()) #  10 개 중에서 3개를 찾고싶다

target_list = list(map(int, input().split())) # 그 3개는 2 9 5
que = deque([i for i in range(1, max_num +1 )])# 1,2,3,4,5,6,7,8,9,10

result = 0

for num in target_list: # 
    if num == que[0]: # 
        que.popleft()
        continue
    left_move = que.index(num) # >> 1 // 2가 몇번째 인덱스냐 1 , 2 >> 0 , 1 // 1번째므로 1값은 1!
    right_move = len(que) - left_move # 10 - 1 / 9 - 6 / 8 - 4

    if left_move <= right_move: # 
        que.rotate(-left_move) # 6,7,8,10,1,3,4
        que.popleft() # 
        result += left_move # 1 + 6 + 
    else: # 
        que.rotate(right_move) # 
        que.popleft() 
        result += 1 # 


print(result)
print(que)# ([6,7,8,10,1,3,4])
