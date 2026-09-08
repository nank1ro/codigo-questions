**Перечисление** (или *enum*) определяет общий тип для группы связанных значений, чтобы вы могли безопасно работать с этими значениями с точки зрения типов.
В Kotlin вы объявляете его с помощью ключевых слов `enum class`, перечисляя его **записи** (entries) через запятую:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
По соглашению имена записей пишутся заглавными буквами. Каждая запись — это значение типа enum, и к ней обращаются через имя класса:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
Классы enum должны объявляться на верхнем уровне файла (или внутри другого класса), но никогда внутри функции.

---

У каждой записи enum есть два встроенных свойства:

- `name` — имя записи в виде `String`
- `ordinal` — её позиция в объявлении, начиная с `0`

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

Записи enum сравниваются с помощью `==`:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

Выражение `when` — естественный способ ветвления по enum. Если оно охватывает **все** записи, оно считается *исчерпывающим* (exhaustive) и не требует ветки `else`:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
Если вы забудете какую-то запись, компилятор сообщит об ошибке, вместо того чтобы допустить баг до этапа выполнения.

---

Класс enum может иметь **конструктор**, как и обычный класс. Каждая запись при этом передаёт свои собственные аргументы, а значения сохраняются в свойствах:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
Свойства конструктора обычно объявляют с помощью `val`, так как данные записи не должны изменяться.

---

Классы enum также могут объявлять **методы**. Список записей нужно закрыть точкой с запятой `;` перед любыми объявлениями членов класса:
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
Внутри метода вы можете обращаться к свойствам записи, а также к `name` и `ordinal`.

---

Каждый класс enum предоставляет свойство `entries`: список всех его записей в порядке объявления. Это удобно для перебора:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
Так как `entries` — это список, он также поддерживает `size` и индексацию, например `Direction.entries[0]` — это `NORTH`.

В старом коде вместо этого используется функция `values()`, возвращающая массив; начиная с Kotlin 1.9 рекомендуется использовать `entries`.

---

Чтобы получить запись обратно из `String`, используйте функцию `valueOf`. Она ищет запись, чьё `name` совпадает точно:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
Сопоставление чувствительно к регистру: `Direction.valueOf("east")` выбрасывает `IllegalArgumentException`, потому что ни одна запись не имеет такого имени.

---

Класс enum может объявлять **абстрактный метод** и позволять каждой записи предоставлять свою собственную реализацию в теле, заключённом в фигурные скобки:
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
Каждая запись ведёт себя по-своему, оставаясь при этом тем же типом с той же сигнатурой метода.

---

**Интерфейс** объявляет методы без тела; любой тип, реализующий его, обязан их предоставить:
```kotlin
interface Greeter {
    fun greet(): String
}
```
Классы enum могут реализовывать интерфейсы. Интерфейс указывается после двоеточия, а каждая реализация помечается словом `override`. Внутри тела enum текущая запись — это `this`, и на другие записи можно ссылаться без имени класса:
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
