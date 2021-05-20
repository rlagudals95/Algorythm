# # for문과 if문을 써서 369 게임 3의 배수에만 X를 출력하게 하라

# a = int(input())

# for i in range(1, a +1):
#     if i % 3 == 0:
#         print('X' ,end= '')    
#     else:
#         print(i ,end='')
    

# 3의 배수는 통과시켜라 // 출력 시키지 말아라!

# a = int(input())

# for i in range(1, a+1):
#     if i % 3 != 0:
#         print(i, end='')
    
# # 두 번째 방법

# for i in range(1, a+1):
#     if i % 3 ==0:
#         continue # 반복문에서 컨티뉴를 쓰면 여기서 부터 다시 for문 시작으로 돌아간다 즉, 3의 배수들 이 나오면 프린터 되지 않음
#     print(i, end='')