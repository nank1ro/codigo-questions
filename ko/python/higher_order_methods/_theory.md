Python에서 함수는 숫자나 문자열처럼 **값**입니다. 변수에 저장하거나, 리스트에 넣거나, 다른 함수에 전달할 수 있습니다. 호출하는 것은 오직 괄호입니다: `shout`는 함수 그 자체이고, `shout("hi")`는 그 결과입니다:
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
다른 함수를 매개변수로 받거나 함수를 반환하는 함수를 **고차 함수**라고 합니다. 그 안에서 매개변수는 다른 함수와 마찬가지로 괄호를 붙여 호출됩니다:
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

함수를 인수로 전달하면 호출자가 **무엇을** 할지 결정하고, 고차 함수는 **몇 번** 또는 **무엇에 대해** 할지 결정합니다. 함수 매개변수는 필요한 만큼 여러 번 호출될 수 있고, 그 결과를 다시 함수에 넣을 수도 있습니다:
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
어떤 호출 가능한 것이라도 됩니다: `def` 함수, `len` 같은 내장 함수 또는 `lambda`.

---

내장 `map(func, iterable)`은 모든 요소에 `func`를 호출하고 각 요소마다 하나의 결과를 만들어 냅니다. 지연 평가되는 *map 객체*를 반환하므로, 값들을 보려면 `list()`로 감싸야 합니다:
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
lambda뿐만 아니라 어떤 호출 가능한 것도 전달할 수 있습니다: `len` 같은 내장 함수, 또는 문자열을 첫 번째 인수로 받는 `str.upper`처럼 클래스에서 가져온 메서드:
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

내장 `filter(func, iterable)`은 `func`가 참인 값을 반환하는 요소만 남깁니다. `map`처럼 지연 객체를 반환하므로 리스트로 바꿔야 합니다:
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
`filter`에 전달되는 함수를 **술어(predicate)**라고 합니다: 하나의 요소를 받아 그에 대한 예/아니오 질문에 답합니다. 함수 대신 `None`을 전달하면 스스로 참인 요소만 남고 `0`, `""`와 `None`은 버려집니다.

---

`sorted(iterable, key=func)`는 요소 자체를 바꾸지 않고 각 요소에 대해 `func`가 반환한 값을 기준으로 요소들을 정렬합니다. `reverse=True`를 추가하면 가장 큰 것부터 얻습니다:
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
정렬은 **안정적(stable)**입니다: 키가 같은 요소들은 원래 순서를 유지합니다. `key` 함수는 요소마다 한 번씩 호출되고 그 결과는 비교에만 사용되므로, 출력에는 길이가 아니라 원래 단어가 그대로 들어 있습니다.

---

`key` 함수는 요소의 **어떤 부분**이든 선택할 수 있습니다. 튜플 리스트에서 `lambda s: s[1]`은 각 튜플의 두 번째 항목을 기준으로 정렬하고, 딕셔너리 리스트에서 `lambda d: d["age"]`는 값을 기준으로 정렬합니다:
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min`과 `max`도 같은 `key` 매개변수를 받으므로, `max(pairs, key=lambda p: p[1])`는 `('a', 3)`, 즉 숫자만이 아니라 튜플 전체를 반환합니다.

---

함수는 함수를 **반환**할 수도 있습니다. `def`로 내부 함수를 정의하고 호출하지 않고 반환하세요:
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
내부 함수는 `make_greeter`가 끝난 후에도 `greeting`을 계속 사용합니다: 자신이 생성된 스코프의 변수를 **기억**합니다. 이런 함수를 **클로저(closure)**라고 합니다. `make_greeter`를 호출할 때마다 자신만의 `greeting`을 가진 새로운 독립적인 클로저가 만들어집니다.

---

클로저는 감싸는 함수의 변수를 읽을 수 있지만, 그 변수에 대입하면 대신 **새로운 지역** 변수가 만들어집니다. 바깥 변수를 갱신하려면 내부 함수 안에서 `nonlocal`로 선언하세요:
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global`은 모듈 수준에서 `count`를 찾지만, 거기에는 존재하지 않습니다. `nonlocal`을 사용하면 반환된 함수를 호출할 때마다 같은 `count`가 갱신되므로, 클로저는 호출 사이에 작은 객체처럼 상태를 유지합니다.

