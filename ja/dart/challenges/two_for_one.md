---
language: dart
exerciseType: 1
difficulty: 1
title: 2対1
---

# --description--

名前が与えられた場合、次のメッセージを含む文字列を返します：
`One for X, one for me.`
ここで`X`は与えられた名前です。
ただし、名前が指定されていない場合は、次の文字列を返します：
`One for you, one for me.`

# --instructions--

正しい文字列を返す関数を書いてください。例：

**入力**: `Walter`
**出力**: `One for Walter, one for me.`

**入力**: `James`
**出力**: `One for James, one for me.`

**入力**: `Martha`
**出力**: `One for Martha, one for me.`

# --seed--

```dart
String twoForOne() {
  
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

名前が指定されていない場合

```dart
  test('test1', () {
    expect(twoForOne(), "One for you, one for me.", reason: '--err-t1--');
  });
```

名前に"James"を渡す

```dart
  test('test2', () {
    expect(twoForOne(name: "James"), "One for James, one for me.", reason: '--err-t2--');
  });
```

名前に"Martha"を渡す

```dart
  test('test3', () {
    expect(twoForOne(name: "Martha"), "One for Martha, one for me.", reason: '--err-t3--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String twoForOne({String? name}) {
  if (name != null) {
    return "One for $name, one for me.";
  }
  return "One for you, one for me.";
}
```


