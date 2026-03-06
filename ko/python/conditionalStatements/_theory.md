특정 조건이 충족될 때만 코드를 실행하려면 의사 결정이 필요합니다.
날씨가 좋을 때만 밖에서 놀고 싶다고 가정해 봅시다.
프로그래밍에서는 불리언 변수 `nice_weather`를 저장하고, 이 변수가 `True`일 때 밖에서 노는 행동을 `if`로 수행할 수 있습니다:
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

이전 예제를 계속 살펴봅시다.
```python
nice_weather = True
if (nice_weather):
    # play outside
```
`if` 문은 조건이 `True`일 때만 코드 블록을 실행한다는 것을 배웠습니다.
또 하나 중요하게 고려해야 할 것은 **콜론** `:`과 **들여쓰기**인데, 이는 코드 블록의 시작을 나타냅니다.
들여쓰기란 코드 줄의 시작 부분에 있는 공백을 말합니다.
다른 프로그래밍 언어에서는 코드의 들여쓰기가 가독성만을 위한 것이지만, Python에서는 들여쓰기가 필수적입니다.
원하는 공백 수(2, 4, 6, 8)를 사용할 수 있으며, 권장되는 것은 4칸입니다.
이 앱에서는 코드 줄을 들여쓸 때 **TAB** 키를 사용하는 것을 권장합니다

---

조건이 발생할 때 코드 블록을 실행하는 방법을 배웠습니다. 이제 첫 번째 조건이 실패할 때 다른 코드 블록을 실행하는 방법을 알아봅시다.
날씨가 좋으면 밖에서 놀고, 그렇지 않으면 집에 있습니다.
Python에서는 `else` 문을 사용할 수 있습니다:
```python
nice_weather = True
if (nice_weather):
    # play outside
else:
    # stay home
```

---

확인해야 할 조건이 하나 더 있다고 가정해 봅시다. 다음 예제를 살펴보겠습니다:
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
이 코드의 출력은 `the number is 3`입니다.
먼저 숫자가 2와 같은지 확인합니다. 이것은 거짓입니다.
그래서 두 번째 문으로 넘어가서 `num`이 3과 같은지 확인하고, 참이므로 `the number is 3`을 출력하는 다음 코드 블록을 실행합니다

---

`elif` 문은 원하는 만큼 추가할 수 있으며, 제한이 없습니다
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
이 코드의 출력은 `the number is 4`입니다.

---

조건문(`if`, `elif` 또는 `else`)을 다른 조건문 안에 중첩하여 더 복잡한 구조를 만들 수도 있습니다.
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
이 코드의 출력은 `the number is 4`입니다.
