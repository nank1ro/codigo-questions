---
language: dart
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

पैनग्राम एक ऐसा वाक्य है जो अंग्रेजी वर्णमाला के हर अक्षर का कम से कम एक बार उपयोग करता है। सबसे प्रसिद्ध उदाहरण "the quick brown fox jumps over the lazy dog" है, जो सभी 26 अक्षरों को नौ छोटे शब्दों में समा लेता है।

यह जाँच अक्षरों के बड़े या छोटे होने का अंतर नहीं करती, इसलिए `A` और `a` एक ही अक्षर गिने जाते हैं। अंक, विराम चिह्न और रिक्त स्थान अनदेखे किए जाते हैं: वे अक्षर नहीं हैं, लेकिन वे किसी वाक्य को अस्वीकार करने का कारण भी नहीं हैं।

# --instructions--

एक फ़ंक्शन `isPangram` लिखें जो एक वाक्य लेता है और यदि वाक्य पैनग्राम है तो `true` लौटाता है, अन्यथा `false` लौटाता है।

उदाहरण:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- खाली वाक्य पैनग्राम नहीं है।
- केवल `a` से `z` तक के 26 अक्षर गिने जाते हैं।

# --seed--

```dart
bool isPangram(String sentence) {
  
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

खाली वाक्य पैनग्राम नहीं है

```dart
  test('test1', () {
    expect(isPangram(''), false, reason: '--err-t1--');
  });
```

क्लासिक वाक्य "the quick brown fox jumps over the lazy dog" एक पैनग्राम है

```dart
  test('test2', () {
    expect(isPangram('the quick brown fox jumps over the lazy dog'), true, reason: '--err-t2--');
  });
```

जिस वाक्य में अक्षर `x` नहीं है वह पैनग्राम नहीं है

```dart
  test('test3', () {
    expect(isPangram('a quick movement of the enemy will jeopardize five gunboats'), false, reason: '--err-t3--');
  });
```

वाक्य "the five boxing wizards jump quickly" एक पैनग्राम है

```dart
  test('test4', () {
    expect(isPangram('the five boxing wizards jump quickly'), true, reason: '--err-t4--');
  });
```

अंडरस्कोर अनदेखे किए जाते हैं, इसलिए वाक्य फिर भी पैनग्राम है

```dart
  test('test5', () {
    expect(isPangram('the_quick_brown_fox_jumps_over_the_lazy_dog'), true, reason: '--err-t5--');
  });
```

अंक अनदेखे किए जाते हैं, इसलिए वाक्य फिर भी पैनग्राम है

```dart
  test('test6', () {
    expect(isPangram('the 1 quick brown fox jumps over the 2 lazy dogs'), true, reason: '--err-t6--');
  });
```

अंक अक्षरों `e`, `i` और `t` की जगह नहीं लेते

```dart
  test('test7', () {
    expect(isPangram('7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog'), false, reason: '--err-t7--');
  });
```

बड़े अक्षरों में लिखा वाक्य भी पैनग्राम है

```dart
  test('test8', () {
    expect(isPangram('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG'), true, reason: '--err-t8--');
  });
```

वर्णमाला के एक ही आधे हिस्से के बड़े और छोटे अक्षर मिलाना पर्याप्त नहीं है

```dart
  test('test9', () {
    expect(isPangram('abcdefghijklm ABCDEFGHIJKLM'), false, reason: '--err-t9--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isPangram(String sentence) {
  final letters = <String>{};

  for (final char in sentence.toLowerCase().split('')) {
    if (char.compareTo('a') >= 0 && char.compareTo('z') <= 0) {
      letters.add(char);
    }
  }

  return letters.length == 26;
}
```
