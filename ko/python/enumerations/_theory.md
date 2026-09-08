**열거형**(enumeration, 줄여서 *enum*)은 요일이나 신호등의 색처럼 관련된 고정된 값들의 그룹에 공통 타입을 정의합니다.
문자열이나 숫자를 그때그때 직접 전달하는 대신 각 값에 **이름**을 부여하므로, 코드가 더 읽기 쉬워지고 오타는 오류가 됩니다.
Python에서는 `enum` 모듈에서 `Enum`을 임포트하고 이를 상속하는 클래스를 선언하여 열거형을 만듭니다.
각 클래스 속성은 이름과 값을 가진 열거형의 **멤버**입니다:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
관례상 멤버 이름은 대문자로 작성합니다. 멤버는 클래스를 통해 접근하며, 출력하면 클래스 이름과 멤버 이름이 표시됩니다:
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

열거형의 모든 멤버는 두 개의 속성을 가집니다: 클래스에 작성한 식별자인 `name`과, 여러분이 할당한 값인 `value`입니다:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
값은 정수뿐만 아니라 어떤 타입이든 될 수 있습니다: 문자열, 튜플, 실수가 흔한 선택입니다.
멤버는 일반 객체이므로 변수에 저장해 두었다가 나중에 그 속성을 읽을 수 있습니다:
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

각 열거형 멤버는 **한 번만** 존재합니다: `Color.RED`를 쓸 때마다 항상 똑같은 객체를 얻습니다.
따라서 멤버는 `==`뿐만 아니라 `is`(동일성)로도 비교할 수 있으며, 둘 다 같은 결과를 줍니다:
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
멤버는 그 원시 값과 **같지 않습니다**. 멤버와 단순한 숫자는 서로 다른 것이기 때문입니다:
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
이것이 열거형을 안전하게 만드는 이유입니다: 프로그램의 다른 곳에서 온 `1`이 `Color.RED`로 잘못 해석될 수 없습니다.

---

열거형 클래스는 **반복 가능**합니다: 클래스에 대한 `for` 반복문은 선언된 순서대로 모든 멤버를 방문합니다:
```python
for color in Color:
    print(color.name, color.value)
```
`len()`은 열거형이 가진 멤버 수를 반환하고, `list(Color)`는 멤버들의 리스트를 만듭니다:
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
리스트 안에서는 멤버가 `repr()`로 표시되며, 여기에는 꺾쇠 괄호 사이에 값이 포함됩니다.

---

클래스를 함수처럼 호출하여 **값**에서 멤버를 얻거나, 대괄호를 사용하여 **이름**에서 멤버를 얻을 수 있습니다:
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
값이나 이름이 파일이나 사용자 입력처럼 프로그램 외부에서 올 때 두 방법 모두 유용합니다.
일치하는 것이 없으면 `Color(9)`는 `ValueError`를 발생시키고, `Color["PINK"]`는 `KeyError`를 발생시킵니다.

---

정확한 값이 중요하지 않은 경우가 많습니다: 멤버들이 서로 구별되기만 하면 됩니다.
그런 경우 `enum` 모듈에서 임포트하는 `auto()`로 Python이 값을 정하도록 할 수 있습니다.
`auto()`는 첫 번째 멤버에 `1`을 할당한 뒤 하나씩 증가시킵니다:
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

일반 `Enum` 멤버는 `<`로 비교하거나 숫자에 더할 수 없습니다.
멤버들이 순서가 필요한 **수준**을 나타낼 때는 대신 `IntEnum`을 상속하세요: 멤버들이 정수이기도 하므로 비교, 산술, 정렬을 지원합니다:
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.LOW + 1)              # 2
print(int(Priority.MEDIUM))          # 2
```
`IntEnum` 멤버는 자신의 정수 값과 같기도 합니다: `Priority.LOW == 1`은 `True`입니다.

---

`StrEnum`(Python 3.11부터 사용 가능)은 `IntEnum`의 문자열 버전입니다: 멤버들이 문자열이기도 하며 자신의 값과 같습니다.
덕분에 설정 키나 API 매개변수처럼 일반 문자열이 기대되는 곳 어디서든 편리하게 사용할 수 있습니다:
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
일반 `Enum`과 달리, `StrEnum` 멤버를 `str()`이나 f-string 안에서 텍스트로 변환하면 `Mode.DARK`가 아니라 그 **값**이 됩니다.

---

열거형은 클래스이므로 다른 클래스처럼 **메서드**와 **프로퍼티**를 가질 수 있습니다.
그 안에서 `self`는 메서드가 호출된 멤버이므로, `self.name`이나 `self.value`를 보거나 `self`를 다른 멤버와 비교할 수 있습니다:
```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2

    def can_go(self):
        return self is Light.GREEN

    @property
    def label(self):
        return self.name.lower()

