---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James는 ATM에서 N달러를 인출하려고 합니다.
현금 인출기는 N이 5의 배수이고 James의 계좌에 인출 거래를 수행하기에 충분한 잔액이 있을 때만 (은행 수수료 포함) 거래를 승인합니다.
인출이 성공할 때마다 은행은 `0.50$`를 수수료로 부과합니다.
인출 시도 후 James의 계좌 잔액을 계산하십시오.
입력은 다음 순서로 주어집니다:
1. James가 인출하려는 금액의 범위: `0 < N <= 2000`.
2. James의 초기 잔액은 소수점 이하 두 자리로 주어지며 범위는 다음과 같습니다: `0 < B <= 2000`.

# --instructions--

인출 시도 후 계좌 잔액을 소수점 이하 두 자리의 숫자로 반환하십시오.
계좌에 거래를 완료하기에 충분한 잔액이 없으면 현재 은행 잔액을 반환하십시오.

함수 호출 예시:
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

성공적인 거래를 수행합니다

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

잔액이 부족합니다

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

거래 거부, 유효하지 않은 금액

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

모든 금액을 성공적으로 인출합니다

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
