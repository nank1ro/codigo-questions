Иногда значение просто отсутствует: пользователь без отчества, поиск, который ничего не находит, текст, который не удаётся превратить в число.
Kotlin представляет отсутствующее значение с помощью `null`, но обычная переменная никогда не может его хранить. Каждый тип по умолчанию **не допускает null**:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
Чтобы разрешить отсутствующее значение, вы объявляете тип, **допускающий null**, добавляя вопросительный знак `?` после типа.
Тип `String?` хранит либо `String`, либо `null`:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` и `String?` — это два разных типа: `String` никогда не отсутствует, `String?` — может.

---

Разница между `String` и `String?` проверяется **компилятором**, а не во время выполнения.
Присваивание `null` типу, не допускающему null, или передача значения, допускающего null, туда, где ожидается значение, не допускающее null, — это ошибка компиляции, поэтому программа даже не запускается:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
Так Kotlin избегает падений с «null pointer», распространённых в других языках: значение может отсутствовать только там, где вы явно объявили это с помощью `?`.

---

Знак `?` работает везде, где записывается тип: функция может принимать параметр, допускающий null, и может возвращать значение, допускающее null.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
Вы не можете вызвать метод напрямую на значении, допускающем null, потому что оно может быть `null`.
Оператор **безопасного вызова** `?.` вызывает метод только тогда, когда значение не `null`; иначе всё выражение равно `null`:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
Результат безопасного вызова всегда допускает null: `word?.length` — это `Int?`, а не `Int`.

---

Очень часто всё, что вам нужно от значения, допускающего null, — это само значение или значение по умолчанию.
**Элвис-оператор** `?:` делает именно это: он возвращает левую часть, когда она не `null`, иначе — значение справа:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
Поскольку правая часть используется только тогда, когда левая равна `null`, результат не допускает null, когда его не допускает значение по умолчанию.
`?:` хорошо сочетается с `?.`, превращая безопасный вызов обратно в обычное значение:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

Безопасные вызовы можно **объединять в цепочки**: как только одно звено равно `null`, остальная часть цепочки пропускается и всё выражение становится `null`.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
Цепочка, заканчивающаяся на `?:`, даёт результат, не допускающий null, в одну строку:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

Цепочки безопасных вызовов отлично проявляют себя с вложенными объектами, где любой уровень может отсутствовать:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
Каждый `?.` защищает следующий шаг, а финальный `?:` подставляет значение по умолчанию.

---

Оператор **не-null утверждения** `!!` превращает значение, допускающее null, в значение, которое его не допускает, сообщая компилятору: «Я уверен, что это не `null`»:
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
Если вы ошиблись и значение равно `null`, программа падает во время выполнения с `NullPointerException` — той самой ошибкой, для предотвращения которой был создан Kotlin:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
Используйте `!!` только тогда, когда значение действительно не может быть `null`; во всех остальных случаях предпочитайте `?.`, `?:` и проверки на null.

---

Когда вы проверяете значение на `null` с помощью `if`, компилятор это запоминает: внутри ветки, где известно, что значение не равно `null`, происходит **умное приведение** к типу, не допускающему null, и вы можете использовать значение напрямую, без `?.` и `!!`:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
То же самое происходит и после раннего выхода:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
Умные приведения работают с переменными `val` и параметрами функций, значение которых не может измениться между проверкой и использованием.

---

`let` выполняет блок кода со значением, на котором он вызван; внутри блока это значение доступно как `it`.
В сочетании с безопасным вызовом `?.let` выполняет блок **только** когда значение не `null`, и внутри блока `it` не допускает null:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
Это компактная альтернатива `if (x != null) { ... }`, когда значение нужно только внутри блока.

---

`let` также **возвращает** значение последнего выражения в своём блоке, поэтому `?.let` может преобразовать значение, допускающее null, а `?:` может подставить значение по умолчанию, когда оно равно `null`:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
Когда `price` равен `null`, блок `let` пропускается, выражение равно `null`, и Элвис-оператор возвращает `"free"`.

---

Коллекции тоже могут хранить элементы, допускающие null: `List<Int?>` может содержать элементы `null`, а `List<Int>` — никогда.
`filterNotNull()` возвращает новый список без элементов `null`, и тип его элементов становится не допускающим null, поэтому элементами можно пользоваться свободно:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

Многие стандартные функции возвращают `null` вместо того, чтобы падать. `toIntOrNull()` преобразует строку в `Int` или возвращает `null`, когда текст не является целым числом:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` преобразует каждый элемент, как `map`, но отбрасывает результаты, равные `null`:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

Иногда свойству нельзя задать значение при создании объекта, но вы знаете, что оно будет установлено до использования.
Вместо того чтобы делать его допускающим null, пометьте его `lateinit`: тип остаётся не допускающим null, и `?.` не нужен при чтении:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
У `lateinit` есть правила: он работает только со свойствами `var`, только с типами, не допускающими null, и не работает с примитивными типами вроде `Int` или `Boolean`.
Чтение свойства `lateinit` до его присваивания бросает `UninitializedPropertyAccessException`; сначала можно проверить его с помощью `::player.isInitialized`.

---

Когда `null` означает, что вызывающий допустил ошибку, завершайтесь как можно раньше с помощью `requireNotNull`.
Он возвращает значение как не допускающее null, когда оно присутствует, и бросает `IllegalArgumentException`, когда оно равно `null`, с необязательным сообщением:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
После этого вызова компилятор также выполняет умное приведение самого `name` к `String`, поэтому `name.length` разрешён начиная с этой строки.
В отличие от `!!`, ошибка несёт понятное сообщение и указывает, что *аргумент* был неверным.

---

Функцию-расширение можно объявить для **получателя, допускающего null**, поэтому её можно вызывать даже на значении `null`. Внутри `this` допускает null и должен быть проверен:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
Обратите внимание, что `?.` в месте вызова не нужен: сама функция обрабатывает случай `null`.
Стандартная библиотека использует этот приём в `isNullOrEmpty()` и `orEmpty()`, которые безопасно вызывать на любом `String?`.

---

Правая часть `?:` может быть любым выражением, включая `return`. Это даёт компактный способ выйти из функции, как только значение отсутствует:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
Все инструменты, которые вы видели, хорошо сочетаются: параметры и возвращаемые типы, допускающие null, описывают *где* значение может отсутствовать, а `?.`, `?:`, `let`, умные приведения и `toIntOrNull` обрабатывают это, не допуская падения.
