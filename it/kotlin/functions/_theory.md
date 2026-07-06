Una funzione è un blocco di codice che esegue un compito specifico e può essere riutilizzato in tutto il programma.
In Kotlin, si definisce una funzione usando la parola chiave `fun`, seguita dal nome della funzione e dalle parentesi:
```kotlin
fun greet() {
    println("Hello!")
}
```
Per chiamare (eseguire) una funzione, usa il suo nome seguito dalle parentesi:
```kotlin
greet() // prints Hello!
```
Una funzione che non restituisce un valore restituisce implicitamente `Unit`.

---

Le funzioni possono restituire un valore. Si specifica il tipo di ritorno dopo le parentesi usando i due punti:
```kotlin
fun getNumber(): Int {
    return 42
}
```
La parola chiave `return` invia un valore al chiamante:
```kotlin
var result = getNumber()
println(result) // prints 42
```
Il tipo di ritorno deve corrispondere al tipo del valore restituito.

---

Le funzioni possono accettare parametri, ovvero input che si passano quando si chiama la funzione.
I parametri sono dichiarati all'interno delle parentesi con un nome e un tipo:
```kotlin
fun greet(name: String) {
    println("Hello, \$name!")
}
```
Si passano argomenti quando si chiama la funzione:
```kotlin
greet("Alice") // prints Hello, Alice!
```
I parametri consentono di scrivere codice riutilizzabile che funziona con valori diversi.

---

Kotlin supporta i valori di parametri predefiniti. Se un chiamante non fornisce un argomento, viene utilizzato il valore predefinito:
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
I valori predefiniti rendono i parametri opzionali, riducendo la necessità di funzioni sovraccaricate.

---

Quando il corpo di una funzione consiste in una singola espressione, puoi usare la sintassi a espressione singola con `=`:
```kotlin
fun square(n: Int): Int = n * n
```
Questo è più conciso della forma a corpo di blocco. Kotlin può spesso inferire il tipo di ritorno, quindi puoi anche scrivere:
```kotlin
fun square(n: Int) = n * n
```
Le funzioni a espressione singola sono un idioma Kotlin comune per calcoli semplici.

---

Le funzioni possono restituire valori `Boolean`, il che è utile per verificare condizioni:
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
Una funzione `Boolean` restituisce `true` o `false`.

---

Le funzioni possono avere più parametri di tipi diversi:
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
Gli argomenti nominati ti permettono di passare valori in qualsiasi ordine usando il nome del parametro:
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Una funzione di base in Kotlin usa la parola chiave `fun` seguita da un nome e parentesi:
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

Per dichiarare un tipo di ritorno per una funzione, aggiungi due punti e il tipo dopo le parentesi:
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

Un parametro di funzione è dichiarato con un nome, due punti e un tipo:
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

Una funzione a espressione singola usa `=` invece di un corpo di blocco:
```kotlin
fun triple(n: Int) = n * 3
```
Questo è l'abbreviazione di:
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
