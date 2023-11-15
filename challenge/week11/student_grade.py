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

# TODO 1: 학생 정보를 딕셔너리에 저장
def loadData(filename):
    score_dict = {}  # 성적을 저장할 딕셔너리 생성

    file = open(filename, 'r', encoding="utf8")
    lines = file.readlines()
    file.close()

    for line in lines[1:]: # 헤더 제외
        token = line.strip().split(',') # 공백 없애고 쉼표 기준으로 토큰을 나눔

        name = token[0] # 이름 저장
        korean = float(token[1]) # 국어 점수 저장
        math = float(token[2]) # 수학 점수 저장
        eng = float(token[3]) # 영어 점수 저장

        std_ins = Student(name, korean, math, eng) # 클래스 사용

        score_dict[name] = std_ins  # 이름을 key로, Student 객체를 value로 저장

    return score_dict # 학생별 점수 딕셔너리 반환

# 파일 이름 입력
filename = 'student.csv'
load_file = loadData(filename) # 파일 불러오기

# 학생들의 평균 점수를 출력
print("-----학생들의 평균 점수-----")
for name, student in load_file.items():
    average_score = student.get_average()
    print(f"{name}의 평균 점수는 {average_score} 입니다.")

# 학생들의 평균 점수를 average.txt 파일에 쓰기
with open('average.txt', 'w', encoding="utf8") as score_file:
    score_file.write("-----학생들의 평균 점수-----\n")

    for name, student in load_file.items():
        average_score = student.get_average()
        score_file.write(f"{name}의 평균 점수는 {average_score} 입니다.\n")
