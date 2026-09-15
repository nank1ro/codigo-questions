**고차 메서드(higher-order method)**는 함수를 인자로 받는 메서드입니다. Dart 컬렉션은 이런 메서드를 많이 제공하며, 전달하는 함수는 보통 화살표 구문 `(x) => ...`으로 작성된 익명 함수입니다:

`map`이 가장 흔한 것입니다: 모든 요소에 함수를 호출하고 각 요소마다 하나씩 결과를 만들어내며, 원본 컬렉션은 그대로 둡니다:

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

출력의 **둥근 괄호**에 주목하세요. `map`은 `List`를 반환하지 않습니다: 순회할 수 있는 시퀀스인 `Iterable`을 반환합니다. 실제 리스트를 다시 얻으려면 **`toList()`**를 호출하세요:

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

출력에서 대괄호는 `List`를 보고 있다는 신호이고, 둥근 괄호는 일반 `Iterable`을 보고 있다는 신호입니다.

---

`where`는 **술어(predicate)**라고 불리는 `bool`을 반환하는 함수를 받고, 그 함수가 `true`를 답하는 요소만 유지합니다. 살아남은 요소들의 순서는 절대 바뀌지 않습니다:

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

`map`과 마찬가지로 `where`는 `Iterable`을 반환하고 원본 컬렉션을 절대 수정하지 않으므로, 결과를 `List`로 바꾸는 것은 여기서도 `toList()`입니다.

다른 언어에서는 이 메서드를 `filter`라고 부릅니다. Dart에서는 `where`입니다.

---

`map`에 주는 함수는 받은 요소와 같은 타입을 반환할 필요가 없습니다. 문자열 리스트를 그 길이로 매핑하면 `List<String>`이 `Iterable<int>`로 바뀌고, `toList()`가 그것을 `List<int>`로 만듭니다:

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

결과는 항상 **원본과 정확히 같은 개수의 요소**를 같은 순서로 가집니다: `map`은 요소를 변환할 뿐, 절대 추가하거나 제거하지 않습니다.

---

일부 고차 메서드는 새 컬렉션을 만드는 대신 컬렉션에 대한 질문에 답합니다. 술어를 받아 `bool`을 반환합니다:

- **최소한 하나의** 요소라도 술어를 만족하면 `any`는 `true`입니다
- **모든** 요소가 술어를 만족하면 `every`는 `true`입니다

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

둘 다 답이 확실해지는 즉시 멈춥니다: `any`는 일치하는 첫 번째 요소에서, `every`는 일치하지 않는 첫 번째 요소에서 멈춥니다.

빈 컬렉션에서 `any`는 `false`이고 `every`는 `true`입니다: 첫 번째를 참으로 만들 요소가 없고, 두 번째를 깨뜨릴 요소도 없습니다.

---

`map`과 `where`는 **지연(lazy)**입니다: 호출해도 아무것도 실행되지 않습니다. 원본과 함수를 기억하는 `Iterable`을 반환하며, 무언가가 결과를 한 요소씩 순회할 때만 함수가 호출됩니다.

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // 아직 아무것도 계산되지 않음
print(doubled.first);                      // 2만 계산됨
```

`toList()`가 시퀀스를 **실체화**합니다: 처음부터 끝까지 순회하며 모든 결과를 실제 `List`에 저장합니다.

지연 평가는 기억할 가치가 있는 두 가지 결과를 낳습니다. 지연 `Iterable`은 순회할 때마다 다시 계산되므로, 값을 두 번 이상 필요로 할 때는 `toList()`로 한 번 실체화하는 것이 더 저렴합니다. 그리고 원본 컬렉션을 계속 바라보므로, 그 컬렉션을 바꾸면 `Iterable`이 만들어내는 것도 바뀝니다:

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold`는 컬렉션 전체를 **하나의 값**으로 결합합니다. 두 개의 인자를 받습니다: **누적 값**의 시작 값, 그리고 지금까지의 누적 값과 다음 요소를 받아 새로운 누적 값을 반환하는 함수:

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

여기서 `acc`는 `0`에서 시작하여 `1`, `3`, `6`이 되고 마침내 `10`이 됩니다.

