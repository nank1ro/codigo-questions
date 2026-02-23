---
language: dart
exerciseType: 1
difficulty: 1
title: Arithmetic mean
---

# --description--

Schreiben Sie eine Funktion namens `mean`, um das _arithmetische Mittel_ eines numerischen Vektors zu finden.

# --instructions--

Schreiben Sie eine Funktion, die das Mittel eines numerischen Vektors zuruckgibt.

Beispiel fur einen Funktionsaufruf:
```dart
print(mean([1, 2, 3]));
// prints 2.0
```

# --seed--

```dart
num mean() {

}
```

# --before-asserts--

```dart
import 'package:dart_runner/main.dart';
import 'package:test/test.dart';

void main() {
  group('MainTest -', () {
```

# --asserts--

Das Mittel von `[1, 2, 3, 4, 5, 6, 7]` muss gleich 4.0 sein

```dart
  test('test1', () {
    expect(mean([1, 2, 3, 4, 5, 6, 7]), 4.0, reason: '--err-t1--');
  });
```

Das Mittel von `[4, 5, 6]` muss gleich 5.0 sein

```dart
  test('test2', () {
    expect(mean([4, 5, 6]), 5.0, reason: '--err-t2--');
  });
```

Das Mittel von `[12, 34, 56, 78]` muss gleich 45.0 sein

```dart
  test('test3', () {
    expect(mean([12, 34, 56, 78]), 45.0, reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
num mean(List<num> numbers) {
  return numbers.reduce((prev, next) => prev + next) / numbers.length;
}
```
