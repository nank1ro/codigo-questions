---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James 想从 ATM 取出 N 美元。
ATM 只会在 N 是 5 的倍数且 James 的账户有足够的现金来执行取款交易（包括银行手续费）时才会接受交易。
每次成功取款，银行收取 `0.50$` 的手续费。
计算 James 在尝试交易后的账户余额。
输入按以下顺序给出：
1. James 希望取出的现金金额范围为：`0 < N <= 2000`。
2. James 的初始余额精确到两位小数，范围为：`0 < B <= 2000`。

# --instructions--

返回尝试交易后的账户余额，以精确到两位小数的数字表示。
如果账户中没有足够的资金完成交易，则返回当前银行余额。

函数调用示例：
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

执行一笔成功的交易

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

资金不足

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

交易被拒绝，金额无效

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

成功取出所有资金

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
