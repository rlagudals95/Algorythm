word = input().lower()

word_list = list(set(word)) #misp

cnt = [] # 4,4,1,1 / m, i, s, p

for i in word_list:
    count = word.count(i) # word에서 m,s,i,p 가 몇개인지 센것 
    cnt.append(count)

if cnt.count(max(cnt)) >= 2: # cnt에서 가장큰 수가 두개가 넘나요?
    print('?')
else:  #아니면 
    print(word_list[(cnt.index(max(cnt)))].upper())

# print((cnt.index(max(cnt)))) // 

