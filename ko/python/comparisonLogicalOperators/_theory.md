비교 연산자는 두 값을 비교해 **불리언** `True` 또는 `False`를 반환합니다. `==` 같음, `!=` 같지 않음, `<` 작음, `>` 큼, `<=` 작거나 같음, `>=` 크거나 같음:
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
결과는 변수에 저장하거나 바로 출력할 수 있습니다. 하나뿐인 `=`는 대입이지 비교가 아닙니다.

---

비교 연산자는 숫자에만 쓰이는 것이 아닙니다. 문자열은 코드 포인트를 사용해 문자 단위로 비교되므로 `"apple" < "banana"`는 `True`이고, 모든 대문자가 소문자보다 앞서기 때문에 `"Zoo" < "apple"`도 `True`입니다. 리스트와 튜플도 같은 방식으로 요소 단위로 비교됩니다:
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
비교는 표현식이므로 함수는 `if`로 감싸지 않고 바로 `return a < b`라고 쓸 수 있습니다.

---

비교는 **연결**할 수 있습니다. `1 < x < 10`은 `x`가 `1`보다 크고 **그리고** `10`보다 작은지를 확인하며, `1 < x and x < 10`과 정확히 같지만 `x`는 한 번만 평가됩니다:
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
어떤 비교 연산자든 연결할 수 있고 각 연산자는 양옆의 두 값에 적용됩니다. `a < b == c`는 `a < b and b == c`를 뜻합니다. 연결을 범위 `low < x < high`처럼 읽는 것이 가장 흔한 사용법입니다.

---

논리 연산자는 불리언을 결합합니다. `and`는 양쪽이 모두 `True`일 때만 `True`이고, `or`는 최소한 한쪽이 `True`일 때이며, `not`은 하나의 값을 뒤집습니다:
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
비교는 논리 연산자보다 우선순위가 높으므로 `age >= 18 and member`에는 괄호가 필요 없습니다. `and` 안에 `or`를 묶으려면 괄호가 필요합니다: `a and (b or c)`.

---

`not`, `and`, `or`가 한 표현식에 함께 나오면 Python은 `not`을 먼저, 그다음 `and`, 마지막으로 `or`를 적용합니다. 그래서 `a or b and c`는 `a or (b and c)`를 뜻하고, `not a == b`는 `not (a == b)`를 뜻합니다:
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
다른 묶음을 의도한다면 괄호를 추가하세요. 괄호는 표현식을 더 읽기 쉽게도 만들어 줍니다.

---

모든 값에는 **진리값**이 있습니다. `bool(value)`는 `0`, `0.0`, `None`, 빈 문자열 `""`, 그리고 `[]`, `{}`, `set()` 같은 빈 컨테이너에 대해 `False`를 반환합니다. 그 밖의 모든 값은 참이며 `"0"`과 `[0]`도 포함됩니다:
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`, `while`, `and`, `or`, `not`이 이 규칙을 사용하므로 `if items:`는 리스트가 비어 있지 않은지 확인하고 `not name`은 문자열이 비어 있는지 확인합니다. `len(items) > 0`이나 `name == ""`라고 쓸 필요가 없습니다.

---

`if value:`가 이미 진리값을 적용하므로 `== True`나 `== False`와 비교하는 것은 불필요하며 틀릴 수도 있습니다. `2 == True`는 `False`이지만 `2`는 참입니다. 값 자체를 검사하세요:
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and`와 `or`가 항상 `True`나 `False`를 반환하는 것은 아닙니다. 이들은 **피연산자** 중 하나를 반환합니다. `a and b`는 `a`가 거짓이면 `a`를, 아니면 `b`를 반환합니다. `a or b`는 `a`가 참이면 `a`를, 아니면 `b`를 반환합니다:
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
결과가 참인지 거짓인지는 표현식 전체와 정확히 일치하므로 `if a and b:`는 그대로 동작합니다. 흔한 사용법은 기본값입니다: `name = user_input or "guest"`.

---

논리 연산자는 **단락 평가**를 합니다. 결과가 이미 정해지므로 `and`는 피연산자가 거짓이 되는 즉시, `or`는 참이 되는 즉시 멈춥니다. 남은 피연산자는 평가되지 않으므로 함수 호출이라면 실행되지 않습니다:
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==`는 **값**을 비교하고 `is`는 **정체성**, 즉 두 이름이 완전히 같은 객체를 가리키는지를 비교합니다. 따로 만든 두 개의 같은 리스트는 `==`이지만 `is`는 아닙니다:
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is`는 `None`, `True`, `False` 같은 싱글턴을 위한 것입니다. `value is None`이나 `value is not None`이라고 쓰고 `value == None`이라고는 절대 쓰지 마세요. 클래스가 `==`를 무엇이든 반환하도록 정의할 수 있기 때문입니다. 숫자나 문자열에 `is`를 쓰는 것은 신뢰할 수 없으며 Python이 경고합니다.

---

단락 평가는 일부 값에서 실패할 연산을 **보호**하는 안전한 방법입니다. `word is not None and len(word) < 4`에서 `len(word)`는 `word`가 `None`이 아닐 때만 실행되므로 호출이 오류를 일으키지 않습니다. 보호 조건이 먼저 와야 합니다:
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
`and`는 피연산자를 반환한다는 점을 기억하세요. `word and len(word) < 4`는 `None`에 대해 `None`을, 빈 문자열에 대해 `""`를 주며 `False`를 주지 않습니다. 불리언이 필요하면 실제 비교로 보호하세요.

---

`in` 연산자는 **포함 여부**를 확인합니다. 어떤 요소가 리스트, 튜플, 집합에 있는지, 부분 문자열이 문자열에 있는지, 키가 딕셔너리에 있는지를 확인합니다. `not in`은 그 부정입니다:
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
둘 다 불리언을 반환하고 영어처럼 읽히므로, 반복문을 쓰는 대신 포함 여부를 확인하는 선호되는 방법입니다.
