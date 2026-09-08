숫자를 두 배로 만드는 것처럼, 딱 한 번만 사용할 작은 함수가 필요할 때가 있습니다.
그것을 위해 완전한 `def` 블록을 작성하는 것은 부담스럽게 느껴집니다.
Python은 더 짧은 형태를 제공합니다. **lambda** 표현식으로, 한 줄로 작성되는 _익명_ 함수입니다.
```python
lambda x: x * 2
```
구문은 `lambda parameters: expression`입니다.
lambda는 이름이 없지만, 변수에 저장하여 다른 함수처럼 호출할 수 있습니다.
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

lambda의 본문에는 `return` 키워드가 없다는 점에 주목하세요.
본문은 **단일 표현식**이며, 그 값은 자동으로 반환됩니다.
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

lambda는 **둘 이상의 매개변수**를 받을 수 있습니다.
`def` 함수에서와 정확히 같은 방식으로 쉼표로 구분합니다.
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

본문이 단일 표현식이어야 하므로, lambda는 **문(statement)을 포함할 수 없습니다**.
`return`도, `if` 블록도, 반복문도, 대입문도 없습니다.
```python
# SyntaxError
increment = lambda x: return x + 1
```
이런 것들이 필요하다면, 대신 일반적인 `def` 함수를 작성하세요.

---

lambda의 매개변수도 **기본값**을 지원합니다.
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

lambda를 저장할 필요조차 없습니다. **즉시 호출**할 수도 있습니다.
lambda를 괄호로 감싼 다음 인자를 추가하세요.
```python
print((lambda x: x + 1)(4))  # 5
```

---

lambda가 진가를 발휘하는 곳은 바로 **다른 함수의 인자**로 사용될 때입니다.
`sorted()`는 `key` 매개변수를 받습니다. 이는 각 항목에 대해 호출되는 함수이며, 그 결과가 순서를 결정합니다.
lambda가 여기에 완벽하게 어울립니다.
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

`key`에 전달하는 lambda는 항목의 어떤 부분이든 선택할 수 있습니다.
리스트의 리스트의 경우, `lambda p: p[1]`은 각 내부 리스트의 두 번째 요소를 기준으로 정렬합니다.

---

`map()`은 리스트의 **모든 항목**에 함수를 적용합니다.
특별한 _map 객체_를 반환하므로, 값을 확인하려면 `list()`로 감싸야 합니다.
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()`는 함수가 `True`를 반환하는 항목만 남깁니다.
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

`map` 객체를 그대로 출력하면 값이 보이지 않고 `<map object at 0x7f2b1c>` 같은 결과가 나옵니다.
`list()`(또는 반복문)를 사용해야 기대한 값을 얻을 수 있습니다.

---

lambda는 내장 함수에만 국한되지 않습니다. **여러분이 직접 만든 함수**도 함수를 매개변수로 받아 호출할 수 있습니다.
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

`max()`와 `min()`도 `sorted()`와 마찬가지로 `key` 함수를 받을 수 있습니다.
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**그렇다면 언제 `def`를 사용해야 할까요?**
lambda는 인자로 전달되는 짧고 일회성인 함수에 적합합니다.
로직에 이름, 여러 줄, docstring이 필요하거나 여러 곳에서 재사용된다면, `def` 함수가 더 명확합니다.
마지막으로 한 가지 팁: `sorted()`는 `reverse=True`도 받을 수 있어서 가장 큰 값부터 얻을 수 있습니다.
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
