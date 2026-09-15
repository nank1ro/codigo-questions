---
language: dart
exerciseType: 1
difficulty: 1
title: कोलैट्ज़ अनुमान
---

# --description--

कोलैट्ज़ अनुमान किसी भी धनात्मक पूर्णांक `n` से शुरू होकर एक ही सरल नियम दोहराता है: यदि `n` सम है, तो उसे आधा कर दें; यदि `n` विषम है, तो उसे `3n + 1` से बदल दें। कभी न कभी अनुक्रम 1 तक पहुँच जाता है।

उदाहरण के लिए, 16 से शुरू करने पर अनुक्रम `16 -> 8 -> 4 -> 2 -> 1` होता है, इसलिए इसमें 4 चरण लगते हैं।

अब तक किसी ने भी यह सिद्ध नहीं किया है कि ऐसा हमेशा होता है, लेकिन यह अब तक परीक्षण की गई हर संख्या पर लागू होता है।

# --instructions--

`collatzSteps` नाम का एक फ़ंक्शन लिखें जो एक धनात्मक पूर्णांक `n` लेता है और 1 तक पहुँचने के लिए आवश्यक चरणों की संख्या लौटाता है।

`collatzSteps(1)` का मान 0 है, क्योंकि 1 पहले से ही अनुक्रम का अंत है। `collatzSteps(12)` का मान 9 है, और `collatzSteps(27)` का मान 111 है।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(collatzSteps(16));
// 4 प्रिंट करता है
```

# --seed--

```dart
int collatzSteps(int n) {

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

`collatzSteps(1)` को 0 लौटाना चाहिए, क्योंकि 1 पहले से ही अनुक्रम का अंत है।

```dart
    test('test1', () {
      expect(collatzSteps(1), 0, reason: '--err-t1--');
    });
```

`collatzSteps(2)` को 1 लौटाना चाहिए।

```dart
    test('test2', () {
      expect(collatzSteps(2), 1, reason: '--err-t2--');
    });
```

`collatzSteps(6)` को 8 लौटाना चाहिए।

```dart
    test('test3', () {
      expect(collatzSteps(6), 8, reason: '--err-t3--');
    });
```

`collatzSteps(7)` को 16 लौटाना चाहिए।

```dart
    test('test4', () {
      expect(collatzSteps(7), 16, reason: '--err-t4--');
    });
```

`collatzSteps(16)` को 4 लौटाना चाहिए।

```dart
    test('test5', () {
      expect(collatzSteps(16), 4, reason: '--err-t5--');
    });
```

`collatzSteps(12)` को 9 लौटाना चाहिए।

```dart
    test('test6', () {
      expect(collatzSteps(12), 9, reason: '--err-t6--');
    });
```

`collatzSteps(27)` को 111 लौटाना चाहिए।

```dart
    test('test7', () {
      expect(collatzSteps(27), 111, reason: '--err-t7--');
    });
```

`collatzSteps(97)` को 118 लौटाना चाहिए।

```dart
    test('test8', () {
      expect(collatzSteps(97), 118, reason: '--err-t8--');
    });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int collatzSteps(int n) {
  int value = n;
  int steps = 0;
  while (value != 1) {
    value = value % 2 == 0 ? value ~/ 2 : 3 * value + 1;
    steps++;
  }
  return steps;
}
```
