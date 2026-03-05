프로그래밍에서 코드 블록을 반복해야 하는 경우가 자주 있습니다. 예를 들어:
```python
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
이 코드는 다음과 같은 출력을 생성합니다:
```python
2 seconds
3 seconds
4 seconds
5 seconds
```
당연히, 긴 구문을 작성하려면 많은 시간이 걸리지만, 다행히 반복문을 사용할 수 있습니다.
위와 동일한 출력을 얻기 위해 `while` 반복문을 배워봅시다.
```python
count = 2
while (count <= 5):
    print(f"{count} seconds")
    count += 1
```
먼저 변수 `count`를 생성하고 초기값 `2`를 할당했습니다.
그런 다음 `while` 문을 사용하여 조건 `count <= 5`가 `True`인 동안 코드 블록을 실행합니다.
코드 블록 내에서 `count += 1` 줄을 **반드시** 추가해야 합니다.
이 줄은 `count` 값을 증가시키며, 그렇지 않으면 반복문이 무한히 실행됩니다

---

`while` 반복문이 반복하는 횟수를 제어하려면, 숫자로 설정된 변수를 사용합니다.
이 변수를 카운터 변수라고 합니다

---

그런 다음, 조건에서 비교를 사용하여 `counter` 변수를 숫자와 비교합니다.

---

코드 블록 내에서 `while` 반복문을 멈추기 위해 `counter` 변수를 증가시킵니다.

---

코드를 작성하는 순서가 출력에 영향을 줍니다.
