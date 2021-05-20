from collections import deque
import sys

c = int(sys.stdin.readline())

cards = deque([])


for i in range(1 ,c+1):
    cards.append(i) 

while True:
    cards.popleft()
    cards.rotate(-1)
    
    if len(cards) == 1:
        break
    
print(cards[0])
