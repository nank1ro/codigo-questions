---
language: dart
exerciseType: 1
difficulty: 1
title: 100 दरवाज़े
---

# --description--

एक पंक्ति में 100 दरवाज़े हैं जो सभी शुरू में बंद हैं।
आप दरवाज़ों से 100 बार गुज़रते हैं।
पहली बार, हर दरवाज़े पर जाएं और दरवाज़े को 'टॉगल' करें (यदि दरवाज़ा बंद है, तो खोलें; यदि खुला है, तो बंद करें)।
दूसरी बार, केवल हर दूसरे दरवाज़े (यानी, दरवाज़ा #2, #4, #6, ...) पर जाएं और उसे टॉगल करें।
तीसरी बार, हर तीसरे दरवाज़े (यानी, दरवाज़ा #3, #6, #9, ...) पर जाएं, आदि, जब तक आप केवल 100वें दरवाज़े पर न पहुंचें।

# --instructions--

अंतिम पास के बाद दरवाज़ों की स्थिति निर्धारित करने के लिए एक फ़ंक्शन लागू करें।
अंतिम परिणाम एक ऐरे में लौटाएं, जिसमें केवल दरवाज़े का नंबर शामिल हो यदि वह खुला है।
> यह विधि दरवाज़ों की एक परिवर्तनीय संख्या के साथ काम करने में सक्षम होनी चाहिए।

# --seed--

```dart
import 'dart:math';

List<int> getFinalOpenedDoors(numDoors: Int) {
    
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

100 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```dart
    test("test1", () {
      const solution1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];

      expect(getFinalOpenedDoors(100), solution1, reason: "--err-t1--");
    });
```

10 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```dart
    test("test2", () {
      const solution2 = [1, 4, 9];
      expect(getFinalOpenedDoors(10), solution2, reason: "--err-t2--");
    });
```

950 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएं

```dart
    test("test3", () {
      const solution3 = [ 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900];
      expect(getFinalOpenedDoors(950), solution3, reason: "--err-t3--");
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
import 'dart:math';

int square(int number) => pow(number.toDouble(), 2.0).toInt();

List<int> getFinalOpenedDoors(int numDoors) {
    final openDoors = <int>[];
    var i = 1;
    while (square(i) <= numDoors) {
        openDoors.add(square(i));
        i += 1;
    }
    return openDoors;
}
```
