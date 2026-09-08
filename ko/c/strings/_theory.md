C에는 전용 문자열 타입이 없습니다. **문자열**은 특수 문자인 **널 종료 문자** `'\0'`로 끝나는 `char` 배열입니다.
문자열을 만드는 가장 쉬운 방법은 큰따옴표로 감싼 문자열 리터럴을 사용하는 것입니다:
```c
char name[] = "Codigo";
```
컴파일러가 문자 수를 세어 끝에 자동으로 `'\0'`을 추가해 줍니다.
문자열을 출력하려면 `%s` 플레이스홀더를 사용합니다:
```c
printf("%s\n", name);
// prints "Codigo"
```

---

널 종료 문자도 메모리에서 공간을 차지합니다: 리터럴 `"hi"`는 `'h'`, `'i'`, `'\0'`의 3바이트를 차지합니다.
크기를 직접 선언할 때는 항상 그 공간을 남겨 두어야 합니다:
```c
char word[6] = "hello"; // 5 letters + '\0'
```
종료 문자가 없으면 C는 문자열이 어디서 끝나는지 알 방법이 없습니다.

---

헤더 `string.h`는 문자열을 다루는 함수들을 제공합니다.
`strlen`은 널 종료 문자 앞까지의 문자 수를 반환합니다(종료 문자 자체는 세지 않습니다):
```c
strlen("hello"); // 5
```
문자열을 받는 함수는 매개변수를 `char *text`, 즉 첫 번째 문자를 가리키는 포인터로 선언합니다.
이 연습 문제들에서는 `string.h`와 `ctype.h`가 코드 위에 이미 포함되어 있습니다.

---

문자열은 배열이므로, 모든 문자는 `0`부터 시작하는 인덱스를 가집니다:
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
문자 하나는 `%c`로 출력합니다. 문자를 교체할 수도 있습니다:
```c
word[0] = 'K'; // word is now "Koding"
```

---

모든 문자열은 `'\0'`으로 끝나기 때문에, 길이를 미리 알지 못해도 순회할 수 있습니다: 현재 문자가 종료 문자가 아닌 동안 계속 진행하면 됩니다.
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

배열은 선언 후에 `=`로 대입할 수 없습니다:
```c
char copy[20];
copy = "Codigo"; // error
```
문자열을 복사하려면 `string.h`의 `strcpy(destination, source)`를 사용합니다.
목적지는 모든 문자와 `'\0'`을 담을 수 있을 만큼 충분히 커야 합니다.

---

`strcat(destination, source)`는 `source`를 `destination`의 끝에 추가합니다:
```c
char text[20] = "Hello";
strcat(text, " World");
// text is now "Hello World"
```
`strcpy`와 마찬가지로, 목적지 배열은 결과를 담을 수 있을 만큼 충분히 커야 합니다.

---

두 문자열은 `==`로 비교할 수 없습니다: 이는 문자가 아니라 메모리 상의 주소를 비교하는 것이기 때문입니다.
대신 `strcmp(first, second)`를 사용하세요. 이 함수는 두 문자열이 정확히 같은 문자로 이루어져 있을 때 `0`을 반환합니다:
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // not 0
```

---

`strcmp`는 문자 코드를 사용하여 문자열을 한 문자씩 비교합니다.
첫 번째 문자열이 두 번째보다 앞서면 음수, 뒤에 오면 양수, 같으면 `0`이 결과가 됩니다:
```c
strcmp("a", "b"); // negative
strcmp("b", "a"); // positive
```

---

`strncpy(destination, source, n)`은 최대 `n`개의 문자를 복사합니다.
`source`가 `n`보다 길면 `'\0'`이 기록되지 않으므로, 직접 결과를 종료해야 합니다.
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix is "Cod"
```

---

헤더 `ctype.h`는 문자 하나를 다루는 함수들을 제공합니다.
`toupper(c)`는 문자의 대문자 버전을, `tolower(c)`는 소문자 버전을 반환하며, 그 외의 문자는 그대로 반환됩니다:
```c
char letter = toupper('a'); // 'A'
```

---

문자열은 함수에 포인터로 전달되므로, `char *text`를 받는 함수는 호출자의 문자를 그 자리에서 바꿀 수 있습니다.
`'\0'`까지의 반복문과 `toupper`를 결합하면 문자열 전체를 변환할 수 있습니다:
```c
text[i] = toupper(text[i]);
```

---

`sprintf`는 `printf`처럼 동작하지만, 서식이 적용된 텍스트를 화면이 아니라 `char` 배열에 씁니다:
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer is "3 items"
```
버퍼는 전체 텍스트와 그 `'\0'`을 담을 수 있을 만큼 충분히 커야 합니다.

---

`sprintf`는 숫자를 텍스트로 바꾸는 편리한 방법입니다: 버퍼에 담기고 나면, 모든 문자열 함수를 사용할 수 있습니다.
