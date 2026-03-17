Funkcja to blok kodu, który wykonuje określone zadanie i może być wielokrotnie używany w programie.
W Kotlinie funkcję definiuje się za pomocą słowa kluczowego `fun`, po którym następuje nazwa funkcji i nawiasy:
```kotlin
fun greet() {
    println("Hello!")
}
```
Aby wywołać (wykonać) funkcję, użyj jej nazwy z nawiasami:
```kotlin
greet() // prints Hello!
```
Funkcja, która nie zwraca wartości, niejawnie zwraca `Unit`.

---

Funkcje mogą zwracać wartość. Typ zwracany określa się po nawiasach za pomocą dwukropka:
```kotlin
fun getNumber(): Int {
    return 42
}
```
Słowo kluczowe `return` odsyła wartość do miejsca wywołania:
```kotlin
var result = getNumber()
println(result) // prints 42
```
Typ zwracany musi odpowiadać typowi zwracanej wartości.

---

Funkcje mogą przyjmować parametry, które są wartościami przekazywanymi podczas wywołania.
Parametry deklaruje się wewnątrz nawiasów z nazwą i typem:
```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}
```
Argumenty przekazuje się podczas wywołania funkcji:
```kotlin
greet("Alice") // prints Hello, Alice!
```
Parametry umożliwiają pisanie wielokrotnie używanego kodu, który działa z różnymi wartościami.

---

Kotlin obsługuje domyślne wartości parametrów. Jeśli wywołujący nie poda argumentu, używana jest wartość domyślna:
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
Wartości domyślne sprawiają, że parametry są opcjonalne, zmniejszając potrzebę przeciążania funkcji.

---

Gdy ciało funkcji składa się z jednego wyrażenia, można użyć składni pojedynczego wyrażenia z `=`:
```kotlin
fun square(n: Int): Int = n * n
```
Jest to bardziej zwięzłe niż forma z blokiem. Kotlin często może wywnioskować typ zwracany, więc można też napisać:
```kotlin
fun square(n: Int) = n * n
```
Funkcje z pojedynczym wyrażeniem to powszechny idiom Kotlina dla prostych obliczeń.

---

Funkcje mogą zwracać wartości `Boolean`, co jest przydatne do sprawdzania warunków:
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
Funkcja `Boolean` zwraca `true` lub `false`.

---

Funkcje mogą mieć wiele parametrów różnych typów:
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
Nazwane argumenty pozwalają przekazywać wartości w dowolnej kolejności, używając nazwy parametru:
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Podstawowa funkcja w Kotlinie używa słowa kluczowego `fun`, po którym następuje nazwa i nawiasy:
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

Aby zadeklarować typ zwracany funkcji, dodaj dwukropek i typ po nawiasach:
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

Parametr funkcji deklaruje się z nazwą, dwukropkiem i typem:
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

Funkcja z pojedynczym wyrażeniem używa `=` zamiast ciała blokowego:
```kotlin
fun triple(n: Int) = n * 3
```
Jest to skrót od:
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
