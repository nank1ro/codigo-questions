코드를 재사용하고 싶지만 값만 약간 다른 상황을 생각해 본 적이 있을 것입니다.
전체 코드를 다시 작성하는 대신, 함수를 정의하여 반복적으로 사용하는 것이 훨씬 깔끔합니다.
C에서는 `return_type` 뒤에 `function` 이름을 사용합니다. 예를 들면:
```c
void say_hello() {
    printf("Hello!\n");
}

int main() {
    say_hello();
    // prints "Hello!"
    return 0;
}
```

---

매개변수를 지정하려면 __함수 정의__에서 괄호를 비워 둘 필요가 없습니다

---

때로는 함수가 값을 __반환__하기를 원합니다.
이를 위해 `return` 키워드가 있습니다.

---

함수는 여러 개의 입력 매개변수를 가질 수 있으며, 함수의 괄호 안에 쉼표로 구분하여 작성합니다.
```c
void say_hello(char *name, bool new_user) {
  char greet[40] = "Hello ";
  strcat(greet, name);
  if (new_user) {
    strcat(greet, "! Welcome on board :)");
  }
  printf("%s\n", greet);
}

int main() {
    // prints "Hello Tom"
    say_hello("Tom", true);
    return 0;
};
```

---

함수에서 함수가 하는 일을 설명하는 _선택적 주석_을 추가할 수 있습니다:
```c
/*
 * Function:  hello_world
 * --------------------
 * prints "Hello, World!" to the screen
 */
function hello_world() {
    printf("Hello, World!\n");
}
```
한 줄 주석에는 `//`를, 여러 줄 주석에는 `/* */`를 사용할 수 있습니다
