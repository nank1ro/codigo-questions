---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James gostaria de sacar N dólares de um ATM.
O caixa eletrônico só aceitará a transação se N for um múltiplo de 5, e a conta de James tiver dinheiro suficiente para realizar a transação de saque (incluindo taxas bancárias).
Para cada saque bem-sucedido, o banco cobra `0.50$`.
Calcule o saldo da conta de James após uma tentativa de transação.
As entradas estão na seguinte ordem:
1. o valor em dinheiro que James deseja sacar está no seguinte intervalo: `0 < N <= 2000`.
2. o saldo inicial de James é dado com duas casas decimais e está no seguinte intervalo: `0 < B <= 2000`.

# --instructions--

Retorne o saldo da conta após a tentativa de transação, dado como um número com duas casas decimais.
Se não houver dinheiro suficiente na conta para completar a transação, retorne o saldo bancário atual.

> DICA: omita os rótulos dos argumentos com o `_` (underscore)

Exemplo de chamada da função:
```swift
print(accountBalance(10, 20))
// prints 9,5
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func accountBalance() -> Double {
    return
}
```

# --asserts--

Realizar uma transação bem-sucedida

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

Fundos insuficientes

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

Transação recusada, valor inválido

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

Sacar todo o dinheiro com sucesso

```swift
do {
    let expected: Double = 0.00
    tryCatch(accountBalance(95, 95.50) == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func accountBalance(_ withdraw: Double,_ balance: Double) -> Double {
    let isMultipleOf5 = withdraw.truncatingRemainder(dividingBy: 5) == 0;
    let isAmountAvailable = balance >= (withdraw + 0.50)
    if isMultipleOf5 && isAmountAvailable {
        return balance - withdraw - 0.50
    }
    return balance
}
```
