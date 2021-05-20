# 회문은 거꾸로 읽어도 똑같은 문장이나 단어를 말한다 토마도, 오디오 등

# input = "abcba"
#
#
# def is_palindrome(string):
#     n = len(string)
#     for i in range(n):
#         if string[i] != string[n-1-i]:  #문자열의 맨앞과 맨뒤(인덱스이기 때문에 맨뒤가 n-1이다 i는 0부터 시작된다 그렇담면 맨앞은 0 맨뒤는 n-1 인상태이다)를 비교한다 그리고 -i씩 좁혀들어가는
#             return False
#
#     return True
#
#
# print(is_palindrome(input))

input = "소주만병만주소"


def is_palindrome(string): # 소주만병만주소 넣어준다
    if string[0] != string[-1]: # 문자열 맨뒤는 [-1] 두개가 같다면 폴스 반환x 통과
        return False #같다면 밑으로 ㄱㄱ
    if len(string) <= 1:  #길이가 1보다 크다면 트루 반환안하고 밑으로
        return True

    return is_palindrome(string[1:-1]) #다통과 했으면 앞뒤로 하나씩 줄여준다 그리고 다시 함수로 복귀




print(is_palindrome(input))