`data class` to klasa, której zadaniem jest **przechowywanie danych**. Na podstawie właściwości zadeklarowanych w konstruktorze głównym kompilator generuje dla ciebie cztery składowe:

- `toString()`, czytelny tekst w postaci `ClassName(prop=value, ...)`
- `equals()` i `hashCode()`, dzięki czemu dwie instancje z tymi samymi danymi są uznawane za równe
- `copy()`, które buduje nową instancję, wykorzystując bieżące wartości

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()` pokazuje pełnię możliwości z **argumentami nazwanymi**: wskazujesz tylko te właściwości, które chcesz zmienić, a wszystkie pozostałe wartości zostają przeniesione.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

Oryginał nigdy nie jest modyfikowany: `copy()` zwraca całkowicie nowy obiekt.

---

Dla każdej właściwości z konstruktora głównego data class generuje też funkcję `componentN()`: `component1()` dla pierwszej właściwości, `component2()` dla drugiej i tak dalej.

Te funkcje napędzają **deklaracje destrukturyzujące**, w których rozpakowujesz obiekt na kilka zmiennych w jednej linii:

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

Kolejność zmiennych wynika z kolejności właściwości, a nie z ich nazw. Użyj `_`, aby pominąć tę, której nie potrzebujesz:

```kotlin
val (_, onlyY) = point
```

---

Wygenerowane `equals()` sprawia, że `==` jest porównaniem **strukturalnym**: dwie instancje są równe, gdy każda właściwość konstruktora głównego jest równa. Operator `===` działa inaczej, pyta, czy obie nazwy wskazują **dokładnie ten sam obiekt** w pamięci.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, te same dane
println(a === b) // false, dwa różne obiekty
println(a === a) // true
```

Ponieważ `hashCode()` jest generowane razem z `equals()`, instancje data class zachowują się poprawnie także wewnątrz `Set` lub jako klucze `Map`: duplikaty się scalają.

```kotlin
println(setOf(a, b).size) // 1
```

Zwykła klasa nie generuje nic z tego, więc dla niej `==` sprowadza się do tożsamości.

---

Wygenerowane składowe biorą pod uwagę tylko właściwości zadeklarowane w **konstruktorze głównym**. Właściwość zadeklarowana w **ciele** klasy jest zwykłą właściwością: nie należy do `toString()`, `equals()`, `hashCode()` ani `copy()`.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

Łatwo o tym zapomnieć, więc w konstruktorze głównym umieszczaj wszystko, co identyfikuje obiekt, a stan pochodny lub tymczasowy trzymaj w ciele klasy.

---

Klasa `sealed` opisuje **zamknięty** zbiór wariantów: dozwolone są tylko podklasy napisane w tym samym pakiecie i module, więc kompilator zna je wszystkie.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

Korzyścią jest **wyczerpujące `when`**: gdy rozgałęziasz się po typie sealed i pokryjesz każdą podklasę, możesz pominąć gałąź `else`. Jeśli później dodasz nową podklasę, kompilator wskaże każde `when`, którego zapomniałeś zaktualizować, zamiast po cichu wejść w `else`.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

Po `is Circle` wartość podlega smart castowi, więc `shape.radius` jest dostępne w tej gałęzi bez żadnego ręcznego rzutowania.
