import sys

n = int(sys.stdin.readline())

a = []

for i in range(n):
    x, y = map(int,sys.stdin.readline().split())
    a.append([y,x]) #여기에 값을 적는다 ex) 0 4 

s_a =sorted(a) #sorted는 첫번째 요소기준으로 정렬 그래서 y를 먼저 넣어줌
               #여기에 y순으로 정렬된다 -1 1이 가장먼저 될듯

for y , x in s_a: #? 정렬된걸 다시 x,y 바꿔서 출력 해주면 조건완성
    print(x,y) 



