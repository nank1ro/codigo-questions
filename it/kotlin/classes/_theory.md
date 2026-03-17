Una **classe** è un modello per la creazione di oggetti. In Kotlin, si dichiara una classe con la parola chiave `class` seguita dal nome della classe.

Una classe può contenere **proprietà** (dati) e **metodi** (comportamento). Per dichiarare una proprietà direttamente nel costruttore, si aggiunge il prefisso `val` o `var`:

```kotlin
class Dog(val name: String)
```

Questo crea una classe `Dog` con una proprietà `name`. Si crea un'istanza chiamando la classe come una funzione:

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

Le classi possono avere più proprietà nel loro **costruttore primario**. Ogni proprietà è dichiarata con `val` (sola lettura) o `var` (mutabile) direttamente nell'elenco dei parametri del costruttore:

```kotlin
class Person(val name: String, var age: Int)
```

La parola chiave `val` rende `name` di sola lettura dopo la creazione, mentre `var` rende `age` mutabile — è possibile modificarla in seguito:

```kotlin
val p = Person("Alice", 30)
p.age = 31  // consentito perché age è var
```

---

Il **blocco `init`** viene eseguito immediatamente dopo il costruttore primario. Viene utilizzato per eseguire validazioni o logica di configurazione quando si crea un oggetto:

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "Radius must be positive" }
    }
}
```

È possibile anche inizializzare proprietà aggiuntive all'interno di `init`:

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

Le classi possono contenere **metodi** — funzioni che appartengono alla classe e operano sulle sue proprietà:

```kotlin
class Counter(var count: Int) {
    fun increment() {
        count++
    }
    fun value(): Int {
        return count
    }
}
```

I metodi vengono chiamati usando la notazione a punto su un'istanza:

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

Una **`data class`** è una classe speciale progettata per contenere dati. Kotlin genera automaticamente `equals()`, `hashCode()`, `toString()` e `copy()`:

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)            // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

La funzione `copy()` crea una nuova istanza con alcune proprietà modificate:

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
