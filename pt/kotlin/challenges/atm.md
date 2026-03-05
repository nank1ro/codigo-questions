---
language: kotlin
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
```kotlin
println(accountBalance(10, 20.00))
// prints 9.5
```

# --seed--

```kotlin
fun accountBalance(): Double {
    return
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Realizar uma transação bem-sucedida

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

Fundos insuficientes

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

Transação recusada, valor inválido

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

Sacar todo o dinheiro com sucesso

```kotlin
    tryCatch(accountBalance(95, 95.50) == 0.00)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun accountBalance(withdraw: Int, balance: Double): Double {
    val isMultipleOf5 = withdraw.rem(5) == 0;
    val isAmountAvailable = balance >= (withdraw + 0.50)
    if (isMultipleOf5 && isAmountAvailable) {
        return balance - withdraw - 0.50
    }
    return balance
}
```
