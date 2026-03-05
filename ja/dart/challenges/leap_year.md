---
language: dart
exerciseType: 1
difficulty: 3
title: うるう年
---

# --description--

暦年にはちょうど365.25日あります。しかし、最終的にはこれが混乱を招くことになります。なぜなら、人間は通常、小数点ではなく1の正確な整除性で数えるからです。そこで、後者を避けるために、4年周期ごとに0.25日をすべて足し合わせ、その年を366日（閏日として2月29日を含む）とし、__うるう年__と呼ぶことが決められました。4年周期の他の3年は365日のみで、__うるう年ではありません__。

# --instructions--

このチャレンジでは、`DateTime`クラス、`switch`文、__ifブロック__、__if-elseブロック__、__三項演算子__（`x ? a : b`）、論理演算子__AND__（`&&`）と__OR__（`||`）を使用せずに、うるう年かどうかを判定してください。ただし、__NOT__（`!`）演算子は使用できます。

うるう年の場合は`true`を、そうでない場合は`false`を返してください。

関数呼び出しの例：
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

`DateTime`、`switch`、`if`、`else`、`&&`、`||`、`?`の使用は許可されていません。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||DateTime",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`年はうるう年です。

```dart
  test('test1', () {
    expect(leapYear(2016), true, reason: '--err-t1--');
  });
```

`1996`年はうるう年です。

```dart
  test('test2', () {
    expect(leapYear(1996), true, reason: '--err-t2--');
  });
```

`1600`年はうるう年です。

```dart
  test('test3', () {
    expect(leapYear(1600), true, reason: '--err-t3--');
  });
```

`2020`年はうるう年です。

```dart
  test('test4', () {
    expect(leapYear(2020), true, reason: '--err-t4--');
  });
```

`2000`年はうるう年です。

```dart
  test('test5', () {
    expect(leapYear(2000), true, reason: '--err-t5--');
  });
```

`2008`年はうるう年です。

```dart
  test('test6', () {
    expect(leapYear(2008), true, reason: '--err-t6--');
  });
```

`1521`年はうるう年ではありません。

```dart
  test('test7', () {
    expect(leapYear(1521), false, reason: '--err-t7--');
  });
```

`1800`年はうるう年ではありません。

```dart
  test('test8', () {
    expect(leapYear(1800), false, reason: '--err-t8--');
  });
```

`2007`年はうるう年ではありません。

```dart
  test('test9', () {
    expect(leapYear(2007), false, reason: '--err-t9--');
  });
```

`2002`年はうるう年ではありません。

```dart
  test('test10', () {
    expect(leapYear(2002), false, reason: '--err-t10--');
  });
```

`1979`年はうるう年ではありません。

```dart
  test('test11', () {
    expect(leapYear(1979), false, reason: '--err-t11--');
  });
```

`2006`年はうるう年ではありません。

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
