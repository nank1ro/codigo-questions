때로는 변수가 아직 담을 **값이 없는** 경우가 있습니다: 로그인하지 않은 사용자, 아무것도 찾지 못한 검색, 한 번도 선택되지 않은 설정. Python은 이를 특별한 값 `None`으로 나타냅니다.
`None`은 다른 값과 마찬가지로 값입니다: 대입하고, 출력하고, 함수에 전달할 수 있습니다. 그 타입은 `NoneType`이며, 프로그램 전체에 정확히 **하나의** `None`만 있으므로 여러분이 쓰는 모든 `None`은 같은 객체를 참조합니다:
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None`은 `0`도, 빈 문자열도, `False`도 아닙니다: "여기엔 아무것도 없다"를 뜻하는 별도의 값입니다.

---

모든 함수 호출은 값을 만들어냅니다. 함수가 아무것도 반환하지 않는 것처럼 보일 때도 마찬가지입니다. `return` 문이 **없는** 함수, 또는 그냥 `return`만 있는 함수는 `None`을 돌려줍니다:
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
그래서 `print(my_list.append(3))`를 호출하면 `None`이 출력됩니다: `append`는 리스트를 제자리에서 변경하고 아무것도 반환하지 않습니다.
동작만 수행하는 함수(출력, 저장, 리스트 변경)는 보통 `None`을 반환하는 반면, 무언가를 계산하는 함수는 반드시 명시적으로 `return`해야 합니다.

---

변수가 `None`을 담고 있는지 확인하려면 `==`이 아니라 `is`와 `is not`을 사용하세요:
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==`는 "이 값들이 *동등한가*?"를 묻고, 어떤 클래스든 `__eq__` 메서드를 정의하여 그 질문에 자신만의 방식으로 답할 수 있습니다. `is`는 "이것들이 *같은 객체*인가?"를 묻고, 아무도 그 답을 바꿀 수 없습니다.
`None`은 하나뿐이므로 `is None`은 항상 올바르고 약간 더 빠른 반면, `== None`은 커스텀 `__eq__`를 가진 객체에 대해 놀라운 답을 줄 수 있습니다.

---

`None`은 조건에서 **거짓**으로 취급되므로, `value`가 `None`일 때 `if not value:`는 `True`입니다. 이를 `None` 검사로 쓰고 싶어지지만, 같은 검사가 `0`, `""`, `[]`를 비롯한 다른 모든 빈 값에 대해서도 `True`입니다:
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
"값 없음"과 "빈 값"을 다르게 다뤄야 할 때는 먼저 `is None`을 확인한 다음 truthiness를 확인하세요:
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
정말로 `None`과 빈 값을 같은 방식으로 다루고 싶을 때만 `if not value:`를 사용하세요.

---

매개변수는 **기본값**을 가질 수 있으며, 이는 호출자가 인자를 생략할 때 사용됩니다. "제공되지 않음"의 기본값으로는 `None`이 보통 쓰입니다:
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
이것이 리스트와 딕셔너리에서 문제가 됩니다. 기본값은 함수가 정의될 때 **한 번만** 평가되므로, `def add(item, items=[])`는 `items`를 생략하는 모든 호출에서 같은 리스트를 공유하고 항목이 쌓입니다. 해결책은 `None`을 기본값으로 두고 함수 안에서 새 리스트를 만드는 것입니다:
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

딕셔너리에서 `[]`로 없는 키를 읽으면 `KeyError`가 발생합니다. `get` 메서드가 안전한 대안입니다: 키가 있으면 값을 반환하고 없으면 `None`을 반환합니다:
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get`은 두 번째 인자를 받습니다. 키가 없을 때 `None` **대신에** 반환할 값입니다:
```python
print(ages.get("Grace", 0))  # 0
```
이것이 일상적인 코드에서 `None`이 나타나는 가장 흔한 방식입니다: 아무것도 찾지 못한 조회입니다.

---

숫자 **또는** `None`을 반환하는 함수는 그 사실을 시그니처에 밝혀야 합니다. **타입 힌트**는 기대되는 타입을 문서화하는 어노테이션입니다: 매개변수에는 `name: str`, 반환 값에는 `-> int`. Python은 힌트를 강제하지 않지만, 편집기와 코드 읽는 사람이 이에 의존합니다:
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None`은 "`int` 또는 `None`"으로 읽습니다. `typing` 모듈의 이전 표기법인 `Optional[int]`는 정확히 같은 의미이며, 기존 코드에서 여전히 만나게 될 것입니다.
시그니처에서 `| None`을 볼 때마다, 그 결과를 사용하기 전에 검사해야 함을 기억하세요.