누적 값은 숫자일 필요도, 요소와 같은 타입일 필요도 없습니다: `''`에서 시작하여 텍스트를 더하면 무엇으로 이루어진 리스트로부터도 `String`을 만들 수 있습니다.

기억해야 할 한 가지 세부 사항: Dart는 시작 값**과** 결과가 사용되는 위치로부터 누적 값의 타입을 알아냅니다. `print(...)` 안에서는 기대되는 타입을 알 수 없으므로, 결과를 먼저 변수에 저장하세요(또는 `fold<int>(...)`를 작성하세요). 그렇지 않으면 컴파일러가 누적 값에 `+`를 사용할 수 없다고 불평합니다.

---

`reduce`는 `fold`의 더 간단한 친척입니다. 시작 값을 받지 않습니다: **첫 번째 요소**가 시작 누적 값이고, 함수는 나머지 모든 요소에 대해 실행됩니다:

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

시작 값이 없기 때문에 결과는 항상 **요소와 같은 타입**이며, 빈 컬렉션에서 `reduce`를 호출하면 `StateError`가 발생합니다: 시작할 첫 번째 요소가 없기 때문입니다. `fold`에는 이런 문제가 없으므로 더 안전한 기본 선택입니다.

`reduce`는 가장 큰 값처럼 여러 요소 중에서 하나의 요소를 찾을 때 가장 빛을 발합니다:

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere`는 모든 요소 대신 술어와 일치하는 **첫 번째** 요소를 반환합니다:

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

아무것도 일치하지 않으면 반환할 요소가 없으므로, `firstWhere`는 `StateError`를 던집니다. 오류 대신 답을 내놓으려면 이름 있는 인자 **`orElse`**를 전달하세요: 매개변수 없이 대체 값을 만들어내는 함수입니다.

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse`는 일반 값이 아니라 함수이므로, 검색이 실패할 때만 호출됩니다. `orElse: 'none'`이라고 작성하면 컴파일되지 않습니다.

---

`map`에 주는 함수가 각 요소에 대해 컬렉션을 반환하면, 컬렉션의 시퀀스가 만들어집니다. **`expand`**도 같은 일을 하지만 그다음 모든 것을 하나의 평평한 시퀀스로 합칩니다:

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

순서는 유지됩니다: 첫 번째 요소가 만들어낸 모든 것이 먼저 오고, 그다음 두 번째 요소가 만들어낸 모든 것이 오는 식입니다.

반환된 컬렉션은 어떤 크기든 가질 수 있으므로, `expand`는 처음보다 **더 많거나 적은** 요소를 만들어내는 방법이기도 합니다: 어떤 요소에 대해 빈 리스트를 반환하면 그 요소는 그저 사라집니다.

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)`은 **처음** `n`개의 요소를 유지하고 `skip(n)`은 그것들을 버립니다. 둘 다 함수를 받지 않지만 둘 다 지연 `Iterable`을 반환하므로, 다른 고차 메서드 사이에 자연스럽게 어울립니다:

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

존재하는 것보다 더 많은 요소를 요구하는 것은 오류가 아닙니다: 존재하는 것을 그저 얻거나 빈 결과를 얻습니다.

`takeWhile`과 `skipWhile`은 술어를 사용하는 버전입니다. 술어가 유지되는 **한** 처음부터 요소를 가져오거나 버리고, 술어를 만족하지 않는 첫 번째 요소에서 멈춥니다. 나중에 오는 요소가 다시 일치하더라도 마찬가지입니다:

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart에는 `sorted` 메서드가 없습니다. `sort`는 `List`에 속하며, 리스트를 **제자리에서** 재배열하고 아무것도 반환하지 않습니다:

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

`void`를 반환하기 때문에 결과를 전혀 사용할 수 없습니다: `final sorted = numbers.sort();`는 컴파일러가 읽지 못하게 하는 값을 내놓습니다. 정렬된 **복사본**을 위한 관용구는 `toList()`에 이어 캐스케이드 `..sort()`를 사용하는 것입니다: `toList()`가 복사본을 만들고, `..`는 복사본 자체를 그대로 돌려주면서 그 위에서 `sort`를 실행합니다.

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], 그대로
```

