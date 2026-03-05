코드의 일부를 약간 다른 값으로 재사용하고 싶은 상황을 생각해 본 적이 있을 것입니다.
전체 코드를 다시 작성하는 대신, 함수를 정의하면 반복적으로 사용할 수 있어 훨씬 깔끔합니다.
Swift에서는 `func` 키워드 뒤에 함수 이름을 사용합니다:
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

매개변수를 지정하려면 __함수 정의__의 괄호를 비워둘 필요가 없습니다

---

때로는 함수가 값을 __반환__하기를 원합니다.
이를 위해 `return` 키워드가 있습니다.

---

함수는 여러 개의 입력 매개변수를 가질 수 있으며, 함수의 괄호 안에 쉼표로 구분하여 작성합니다.
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

튜플 타입을 함수의 반환 타입으로 사용하여 하나의 복합 반환 값으로 여러 값을 반환할 수 있습니다.

---

매개변수에 인수 레이블을 사용하고 싶지 않다면, 해당 매개변수의 명시적 인수 레이블 대신 밑줄 `_`을 작성합니다

---

매개변수의 타입 뒤에 값을 할당하여 함수의 모든 매개변수에 _기본_ 값을 정의할 수 있습니다.
기본 값이 정의되어 있으면 함수를 호출할 때 해당 매개변수를 생략할 수 있습니다
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

_가변 매개변수_는 지정된 타입의 값을 0개 이상 받습니다.
가변 매개변수를 사용하면 함수를 호출할 때 다양한 수의 입력 값을 전달할 수 있습니다.
매개변수의 타입 이름 뒤에 세 개의 마침표 `...`를 삽입하여 가변 매개변수를 작성합니다.
가변 매개변수에 전달된 값은 함수 본문 내에서 적절한 타입의 배열로 사용할 수 있습니다.
예를 들어, 이름이 `numbers`이고 타입이 `Double...`인 가변 매개변수는 함수 본문 내에서 `[Double]` 타입의 상수 배열 numbers로 사용할 수 있습니다

---

함수에 함수가 하는 일을 설명하는 _선택적 주석_을 추가할 수 있습니다:
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
한 줄 주석에는 `///`를, 여러 줄 주석에는 `/** */`를 사용할 수 있습니다