print(Light.GREEN.can_go())  # True
print(Light.RED.label)       # red
```
클래스 본문에 할당된 일반 값은 멤버가 되지만, 함수와 프로퍼티는 어디에 나타나더라도 절대 멤버가 되지 않습니다.

---

두 멤버가 같은 값을 가지면 두 번째 멤버는 새로운 멤버가 아니라 첫 번째 멤버의 **별칭(alias)**입니다:
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
별칭은 반복할 때 건너뛰어지며 `len()`으로 세지 않습니다.
보통 중복된 값은 실수입니다. `enum`에서 임포트하는 `unique` 데코레이터는 별칭을 가진 열거형이 선언되는 즉시 Python이 `ValueError`를 발생시키게 합니다:
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

`Flag`는 멤버들을 **조합**할 수 있는 열거형입니다: 하나의 값이 옵션 집합처럼 여러 멤버를 한 번에 담을 수 있습니다.
멤버는 `auto()`로 선언하세요. `Flag`에서 `auto()`는 2의 거듭제곱(`1`, `2`, `4`, ...)을 할당하므로 모든 조합이 고유한 값을 가집니다:
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
`|`로 멤버를 조합하고, `in`으로 멤버가 조합에 포함되어 있는지 확인하고, `value`로 결과 숫자를 확인하세요:
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

열거형은 `match` 문(Python 3.10부터 사용 가능)과 자연스럽게 어울립니다. `match` 문은 값을 일련의 `case` 패턴과 비교하여 일치하는 첫 번째 패턴을 실행합니다:
```python
def action(light):
    match light:
        case Light.RED:
            return "Stop"
        case Light.GREEN:
            return "Go"
        case _:
            return "Slow down"
```
항상 `Light.RED`처럼 멤버를 클래스와 함께 작성하세요: `case RED:` 같은 맨 이름은 아무것도 비교하지 않고, 그저 값을 새 변수 `RED`에 담아 모든 것에 일치시킬 뿐입니다.
와일드카드 `case _:`는 기본값이며 마지막에 와야 합니다. 그 뒤에 오는 패턴은 절대 도달할 수 없기 때문입니다.

---

열거형 멤버는 **해시 가능**하므로 딕셔너리 키와 집합 요소로 사용할 수 있습니다.
열거형을 키로 하는 딕셔너리는 각 멤버에 데이터를 붙이는 깔끔한 방법이며, 멤버로 조회하는 것은 오타가 날 수 있는 일반 문자열을 사용하는 것보다 안전합니다:
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
멤버는 어떤 컬렉션에도 나타날 수 있으므로, 리스트, 집합, 컴프리헨션에 대해 아는 모든 것이 멤버에도 그대로 적용됩니다:
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

멤버 값은 **튜플**일 수 있으며, 이를 통해 각 멤버에 여러 조각의 데이터를 붙일 수 있습니다.
열거형이 `__init__` 메서드를 정의하면 Python은 각 멤버마다 한 번씩 호출하면서 튜플을 매개변수로 언패킹하므로, 각 조각을 자신만의 속성에 저장할 수 있습니다:
```python
from enum import Enum

class Planet(Enum):
    EARTH = (5.97, 6371)
    MARS = (0.64, 3390)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

print(Planet.MARS.radius)  # 3390
print(Planet.MARS.value)   # (0.64, 3390)
```
멤버의 `value`는 전체 튜플 그대로입니다.

---

로그 줄이나 파일처럼 외부에서 들어오는 데이터를 처리할 때는 클래스를 반복하는 것과 이름으로 멤버를 조회하는 것이 잘 어울립니다.
클래스에 대한 딕셔너리 컴프리헨션이 멤버마다 하나의 항목을 준비하고, `Level[name]`이 들어오는 각 문자열을 일치하는 멤버로 변환합니다:
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
열거형은 선언 순서를 유지하므로, 나중에 `counts`를 반복하면 그와 같은 순서로 멤버를 얻습니다.

---

일반 메서드 외에도 열거형은 `@classmethod`로 **클래스 메서드**를 정의할 수 있습니다. 클래스 메서드는 열거형 클래스 자신을 `cls`로 받으므로, 멤버를 찾는 대체적인 방법을 담기에 알맞은 자리입니다:
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
`auto()`와 메서드, 프로퍼티, 조회가 함께 어우러져 자신만의 동작을 지니는 열거형을 만들 수 있습니다.
