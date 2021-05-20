n, m = map(int, input().split()) # 큐의 크기 , 뽑고싶은 수의 갯수
s = list(map(int, input().split())) # 뽑으려고 하는 수의 위치
q = [i for i in range(1,n+1)] #큐의 크기 레인지 1,2,3 ~~ 10

cnt = 0

for i in range(m):
    q_len = len(q) # 큐의 크기 10
    q_index = q.index(s[i]) # 리스트에서 몇번째 인덱스인지 찾아줌
    if q_index < q_len - q_index: # 찾으려고 하는 순서 < 큐크기 - 찾으려는순서 (왼쪽에 더 가까움)
        while True:
            if q[0] == s[i]: # 큐의 첫번째가 찾으려는 순서와 같다면
                del q[0] # 큐의 첫번째를 지워버리고 브레이크
                break
            else: # 아니라면 q의 첫번째 원소를 다시 큐로 돌려보내고
                q.append(q[0])  
                del q[0] # 지워버려라
                cnt += 1 #그리고 카운트 >> 한번 돌림을 의미
    else: # 찾으려고 하는 순서 > 큐크기 - 찾으려는순서 (오른쪽에 더 가까움)
        while True: # 디큐 ?
            if q[0] == s[i]: # 
                del q[0]
                break
            else:
                q.insert(0,q[-1]) #맨뒤에 넣어준다
                del q[-1] # 그리고 지워버려
                cnt += 1 #

print(cnt)