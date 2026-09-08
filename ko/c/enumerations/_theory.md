**열거형**(`enum`)은 관련된 정수 상수들의 집합에 이름을 붙여, 그냥 숫자 대신 `RED`처럼 쓸 수 있게 해줍니다.
`enum` 키워드, 이름, 그리고 중괄호로 감싼 상수 목록으로 선언합니다.
```c
enum Color { RED, GREEN, BLUE };
```
모든 상수는 정수입니다. 별도로 지정하지 않으면 첫 번째 상수는 `0`이고 이후 값은 이전 값에 1을 더한 값이 되므로, `RED`는 `0`, `GREEN`은 `1`, `BLUE`는 `2`입니다.
정수이므로 `%d`로 출력합니다.
```c
printf("%d\n", GREEN);
// prints "1"
```

---

번호 매기기는 나열한 상수의 개수만큼 자동으로 계속됩니다: 네 번째 상수는 `3`, 다섯 번째는 `4`가 됩니다.
이름은 다른 상수와 마찬가지로 보통 대문자로 작성하며, 프로그램 전체에서 고유해야 합니다: 두 열거형이 같은 상수 이름을 공유할 수 없습니다.

---

`=`를 사용해 상수에 명시적인 값을 지정할 수도 있습니다. 그 이후의 상수들은 해당 값부터 계속 이어서 셉니다.
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
명시적인 값은 연속적이거나 증가하는 값일 필요가 없습니다: `enum Status { OK = 200, NOT_FOUND = 404 };`도 완전히 유효합니다.

---

열거형은 타입이기도 합니다: `enum` 뒤에 열거형 이름을 써서 그 타입의 변수를 선언하고, 상수 중 하나를 대입할 수 있습니다.
```c
enum Color favorite = GREEN;
```
상수는 정수이므로, 열거형 변수도 일반적인 연산자로 비교합니다.
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

열거형은 `int`와 마찬가지로 함수 매개변수의 타입이 될 수 있습니다.
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
함수 안에서는 `switch`가 각 상수를 처리하는 자연스러운 방법입니다. 열거형 상수는 `case` 레이블로 바로 사용할 수 있기 때문입니다.
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

`switch`의 모든 case가 하나의 상수를 처리할 때는 각 case 뒤에 `break`를 잊지 마세요. 그렇지 않으면 실행이 다음 case로 흘러 들어갑니다.
열거형의 모든 상수를 다룬다면 `default` case는 필수가 아닙니다.

---

함수도 열거형을 반환할 수 있습니다. 반환 타입으로 열거형 타입을 사용하고 그 상수 중 하나를 반환하기만 하면 됩니다.
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
이름 있는 상수를 반환하는 것이 그냥 `0`이나 `1`을 반환하는 것보다 호출자 입장에서 훨씬 명확합니다.

---

매번 `enum Color`라고 쓰는 것은 장황합니다. `typedef`를 사용하면 열거형에 짧은 타입 이름을 붙일 수 있고, 열거형 자체는 이름 없이 둘 수 있습니다.
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
새 이름 `Color`는 앞에 `enum` 키워드 없이 단독으로 사용됩니다.

---

enum 상수는 자동으로 `int`로 변환되므로, `int n = BLUE;`는 유효하며 `2`를 저장합니다.
반대 방향은 **캐스트**로 이루어지며, 정수 앞 괄호 안에 enum 타입을 씁니다.
```c
enum Color c = (enum Color)1; // c is GREEN
```
C는 그 숫자가 어떤 상수와 일치하는지 확인하지 않습니다: `(enum Color)7`은 `7`인 상수가 없어도 컴파일되므로, 변환하기 전에 정수를 검증해야 합니다.

---

enum 값에 대한 산술 연산은 그냥 `int`를 만들어냅니다: `GREEN + 1`은 `BLUE`가 아니라 `2`입니다.
결과를 enum 변수에 다시 저장하거나 함수에서 반환하려면 enum 타입으로 캐스트하세요.
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
나머지 연산자 `%`와 결합하면 상수를 순환시키며 처음 상수로 되돌아가게 할 수 있습니다.

---

흔히 쓰이는 방법은 열거형 끝에 보통 `COUNT`라는 이름의 상수를 하나 더 추가하는 것입니다: 번호 매기기가 `0`부터 시작하므로, 그 값은 정확히 그 앞에 있는 실제 상수의 개수가 됩니다.
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
이 경계값(sentinel)을 이용하면 숫자를 하드코딩하지 않고도 모든 상수를 순회할 수 있고, 그 앞에 상수를 추가해도 여전히 정확하게 동작합니다.
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

`COUNT` 경계값은 상수 하나당 슬롯 하나를 갖는 배열의 크기로도 안성맞춤이며, 상수는 그 배열에 대한 읽기 쉬운 인덱스가 됩니다.
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
`0`부터 `FRUIT_COUNT`까지의 루프는 모든 슬롯을 방문하며, 반환해야 할 때는 루프 인덱스를 다시 `enum Fruit`로 캐스트할 수 있습니다.

---

C에는 enum 상수의 이름을 얻는 내장 방법이 없습니다. `printf("%d\n", SUMMER)`는 `Summer`가 아니라 `2`를 출력합니다. 일반적인 해결책은 `switch`로 각 상수에 해당하는 문자열을 반환하는 작은 함수를 만드는 것입니다.

---

enum 값은 다른 정수와 마찬가지로 배열에 저장할 수 있습니다: `enum Fruit basket[] = {APPLE, APPLE, CHERRY};`는 세 개의 과일을 담고 있으며, 각 요소는 상수와 비교할 수 있습니다.
