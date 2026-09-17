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

---

Czasem potrzebujesz dokładnie **jednej** instancji czegoś: loggera, rejestru, konfiguracji aplikacji. Zamiana `class` na `object` deklaruje ten singleton za ciebie:

```kotlin
object Registry {
    var size = 0
    fun add() {
        size++
    }
}

Registry.add()
println(Registry.size) // 1
```

Instancja powstaje przy pierwszym użyciu, a korzystasz z samej nazwy: nie ma wywołania `Registry()` ani konstruktora. `object` może zawierać właściwości, metody, bloki `init`, może też implementować interfejsy lub dziedziczyć po klasie.

---

`companion object` to singleton należący do klasy. Poza stałymi jego naturalnym zadaniem jest przechowywanie **funkcji fabrykujących**: funkcji, które sprawdzają lub przekształcają dane wejściowe przed zbudowaniem instancji i mogą zwrócić `null`, gdy dane wejściowe nie mają sensu.

Oznaczenie konstruktora jako `private` zmusza każdego wywołującego do przejścia przez fabrykę:

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

Companion wywołuje się na nazwie klasy, `Age.of(...)`, i ma dostęp do prywatnego konstruktora, ponieważ znajduje się wewnątrz klasy.

---

`interface` wymienia, co dany typ potrafi. Jego składowe są domyślnie abstrakcyjne, ale interfejs może też dostarczyć **domyślną implementację**, czyli ciało, które każda implementująca klasa dziedziczy za darmo i może nadpisać:

```kotlin
interface Greeter {
    val name: String              // abstrakcyjna, klasa musi ją dostarczyć
    fun greet(): String = "Hi, $name"  // domyślna implementacja
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

Interfejs nie może przechowywać stanu (nie ma pól zaplecza), więc właściwość abstrakcyjną musi zaimplementować klasa, zwykle przez `override val` w konstruktorze. W przeciwieństwie do klasy, typ może implementować dowolnie wiele interfejsów.

---

Klasa `abstract` plasuje się między interfejsem a zwykłą klasą: nie można jej instancjonować i łączy składowe **abstrakcyjne**, które nie mają ciała i muszą zostać nadpisane, ze składowymi konkretnymi, które podklasy dziedziczą bez zmian.

```kotlin
abstract class Vehicle(val name: String) {
    abstract fun wheels(): Int
    fun describe(): String = "$name has ${wheels()} wheels"
}

class Bike(name: String) : Vehicle(name) {
    override fun wheels(): Int = 2
}

println(Bike("BMX").describe()) // BMX has 2 wheels
```

W przeciwieństwie do interfejsu klasa abstrakcyjna ma konstruktor i może przechowywać stan we właściwościach, dlatego podklasa przekazuje `name` w górę przez `: Vehicle(name)`. Klasa może dziedziczyć tylko po jednej klasie, więc sięgaj po klasę abstrakcyjną, gdy podklasy dzielą dane, a po interfejs, gdy dzielą tylko zachowanie. Składowe abstrakcyjne można nadpisywać bez dodawania `open`.

---

Klasa zadeklarowana wewnątrz innej klasy jest domyślnie **zagnieżdżona** (nested). Nic nie wie o instancji zewnętrznej, a budujesz ją od nazwy klasy zewnętrznej:

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

Dodaj słowo kluczowe `inner`, a sytuacja się zmienia: klasa `inner` niesie referencję do instancji zewnętrznej, więc może czytać jej właściwości, i budujesz ją **z instancji**:

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

Wewnątrz klasy `inner` `this` oznacza obiekt wewnętrzny; użyj `this@Counter`, gdy potrzebujesz wyraźnie tego zewnętrznego.

---

Elementy tego tematu zwykle się łączą: `enum class`, której stałe niosą własne właściwości, modeluje ustalony zbiór etykiet, a `data class` przenosi towarzyszące im dane.

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
