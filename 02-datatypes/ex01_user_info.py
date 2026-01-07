# ex1 - 사용자 정보 카드 만들기
# 사용자로부터 정보를 입력받아 정해진 형식으로 출력하는 프로그램을 작성해 보세요.
# input() 함수를 사용하여 이름, 나이, 키(소수점 포함)를 각각 변수에 저장하세요.
# 나이는 정수(int)로, 키는 실수(float)로 형변환 하세요.
# 입력받은 나이에 1을 더해 "내년 나이"를 계산하세요.
# 아래와 같은 형식으로 출력하세요. 

# 출력 예시:
# 이름: 최서원 (타입: <class 'str'>)
# 내년 나이: 24세
# 입력한 키: 155.5cm

name = input()
age = int(input())
height = float(input())
next_age = age + 1

print("이름: " + name + " (타입: " + str(type(name)) + ")")
print("내년 나이: " + str(next_age) + "세")
print("입력한 키: " + str(height) + "cm")