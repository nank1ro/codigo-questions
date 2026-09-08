매우 흔한 작업은 기존 리스트에서 새 리스트를 만드는 것입니다.
`for` 반복문과 `append()`를 사용하면 몇 줄이 필요합니다.
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Python은 바로 이 작업을 위한 더 짧은 형태를 제공합니다: **리스트 컴프리헨션**으로, 리스트 전체를 하나의 표현식으로 만듭니다.
```python
doubled = [n * 2 for n in nums]
```
구문은 `[expression for item in iterable]`입니다: `for` 부분이 항목들을 반복하고, 왼쪽의 표현식이 각 항목에 대해 평가됩니다.
결과는 반복문으로 만든 것과 정확히 같은, 완전히 새로운 리스트입니다.

---

왼쪽의 표현식은 값을 만들어내는 것이라면 무엇이든 될 수 있습니다: 계산, 함수 호출, 메서드 호출 등입니다.
반복 변수는 원하는 이름을 가질 수 있으며, 이는 대괄호 안에서만 존재합니다.
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

컴프리헨션은 항목을 **필터링**할 수도 있습니다.
`for` 부분 뒤에 `if` 조건을 추가하면, 조건이 `True`인 항목만 새 리스트에 들어갑니다.
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
이는 안에 `if`가 있는 반복문과 같으며, lambda를 사용한 `filter()`를 더 읽기 쉬운 방식으로 대체합니다.

---

필터 조건은 `len()`과 같은 함수 호출을 포함하여, 불리언 값을 반환하는 모든 표현식이 될 수 있습니다.
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

이터러블이 꼭 리스트일 필요는 없습니다: 반복할 수 있는 것이라면 무엇이든 사용할 수 있고, `range()`가 대표적입니다.
숫자 리스트를 만드는 가장 빠른 방법입니다.
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
`range(start, stop)`은 `stop`을 포함하지 않는다는 점을 기억하세요.

---

컴프리헨션은 **문자열 변환**에도 매우 유용합니다.
각 항목에 문자열 메서드를 호출하거나, f-문자열로 새 문자열을 만들 수 있습니다.
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

컴프리헨션 안에서는 그 전에 정의된 변수를, 예를 들어 `range()`의 상한값으로 사용할 수 있습니다.

---

때로는 항목을 제거하는 것이 아니라, 일부 항목에 **다른 값**을 선택하고 싶을 수 있습니다.
`for`의 왼쪽에 있는 표현식으로 조건 표현식 `a if condition else b`를 사용하세요.
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
위치에 주의하세요: `if-else`는 `for` **앞**에 오며 항상 값을 만들어내고, 필터 `if`는 `for` **뒤**에 오며 `else`가 없습니다.

---

두 조건을 같은 컴프리헨션 안에서 결합할 수 있습니다: 값을 선택하는 `if-else`와, 일부 항목을 걸러내는 마지막의 필터 `if`입니다.
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

`if` 의 두 위치는 헷갈리기 쉬우므로 구분해서 기억하세요:
```python
values = [n if n > 0 else 0 for n in nums]  # for 앞의 if-else: 값을 고른다. else 필수
positives = [n for n in nums if n > 0]      # for 뒤의 if: 걸러낸다. else 사용 불가
```
필터 `if` 뒤에 `else` 를 쓰면 문법 오류입니다.

---

컴프리헨션은 **둘 이상의 `for`**를 가질 수 있습니다.
이는 중첩된 반복문처럼 동작하며, 첫 번째 `for`가 바깥쪽 반복문, 두 번째가 안쪽 반복문입니다.
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

안쪽의 `for`는 바깥쪽의 변수를 사용할 수 있습니다.
이는 리스트의 리스트를 하나의 리스트로 **평탄화**하는 전형적인 방법입니다.
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
그런 다음 `sum()` 함수가 리스트의 모든 숫자를 더합니다.

---

**딕셔너리**도 반복할 수 있습니다.
`.items()`를 사용하면 `for` 부분이 각 쌍을 키와 값 두 변수로 풀어냅니다.
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

같은 방식이 딕셔너리에도 적용됩니다: **딕셔너리 컴프리헨션**은 중괄호와 `key: value` 표현식을 사용합니다.
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

`key: value` 부분이 **없는** 중괄호는 **집합 컴프리헨션**이 됩니다.
집합(set)은 순서가 없고 고유한 값만 유지하는 컬렉션이므로, 중복은 자동으로 사라집니다.
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**컴프리헨션은 언제 사용해야 할까요?**
결과가 리스트(또는 딕셔너리, 집합)이고 로직이 읽기 쉬운 한 줄에 들어갈 때, 즉 단순한 변환이나 선택적 필터일 때 완벽합니다.
여러 문장이 필요하거나, 중첩된 `for`가 두 개를 넘어가거나, 줄이 읽기 어려워진다면 대신 평범한 `for` 반복문을 작성하세요: 코드는 더 길어지지만 더 명확해집니다.
컴프리헨션은 또한 lambda를 사용한 `map()`과 `filter()`의 대부분의 용도를 대체합니다.
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
