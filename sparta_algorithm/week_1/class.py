# 분류집합 같은 속성과 기근ㅇ을 가진 객체를 총칭하는 개념

class Person:
    def __init__(self, param_name): #self는 항상존재해야한다
        self.name = param_name #유재석, 박명수 저장

    def talk(self): #토크 매쏘드만듬
        print("안녕하세요, 제 이름은", self.name, "입니다")



person_1 = Person("유재석") #Person이 호출된 순간 위의 클래스 내부의 함수가 불리게됨
print(person_1.name) 

person_2 = Person("박명수") #요 정보들을 펄슨 클래스 셀프네이에 저장해주고 
print(person_2.name) # 이렇게 호출해주면 프린트됨

person_1.talk()
person_2.talk()