---

`None`을 받을 수 있는 함수는 종종 **가드**로 시작합니다: 다룰 것이 없을 때 일찍 반환하는 `if`입니다. 그러면 함수의 나머지 부분은 모든 것을 `else` 안에 중첩하지 않고도 값이 존재한다고 가정할 수 있습니다:
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
가드는 검사가 일어나야 하는 순서대로 맨 앞에 옵니다: `text`가 `None`이 아님을 알기 전에는 `text.split()`을 호출할 수 없습니다.

---

`or` 연산자는 `True`나 `False`를 반환하지 않습니다: 왼쪽 피연산자가 참이면 **왼쪽** 피연산자를, 그렇지 않으면 **오른쪽** 피연산자를 반환합니다. 이를 통해 한 줄로 폴백을 제공할 수 있습니다:
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
문제는 `or`가 `None`이 아니라 truthiness를 본다는 것입니다: `0`, `""`, `[]`도 폴백으로 대체됩니다. 모든 빈 값이 폴백이 되어도 괜찮을 때만 `x or fallback`을 사용하세요.

---

`0`이나 `""`를 유지하고 `None`만 대체해야 할 때는, 폴백에 명시적인 `is None` 검사가 필요합니다. 간결한 형태는 **조건부 표현식** `a if condition else b`로, 조건이 참이면 `a`로 평가되고 그렇지 않으면 `b`로 평가됩니다:
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

리스트에는 실제 값 옆에 `None`이 담길 수 있습니다. 예를 들어 실패한 측정값이나 건너뛴 답변처럼 말입니다. 대부분의 연산은 이를 받아들이지 않습니다: `sum([8, None])`은 `TypeError`를 발생시킵니다.
조건이 `is not None`인 리스트 컴프리헨션으로 `None` 값을 걸러내세요:
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
대신 `if r`을 쓰면 모든 `0`까지 걸러지므로, 0이 유효한 측정값일 때는 명시적으로 쓰세요.

---

조회 후 `None` 검사는 보통 두 줄이 필요합니다: 결과를 저장하는 줄과 검사하는 줄입니다. **대입 표현식** 연산자 `:=`는 별명이 *walrus*이며, 표현식 **안에서** 값을 대입하므로 두 단계 모두 `if` 안에 들어갈 수 있습니다:
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
괄호가 필요합니다: 괄호가 없으면 `:=`가 비교 전체를 대입하려 합니다. `if` 이후에는 `age`가 다른 변수처럼 계속 사용할 수 있습니다.

---

모든 "찾지 못함"이 `None`으로 보고되는 것은 아닙니다. 일부 오래된 함수는 대신 **센티널** 값을 반환합니다. 특별한 의미가 부여된 일반 값입니다. 문자열 메서드 `find`는 부분 문자열의 인덱스를 반환하고, 없으면 `-1`을 반환합니다:
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
`re` 모듈의 `re.match(pattern, text)` 함수는 `text`가 `pattern`으로 시작하는지 검사하며, 매치 객체를 반환하거나 일치하지 않으면 `None`을 반환합니다.
`None`이 더 안전한 관례입니다: `-1`은 유효한 인덱스이므로 `text[text.find("x")]`는 실패하지 않고 조용히 마지막 문자를 반환하는 반면, `None`을 인덱스로 쓰면 바로 오류가 발생합니다.

---

`None`은 순서를 매길 수 없습니다: `None < 1`은 `TypeError`를 발생시킵니다. Python은 "아무것도 없음"이 숫자보다 작은지 큰지 알 방법이 없기 때문입니다.
`None`이 "지금까지 본 최고 값(있다면)" 같은 탐색의 시작 값으로 쓰일 때 이것이 문제가 됩니다. 모든 비교는 **먼저** 놓인 `is None` 검사로 보호되어야 합니다. 그래야 `or`가 단락 평가되어 아직 비교할 것이 없을 때 비교를 건너뜁니다:
```python
if best is None or value > best:
    best = value
```
반대로 쓰면 `value > best or best is None`이 첫 반복에서 `None`과 비교하다가 충돌합니다.
