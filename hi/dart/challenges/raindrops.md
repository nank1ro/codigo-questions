---
language: dart
exerciseType: 1
difficulty: 1
title: बारिश की बूंदें
---

# --description--

आपका कार्य एक संख्या को एक स्ट्रिंग में बदलना है जिसमें कुछ संभावित गुणनखंडों के अनुरूप बारिश की बूंदों की आवाज़ें हों।
गुणनखंड वह संख्या है जो किसी अन्य संख्या को पूरी तरह से विभाजित करती है, बिना कोई शेषफल छोड़े।
यह जांचने का सबसे सरल तरीका कि कोई संख्या किसी अन्य का गुणनखंड है या नहीं, मॉड्यूलो ऑपरेशन का उपयोग करना है।
बारिश की बूंदों के नियम हैं कि यदि दी गई संख्या:

- का गुणनखंड 3 है, तो परिणाम में 'Pling' जोड़ें।
- का गुणनखंड 5 है, तो परिणाम में 'Plang' जोड़ें।
- का गुणनखंड 7 है, तो परिणाम में 'Plong' जोड़ें।
- का गुणनखंड 3, 5, या 7 में से कोई नहीं है, तो परिणाम संख्या के अंक होने चाहिए।

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

- 28 का गुणनखंड 7 है, लेकिन 3 या 5 नहीं, इसलिए परिणाम `"Plong"` होगा।
- 30 के गुणनखंड 3 और 5 दोनों हैं, लेकिन 7 नहीं, इसलिए परिणाम `"PlingPlang"` होगा।
- 34 का गुणनखंड 3, 5, या 7 नहीं है, इसलिए परिणाम `"34"` होगा।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(raindrops(28))
// prints "Plong"
```

# --seed--

```dart
String raindrops() {

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

1 के लिए ध्वनि "1" है

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

3 के लिए ध्वनि "Pling" है

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

5 के लिए ध्वनि "Plang" है

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

7 के लिए ध्वनि "Plong" है

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

6 के लिए ध्वनि "Pling" है

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

8 के लिए ध्वनि "8" है

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

9 के लिए ध्वनि "Pling" है

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

10 के लिए ध्वनि "Plang" है

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

14 के लिए ध्वनि "Plong" है

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

15 के लिए ध्वनि "PlingPlang" है

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

21 के लिए ध्वनि "PlingPlong" है

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

25 के लिए ध्वनि "Plang" है

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

27 के लिए ध्वनि "Pling" है

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

35 के लिए ध्वनि "PlangPlong" है

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

49 के लिए ध्वनि "Plong" है

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

52 के लिए ध्वनि "52" है

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

105 के लिए ध्वनि "PlingPlangPlong" है

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

3125 के लिए ध्वनि "Plang" है

```dart
  test('test18', () {
    expect(raindrops(3125), "Plang", reason: '--err-t18--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String raindrops(int number) {
  var result = "";
  if (number % 3 == 0) {
    result += "Pling";
  }
  if (number % 5 == 0) {
    result += "Plang";
  }
  if (number % 7 == 0) {
    result += "Plong";
  }
  if (result.isEmpty) {
    result = number.toString();
  }
  return result;
}
```
