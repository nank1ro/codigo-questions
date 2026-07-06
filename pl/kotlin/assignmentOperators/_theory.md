Operatory przypisania służą do przypisywania wartości do zmiennych.
Najbardziej podstawowym operatorem przypisania jest `=`, który przypisuje wartość po prawej stronie do zmiennej po lewej:
```kotlin
var x = 10
```
Tutaj `10` jest przypisane do zmiennej `x`.
Możesz również przypisać nową wartość do istniejącej zmiennej:
```kotlin
x = 20
```
Teraz `x` przechowuje wartość `20`.

---

Operator `+=` to skrót, który dodaje wartość do zmiennej i przypisuje wynik z powrotem do niej.
Zamiast pisać:
```kotlin
x = x + 5
```
Możesz napisać:
```kotlin
x += 5
```
Oba wyrażenia robią to samo: zwiększają wartość `x` o `5`.

---

Operator `-=` odejmuje wartość od zmiennej i przypisuje wynik z powrotem do niej.
Zamiast pisać:
```kotlin
x = x - 3
```
Możesz napisać:
```kotlin
x -= 3
```
To zmniejsza wartość `x` o `3`.

---

Operator `*=` mnoży zmienną przez wartość i przypisuje wynik z powrotem do niej.
Zamiast pisać:
```kotlin
x = x * 4
```
Możesz napisać:
```kotlin
x *= 4
```
To mnoży `x` przez `4` i przechowuje wynik z powrotem w `x`.

---

Operator `/=` dzieli zmienną przez wartość i przypisuje wynik z powrotem do niej.
Zamiast pisać:
```kotlin
x = x / 2
```
Możesz napisać:
```kotlin
x /= 2
```
Uwaga: gdy oba operandy są typu `Int`, Kotlin wykonuje **dzielenie całkowite** (część ułamkowa jest odrzucana):
```kotlin
var x = 7
x /= 2
// x wynosi teraz 3 (nie 3.5)
```
