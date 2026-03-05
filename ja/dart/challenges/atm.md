---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

ジェームズはATMからN ドルを引き出したいと考えています。
ATMは、Nが5の倍数であり、かつジェームズの口座に取引を実行するのに十分な残高がある場合（銀行手数料を含む）にのみ取引を受け付けます。
引き出しが成功するたびに、銀行は`0.50$`の手数料を請求します。
取引後のジェームズの口座残高を計算してください。
入力は以下の順序です：
1. ジェームズが引き出したい金額は次の範囲です：`0 < N <= 2000`。
2. ジェームズの初期残高は小数点以下2桁で与えられ、次の範囲です：`0 < B <= 2000`。

# --instructions--

取引後の口座残高を小数点以下2桁の数値で返してください。
口座に取引を完了するのに十分な残高がない場合は、現在の口座残高を返してください。

関数呼び出しの例：
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

取引が成功する場合

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

残高不足の場合

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

取引拒否、無効な金額

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

全額引き出しが成功する場合

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
