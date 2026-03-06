---
language: dart
exerciseType: 1
difficulty: 3
title: लीप वर्ष
---

# --description--

एक कैलेंडर वर्ष में ठीक 365.25 दिन होते हैं। लेकिन, अंततः, यह भ्रम पैदा करेगा क्योंकि मनुष्य सामान्यतः 1 की सटीक विभाज्यता से गिनते हैं न कि दशमलव बिंदुओं से। इसलिए, इससे बचने के लिए, हर चार साल के चक्र में सभी 0.25 दिनों को जोड़ने और उस वर्ष को 366 दिन (29 फरवरी को अधिवर्ष दिवस के रूप में शामिल करते हुए) देने और इसे __लीप वर्ष__ कहने का निर्णय लिया गया। चार साल के चक्र में अन्य तीन वर्षों में केवल 365 दिन होंगे और __लीप वर्ष नहीं होंगे__।

# --instructions--

इस चुनौती में हम इसे एक नए स्तर पर ले जाएंगे, जहां आपको `DateTime` क्लास, `switch` स्टेटमेंट, __if ब्लॉक__, __if-else ब्लॉक__ या __टर्नरी ऑपरेशन__ (`x ? a : b`) और न ही लॉजिकल ऑपरेटर __AND__ (`&&`) और __OR__ (`||`) के उपयोग के बिना यह निर्धारित करना है कि यह लीप वर्ष है या नहीं, __NOT__ (`!`) ऑपरेटर को छोड़कर।

यदि यह लीप वर्ष है तो `true` लौटाएं, अन्यथा `false`।

फ़ंक्शन कॉल का उदाहरण:
```dart
print(leapYear(2000));
// prints true
```

# --seed--

```dart
bool leapYear(int year) {
  
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

`DateTime`, `switch`, `if`, `else`, `&&`, `||` या `?` का उपयोग अनुमत नहीं है।

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

वर्ष `2016` एक लीप वर्ष है।

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

वर्ष `1996` एक लीप वर्ष है।

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

वर्ष `1600` एक लीप वर्ष है।

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

वर्ष `2020` एक लीप वर्ष है।

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

वर्ष `2000` एक लीप वर्ष है।

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

वर्ष `2008` एक लीप वर्ष है।

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

वर्ष `1521` एक लीप वर्ष नहीं है।

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

वर्ष `1800` एक लीप वर्ष नहीं है।

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

वर्ष `2007` एक लीप वर्ष नहीं है।

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

वर्ष `2002` एक लीप वर्ष नहीं है।

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

वर्ष `1979` एक लीप वर्ष नहीं है।

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

वर्ष `2006` एक लीप वर्ष नहीं है।

```dart
  test('test12', () {
    expect(leapYear(2006), false, reason: '--err-t12--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
bool leapYear(int year) {
  return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0));
}
```

```dart
bool leapYear(int year) {
  while (year % 100 == 0) {
    year = year ~/ 100;
  }
  return year % 4 == 0;
}
```