`sort`는 **비교자(comparator)**도 받습니다: 두 요소를 받는 함수로, 첫 번째가 두 번째보다 앞설 때는 음수, 같을 때는 `0`, 그 외에는 양수를 반환합니다. `compareTo`가 정확히 그것을 만들어내므로, 어떤 키로든 정렬하는 것은 한 줄입니다:

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold`와 `reduce`는 비슷해 보이며, 둘 사이의 선택은 두 가지 질문으로 귀결됩니다: 컬렉션이 비어 있을 수 있는가, 그리고 결과가 요소와 같은 타입인가?

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String from Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int, Strings로부터
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce`는 요소에서 시작하기 때문에 요소 타입밖에 돌려줄 수 없습니다. `fold`는 여러분이 고른 값에서 시작하므로, 누적 값은 개수를 세는 `int`, 불어나는 `String`, 심지어 쌓여가는 `List`일 수도 있습니다. 그리고 그 시작 값이 이미 존재하기 때문에, 빈 컬렉션은 그저 `fold`가 그대로 반환하는 답이 됩니다. 반면 `reduce`는 반환할 것이 없어 예외를 던집니다.

---

이 메서드들은 모두 `Iterable`을 반환하고, 모든 `Iterable`은 다시 같은 메서드들을 가지고 있습니다. 그렇기 때문에 **연쇄**할 수 있습니다: 전체 계산이 왼쪽에서 오른쪽으로 읽히는 파이프라인이 되고, 각 단계는 이전 단계가 만들어낸 것을 다룹니다.

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

`toList()`가 필요한 것은 마지막 단계뿐입니다: 중간에 호출하면 아무도 갖고 있지 않은 리스트가 만들어질 뿐입니다.

타입은 체인을 따라 바뀌고, 다음 함수가 받는 것도 바뀝니다: `List<String>`에 대한 `where` 다음에는 여전히 문자열을 다루지만, `map((w) => w.length)` 다음에는 다음 단계가 숫자를 봅니다.

각 단계가 지연되기 때문에 순서는 결과뿐 아니라 수행되는 작업에도 중요합니다: `where`로 먼저 거르면 더 적은 요소에 `map`이 호출됩니다.

---

이 메서드들에는 특별한 것이 없습니다: 그저 **매개변수로 함수**를 가질 뿐이고, 여러분의 함수도 똑같이 할 수 있습니다. 함수 매개변수의 타입은 반환 타입, 그다음 `Function`, 그다음 괄호 안의 매개변수 타입으로 씁니다:

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

호출자는 **무엇이** 일어날지 결정하고, 함수는 **무엇에 대해** 결정합니다. `operation`이 `map`에 곧바로 전달되는 방식에 주목하세요: 함수 값은 다른 값처럼 전달될 수 있습니다.

인자는 익명 함수이거나 기존 함수의 **이름**일 수 있으며, 괄호 없이 씁니다. 괄호를 붙이면 전달하는 대신 호출해 버립니다:

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

함수는 함수를 **반환**할 수도 있습니다. 반환 타입은 함수 매개변수 타입과 정확히 같은 방식으로 쓰고, 반환되는 값은 보통 익명 함수입니다:

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)`은 아무것도 곱하지 않습니다: `3`을 곱하는 새로운 함수를 만들어 돌려줄 뿐입니다. 그 함수는 그다음 다른 함수처럼 저장되거나, 호출되거나, `map`에 전달됩니다:

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

반환된 함수는 `multiplier`가 끝난 후에도 `factor`를 여전히 기억합니다. 자신이 생성된 스코프의 변수들을 유지하는 함수를 **클로저(closure)**라고 부르며, 바로 그것이 이런 함수 팩토리를 가능하게 합니다.

---

이 메서드들을 합치면 대부분의 손으로 작성한 반복문을 대체합니다. 파이프라인은 보통 세 단계로 읽힙니다: `where`로 요소를 **선택**하고, `map`으로 **변환**한 다음, `fold`로 **결합**합니다:

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

`fold`는 자신만의 시작 값을 고르기 때문에, 요소와 아무 상관 없는 타입으로 체인을 끝낼 수도 있습니다. 한 조각씩 자라나는 `String`처럼요:

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

각 단계는 짧게 유지되며 자신이 하는 일을 말해줍니다. 세 가지를 한꺼번에 하는 반복문보다 이것들을 선호하는 진짜 이유입니다.
