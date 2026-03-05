프로그래밍에서 코드 블록을 반복해야 하는 경우가 자주 있습니다. 예를 들면:
```javascript
console.log("2 seconds");
console.log("3 seconds");
console.log("4 seconds");
console.log("5 seconds");
```
이 코드는 다음과 같은 출력을 생성합니다:
```javascript
2 seconds
3 seconds
4 seconds
5 seconds
```
당연히 긴 구문에 대해서는 코드를 작성하는 데 많은 시간을 소비하게 되지만, 다행히도 반복문을 사용할 수 있습니다.
위와 같은 출력을 얻기 위해 `while` 반복문을 배워봅시다.
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
변수 `count`를 만들고 초기값 `2`를 할당했습니다.
그런 다음 `while` 문을 사용하여 조건 `count <= 5`가 `true`인 동안 코드 블록을 실행합니다.
코드 블록 내에서 `count += 1` 줄을 **반드시** 추가해야 합니다.
이 줄은 `count` 값을 증가시키며, 그렇지 않으면 반복문이 무한히 실행됩니다

---

`while` 반복문의 반복 횟수를 제어하려면 숫자로 설정된 변수부터 시작합니다.
이 변수를 카운터 변수라고 합니다

---

그런 다음, 조건에서 비교를 사용하여 `counter` 변수를 숫자와 비교합니다.

---

코드 블록 내에서 `while` 반복문을 멈추려면 `counter` 변수를 증가시켜야 합니다.

---

코드를 작성하는 순서가 출력에 영향을 미칩니다.

---

JavaScript에는 `while` 반복문의 **do-while** 변형도 있습니다.
이 구문은 반복문의 조건을 확인하기 _전에_ 먼저 코드 블록을 한 번 실행합니다.
그런 다음 조건이 `false`가 될 때까지 반복문을 계속 실행합니다.
