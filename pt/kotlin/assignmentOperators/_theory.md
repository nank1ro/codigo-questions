Os operadores de atribuição são usados para atribuir valores a variáveis.
O operador de atribuição mais básico é `=`, que atribui o valor à direita à variável à esquerda:
```kotlin
var x = 10
```
Aqui, `10` é atribuído à variável `x`.
Você também pode reatribuir um novo valor a uma variável existente:
```kotlin
x = 20
```
Agora `x` contém o valor `20`.

---

O operador `+=` é um atalho que adiciona um valor a uma variável e atribui o resultado de volta a ela.
Em vez de escrever:
```kotlin
x = x + 5
```
Você pode escrever:
```kotlin
x += 5
```
Ambas as expressões fazem a mesma coisa: aumentam o valor de `x` em `5`.

---

O operador `-=` subtrai um valor de uma variável e atribui o resultado de volta a ela.
Em vez de escrever:
```kotlin
x = x - 3
```
Você pode escrever:
```kotlin
x -= 3
```
Isso diminui o valor de `x` em `3`.

---

O operador `*=` multiplica uma variável por um valor e atribui o resultado de volta a ela.
Em vez de escrever:
```kotlin
x = x * 4
```
Você pode escrever:
```kotlin
x *= 4
```
Isso multiplica `x` por `4` e armazena o resultado de volta em `x`.

---

O operador `/=` divide uma variável por um valor e atribui o resultado de volta a ela.
Em vez de escrever:
```kotlin
x = x / 2
```
Você pode escrever:
```kotlin
x /= 2
```
Observação: quando ambos os operandos são `Int`, o Kotlin realiza **divisão inteira** (a parte fracionária é descartada):
```kotlin
var x = 7
x /= 2
// x agora é 3 (não 3.5)
```
