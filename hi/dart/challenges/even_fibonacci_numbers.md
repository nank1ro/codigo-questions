---
language: dart
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

फिबोनाची अनुक्रम में प्रत्येक नया पद पिछले दो पदों को जोड़कर बनता है। 1 और 2 से शुरू करते हुए, पहले 10 पद हैं: 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो फिबोनाची अनुक्रम के उन सभी सम-मान पदों का योग लौटाता है जो `n` से अधिक नहीं हैं।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(fibonacciEvenSum(8));
// prints 10
```

# --seed--

```dart
int fibonacciEvenSum(int n) {

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

8 से अधिक न होने वाले सम फिबोनाची पदों का योग 10 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(fibonacciEvenSum(8), 10, reason: '--err-t1--');
  });
```

10 से अधिक न होने वाले सम फिबोनाची पदों का योग 10 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(fibonacciEvenSum(10), 10, reason: '--err-t2--');
  });
```

34 से अधिक न होने वाले सम फिबोनाची पदों का योग 44 के बराबर होना चाहिए

```dart
  test('test3', () {
    expect(fibonacciEvenSum(34), 44, reason: '--err-t3--');
  });
```

1000 से अधिक न होने वाले सम फिबोनाची पदों का योग 798 के बराबर होना चाहिए

```dart
  test('test4', () {
    expect(fibonacciEvenSum(1000), 798, reason: '--err-t4--');
  });
```

4000000 से अधिक न होने वाले सम फिबोनाची पदों का योग 4613732 के बराबर होना चाहिए

```dart
  test('test5', () {
    expect(fibonacciEvenSum(4000000), 4613732, reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int fibonacciEvenSum(int n) {
  int sum = 0;
  int a = 1, b = 2;
  while (a <= n) {
    if (a % 2 == 0) {
      sum += a;
    }
    int temp = a + b;
    a = b;
    b = temp;
  }
  return sum;
}
```
