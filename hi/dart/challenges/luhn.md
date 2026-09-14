---
language: dart
exerciseType: 1
difficulty: 2
title: लूह्न चेकसम
---

# --description--

लूह्न एल्गोरिदम एक सरल चेकसम है जिसका उपयोग क्रेडिट कार्ड नंबरों जैसी पहचान संख्याओं को मान्य करने के लिए किया जाता है।

किसी संख्या की जांच करने से पहले, स्ट्रिंग से हर स्पेस हटा दें। स्ट्रिंग तभी मान्य है जब शेष बचा हिस्सा एक कैरेक्टर से लंबा हो और मूल स्ट्रिंग में अंकों और स्पेस के अलावा कुछ और न हो।

जांच करने के लिए, सबसे दाईं ओर के अंक से शुरू करें और बाईं ओर बढ़ते हुए हर दूसरे अंक को दोगुना करें। जब दोगुना करने पर 9 से बड़ी संख्या बनती है, तो उसमें से 9 घटा दें। फिर सभी अंकों का योग करें: संख्या तभी मान्य होती है जब योग 10 से विभाज्य हो।

उदाहरण के लिए, `"059"` देता है `0`, फिर `5` का दोगुना `10` होता है जो `1` बन जाता है, फिर `9`। उनका योग `10` है, जो 10 से विभाज्य है, इसलिए संख्या मान्य है।

# --instructions--

एक फ़ंक्शन `isValid` लिखें जो एक स्ट्रिंग लेता है और संख्या मान्य होने पर `true` लौटाता है, अन्यथा `false`।

- `"4539 3195 0343 6467"` चेकसम पास करता है, इसलिए परिणाम `true` है।
- `"8273 1232 7352 0569"` चेकसम में विफल होता है, इसलिए परिणाम `false` है।
- `"0"` केवल एक कैरेक्टर लंबा है, इसलिए परिणाम `false` है।
- `"055-444-285"` में ऐसा कैरेक्टर है जो अंक या स्पेस नहीं है, इसलिए परिणाम `false` है।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(isValid("095 245 88"));
// prints true
```

# --seed--

```dart
bool isValid(String value) {
  
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

एक अकेला अंक मान्य नहीं है।

```dart
  test('test1', () {
    expect(isValid("0"), false, reason: '--err-t1--');
  });
```

शुरुआत में स्पेस के साथ एक अकेला अंक मान्य नहीं है।

```dart
  test('test2', () {
    expect(isValid(" 0"), false, reason: '--err-t2--');
  });
```

संख्या `"059"` मान्य है।

```dart
  test('test3', () {
    expect(isValid("059"), true, reason: '--err-t3--');
  });
```

संख्या `"59"` मान्य है।

```dart
  test('test4', () {
    expect(isValid("59"), true, reason: '--err-t4--');
  });
```

संख्या `"055 444 285"` मान्य है।

```dart
  test('test5', () {
    expect(isValid("055 444 285"), true, reason: '--err-t5--');
  });
```

संख्या `"055 444 286"` मान्य नहीं है।

```dart
  test('test6', () {
    expect(isValid("055 444 286"), false, reason: '--err-t6--');
  });
```

संख्या `"8273 1232 7352 0569"` मान्य नहीं है।

```dart
  test('test7', () {
    expect(isValid("8273 1232 7352 0569"), false, reason: '--err-t7--');
  });
```

संख्या `"4539 3195 0343 6467"` मान्य है।

```dart
  test('test8', () {
    expect(isValid("4539 3195 0343 6467"), true, reason: '--err-t8--');
  });
```

संख्या `"1 2345 6789 1234 5678 9012"` मान्य नहीं है।

```dart
  test('test9', () {
    expect(isValid("1 2345 6789 1234 5678 9012"), false, reason: '--err-t9--');
  });
```

संख्या `"095 245 88"` मान्य है।

```dart
  test('test10', () {
    expect(isValid("095 245 88"), true, reason: '--err-t10--');
  });
```

एक अक्षर संख्या को अमान्य बना देता है।

```dart
  test('test11', () {
    expect(isValid("055a 444 285"), false, reason: '--err-t11--');
  });
```

डैश संख्या को अमान्य बना देते हैं।

```dart
  test('test12', () {
    expect(isValid("055-444-285"), false, reason: '--err-t12--');
  });
```

एक विराम चिह्न कैरेक्टर संख्या को अमान्य बना देता है।

```dart
  test('test13', () {
    expect(isValid(":9"), false, reason: '--err-t13--');
  });
```

प्रतीक संख्या को अमान्य बना देते हैं।

```dart
  test('test14', () {
    expect(isValid("055# 444\$ 285"), false, reason: '--err-t14--');
  });
```

खाली स्ट्रिंग मान्य नहीं है।

```dart
  test('test15', () {
    expect(isValid(""), false, reason: '--err-t15--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isValid(String value) {
  var sum = 0;
  var count = 0;
  for (var i = value.length - 1; i >= 0; i--) {
    final code = value.codeUnitAt(i);
    if (code == 32) {
      continue;
    }
    if (code < 48 || code > 57) {
      return false;
    }
    var digit = code - 48;
    if (count % 2 == 1) {
      digit *= 2;
      if (digit > 9) {
        digit -= 9;
      }
    }
    sum += digit;
    count++;
  }
  return count > 1 && sum % 10 == 0;
}
```
