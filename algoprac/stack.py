word = input()
world_list = list(word)

result = []

for _ in range(len(world_list)):
    result.append(world_list.pop()) # 입력한 반대로 출력이 된다.

print("".join(result)) #  "".join(result) >> "" 없이 문자형태로 붙여서 정렬됨
print(word[])