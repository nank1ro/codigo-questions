---
language: dart
exerciseType: 1
difficulty: 2
title: 10001st prime
---

# --description--

最初の 6 つの素数を列挙すると: 2、3、5、7、11、13 となり、6 番目の素数が 13 であることがわかります。

# --instructions--

`n` 番目の素数を返す関数を書いてください。

関数呼び出しの例:
```dart
print(nthPrime(6));
// prints 13
```

# --seed--

```dart
int nthPrime(int n) {

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

6 番目の素数は 13 と等しくなければならない

```dart
  test('test1', () {
    expect(nthPrime(6), 13, reason: '--err-t1--');
  });
```

10 番目の素数は 29 と等しくなければならない

```dart
  test('test2', () {
    expect(nthPrime(10), 29, reason: '--err-t2--');
  });
```

1000 番目の素数は 7919 と等しくなければならない

```dart
  test('test3', () {
    expect(nthPrime(1000), 7919, reason: '--err-t3--');
  });
```

10001 番目の素数は 104743 と等しくなければならない

```dart
  test('test4', () {
    expect(nthPrime(10001), 104743, reason: '--err-t4--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 5)));
}
```

# --solutions--

```dart
bool _isPrime(int n) {
  if (n < 2) return false;
  if (n == 2) return true;
  if (n % 2 == 0) return false;
  for (int i = 3; i * i <= n; i += 2) {
    if (n % i == 0) return false;
  }
  return true;
}

int nthPrime(int n) {
  int count = 0;
  int candidate = 1;
  while (count < n) {
    candidate++;
    if (_isPrime(candidate)) {
      count++;
    }
  }
  return candidate;
}
```
