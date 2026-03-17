**Klasa** jest szablonem do tworzenia obiektów. W Kotlinie deklarujesz klasę za pomocą słowa kluczowego `class`, po którym następuje nazwa klasy.

Klasa może przechowywać **właściwości** (dane) i **metody** (zachowanie). Aby zadeklarować właściwość bezpośrednio w konstruktorze, poprzedź ją słowem `val` lub `var`:

```kotlin
class Dog(val name: String)
```

Tworzy to klasę `Dog` z właściwością `name`. Instancję tworzy się, wywołując klasę jak funkcję:

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

Klasy mogą mieć wiele właściwości w swoim **konstruktorze głównym**. Każda właściwość jest deklarowana za pomocą `val` (tylko do odczytu) lub `var` (modyfikowalna) bezpośrednio na liście parametrów konstruktora:

```kotlin
class Person(val name: String, var age: Int)
```

Słowo kluczowe `val` sprawia, że `name` jest tylko do odczytu po utworzeniu, natomiast `var` sprawia, że `age` jest modyfikowalne — można je później zmieniać:

```kotlin
val p = Person("Alice", 30)
p.age = 31  // dozwolone, ponieważ age jest var
```

---

**Blok `init`** wykonuje się natychmiast po konstruktorze głównym. Służy do przeprowadzania walidacji lub logiki inicjalizacyjnej podczas tworzenia obiektu:

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "Promień musi być dodatni" }
    }
}
```

Możesz również inicjalizować dodatkowe właściwości wewnątrz `init`:

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

Klasy mogą zawierać **metody** — funkcje należące do klasy, które operują na jej właściwościach:

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

Metody są wywoływane przy użyciu notacji kropkowej na instancji:

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

**`data class`** to specjalna klasa przeznaczona do przechowywania danych. Kotlin automatycznie generuje dla ciebie `equals()`, `hashCode()`, `toString()` i `copy()`:

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)           // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

Funkcja `copy()` tworzy nową instancję z niektórymi zmienionymi właściwościami:

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
