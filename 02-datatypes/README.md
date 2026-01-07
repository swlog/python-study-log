# 02. 자료형 (Data Types)

## 1. 자료형이란?

자료형이란 **데이터의 종류를 구분하는 것**이며,  
값이 **메모리에 어떻게 저장되고 어떤 연산이 가능한지**를 결정한다.

같은 연산이라도 자료형에 따라 결과가 달라질 수 있다.

```python
print(3 + 3)       # 6 (숫자 덧셈)
print("3" + "3")   # 33 (문자열 연결)
```

---

## 2. 기본 자료형

### 1) 숫자형 (Number)

#### (1) 정수형 (int)

- 양의 정수, 음의 정수, 0을 포함
- 파이썬의 정수형은 **크기 제한이 없음** (다른 언어와의 차이점)

```python
a = 10
b = -5
c = 0

# 큰 숫자도 표현 가능
big_num = 999999999999
print(type(big_num))  # <class 'int'>
```

#### (2) 실수형 (float)

- 소수점이 포함된 숫자
- **부동소수점 방식**으로 저장되어 정확하지 않은 결과가 나올 수 있음

```python
x = 3.14
y = -0.5

print(0.1 + 0.2)   # 0.30000000000000004 (부동소수점 오차)
```

#### (3) 복소수형 (complex)

- 실수부와 허수부로 이루어진 숫자
- 허수는 `j`로 표현

```python
z = 3 + 4j

print(z.real)  # 3.0 (실수부)
print(z.imag)  # 4.0 (허수부)
```

---

### 2) 문자열 (string, str)

문자, 단어, 문장 등 **텍스트 데이터**를 다루는 자료형이다. 큰 따옴표(""), 작은 따옴표('') 사용

#### 문자열 생성

```python
s1 = "Python"       # 큰 따옴표
s2 = 'Hello'        # 작은 따옴표
s3 = """여러 줄
문자열"""            # 삼중 따옴표 (여러 줄)
```

#### 문자열 연산

```python
# 문자열 연결 
print("Py" + "thon")   # Python

# 문자열 반복
print("seowon" * 3)        # seowonseowonseowon

# 문자열 길이
print(len("Python"))   # 6
```

#### 문자열 인덱싱

문자열의 각 문자는 인덱스를 가진다. (0부터 시작, 음수는 뒤에서부터)

```python
s = "Python"

print(s[0])   # P 
print(s[5])   # n 
print(s[-1])  # n 
print(s[-2])  # o 
```
> 범위를 벗어난 인덱스를 사용하면 `IndexError` 발생

#### 문자열 슬라이싱

형식: `s[시작:종료:간격]` (종료 인덱스는 포함되지 않음)

```python
s = "Python"

print(s[0:3])   # Pyt 
print(s[1:])    # ython 
print(s[:3])    # Pyt 
print(s[::2])   # Pto 
print(s[::-1])  # nohtyP 
```

#### 문자열은 불변(immutable)

한 번 생성된 문자열은 수정할 수 없다.

```python
s = "Python"
# s[0] = "p"  # TypeError 발생!
```

#### 이스케이프 문자

| 이스케이프 문자 | 설명 |
|:---:|:---|
| `\n` | 줄바꿈 |
| `\t` | 탭 |
| `\\` | 백슬래시 |
| `\'` | 작은 따옴표 |
| `\"` | 큰 따옴표 |

```python
print("Hello\nWorld")   # 줄바꿈
print("Hello\tWorld")   # 탭
print("She said \"Hi\"")  # 따옴표 출력
```

---

### 3) 불 자료형 (Boolean, bool)

`True` 또는 `False` **두 가지 값만** 가지며, 프로그램의 흐름을 제어할 때 사용된다.

```python
print(10 > 5)     # True
print(3 == 5)     # False
print(3 != 5)     # True
print(10 >= 10)   # True
```

---

### 4) None 자료형

`None`은 **"값이 없음"** 을 나타내는 특별한 자료형이다.

```python
x = None

print(x)         # None
print(type(x))   # <class 'NoneType'>

# None 비교는 is 사용
print(x is None)      # True
```

---

## 3. type() 함수

값이나 변수의 자료형을 확인하는 함수이다.

```python
print(type(20))        # <class 'int'>
print(type(3.14))      # <class 'float'>
print(type("Hello"))   # <class 'str'>
print(type(True))      # <class 'bool'>
print(type(None))      # <class 'NoneType'>
```

#### 같은 값처럼 보여도 자료형은 다를 수 있다

```python
a = 10
b = "10"

print(type(a))  # <class 'int'>
print(type(b))  # <class 'str'>
print(a == b)   # False
```

---

## 4. 형변환 (Type Casting)

자료형을 다른 자료형으로 변환하는 것이다.

### 기본 형변환 함수

| 함수 | 설명 |
|:---:|:---|
| `int()` | 정수로 변환 |
| `float()` | 실수로 변환 |
| `str()` | 문자열로 변환 |
| `bool()` | 불 자료형으로 변환 |

```python
# 문자열 → 숫자
print(int("10"))      # 10
print(float("3.14"))  # 3.14

# 숫자 → 문자열
print(str(100))       # "100"
print(str(3.14))      # "3.14"

# 실수 → 정수 (소수점 버림)
print(int(3.7))       # 3
print(int(-3.7))      # -3

# 정수 → 실수
print(float(10))      # 10.0
```

### 형변환 주의사항

```python
# 숫자가 아닌 문자열은 변환 불가
# int("abc")  # ValueError!
# int("3.14") # ValueError! (실수 형태 문자열)

# 실수 형태 문자열은 float()으로 먼저 변환
print(int(float("3.14")))  # 3
```

---

## 5. 실습 예제

### 예제 1: 사용자 정보 카드 만들기
> 사용자로부터 이름, 나이, 키를 입력받아 정해진 형식으로 출력하기

📄 `ex01_user_info.py`

---

### 예제 2: 문자열 슬라이싱으로 날짜/시간 추출
> `"20260107-143005"` 형식의 데이터에서 날짜와 시간을 분리하여 포맷팅하기

📄 `ex02_datetime_slice.py`

---

## 6. 배운 점

### input()은 항상 문자열을 반환한다
```python
age = input()       # "25" (문자열)
age = int(input())  # 25 (정수) - 형변환 필요
```

### 문자열 연결 시 숫자는 str()로 변환해야 한다
```python
age = 24
# print("나이: " + age)        # TypeError!
print("나이: " + str(age))     # "나이: 24"
```

### 슬라이싱 인덱스는 다양한 방식으로 활용 가능
```python
data = "20260107-143005"

# 양수 인덱스
data[:8]      # 처음부터 8번째 전까지 → "20260107"

# 음수 인덱스
data[-6:]     # 뒤에서 6번째부터 끝까지 → "143005"

# 거꾸로 출력
data[::-1]    # 전체를 역순으로
```

### 원본 데이터를 수정하면 이후 슬라이싱 결과가 달라진다
```python
data = "20260107-143005"

# 원본을 덮어쓰면 이후 슬라이싱이 꼬임
data = data[:8]   # "20260107" (8글자로 변경됨)
time = data[-6:]  # "260107" 

```