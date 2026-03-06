---
language: dart
exerciseType: 1
difficulty: 1
title: 雨粒
---

# --description--

あなたのタスクは、数値を特定の約数に対応する雨粒の音を含む文字列に変換することです。
約数とは、別の数を余りなく均等に割り切れる数のことです。
ある数が別の数の約数であるかどうかをテストする最も簡単な方法は、剰余演算を使用することです。
雨粒のルールは、与えられた数が：

- 3を約数に持つ場合、結果に'Pling'を追加します。
- 5を約数に持つ場合、結果に'Plang'を追加します。
- 7を約数に持つ場合、結果に'Plong'を追加します。
- 3、5、7のいずれも約数に持たない場合、結果はその数の数字そのものになります。

# --instructions--

正しい文字列を返す関数を書いてください。例：

- 28は7を約数に持ちますが、3や5は持たないため、結果は`"Plong"`になります。
- 30は3と5の両方を約数に持ちますが、7は持たないため、結果は`"PlingPlang"`になります。
- 34は3、5、7のいずれも約数に持たないため、結果は`"34"`になります。

関数呼び出しの例：
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

1の音は"1"

```dart
  test('test1', () {
    expect(raindrops(1), "1", reason: '--err-t1--');
  });
```

3の音は"Pling"

```dart
  test('test2', () {
    expect(raindrops(3), "Pling", reason: '--err-t2--');
  });
```

5の音は"Plang"

```dart
  test('test3', () {
    expect(raindrops(5), "Plang", reason: '--err-t3--');
  });
```

7の音は"Plong"

```dart
  test('test4', () {
    expect(raindrops(7), "Plong", reason: '--err-t4--');
  });
```

6の音は"Pling"

```dart
  test('test5', () {
    expect(raindrops(6), "Pling", reason: '--err-t5--');
  });
```

8の音は"8"

```dart
  test('test6', () {
    expect(raindrops(8), "8", reason: '--err-t6--');
  });
```

9の音は"Pling"

```dart
  test('test7', () {
    expect(raindrops(9), "Pling", reason: '--err-t7--');
  });
```

10の音は"Plang"

```dart
  test('test8', () {
    expect(raindrops(10), "Plang", reason: '--err-t8--');
  });
```

14の音は"Plong"

```dart
  test('test9', () {
    expect(raindrops(14), "Plong", reason: '--err-t9--');
  });
```

15の音は"PlingPlang"

```dart
  test('test10', () {
    expect(raindrops(15), "PlingPlang", reason: '--err-t10--');
  });
```

21の音は"PlingPlong"

```dart
  test('test11', () {
    expect(raindrops(21), "PlingPlong", reason: '--err-t11--');
  });
```

25の音は"Plang"

```dart
  test('test12', () {
    expect(raindrops(25), "Plang", reason: '--err-t12--');
  });
```

27の音は"Pling"

```dart
  test('test13', () {
    expect(raindrops(27), "Pling", reason: '--err-t13--');
  });
```

35の音は"PlangPlong"

```dart
  test('test14', () {
    expect(raindrops(35), "PlangPlong", reason: '--err-t14--');
  });
```

49の音は"Plong"

```dart
  test('test15', () {
    expect(raindrops(49), "Plong", reason: '--err-t15--');
  });
```

52の音は"52"

```dart
  test('test16', () {
    expect(raindrops(52), "52", reason: '--err-t16--');
  });
```

105の音は"PlingPlangPlong"

```dart
  test('test17', () {
    expect(raindrops(105), "PlingPlangPlong", reason: '--err-t17--');
  });
```

3125の音は"Plang"

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
