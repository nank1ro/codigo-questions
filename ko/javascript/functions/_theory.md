코드의 일부를 약간 다른 값으로 재사용하고 싶은 상황을 생각해 본 적이 있을 것입니다.
전체 코드를 다시 작성하는 대신, 함수를 정의하면 반복적으로 사용할 수 있어 훨씬 깔끔합니다.
JavaScript에서는 `function` 키워드 뒤에 함수 이름을 사용합니다:
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

매개변수를 지정하려면 __함수 정의__의 괄호가 비어 있을 필요가 없습니다

---

때때로 함수가 값을 __반환__하기를 원할 때가 있습니다.
이를 위해 `return` 키워드가 있습니다.

---

함수는 여러 개의 입력 매개변수를 가질 수 있으며, 이는 함수의 괄호 안에 쉼표로 구분하여 작성합니다.
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

매개변수의 타입 뒤에 값을 할당하여 함수의 모든 매개변수에 _기본_ 값을 정의할 수 있습니다.
기본값이 정의되어 있으면 함수를 호출할 때 해당 매개변수를 생략할 수 있습니다
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

__나머지 매개변수__ 구문을 사용하면 불특정 다수의 인수를 배열로 나타낼 수 있습니다.
매개변수 이름 앞에 마침표 세 개 `...`를 삽입하여 나머지 매개변수를 작성합니다.
나머지 매개변수에 전달된 값은 함수 본문 내에서 배열로 사용할 수 있습니다.
예를 들어, `numbers`라는 이름의 나머지 매개변수는 함수 본문 내에서 numbers라는 상수 배열로 사용할 수 있습니다

---

함수에서 함수가 하는 일을 설명하는 _선택적 주석_을 추가할 수 있습니다:
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
한 줄 주석에는 `//`를, 여러 줄 주석에는 `/** */`를 사용할 수 있습니다
