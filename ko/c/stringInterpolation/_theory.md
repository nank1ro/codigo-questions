C에는 문자열 보간이 없습니다. 텍스트와 값은 **형식 문자열**을 통해 `printf`가 결합하며, 각 `%` 지정자는 대응하는 인자로 대체됩니다. 가장 흔한 지정자는 다음과 같습니다:
```c
printf("%d\n", 42);      // prints "42" (int, %i is the same)
printf("%f\n", 2.5);     // prints "2.500000" (double, 6 decimals by default)
printf("%s\n", "hi");    // prints "hi" (string)
printf("%c\n", 'A');     // prints "A" (single character)
printf("%x\n", 255);     // prints "ff" (int as lowercase hexadecimal)
printf("100%%\n");       // prints "100%" (a literal percent sign)
```
지정자는 인자의 타입과 일치해야 합니다. `double`을 `%d`로, `int`를 `%s`로 출력하면 값이 변환되지 않고 쓰레기 값이 출력되거나 프로그램이 죽습니다.

---

`sprintf`는 `printf`와 똑같이 동작하지만, 화면에 쓰는 대신 형식화된 텍스트를 **버퍼**라고 부르는 `char` 배열에 쓰고 그 뒤에 종료 문자 `'\0'`을 붙입니다:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // prints "3-7"
```
버퍼는 호출 전에 선언해야 하고 전체 텍스트에 종료 문자까지 담을 만큼 커야 합니다. 그렇지 않으면 `sprintf`가 버퍼 끝을 넘어서 씁니다.

---

문자열을 만드는 함수는 보통 버퍼를 매개변수로 받아 `sprintf`로 채웁니다. 배열은 호출한 쪽의 것이며, 호출이 끝나면 결과를 읽을 수 있습니다:
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // prints "Hello, Ada!"
```
이 연습들에서는 `string.h`가 코드 위에 이미 포함되어 있으므로, 결과를 비교할 때 `strcmp`를 사용할 수 있습니다.

---

`%x`는 정수를 소문자 16진수로 출력하고, `%X`는 같은 일을 대문자로 합니다. `%c`는 정수 문자 코드를 받아 그 코드가 나타내는 문자를 출력하므로, `65`와 함께 쓴 `%c`는 `A`를 출력합니다:
```c
printf("%x %X %c\n", 31, 31, 66); // prints "1f 1F B"
```

---

`%`와 문자 사이의 숫자는 필드의 최소 **너비**를 정합니다. 값은 왼쪽이 공백으로 채워지며, `%` 바로 뒤에 놓은 **플래그**가 이 채움 방식을 바꿉니다:
```c
printf("[%5d]\n", 42);  // prints "[   42]" right-aligned in 5 columns
printf("[%-5d]\n", 42); // prints "[42   ]" the - flag aligns to the left
printf("[%05d]\n", 42); // prints "[00042]" the 0 flag pads with zeros
printf("[%+d]\n", 42);  // prints "[+42]" the + flag always shows the sign
```
너비보다 긴 값은 절대 잘리지 않고, 필드가 그만큼 늘어날 뿐입니다.

---

너비와 플래그는 모든 지정자에서 동작하므로, `%02x`는 정수를 두 자리까지 0으로 채운 16진수로 출력합니다. 색을 `#rrggbb`로 쓰는 방식이 바로 이것입니다:
```c
printf("%02x\n", 5);   // prints "05"
printf("%02x\n", 255); // prints "ff"
```

---

점 뒤에 오는 숫자는 **정밀도**를 정합니다. `%f`에서는 반올림된 소수점 이하 자릿수이고, `%s`에서는 출력할 최대 문자 수입니다:
```c
printf("%.2f\n", 3.14159);    // prints "3.14"
printf("%.3s\n", "formatting"); // prints "for"
```
너비와 정밀도는 함께 쓸 수 있습니다. `%8.2f`는 소수점 이하 두 자리를 8칸에 오른쪽 정렬로 출력합니다.

