---
language: dart
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

एक फ़ंक्शन बनाएं जो एक संख्या को तर्क के रूप में लेता है और `"Fizz"`, `"Buzz"` या `"FizzBuzz"` लौटाता है।

# --instructions--

- यदि संख्या `3` का गुणज है तो आउटपुट `"Fizz"` होना चाहिए
- यदि दी गई संख्या `5` का गुणज है, तो आउटपुट `"Buzz"` होना चाहिए।
- यदि दी गई संख्या `3` और `5` दोनों का गुणज है, तो आउटपुट `"FizzBuzz"` होना चाहिए।
- यदि संख्या `3` या `5` में से किसी का भी गुणज नहीं है, तो संख्या को नीचे दिए गए उदाहरणों में दिखाए अनुसार स्वयं आउटपुट किया जाना चाहिए।
- आउटपुट हमेशा एक स्ट्रिंग होना चाहिए भले ही यह `3` या `5` का गुणज न हो।

उदाहरण:
```dart
fizz_buzz(3); // ➞ "Fizz"
fizz_buzz(5); // ➞ "Buzz"
fizz_buzz(15); // ➞ "FizzBuzz"
fizz_buzz(4); // ➞ "4"
```

# --seed--

```dart
String fizzBuzz() {
  
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

संख्या `3` `"Fizz"` के बराबर होनी चाहिए

```dart
  test('test1', () {
    expect(fizzBuzz(3), 'Fizz', reason: '--err-t1--');
  });
```

संख्या `5` `"Buzz"` के बराबर होनी चाहिए

```dart
  test('test2', () {
    expect(fizzBuzz(5), 'Buzz', reason: '--err-t2--');
  });
```

संख्या `15` `"FizzBuzz"` के बराबर होनी चाहिए

```dart
  test('test3', () {
    expect(fizzBuzz(15), 'FizzBuzz', reason: '--err-t3--');
  });
```

संख्या `10` `"Buzz"` के बराबर होनी चाहिए

```dart
  test('test4', () {
    expect(fizzBuzz(10), 'Buzz', reason: '--err-t4--');
  });
```

संख्या `98` `"98"` के बराबर होनी चाहिए

```dart
  test('test5', () {
    expect(fizzBuzz(98), '98', reason: '--err-t5--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String fizzBuzz(int number) {
  if (number % 3 == 0 && number % 5 == 0) {
    return 'FizzBuzz';
  }
  if (number % 3 == 0) {
    return 'Fizz';
  }
  if (number % 5 == 0) {
    return 'Buzz';
  }
  return number.toString();
}
```
