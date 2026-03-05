타입을 사용하면 코드에서 사용하는 모든 다양한 데이터를 분류할 수 있습니다.
Dart에서 __타입__은 주어진 데이터를 어떻게 사용할 것인지 컴파일러에게 알려주는 방법입니다.
다음은 Dart가 지원하는 타입의 예시입니다:
- int
- String
- double
- dynamic
- num

Dart는 그 밖에도 많은 타입을 지원합니다. 위에 나열된 것들이 주로 사용하게 될 주요 타입입니다.

---

변수의 타입을 명시적으로 정의하는 것도 괜찮습니다. 예를 들어:
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

명시적 타입이 있는 변수도 상수가 될 수 있습니다. 타입 앞에 `const` 또는 `final` 키워드를 추가하면 됩니다:
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> 참고: 가변 데이터는 원할 때 쉽게 변경할 수 있습니다. 그러나 많은 숙련된 프로그래머들은 불변 데이터의 장점을 높이 평가합니다. 값이 불변이면, 생성한 후 아무도 그 값을 변경할 수 없다는 것을 신뢰할 수 있습니다. 이러한 방식으로 데이터를 제한하면 찾기 어려운 많은 버그를 방지하고 프로그램을 더 쉽게 이해하고 테스트할 수 있습니다.

---

변수의 타입을 명시하는 것은 가능하지만 불필요합니다. `10`이 `int` 타입이고 `3.14`가 `double` 타입이라는 것을 알고 있습니다. Dart 컴파일러는 __타입 추론__ 덕분에 이를 추론할 수 있습니다. 모든 프로그래밍 언어가 _타입 추론_을 지원하는 것은 아니며, 이것이 Dart를 매우 강력한 프로그래밍 언어로 만듭니다.

변수에서 타입을 간단히 제거할 수 있습니다. 예를 들어:
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

변수의 타입이 명시적으로 지정되지 않으면, Dart는 해당 타입을 추론하려고 시도합니다.

---

변수의 타입을 프로그래밍적으로 확인하는 방법이 있습니다. 바로 `is` 키워드를 사용하는 것입니다:
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

보시다시피 Dart는 변수 `number`에 `double` 타입을 할당했습니다.

---

`is` 키워드를 사용하면 변수가 지정한 타입인지 확인할 수 있습니다. 하지만 `is!` 키워드를 사용하여 변수가 지정한 타입이 아닌지도 확인할 수 있습니다
```dart
final number = 3.14;
print(number is! int); // true
```

---

_런타임_ 변수의 타입을 확인하는 또 다른 방법은 모든 타입에서 사용할 수 있는 `runtimeType` 속성을 사용하는 것입니다.
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

때때로 한 타입을 가지고 있지만 다른 타입으로 변환해야 하는 상황이 생길 수 있습니다. 다음과 같이 하고 싶을 수도 있습니다:

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

하지만 Dart는 다음과 같은 오류를 발생시킵니다:
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

일부 프로그래밍 언어는 이렇게 제한적이지 않으며 자동으로 변환합니다. 경험적으로 이러한 암묵적 자동 변환은 버그와 성능 문제의 빈번한 원인입니다. Dart는 이러한 문제를 피하기 위해 이 기능을 비활성화했습니다.

기억하세요, 컴퓨터는 프로그래머가 무엇을 할지 알려주는 것에 의존합니다. Dart에서는 타입 변환에 대해 명시적이어야 합니다.

Dart의 암묵적 변환을 기대하는 대신, Dart에게 타입을 변환하도록 명시적으로 요청해야 합니다. 다음은 `double` 숫자를 `int`로 변환하는 방법입니다:
```dart
var integer = decimal.toInt();
```

이 할당은 Dart에게 원래 타입 `double`에서 새로운 타입 `double`로 변환하겠다는 것을 명확하게 알려줍니다.

> 참고: 이 경우, 소수 값을 정수에 할당하면 정밀도가 손실됩니다. 변수 `integer`의 값은 __3.14__가 아닌 __3__이 됩니다. 이것이 명시적이어야 하는 이유입니다. Dart는 여러분이 무엇을 하고 있는지 확인하고, 변환 시 정보가 손실된다는 것을 알려줍니다.

---

지금까지 정수나 소수에서 독립적으로 사용되는 연산자를 살펴보았습니다. 정수를 소수와 곱해야 한다면 어떻게 해야 할까요? 예시를 살펴보겠습니다:
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius`는 `int` 타입이고 `pi`는 `double` 타입입니다. `circumference`의 타입은 무엇이 될까요? Dart는 변수 `circumference`에 `double` 타입을 할당합니다. `int` 타입으로 만들었다면 정밀도 손실이 발생할 수 있으므로 이것이 더 안전한 선택입니다.

결과를 `int`로 원한다면, 명시적으로 변환해야 합니다:
```dart
const circumference = (2 * pi * radius).toInt();
```

괄호는 Dart에게 먼저 곱셈을 수행한 다음 결과를 정수 값으로 변환하라고 지시합니다. 안타깝게도 분석기는 이 코드를 좋아하지 않습니다:
 > Const variables must be initialized with a constant value.

문제는 `toInt` 메서드가 런타임 전용 메서드라는 것입니다. 이는 `circumference` 변수를 컴파일 타임에 결정할 수 없으므로 상수가 될 수 없다는 것을 의미합니다. 이를 수정하려면 `const`를 `final`로 교체하세요:

```dart
final circumference = (2 * pi * radius).toInt();
```

이제 `circumference`는 `int` 타입의 __런타임 상수__ 변수입니다.

---

때때로 일반적인 타입의 변수가 있지만, 하위 타입에만 존재하는 기능이 필요한 경우가 있습니다. 변수의 타입이 필요한 하위 타입이라고 확신하는 경우, `as` 키워드를 사용하여 타입을 변경할 수 있습니다. 이 절차를 __타입 캐스팅__이라고도 합니다. 다음은 예시입니다:

```dart
num number = 3;
```

숫자가 짝수인지 확인하고 싶다고 가정해 보겠습니다. 해당 기능은 `int` 하위 타입에만 존재합니다.
```dart
print(number.isEven);
```

위 코드는 타입 오류를 반환합니다:
> The getter `isEven` isn't defined for the type 'num'.

`num` 타입은 숫자가 짝수인지 홀수인지 알기에는 너무 일반적인 타입입니다. 정수만 짝수 또는 홀수가 될 수 있습니다.
`num`은 `double`과 `int` 타입을 모두 포함하므로 `num`에 `double` 값이 들어있는 경우 문제가 발생합니다. 이 경우, __3__이 정수라는 것을 확신하므로 `int`로 캐스팅할 수 있습니다

```dart
final integer = number as int;
print(integer.isEven); // false
```

`as` 키워드는 컴파일러가 변수 `integer`를 `int` 타입으로 인식하게 합니다. 이를 통해 정수에 존재하는 `isEven` 속성을 사용할 수 있습니다. 숫자 __3__은 짝수가 아니므로 결과는 false입니다.

캐스팅할 때 주의해야 합니다. 타입을 잘못 캐스팅하면 런타임 오류가 발생합니다:
```dart
num numero = 3;
final decimale = numero as double;
```

이렇게 하면 다음 오류와 함께 프로그램이 충돌합니다:
> CastError (type 'int' is not a subtype of type 'double' in type cast)

`number`의 런타임 타입은 `double`이 아닌 `int`입니다. Dart에서는 `int`와 `double`과 같은 동일 수준의 타입으로 캐스팅할 수 없습니다. 하위 타입으로만 캐스팅할 수 있습니다.
