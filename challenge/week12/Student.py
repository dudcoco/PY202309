# Student.py

# Student 클래스 생성
class Student:
    # 생성자 작성 - 이름, 국어, 수학, 영어 입력받아 초기화함
    def __init__(self, name, korean, math, eng):
        self.name = name
        self.korean = korean
        self.math = math
        self.eng = eng
    
    # 평균을 구하는 메서드 생성
    def get_average(self):
        return (self.korean + self.math + self.eng) / 3
