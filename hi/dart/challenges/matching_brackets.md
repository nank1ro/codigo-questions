---
language: dart
exerciseType: 1
difficulty: 3
title: कोष्ठकों का मिलान
---

# --description--

कोड, गणित या मार्कअप ले जाने वाला टेक्स्ट कोष्ठकों से भरा होता है, और हर खोलने वाले कोष्ठक को उसी किस्म का एक बंद करने वाला कोष्ठक चाहिए। एक स्ट्रिंग तब संतुलित होती है जब उसके कोष्ठक जोड़े बनाते हैं और प्याज की परतों की तरह एक-दूसरे के भीतर नेस्ट होते हैं: `{[()]}` संतुलित है, जबकि `{[(])}` संतुलित नहीं है, क्योंकि गोल जोड़ा उस वर्ग जोड़े से पहले बंद हो जाता है जिसके भीतर वह स्थित है।

यहाँ तीन जोड़े मायने रखते हैं: गोल `()`, वर्ग `[]` और कर्ली `{}`। स्ट्रिंग का बाकी हर कैरेक्टर नज़रअंदाज़ कर दिया जाता है। एक बंद करने वाले कोष्ठक को सबसे हाल में खोले गए उस कोष्ठक को बंद करना चाहिए जो अभी भी खुला है, और जब स्ट्रिंग समाप्त हो जाए तो कोई कोष्ठक खुला नहीं रहना चाहिए।

# --instructions--

एक फ़ंक्शन `isBalanced` लिखें जो एक स्ट्रिंग लेता है और तब `true` लौटाता है जब उसके सभी कोष्ठक मेल खाते हों और ठीक से नेस्ट होते हों, अन्यथा `false`।

उदाहरण:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- खाली स्ट्रिंग संतुलित होती है।
- जो कैरेक्टर कोष्ठक नहीं हैं उन्हें नज़रअंदाज़ कर दिया जाता है।
- एक बंद करने वाला कोष्ठक सबसे हाल में खोले गए उस कोष्ठक से मेल खाना चाहिए जो अभी भी खुला है।
- जब स्ट्रिंग समाप्त हो तब कोई कोष्ठक खुला नहीं रहना चाहिए।

# --seed--

```dart
bool isBalanced(String text) {
  
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

खाली स्ट्रिंग संतुलित होती है

```dart
  test('test1', () {
    expect(isBalanced(''), true, reason: '--err-t1--');
  });
```

गोल कोष्ठकों का एक जोड़ा संतुलित होता है

```dart
  test('test2', () {
    expect(isBalanced('()'), true, reason: '--err-t2--');
  });
```

एक-दूसरे के भीतर नेस्ट किए गए तीनों किस्म के जोड़े संतुलित होते हैं

```dart
  test('test3', () {
    expect(isBalanced('{[()]}'), true, reason: '--err-t3--');
  });
```

दूसरे टेक्स्ट के साथ मिले कोष्ठक भी संतुलित होते हैं

```dart
  test('test4', () {
    expect(isBalanced('{what is (42)}[?]'), true, reason: '--err-t4--');
  });
```

बगल में रखे गए जोड़े संतुलित होते हैं

```dart
  test('test5', () {
    expect(isBalanced('()[]{}'), true, reason: '--err-t5--');
  });
```

बिना किसी कोष्ठक वाली स्ट्रिंग संतुलित होती है

```dart
  test('test6', () {
    expect(isBalanced('no brackets in here at all'), true, reason: '--err-t6--');
  });
```

क्रॉस हो चुका जोड़ा संतुलित नहीं होता

```dart
  test('test7', () {
    expect(isBalanced('{[(])}'), false, reason: '--err-t7--');
  });
```

कभी बंद न होने वाला खोलने वाला कोष्ठक संतुलित नहीं होता

```dart
  test('test8', () {
    expect(isBalanced('('), false, reason: '--err-t8--');
  });
```

किसी खोलने वाले कोष्ठक से पहले आया बंद करने वाला कोष्ठक संतुलित नहीं होता

```dart
  test('test9', () {
    expect(isBalanced(')('), false, reason: '--err-t9--');
  });
```

स्ट्रिंग में गहराई में क्रॉस हो चुके जोड़े संतुलित नहीं होते

```dart
  test('test10', () {
    expect(isBalanced('(([]{[}]))'), false, reason: '--err-t10--');
  });
```

अंत में बचा हुआ बंद करने वाला कोष्ठक संतुलित नहीं होता

```dart
  test('test11', () {
    expect(isBalanced('())'), false, reason: '--err-t11--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool isBalanced(String text) {
  const pairs = {')': '(', ']': '[', '}': '{'};
  final stack = <String>[];

  for (final char in text.split('')) {
    if (char == '(' || char == '[' || char == '{') {
      stack.add(char);
    } else if (pairs.containsKey(char)) {
      if (stack.isEmpty || stack.removeLast() != pairs[char]) {
        return false;
      }
    }
  }

  return stack.isEmpty;
}
```
