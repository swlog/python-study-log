# 03. 연산자 (Operators)

## 1. 산술 연산자

### (1) 덧셈 (+)

#### 1) 숫자 덧셈

```python
print(5 + 3)      # 8
print(0.3 + 0.1)  # 0.4
```

#### 2) 문자열 덧셈

```python
s1 = "Hello"
s2 = "I'm seowon"
res = s1 + " " + s2
print(res)  # Hello I'm seowon
```

#### 3) 리스트, 튜플 덧셈

```python
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
add_lst = lst1 + lst2
print(add_lst)  # [1, 2, 3, 4, 5, 6]

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
add_tup = tup1 + tup2
print(add_tup)  # (1, 2, 3, 4, 5, 6)
```

#### 주의사항

**1. 서로 다른 자료형끼리는 덧셈이 안 된다.**

```python
print("hello" + 5)  # TypeError: can only concatenate str (not "int") to str
```

**2. 덧셈이 지원되지 않는 자료형이 있다. (딕셔너리, 셋)**

```python
print({'one': 1} + {'two': 2})  # TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
print({1} + {2})                # TypeError: unsupported operand type(s) for +: 'set' and 'set'
```

→ `+` 대신 `|`를 사용하여 결합

```python
print({'one': 1} | {'two': 2})  # {'one': 1, 'two': 2}
print({1} | {2})                # {1, 2}
```

---

### (2) 뺄셈 (-)

#### 1) 숫자 뺄셈

```python
print(1 - 10)    # -9
print(10 - 3.5)  # 6.5
```

#### 2) 셋의 뺄셈

```python
print({1, 2, 3} - {2})              # {1, 3}
print({1, 2, 3}.difference({2}))    # {1, 3}
```

#### 주의사항

**1. 서로 다른 자료형끼리 뺄셈 불가**

```python
print("hello" - 5)  # TypeError: unsupported operand type(s) for -: 'str' and 'int'
```

**2. 문자열, 리스트, 튜플 등에서 뺄셈 연산자는 지원되지 않음**

→ 메서드나 슬라이싱 등을 사용해야 한다.

---

### (3) 곱셈 (*)

#### 1) 숫자 곱셈

```python
print(2 * 4)    # 8
print(3 * 1.5)  # 4.5
```

#### 2) 문자열 곱셈

```python
print("hi" * 3)    # hihihi
print("hi" * 3.0)  # TypeError: can't multiply sequence by non-int of type 'float'
```

#### 3) 리스트 곱셈

```python
print([1, 2, 3] * 2)  # [1, 2, 3, 1, 2, 3]
```

> 리스트와 실수를 곱하거나, 리스트끼리 곱하는 것은 지원되지 않는다.  
> 리스트를 행렬로 취급하여 곱하고 싶다면 `numpy` 모듈을 사용한다.

---

### (4) 나눗셈 (/, //)

| 연산자 | 설명 | 반환 타입 |
|:---:|:---|:---:|
| `/` | 소수점까지 계산 | float |
| `//` | 소수점 버림 (몫) | int |

```python
a = 10
b = 5
print(a / b)   # 2.0
print(a // b)  # 2
```

#### 음수 나눗셈

```python
a = -5
b = 2
print(a / b)   # -2.5
print(a // b)  # -3 (내림)
```

#### 주의사항

**1. 0으로 나누면 에러 발생**

```python
a = 5
b = 0
print(a / b)  # ZeroDivisionError: division by zero
```

**2. 소수점 자릿수 지정 출력**

```python
a = 10
b = 3
divide = a / b
print(f'{a} ÷ {b} = {divide:.2f}')  # 10 ÷ 3 = 3.33
```

---

### (5) 나머지 (%)

한 숫자를 다른 숫자로 나누었을 때의 **나머지**를 반환하는 연산자

```python
print(10 % 3)  # 1
```

> 홀짝 판별, 특정 자릿수 추출 등에 주로 사용된다.

---

### (6) 거듭제곱 (**)

```python
print(10 ** 3)  # 1000
```

#### 주의사항

```python
print(-2 ** 2)    # -4 (거듭제곱 먼저, 부호는 나중에 적용)
print((-2) ** 2)  # 4
```

---

### 파이썬에는 증감 연산자가 없다

파이썬에는 `++a`, `a++` 같은 전위/후위 증감 연산자가 없다.

```python
# a++  # SyntaxError
a += 1  # 이 방식을 사용
```

> 이는 연산 시점의 혼란을 줄이고, `a += 1`과 같은 명확한 문법을 강제하여  
> 코드 가독성과 안정성을 높이기 위함이다.

---

## 2. 비교 연산자

비교 연산자는 두 값을 비교하여 **참(True)과 거짓(False)을 판단**하며, 주로 조건문과 반복문에서 사용된다.

### (1) 비교 연산자 종류

| 연산자 | 설명 |
|:---:|:---|
| `==` | 같음 |
| `!=` | 같지 않음 |
| `<` | 작음 |
| `<=` | 작거나 같음 |
| `>` | 큼 |
| `>=` | 크거나 같음 |

#### 1) == (같음)

```python
print(1 == 1)          # True
print("hi" == "hi")    # True
print("hi" == "hello") # False
```

#### 2) != (같지 않음)

```python
print(1 != 2)  # True
```

#### 3) < (작음)

```python
print(3 < 5)  # True
```

#### 4) <= (작거나 같음)

```python
print(5 <= 5)  # True
```

#### 5) > (큼)

```python
print(6 > 5)  # True
```

#### 6) >= (크거나 같음)

```python
print(5 >= 5)  # True
```

---

### (2) 문자열, 리스트, 튜플 비교

#### 문자열 비교

문자열은 맨 앞자리부터 **유니코드 순서대로** 비교한다.

```python
print("abc" < "efg")  # True
```

맨 앞자리가 같으면 다음 자리로 넘어가 비교한다.

```python
print("abcde" > "abcba")  # True
```

> 한글 비교는 쉽지 않다.

#### 연속 비교

```python
x = 5
print(1 < x < 10)  # True
```

#### 리스트 비교

리스트도 맨 앞자리부터 비교한다.

```python
print([10, 20, 30] > [20, 30, 40])  # False
```

---

### (3) 부동소수점 비교

부동소수점은 오차가 발생할 수 있으므로 `math.isclose()`를 사용하여 두 수가 충분히 가까운지 확인한다.

```python
import math

value = 1.1 + 2.2

print(value == 3.3)                    # False
print(math.isclose(value, 3.3))        # True
print(math.isclose(value, 3.29))       # False
print(math.isclose(value, 3.31))       # False
print(math.isclose(value, 3.30000001)) # False
```

---