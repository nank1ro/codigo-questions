**Enumeracja** (lub *enum*) definiuje wspólny typ dla grupy powiązanych wartości, dzięki czemu możesz operować na tych wartościach w sposób bezpieczny pod względem typów.
W Kotlinie deklarujesz ją za pomocą słów kluczowych `enum class`, wypisując jej **wartości** (entries) oddzielone przecinkami:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
Zgodnie z konwencją nazwy wartości pisze się wielkimi literami. Każda wartość jest instancją typu enum i jest dostępna poprzez nazwę klasy:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
Klasy enum muszą być zadeklarowane na najwyższym poziomie pliku (lub wewnątrz innej klasy), nigdy wewnątrz funkcji.

---

Każda wartość enum ma dwie wbudowane właściwości:

- `name` to nazwa wartości jako `String`
- `ordinal` to jej pozycja w deklaracji, licząc od `0`

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

Wartości enum porównuje się za pomocą `==`:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

Wyrażenie `when` to naturalny sposób rozgałęziania po enumie. Gdy obejmuje **wszystkie** wartości, jest *wyczerpujące* (exhaustive) i nie potrzebuje gałęzi `else`:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
Jeśli zapomnisz o jakiejś wartości, kompilator zgłosi błąd, zamiast pozwolić, by błąd dotarł do środowiska uruchomieniowego.

---

Klasa enum może mieć **konstruktor**, tak jak zwykła klasa. Każda wartość przekazuje wtedy swoje własne argumenty, a wartości są przechowywane we właściwościach:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
Właściwości konstruktora zwykle deklaruje się za pomocą `val`, ponieważ dane wartości nie powinny się zmieniać.

---

Klasy enum mogą też deklarować **metody**. Lista wartości musi zostać zakończona średnikiem `;` przed jakąkolwiek deklaracją składowej:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2);

    fun hasMoons(): Boolean {
        return moons > 0
    }
}
println(Planet.EARTH.hasMoons()) // true
```
Wewnątrz metody masz dostęp do właściwości wartości, a także do `name` i `ordinal`.

---

Każda klasa enum udostępnia właściwość `entries`: listę wszystkich jej wartości w kolejności deklaracji. Jest to przydatne przy iteracji:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
Ponieważ `entries` jest listą, obsługuje też `size` oraz indeksowanie, np. `Direction.entries[0]` to `NORTH`.

Starszy kod używa zamiast tego funkcji `values()`, która zwraca tablicę; `entries` jest zalecanym wyborem od Kotlina 1.9.

---

Aby przejść od `String` z powrotem do wartości enum, użyj funkcji `valueOf`. Wyszukuje ona wartość, której `name` dokładnie pasuje:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
Dopasowanie rozróżnia wielkość liter: `Direction.valueOf("east")` rzuca `IllegalArgumentException`, ponieważ żadna wartość nie ma takiej nazwy.

---

Klasa enum może deklarować **metodę abstrakcyjną** i pozwolić każdej wartości dostarczyć własną implementację w ciele ujętym w klamry:
```kotlin
enum class Operation {
    ADD {
        override fun apply(a: Int, b: Int): Int = a + b
    },
    SUBTRACT {
        override fun apply(a: Int, b: Int): Int = a - b
    };

    abstract fun apply(a: Int, b: Int): Int
}
println(Operation.ADD.apply(2, 3)) // 5
```
Każda wartość zachowuje się inaczej, wciąż jednak dzieląc ten sam typ i sygnaturę metody.

---

**Interfejs** deklaruje metody bez ciała; każdy typ, który go implementuje, musi je dostarczyć:
```kotlin
interface Greeter {
    fun greet(): String
}
```
Klasy enum mogą implementować interfejsy. Interfejs wymieniasz po dwukropku, a każdą implementację oznaczasz słowem `override`. Wewnątrz ciała enuma bieżąca wartość to `this`, a inne wartości można przywoływać bez nazwy klasy:
```kotlin
enum class Language : Greeter {
    ENGLISH, ITALIAN;

    override fun greet(): String = when (this) {
        ENGLISH -> "Hello"
        ITALIAN -> "Ciao"
    }
}
println(Language.ITALIAN.greet()) // Ciao
```
