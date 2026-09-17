`String` — это последовательность символов, записанная между двойными кавычками.
Свойство `length` показывает, сколько символов содержит строка, включая пробелы:
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

Каждый символ строки имеет **индекс**, начиная с `0` для первого.
Один символ можно прочитать с помощью квадратных скобок или функции `get`, результатом будет `Char`:
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
Последний символ находится по индексу `length - 1`. Функции `first()` и `last()` — удобные сокращения:
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` возвращает копию строки, в которой все буквы записаны заглавными, `lowercase()` делает обратное.
Исходная строка не изменяется:
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

Чтобы проверить, содержит ли строка определённый фрагмент текста, используются `contains`, `startsWith` и `endsWith`. Все они возвращают `Boolean`:
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
Проверка чувствительна к регистру, если только вы не передадите `ignoreCase = true`:
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` возвращает индекс, по которому фрагмент текста встречается **впервые**, или `-1`, если он не встречается вовсе.
`lastIndexOf` ищет с конца:
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` извлекает часть строки. С двумя аргументами она берёт символы от начального индекса до конечного индекса, **не включая** его.
С одним аргументом она берёт всё от этого индекса до конца:
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
Сочетание `indexOf` и `substring` позволяет вырезать строку вокруг маркера:
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` разбивает строку на `List` частей вокруг разделителя, а `joinToString`, наоборот, склеивает элементы коллекции в одну строку с выбранным вами разделителем:
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

Поскольку `split` возвращает `List`, вы можете перебирать её элементы, как и любой другой список:
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// выводит a, затем b
```

---

Пользовательский ввод часто содержит лишние пробелы. `trim()` возвращает строку без пробелов в начале и в конце, `trimStart()` и `trimEnd()` убирают их только с одной стороны:
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` равно `true` для `""`, а `isBlank()` также равно `true` для строк, состоящих только из пробелов:
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` возвращает копию строки, в которой **каждое** вхождение `old` заменено на `new`:
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` возвращает строку, повторённую `n` раз:
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` добавляет `char` в начало, пока строка не достигнет `width` символов; `padEnd` добавляет их в конец.
Если строка уже достаточно длинная, она возвращается без изменений:
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
Числа — это не строки: сначала вызовите `toString()`, как в `42.toString().padStart(4, '0')`.

---

Две строки равны, когда они содержат одинаковые символы в одинаковом порядке. В Kotlin `==` сравнивает **содержимое** строк, поэтому это обычный способ их сравнения.
`equals` делает то же самое, но также принимает `ignoreCase = true`, чтобы игнорировать разницу между заглавными и строчными буквами:
```kotlin
println("hello" == "hello")                          // true
println("Hello" == "hello")                          // false
println("Hello".equals("hello", ignoreCase = true))  // true
```
`===` проверяет, указывают ли две переменные на один и тот же объект в памяти, что почти никогда не нужно для строк.

---

`reversed()` возвращает строку с символами в обратном порядке:
```kotlin
println("stressed".reversed()) // desserts
```
Слово, которое читается одинаково в обоих направлениях, например `"level"`, называется **палиндромом**.

---

Строки **неизменяемы**: после создания они никогда не меняются. Каждая функция, которую вы видели до сих пор, например `uppercase()` или `replace()`, возвращает **новую** строку и не трогает исходную.
Чтобы сохранить результат, его нужно записать, например переприсвоив `var`:
```kotlin
var name = "kotlin"
name.uppercase()        // результат отбрасывается
println(name)           // kotlin
name = name.uppercase() // результат сохраняется
println(name)           // KOTLIN
```

---

Построение длинной строки по частям с помощью `+` создаёт новую строку на каждом шаге. `StringBuilder` — это изменяемый текстовый буфер, созданный именно для этой задачи: `append` добавляет текст в конец (и возвращает сам builder, поэтому вызовы можно объединять в цепочку), а `toString()` даёт итоговую `String`:
```kotlin
val sb = StringBuilder()
sb.append("Hello")
sb.append(", ").append("world")
println(sb.toString()) // Hello, world
```
`append` принимает строки, символы и числа.
