Una `data class` è una classe il cui compito è **contenere dati**. Dalle proprietà che dichiari nel costruttore primario il compilatore genera per te quattro membri:

- `toString()`, un testo leggibile nella forma `ClassName(prop=value, ...)`
- `equals()` e `hashCode()`, così due istanze con gli stessi dati risultano uguali
- `copy()`, che costruisce una nuova istanza riutilizzando i valori attuali

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()` dà il meglio di sé con gli **argomenti con nome**: indichi solo le proprietà che vuoi cambiare, e ogni altro valore viene riportato.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

L'originale non viene mai modificato: `copy()` restituisce un oggetto del tutto nuovo.

---

Per ogni proprietà del costruttore primario una data class genera anche una funzione `componentN()`: `component1()` per la prima proprietà, `component2()` per la seconda, e così via.

Queste funzioni alimentano le **dichiarazioni di destrutturazione**, con cui scomponi un oggetto in più variabili in una sola riga:

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

L'ordine delle variabili segue l'ordine delle proprietà, non i loro nomi. Usa `_` per saltare quella che non ti serve:

```kotlin
val (_, onlyY) = point
```

---

L'`equals()` generato rende `==` un confronto **strutturale**: due istanze sono uguali quando ogni proprietà del costruttore primario è uguale. L'operatore `===` è diverso, chiede se entrambi i nomi puntano **allo stesso identico oggetto** in memoria.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, same data
println(a === b) // false, two different objects
println(a === a) // true
```

Poiché `hashCode()` viene generato insieme a `equals()`, le istanze di una data class si comportano correttamente anche dentro un `Set` o come chiavi di una `Map`: i duplicati collassano.

```kotlin
println(setOf(a, b).size) // 1
```

Una classe normale non genera nulla di tutto questo, quindi per essa `==` ricade sull'identità.

---

I membri generati considerano solo le proprietà dichiarate nel **costruttore primario**. Una proprietà dichiarata nel **corpo** della classe è una proprietà normale: non fa parte di `toString()`, `equals()`, `hashCode()` o `copy()`.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

È facile dimenticarsene, quindi metti nel costruttore primario tutto ciò che identifica l'oggetto, e tieni nel corpo lo stato derivato o temporaneo.

---

Una classe `sealed` descrive un insieme **chiuso** di alternative: sono ammesse solo le sottoclassi scritte nello stesso package e modulo, così il compilatore le conosce tutte.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

Il vantaggio è il **`when` esaustivo**: quando ramifichi su un tipo sealed e copri ogni sottoclasse, puoi omettere il ramo `else`. Se più avanti aggiungi una nuova sottoclasse, il compilatore segnala ogni `when` che hai dimenticato di aggiornare, invece di prendere silenziosamente l'`else`.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

Dopo `is Circle` il valore viene sottoposto a smart cast, quindi `shape.radius` è disponibile dentro quel ramo senza alcun cast manuale.
