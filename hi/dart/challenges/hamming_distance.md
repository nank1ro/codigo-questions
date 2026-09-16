---
language: dart
exerciseType: 1
difficulty: 1
title: हैमिंग दूरी
---

# --description--

DNA को न्यूक्लियोटाइडों के स्ट्रैंड के रूप में लिखा जाता है, जिनमें से प्रत्येक एक अक्षर होता है: `A`, `C`, `G` या `T`। जब समान लंबाई के दो स्ट्रैंड साथ-साथ पंक्तिबद्ध किए जाते हैं, तो कुछ स्थानों पर एक ही न्यूक्लियोटाइड होता है और कुछ स्थानों पर अलग-अलग।

जिन स्थानों पर दोनों स्ट्रैंड भिन्न होते हैं, उनकी संख्या हैमिंग दूरी कहलाती है, और जीववैज्ञानिक इसका उपयोग यह मापने के लिए करते हैं कि दो स्ट्रैंड कितनी दूर अलग हो गए हैं। `GAGCCTACTAACGGGAT` को `CATCGTAATGACGGCCT` के साथ पंक्तिबद्ध करने पर 7 स्थान भिन्न मिलते हैं, इसलिए उनकी हैमिंग दूरी 7 होती है।

# --instructions--

`hammingDistance` नाम का एक फ़ंक्शन लिखें जो समान लंबाई के दो DNA स्ट्रैंड लेता है और उन स्थानों की संख्या लौटाता है जहाँ वे भिन्न होते हैं।

उदाहरण:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- दोनों स्ट्रैंड हमेशा समान लंबाई के होते हैं, इसलिए आपको कभी अलग-अलग लंबाई वाले स्ट्रैंड संभालने की ज़रूरत नहीं है।
- दो खाली स्ट्रैंड कहीं भिन्न नहीं होते, इसलिए उनकी दूरी 0 होती है।

# --seed--

```dart
int hammingDistance(String left, String right) {
  
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

दो खाली स्ट्रैंड कहीं भिन्न नहीं होते

```dart
  test('test1', () {
    expect(hammingDistance('', ''), 0, reason: '--err-t1--');
  });
```

दो समान एकल-न्यूक्लियोटाइड स्ट्रैंड में कोई अंतर नहीं होता

```dart
  test('test2', () {
    expect(hammingDistance('A', 'A'), 0, reason: '--err-t2--');
  });
```

दो भिन्न एकल-न्यूक्लियोटाइड स्ट्रैंड एक स्थान पर भिन्न होते हैं

```dart
  test('test3', () {
    expect(hammingDistance('A', 'G'), 1, reason: '--err-t3--');
  });
```

दो छोटे स्ट्रैंड जो हर स्थान पर भिन्न होते हैं

```dart
  test('test4', () {
    expect(hammingDistance('AG', 'CT'), 2, reason: '--err-t4--');
  });
```

दो छोटे स्ट्रैंड जो केवल पहले स्थान पर भिन्न होते हैं

```dart
  test('test5', () {
    expect(hammingDistance('AT', 'CT'), 1, reason: '--err-t5--');
  });
```

स्ट्रैंडों के बीच में एक भिन्न न्यूक्लियोटाइड

```dart
  test('test6', () {
    expect(hammingDistance('GGACG', 'GGTCG'), 1, reason: '--err-t6--');
  });
```

अलग-अलग स्थानों पर समान न्यूक्लियोटाइड भी अंतर में गिने जाते हैं

```dart
  test('test7', () {
    expect(hammingDistance('TAG', 'GAT'), 2, reason: '--err-t7--');
  });
```

चार अंतरों वाले स्ट्रैंडों का एक लंबा जोड़ा

```dart
  test('test8', () {
    expect(hammingDistance('GATACA', 'GCATAA'), 4, reason: '--err-t8--');
  });
```

एक स्ट्रैंड को एक स्थान खिसकाने पर लगभग हर स्थान भिन्न हो जाता है

```dart
  test('test9', () {
    expect(hammingDistance('GGACGGATTCTG', 'AGGACGGATTCT'), 9, reason: '--err-t9--');
  });
```

विवरण वाले दोनों स्ट्रैंड की दूरी सात है

```dart
  test('test10', () {
    expect(hammingDistance('GAGCCTACTAACGGGAT', 'CATCGTAATGACGGCCT'), 7, reason: '--err-t10--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
int hammingDistance(String left, String right) {
  var distance = 0;

  for (var i = 0; i < left.length; i++) {
    if (left[i] != right[i]) {
      distance++;
    }
  }

  return distance;
}
```
