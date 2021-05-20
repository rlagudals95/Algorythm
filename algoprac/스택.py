import sys

lines = sys.stdin.readline()

for line in lines[:-1]: # 마지막 문자제거 
    stack = [] #스택 문자열 생성  # ([]())[]()(])(([)]
    for t in line: # 입력값을 for문으로 돌린다
        if t in '([': # 입력값이 ([라면  스택에 넣어준다
            stack.append(t)
        elif t == "]": #그리고 ]하나고 스택이 아니라면 혹은 스택에 들어간 마지막 값이 [이 아니라면 프린트 노
            if not stack or stack.pop() != '[': # 스택이 아니거나 마지막 값이 [이 아니라면
                print('no')
                break # no 가 나오면 브레이크하고 처음으로
        elif t == ')': # ) 하나고 스택에 없거나 마지막입력된 값이 (가 아니라면
            if not stack or stack.pop() != '(':
                print('no') # no 
                break
        elif t == '.': # 만약 가 .이라면
            if stack:       
                print('no') 
            else:
                print('yes')


