---
language: dart
exerciseType: 1
difficulty: 2
title: अनाग्राम
---

# --description--

दो शब्द अनाग्राम होते हैं जब एक दूसरे के अक्षरों की पुनर्व्यवस्था हो: वे बिल्कुल वही अक्षर उपयोग करते हैं, प्रत्येक अक्षर उतनी ही बार, बस अलग क्रम में। `listen` और `silent` अनाग्राम हैं, और वैसे ही `stone` और `tones` भी।

कोई शब्द कभी अपने आप का अनाग्राम नहीं होता। यदि दोनों शब्द बिल्कुल समान हैं, तो कुछ भी पुनर्व्यवस्थित नहीं हुआ, इसलिए उत्तर `false` है। दोनों शब्द छोटे अक्षरों में दिए जाते हैं और उनमें केवल `a` से `z` तक के अक्षर होते हैं।

# --instructions--

एक फ़ंक्शन `isAnagram` लिखें जो दो शब्द, `first` और `second`, लेता है और यदि वे एक-दूसरे के अनाग्राम हैं तो `true` लौटाता है, अन्यथा `false` लौटाता है।

उदाहरण:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- दो समान शब्द अनाग्राम नहीं होते।
- अलग-अलग लंबाई के शब्द कभी अनाग्राम नहीं होते।
- प्रत्येक अक्षर दोनों शब्दों में उतनी ही बार आना चाहिए।

# --seed--

```dart
bool isAnagram(String first, String second) {
  
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

शब्द "listen" और "silent" अनाग्राम हैं

```dart
  test('test1', () {
    expect(isAnagram('listen', 'silent'), true, reason: '--err-t1--');
  });
```

शब्द "stone" और "tones" अनाग्राम हैं

```dart
  test('test2', () {
    expect(isAnagram('stone', 'tones'), true, reason: '--err-t2--');
  });
```

कोई शब्द अपने आप का अनाग्राम नहीं होता

```dart
  test('test3', () {
    expect(isAnagram('stone', 'stone'), false, reason: '--err-t3--');
  });
```

अलग-अलग लंबाई के शब्द अनाग्राम नहीं होते

```dart
  test('test4', () {
    expect(isAnagram('abc', 'abcd'), false, reason: '--err-t4--');
  });
```

समान अक्षरों की अलग-अलग मात्रा अनाग्राम नहीं होती

```dart
  test('test5', () {
    expect(isAnagram('aab', 'abb'), false, reason: '--err-t5--');
  });
```

शब्द "anagram" और "nagaram" अनाग्राम हैं

```dart
  test('test6', () {
    expect(isAnagram('anagram', 'nagaram'), true, reason: '--err-t6--');
  });
```

समान लंबाई वाले दो शब्द जिनके अक्षर अलग हैं, अनाग्राम नहीं होते

```dart
  test('test7', () {
    expect(isAnagram('rat', 'car'), false, reason: '--err-t7--');
  });
```

दो खाली शब्द समान होते हैं, इसलिए वे अनाग्राम नहीं होते

```dart
  test('test8', () {
    expect(isAnagram('', ''), false, reason: '--err-t8--');
  });
```

दो अलग एकल अक्षर अनाग्राम नहीं होते

```dart
  test('test9', () {
    expect(isAnagram('a', 'b'), false, reason: '--err-t9--');
  });
```

शब्द "evil" और "vile" अनाग्राम हैं

```dart
  test('test10', () {
    expect(isAnagram('evil', 'vile'), true, reason: '--err-t10--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isAnagram(String first, String second) {
  if (first == second) {
    return false;
  }

  final firstLetters = first.split('')..sort();
  final secondLetters = second.split('')..sort();

  return firstLetters.join() == secondLetters.join();
}
```
