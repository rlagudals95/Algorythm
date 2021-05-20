# while True:
#     s = input()
#     if s == '.': #인풋값에 .이 있다면 while문 브레이크 >>
#         break
#     stk = []
#     temp = True
#     for i in s:
#         if i == '(' or i == '[': #반복문을 돌려주는데 그중에 (,[ 이 있다면 스택에 넣어줘
#             stk.append(i)
#         elif i == ')': # 그리고 )가 있다면
#             if not stk or stk[-1] == '[': # stk 혹은 stk 마지막 원소가 '['가 아닌 경우엔
#                 temp = False
#                 break
#             elif stk[-1] == '(': #그리고  스택의 마지막 값이 (가 아니면
#                 stk.pop() # 마지막 값 없애버려
#         elif i == ']': # i가 ] 이고
#             if not stk or stk[-1] == '(': # stk이 아니거나 stk의 마지막이 (이 아니라면
#                 temp = False
#                 break
#             elif stk[-1] == '[': # 스택 마지막이 [라면
#                 stk.pop() # 없애 버려
    
#     if temp == True and not stk:
#         print('yes')
#     else:
#         print('no')

#여는 괄호를 찾으면 스택에 그대로 넣어주고 닫는 괄호를 찾았을땐 스택이 비었는지 혹은 스택 마지막이 자기랑 짝이 맞는지 검사
# 만약 닫는 괄호를 찾았을때 스택이 비워져 있거나 마지막과 짝이 안맞는다면 temp를 false로 바꿔주고 break
# 마지막에 temp가 true이거나 스택이 비워져 있으면 yes 아니면 no

# while True:
#     s = input()
#     if s == '.': # s가 . 이라면 중단
#         break
#     stk = [] 
#     temp = True
#     for i in s:
#         if i == '(' or i == '[': # ([ 이 들어오면 일단 stk로 전송
#             stk.append(i)
#         elif i == ')':    # 그리고 ) 이 들어오면 
#             if not stk or stk[-1] == '[': # stk가 비어있거나 맨끝이 [ 면 중단
#                 temp = False
#                 break
#             elif stk[-1] == '(': # stk 끝이 ( 면 제거
#                 stk.pop()
#         elif i == ']':  # ] 이 들어오면
#             if not stk or stk[-1] == '(': # stk가 비었거나 끝이 ( 이면 중단
#                 temp = False
#                 break
#             elif stk[-1] == '[': # 그리고 끝자리가 [ 면 제거
#                 stk.pop()
#     if temp == True and not stk: # (), []짝이 맞아 pop 될때 혹은 stk가 비어있을때 마다 yes 
#         print('yes')
#     else:   # 그외엔 no
#         print('no')

# while True:
#     s = input()
#     if s == '.': # .은 못들어가니까 yes
#         break
#     stk = []
#     temp = True
#     for i in s:
#         if i == '(' or i == '[':
#             stk.append(i)
#         elif i == ')':
#             if not stk or stk[-1] == '[': #너도 안들어가져
#                 temp = False
#                 break
#             elif stk[-1] == '(':
#                 stk.pop() # 짝이 맞아서 pop 값은 True
#         elif i == ']':
#             if not stk or stk[-1] == '(':
#                 temp = False
#                 break
#             elif stk[-1] == '[':
#                 stk.pop()
#     if temp == True and not stk:
#         print('yes')
#     else:
#         print('no')


while True:
    s = input()
    if s == '.':
        break
    stk = []
    temp = 0
    for i in s:
        if i == '(' or i == '[':
            stk.append(i)
        elif i == ')':
            if not stk or stk[-1] == '[':
                temp = False
                break
            elif stk[-1] == '(':
                stk.pop()
        elif i == ']':
            if not stk and stk[-1] == '(':
                temp = False
                break
            elif stk[-1] == '[':
                stk.pop()

    if temp == True and not stk:
        print('yes')
    else:
        print('no')