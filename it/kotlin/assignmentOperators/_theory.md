Gli operatori di assegnazione vengono usati per assegnare valori alle variabili.
L'operatore di assegnazione più semplice è `=`, che assegna il valore a destra alla variabile a sinistra:
```kotlin
var x = 10
```
Qui, `10` viene assegnato alla variabile `x`.
Puoi anche riassegnare un nuovo valore a una variabile esistente:
```kotlin
x = 20
```
Ora `x` contiene il valore `20`.

---

L'operatore `+=` è una forma abbreviata che aggiunge un valore a una variabile e riassegna il risultato.
Invece di scrivere:
```kotlin
x = x + 5
```
Puoi scrivere:
```kotlin
x += 5
```
Entrambe le espressioni fanno la stessa cosa: aumentano il valore di `x` di `5`.

---

L'operatore `-=` sottrae un valore da una variabile e riassegna il risultato.
Invece di scrivere:
```kotlin
x = x - 3
```
Puoi scrivere:
```kotlin
x -= 3
```
Questo diminuisce il valore di `x` di `3`.

---

L'operatore `*=` moltiplica una variabile per un valore e riassegna il risultato.
Invece di scrivere:
```kotlin
x = x * 4
```
Puoi scrivere:
```kotlin
x *= 4
```
Questo moltiplica `x` per `4` e memorizza il risultato di nuovo in `x`.

---

L'operatore `/=` divide una variabile per un valore e riassegna il risultato.
Invece di scrivere:
```kotlin
x = x / 2
```
Puoi scrivere:
```kotlin
x /= 2
```
Nota: quando entrambi gli operandi sono `Int`, Kotlin esegue la **divisione intera** (la parte frazionaria viene scartata):
```kotlin
var x = 7
x /= 2
// x è ora 3 (non 3.5)
```
