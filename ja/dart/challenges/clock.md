---
language: dart
exerciseType: 1
difficulty: 2
title: 時計
---

# --description--

24時間時計は、時刻を `HH:MM` の形で表します。真夜中の直後の `00:00` に始まり、次の真夜中の1分前の `23:59` で終わります。どちらの部分も常に2桁で書かれるため、午前11時9分は `11:09` と表示されます。

1日はちょうど1440分です。時計が `23:59` を過ぎると `00:00` に折り返して1日がまた始まり、逆に `00:00` より前へ巻き戻すと `23:59` に到達します。

# --instructions--

2つの整数 `hours` と `minutes` を受け取り、24時間時計の時刻を、両方の部分が2桁になるようゼロ埋めした文字列 `"HH:MM"` として返す関数 `clockTime` を書いてください。

例:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- どちらの数も、負の値や実際の時計が取りうる範囲を超える大きな値になることがあります。
- 合計分数を `hours * 60 + minutes` として求め、その合計を `0` から `1439` の範囲に折り返して、時計がどちらの方向にも巡るようにします。
- `clockTime(24, 0)` はちょうど1日なので、`"00:00"` と表示されます。

# --seed--

```dart
String clockTime(int hours, int minutes) {
  
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

午前8時は `08:00` と表示される

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

1桁の数字は2桁になるようゼロ埋めされるため、午前11時9分は `11:09` と表示される

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

ちょうど1日分の時間は `00:00` に折り返される

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

60を超える分は時間の方へ繰り越される

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

負の時間は時計を真夜中より前へ巻き戻す

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

負の分数も時計を巻き戻す

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

1日より多く巻き戻しても折り返しが続く

```dart
  test('test7', () {
    expect(clockTime(-25, 0), "23:00", reason: '--err-t7--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String clockTime(int hours, int minutes) {
  // Dartの%はユークリッド剰余なので、負の合計はそのまま
  // 0..1439の範囲に折り返されます。
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