---

정밀도는 문자열에서 `double`이 어떻게 보일지 조절하는 일반적인 방법입니다. `0.425` 같은 비율은 `100`을 곱하고 소수점 이하 한 자리와 `%%`를 출력하면 백분율이 됩니다:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out is "42.5%"
```

---

`sprintf`와 `printf`는 종료 문자 `'\0'`을 빼고 쓴 문자 수를 **반환**합니다. 이는 방금 만든 문자열의 길이이며, `strlen`을 따로 호출할 필요가 없습니다:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // prints "3"
```

---

`sprintf`는 버퍼가 얼마나 큰지 전혀 모릅니다. `snprintf`는 버퍼 크기를 두 번째 인자로 받아 `size - 1`개의 문자와 `'\0'`을 넘겨 쓰는 일이 없으며, 필요하면 텍스트를 자릅니다. 반환값은 **완전한** 텍스트였다면 가졌을 길이이므로, `size` 이상인 결과는 출력이 잘렸다는 뜻입니다:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // prints "formatt 10"
```
`sizeof buffer`는 배열의 크기를 바이트로 주며, `char` 배열에서는 그것이 원소 개수와 같습니다.

---

`snprintf`의 반환값을 버퍼 크기와 비교하면 전부 들어갔는지 알 수 있습니다. 길이를 모르는 문자열을 만들 때 쓰는 안전한 패턴입니다:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out holds only the first size - 1 characters of text
}
```

---

문자열은 각 조각을 앞 조각 바로 뒤에 써서 여러 단계로 만들 수도 있습니다. 반환값이 텍스트가 끝나는 위치를 알려주므로 `buffer + n`은 종료 문자의 주소이고, 다음 `sprintf`는 그 자리에서 이어 쓸 수 있습니다:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer is "Hello, world", n is 12
```
각 반환값을 `n`에 더하면 `n`은 지금까지 만든 텍스트의 전체 길이와 같게 유지됩니다.

---

문자열은 형식 문자열 없이도 결합할 수 있습니다. `string.h`의 `strcat`은 두 번째 인자의 사본을 첫 번째 인자 끝에 덧붙이며 첫 번째 인자에는 빈 공간이 충분해야 하고, `strncat`은 주어진 개수까지만 문자를 덧붙입니다:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text is "Hi!!!"
strncat(text, "abcdef", 2); // text is "Hi!!!ab"
```
둘 다 덧붙인 문자 뒤에 항상 종료 문자 `'\0'`을 추가합니다.

---

형식화할 것이 없을 때는 `puts`가 문자열을 출력하고 줄바꿈을 덧붙입니다. `printf`와 달리 `%`를 해석하지 않으므로 텍스트가 쓰인 그대로 출력됩니다:
```c
puts("Done");      // prints "Done" and a newline
puts("50% off");   // prints "50% off" and a newline
printf("50% off"); // undefined: % off is not a valid specifier
```
고정된 텍스트에는 `puts`가, 값을 끼워 넣어야 할 때는 `printf`가 알맞은 선택입니다.

---

`strncat`은 문자열의 일부만 덧붙여야 하거나, 덧붙이는 조각을 최대 길이로 제한해야 할 때 유용합니다:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name is "file.ba"
```
제한이 문자열보다 크면 문자열 전체가 덧붙습니다.

---

모두 합치면: 보고서 한 행은 왼쪽 정렬한 텍스트 필드, 구분자, 그리고 소수점 이하 자릿수가 고정된 오른쪽 정렬 숫자를 결합하며, 버퍼를 넘치지 않도록 `snprintf`로 씁니다:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out is "Ada   |  9.5"
```
모든 값이 각자의 너비에 들어가는 한 모든 행의 길이가 같으므로, 행을 위아래로 출력하면 열이 나란히 맞습니다.
