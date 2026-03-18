---
language: dart
exerciseType: 1
difficulty: 2
title: Special pythagorean triplet
---

# --description--

पाइथागोरस त्रिक तीन प्राकृतिक संख्याओं का एक समुच्चय है, a < b < c, जिसके लिए a² + b² = c² होता है।

उदाहरण के लिए, 3² + 4² = 9 + 16 = 25 = 5²। केवल एक ऐसा पाइथागोरस त्रिक है जिसके लिए a + b + c = 1000 है।

# --instructions--

एक ऐसा फ़ंक्शन लिखें जो उस पाइथागोरस त्रिक को खोजे जहाँ a + b + c का मान `n` के बराबर है, और गुणनफल a × b × c लौटाए।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(specialPythagoreanTriplet(12));
// prints 60
```

# --seed--

```dart
int specialPythagoreanTriplet(int n) {

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

उस पाइथागोरस त्रिक का गुणनफल जहाँ a+b+c=12 है, 60 के बराबर होना चाहिए

```dart
  test('test1', () {
    expect(specialPythagoreanTriplet(12), 60, reason: '--err-t1--');
  });
```

उस पाइथागोरस त्रिक का गुणनफल जहाँ a+b+c=1000 है, 31875000 के बराबर होना चाहिए

```dart
  test('test2', () {
    expect(specialPythagoreanTriplet(1000), 31875000, reason: '--err-t2--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int specialPythagoreanTriplet(int n) {
  for (int a = 1; a < n; a++) {
    for (int b = a + 1; b < n - a; b++) {
      int c = n - a - b;
      if (c > b && a * a + b * b == c * c) {
        return a * b * c;
      }
    }
  }
  return -1;
}
```