---

`functools` 모듈의 `reduce(func, iterable, initial)`은 시퀀스를 **하나의 값**으로 접습니다. `initial`에서 시작하여 지금까지의 결과와 다음 요소로 `func`를 호출합니다:
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
단계는 `0 + 1`, 그다음 `1 + 2`, 그다음 `3 + 3`입니다. `initial`이 생략되면 첫 번째 요소가 시작 값으로 사용되지만, 그 경우 빈 시퀀스는 `TypeError`를 발생시키므로 시퀀스가 비어 있을 수 있다면 항상 초기 값을 주세요.

---

`functools`의 `partial(func, *fixed)`는 일부 인수가 **이미 채워진** 새 함수를 만듭니다. 그 결과를 호출하면 나머지 인수를 공급합니다:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
`partial`에 주어진 위치 인수는 첫 매개변수들을 채웁니다; 키워드 인수는 이름으로 매개변수를 고정하며 호출 시점에 여전히 재정의할 수 있습니다. partial은 일반적인 호출 가능 객체이므로 `map`, `sorted` 또는 다른 어떤 고차 함수에도 전달할 수 있습니다.

---

`partial`은 옵션을 받는 내장 함수와 함께 쓰면 유용합니다. `int(text, base=16)`은 16진수 문자열을 파싱합니다; 밑을 고정하면 `map`에 딱 맞는 인수 하나짜리 변환기가 됩니다:
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
partial 객체는 감싸고 있는 것을 기억합니다: `hex_to_int.func`는 `int`이고, `hex_to_int.keywords`는 `{'base': 16}`입니다.

---

**데코레이터(decorator)**는 함수를 받아 그것을 감싸는 새 함수를 반환하는 고차 함수로, 보통 원래 호출 전후에 동작을 추가합니다:
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__`은 함수가 정의될 때의 이름입니다. 데코레이터를 적용하는 것은 그저 호출입니다: `greet = announce(greet)`. `def` **위** 줄에 놓이는 `@` 구문이 정확히 그것을 합니다:
```python
@announce
def greet(name):
    return "Hello, " + name
```
데코레이터는 `@`와 함께 사용되기 전에 정의되어야 합니다. 교체는 `def`가 실행되자마자 일어나기 때문입니다.

---

인수를 하나만 받는 데코레이터는 별로 쓸모가 없습니다. **어떤** 함수든 감싸려면 wrapper가 모든 위치 인수를 `*args`로, 모든 키워드 인수를 `**kwargs`로 모아 변경 없이 전달합니다:
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
wrapper 안에서 `args`는 튜플이고 `kwargs`는 딕셔너리입니다; 호출 시의 `*`와 `**`는 이들을 다시 개별 인수로 풀어줍니다.

---

`any(iterable)`은 **적어도 하나의** 요소가 참이면 `True`를 반환하고, `all(iterable)`은 **모든** 요소가 참이면 `True`를 반환합니다. 둘은 **제너레이터 표현식**과 자연스럽게 어울립니다: 대괄호 없이 쓴 리스트 컴프리헨션으로, 리스트를 만드는 대신 값을 한 번에 하나씩 만들어 냅니다:
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
값이 지연되어 만들어지기 때문에, `any`는 첫 번째 `True`에서, `all`은 첫 번째 `False`에서 나머지를 평가하지 않고 멈춥니다. `sum`도 제너레이터 표현식을 받습니다: `sum(1 for age in ages if age >= 18)`은 어른의 수를 셉니다.
