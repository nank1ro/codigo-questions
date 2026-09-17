**예외(exception)**는 문장을 실행할 수 없다고 Python이 말하는 방식입니다. 0으로 나누기, `"abc"`를 정수로 변환하기, 존재하지 않는 딕셔너리 키 읽기는 모두 예외를 발생시킵니다. 아무것도 처리하지 않으면 프로그램은 바로 그 자리에서 멈추고 **트레이스백(traceback)**을 출력합니다:
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
트레이스백은 실행 중이던 줄들을 나열하고, 마지막 줄은 **예외 타입**(`ZeroDivisionError`)과 그 메시지(`division by zero`)를 알려줍니다. 이 마지막 줄을 가장 먼저 읽어야 합니다.

프로그램을 계속 살아 있게 하려면 위험한 문장을 `try` 블록에 넣고, 복구 방법을 `except` 블록에 기술하세요:
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Python은 `try` 블록을 실행합니다; 이름 붙은 예외가 발생하면 곧바로 일치하는 `except` 블록으로 점프하여 프로그램의 나머지 부분을 계속 진행합니다.

---

`try` 블록은 예외를 발생시키는 **첫 번째** 문장에서 멈춥니다; 그 뒤의 줄들은 건너뛰고 제어는 `except` 블록으로 이동합니다. `try` 블록 안의 어떤 것도 되돌려지지 않으므로, 가능한 한 짧게 유지하세요:
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
`except` 안의 `return`은 다른 `return`과 똑같이 동작하므로, `try`/`except`는 프로그램을 강종하는 대신 대체 값을 돌려주는 자연스러운 방법이 됩니다.

---

어떤 `except` 블록과도 일치하지 않는 예외는 계속 바깥쪽으로 전파됩니다: 해당 줄을 벗어나, 그 줄을 실행한 함수를 벗어나고, 다시 그 호출자를 벗어나는 식입니다. 프로그램의 최상위에 이를 때까지 아무것도 잡지 못하면 Python은 트레이스백을 출력하고 프로세스는 0이 아닌 종료 상태로 끝납니다. 실패한 문장 뒤의 줄들은 절대 실행되지 않습니다.

---

`except` 절은 이름을 명시한 타입과 그 하위 클래스만 잡습니다. 이것이 핵심입니다: 그 밖의 모든 것은 계속 바깥쪽으로 전파되므로, 예상하지 못한 버그는 삼켜지는 대신 여전히 트레이스백으로 나타납니다.

`int(text)`는 텍스트가 정수를 나타내지 않을 때 **`ValueError`**를 발생시키므로, 사용자 입력을 읽을 때 명시할 타입은 바로 이것입니다:
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
여기서 `ValueError`를 명시하는 것은 형식이 아니라 결정입니다: `int(None)`은 `TypeError`를 발생시키는데, 이 함수는 일부러 그것을 **잡지 않습니다**. `None`을 전달하는 것은 프로그래밍 실수이며 드러나야 하기 때문입니다.

---

예상하는 실패를 다루는 가장 좁은 타입을 고르는 것이 오류 처리를 신뢰할 수 있게 만듭니다. 텍스트를 읽는 함수는 잘못된 텍스트(`ValueError`)에서는 복구해야 하지만, 잘못된 종류의 인자로 호출되는 것(`TypeError`)은 숨겨서는 안 됩니다 — 그 오류는 호출자의 몫이므로 그대로 통과시키세요.

---

하나의 `try` 블록 뒤에는 **여러 개의** `except` 절이 올 수 있으며, 각 절은 서로 다른 실패를 서로 다른 복구 방법으로 처리합니다. Python은 발생한 예외를 위에서부터 아래로 비교하여 일치하는 **첫 번째** 절을 실행하고, 나머지는 건너뜁니다:
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
첫 번째 일치가 이기므로, 타입들이 서로 관련되어 있을 때는 순서가 중요합니다: 일반 타입의 절이 더 구체적인 타입의 절 위에 놓이면 항상 일반 절이 이겨서 구체적인 절에는 도달할 수 없게 됩니다.

---

여러 실패가 **같은** 복구를 필요로 할 때는, 블록을 반복하는 것보다 하나의 절에 튜플로 나열하는 쪽이 더 간결합니다:
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
괄호는 필수입니다: `except ValueError, ZeroDivisionError:`는 Python 3에서 문법 오류입니다. 튜플은 여전히 명시적인 타입 목록입니다.

---

뒤에 타입 없이 `except:`만 쓰면 이를 **베어 except(bare except)**라 합니다. 이것은 모든 것과 일치하며, 여러분이 보호하던 연산과 아무 상관 없는 예외까지도 포함합니다. 따라서 규칙은 간단합니다: 실제로 복구할 수 있는 타입은 항상 명시하세요.

---

