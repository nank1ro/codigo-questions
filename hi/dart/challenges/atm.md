---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

जेम्स ATM से N डॉलर निकालना चाहता है।
कैश मशीन लेनदेन तभी स्वीकार करेगी जब N 5 का गुणज हो, और जेम्स के खाते में निकासी लेनदेन (बैंक शुल्क सहित) करने के लिए पर्याप्त नकदी हो।
प्रत्येक सफल निकासी के लिए बैंक `0.50$` शुल्क लेता है।
एक प्रयास किए गए लेनदेन के बाद जेम्स के खाते की शेष राशि की गणना करें।
इनपुट निम्नलिखित क्रम में हैं:
1. जेम्स जितनी नकदी निकालना चाहता है वह निम्नलिखित सीमा में है: `0 < N <= 2000`।
2. जेम्स की प्रारंभिक शेष राशि दो दशमलव अंकों की सटीकता के साथ दी गई है और निम्नलिखित सीमा में है: `0 < B <= 2000`।

# --instructions--

प्रयास किए गए लेनदेन के बाद खाते की शेष राशि लौटाएं, जो दो दशमलव अंकों की सटीकता वाली संख्या के रूप में दी गई हो।
यदि लेनदेन पूरा करने के लिए खाते में पर्याप्त पैसे नहीं हैं, तो वर्तमान बैंक शेष राशि लौटाएं।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(accountBalance(10, 20.00))
// prints 9.5
```

# --seed--

```dart
double accountBalance() {
    return
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

एक सफल लेनदेन करें

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

अपर्याप्त धनराशि

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

अस्वीकृत लेनदेन, अमान्य राशि

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

सारा पैसा सफलतापूर्वक निकालें

```dart
    test('test4', () {
      expect(accountBalance(95, 95.50), 0.00, reason: '--err-t4--');
    });
```

# --after-asserts--

```dart
    }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
double accountBalance(int withdraw, double balance) {
  final isMultipleOf5 = withdraw % 5 == 0;
  final isAmountAvailable = balance >= (withdraw + 0.50);
  if (isMultipleOf5 && isAmountAvailable) {
    return balance - withdraw - 0.50;
  }
  return balance;
}
```
