---
language: dart
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James gostaria de sacar N dólares de um caixa eletrônico.
O caixa eletrônico só aceitará a transação se N for um múltiplo de 5, e a conta de James tiver dinheiro suficiente para realizar a transação de saque (incluindo taxas bancárias).
Para cada saque bem-sucedido, o banco cobra `0.50$`.
Calcule o saldo da conta de James após uma tentativa de transação.
As entradas estão na seguinte ordem:
1. o valor em dinheiro que James deseja sacar está no seguinte intervalo: `0 < N <= 2000`.
2. o saldo inicial de James é fornecido com duas casas decimais e está no seguinte intervalo: `0 < B <= 2000`.

# --instructions--

Retorne o saldo da conta após a tentativa de transação, dado como um número com duas casas decimais.
Se não houver dinheiro suficiente na conta para completar a transação, retorne o saldo bancário atual.

Exemplo de chamada da função:
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

Realizar uma transação bem-sucedida

```dart
    test('test1', () {
      expect(accountBalance(50, 120.00), 69.50, reason: '--err-t1--');
    });
```

Fundos insuficientes

```dart
    test('test2', () {
      expect(accountBalance(200, 120.00), 120.00, reason: '--err-t2--');
    });
```

Transação recusada, valor inválido

```dart
    test('test3', () {
      expect(accountBalance(22, 120.00), 120.00, reason: '--err-t3--');
    });
```

Sacar todo o dinheiro com sucesso

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