예외는 객체이며, `as`는 그 객체를 이름에 묶어서 핸들러가 들여다볼 수 있게 해줍니다:
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)` — `print(e)`와 f-string 슬롯이 사용하는 것입니다 — 는 예외가 만들어질 때 담긴 메시지를 주고, `type(e).__name__`은 클래스 이름을 텍스트로 줍니다. `as`가 묶은 이름은 `except` 블록 안에서만 존재하며, 블록이 끝나면 Python이 그 이름을 삭제합니다.

---

`try` 블록 뒤에는 `else` 블록이 올 수 있으며, 이것은 **`try` 블록이 예외 없이 끝났을 때만** 실행됩니다:
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
`print(number * 2)`를 `try` 블록 안에 넣어도 동작은 하지만, 그렇게 하면 출력 자체가 발생시킨 `ValueError`가 변환 실패로 오인될 수 있습니다. `else`는 `try` 블록을 보호 대상인 단 하나의 문장으로 유지하고, 성공했을 때 일어나야 할 모든 일을 담습니다.

---

`finally` 블록은 **무슨 일이 있어도** 실행됩니다: `try` 블록이 문제없이 끝난 후에도, `except` 블록 후에도, 아무도 잡지 않은 예외가 바깥쪽으로 전파되는 중에도, `try`나 `except` 블록이 `return`을 실행할 때에도 마찬가지입니다:
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
두 경로 모두 값이 함수를 떠나기 전에 `done`을 출력합니다. 이 보장이 `finally`의 존재 이유입니다: 파일 닫기, 락 해제, 설정 복원 같은 일이죠. 전체 모양은 `try` / `except` / `else` / `finally`입니다; `try`에는 최소한 하나의 `except`나 `finally`가 필요하고, `else`는 `except`와 함께 있을 때만 동작합니다.

---

여러분의 코드도 `raise` 문 뒤에 예외 객체를 두어 예외를 발생시킬 수 있습니다:
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise`는 내장 실패가 그러하듯 함수를 즉시 멈춥니다. 대신 오류 값을 반환하는 것 — `-1`, `None`, `False` — 은 호출자가 잊기 쉽습니다; 예외는 우연히 무시될 수 없습니다.

문제를 설명하는 타입을 고르세요: 인자의 타입은 맞지만 값이 불가능하면 `ValueError`, 아예 타입이 틀리면 `TypeError`입니다. 예외에 전달된 텍스트가 그 메시지입니다.

---

소수의 내장 예외만으로 일상적인 대부분의 실패를 다룰 수 있습니다:

| 예외 | 발생 조건 | 예시 |
|---|---|---|
| `ValueError` | 타입은 맞지만 값이 불가능한 경우 | `int("abc")` |
| `TypeError` | 타입 자체가 틀린 경우 | `"x" + 1` |
| `ZeroDivisionError` | 나눗셈이나 모듈로의 나눗수가 0인 경우 | `1 / 0` |
| `KeyError` | 딕셔너리에 그런 키가 없는 경우 | `{"a": 1}["b"]` |
| `IndexError` | 시퀀스 인덱스가 범위를 벗어난 경우 | `[1, 2][5]` |

새 타입을 만드는 대신 이 중 하나를 사용하면, Python을 아는 누구에게나 여러분의 오류가 읽기 쉽게 유지됩니다.

---

때로는 핸들러가 실패를 자신의 책임으로 떠안지 않고 반응만 해야 할 때가 있습니다: 기록하고, 세고, 무언가를 닫은 다음 — 호출자가 처리하도록 남겨두는 것입니다. `except` 블록 안에서 홀로 쓰인 `raise`는 처리 중인 예외를 원래의 타입, 메시지, 트레이스백을 그대로 둔 채 **다시 발생시킵니다**:
```python
try:
    value = int(text)
except ValueError:
    print("could not read the value")
    raise
```
대신 `raise ValueError(...)`를 쓰면 자체 트레이스백을 가진 새 예외가 만들어집니다 — 더 이상 잡았던 것과 같은 실패가 아니게 되는데, 바로 이 동일성을 홀로 쓰인 `raise`가 지켜줍니다.

---

내장 타입이 맞지 않을 때는 `Exception`을 상속하여 직접 정의하세요. 빈 몸통으로도 보통 충분합니다 — 이름 자체가 읽는 이에게 하는 메시지입니다:
```python
class ConfigError(Exception):
    pass
```
다른 예외와 똑같이 동작합니다: `raise ConfigError("bad port")`로 발생시키고, `except ConfigError:`로 잡습니다.

저수준 실패를 여러분의 타입으로 바꿔 번역하는 일은 흔하며, 그 과정에서 원래 오류가 사라져서는 안 됩니다. `raise NewError(...) from original`은 둘을 **연결**합니다: `original`을 새 예외의 `__cause__` 속성에 저장하고, 트레이스백은 *The above exception was the direct cause of the following exception* 아래에 둘 다 보여줍니다:
```python
try:
    port = int(text)
except ValueError as e:
    raise ConfigError("bad port") from e
```
`from e`가 없어도 둘은 암묵적으로 연결되지만, `from`은 첫 번째 오류가 두 번째를 일으켰다는 사실을 말로 밝혀줍니다.
