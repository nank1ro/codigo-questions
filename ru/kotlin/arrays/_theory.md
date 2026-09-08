**Массив** хранит фиксированное количество значений одного типа под одним именем переменной.
Вы создаёте его с помощью `arrayOf`, читаете элемент с помощью квадратных скобок и **индекса**, начинающегося с `0`, а количество элементов получаете с помощью `size`:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
Последний элемент находится по индексу `size - 1`.

---

`arrayOf(1, 2, 3)` создаёт `Array<Int>`, где каждый элемент — это упакованный (boxed) объект.
Для примитивных типов Kotlin предлагает специальные, более эффективные типы, такие как `IntArray`, `DoubleArray` и `BooleanArray`:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
Вы также можете построить массив заданного размера с помощью лямбды **инициализации**, которая получает каждый индекс, или заполненный нулями `IntArray`:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

У каждого массива есть два полезных свойства для работы с индексами:
- `indices` — диапазон допустимых индексов, от `0` до последнего
- `lastIndex` — индекс последнего элемента, то есть `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

Даже если массив объявлен с `val`, его **элементы** можно заменить, присвоив значение по индексу:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
Чтобы посетить каждый элемент, можно использовать цикл `for` или `forEach`:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
Обратите внимание, что `n` и `it` — это копии значений только для чтения, им нельзя ничего присвоить, поэтому для изменения элементов нужен их индекс.

---

Чтобы проверить, содержит ли массив значение, используйте `in` или `contains`, оба возвращают `Boolean`.
`indexOf` возвращает индекс первого вхождения, или `-1`, если значения нет:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

Прямой вывод массива не показывает его элементы, он выводит что-то вроде `[Ljava.lang.String;@1b6d3586`.
Используйте `joinToString`, чтобы получить читаемую строку, при желании с собственным разделителем (по умолчанию `", "`), или `contentToString`, чтобы получить элементы в квадратных скобках:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

Массивы можно сортировать **на месте** или копировать в новую отсортированную коллекцию:
- `sort()` и `sortDescending()` переупорядочивают сам массив и ничего не возвращают
- `reverse()` меняет порядок самого массива на обратный
- `sorted()`, `sortedDescending()` и `reversed()` оставляют массив нетронутым и возвращают новый `List`
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

Числовые массивы имеют агрегатные функции:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` и `min()` выбрасывают исключение на пустом массиве, используйте `maxOrNull()` и `minOrNull()`, если массив может быть пустым.

---

Главное отличие массива от `MutableList` в том, что массив имеет **фиксированный размер**: после создания вы можете заменять его элементы, но никогда не можете добавить или удалить элемент, функции `add` не существует.
Выражения вроде `nums + 4` не увеличивают `nums`, они создают совершенно новый массив:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
Предпочитайте `MutableList`, когда количество элементов меняется со временем, и массив, когда оно известно заранее или когда нужна производительность примитивов.

---

Массивы поддерживают те же функции преобразования, что и списки. `filter` оставляет элементы, удовлетворяющие условию, а `map` преобразует каждый элемент.
Обе возвращают новый `List`, а не массив:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
Поскольку результат — список, вывод его напрямую показывает его элементы.

---

Когда во время цикла вам нужен и индекс, и значение, используйте `withIndex()` и деструктурируйте каждую пару, либо `forEachIndexed`:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

Массивы и списки легко конвертируются друг в друга:
- `toList()` и `toMutableList()` копируют массив в список
- `toTypedArray()` копирует список в `Array<T>`
- `toIntArray()` копирует список `Int` в `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
Каждое преобразование создаёт **копию**, поэтому изменение результата не влияет на оригинал.

---

В отличие от списков, два массива с одинаковыми элементами **не** равны при `==`: массивы сравниваются по ссылке, поэтому `==` даёт `true` только для одного и того же объекта массива.
Чтобы сравнить содержимое, используйте `contentEquals`:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

Поскольку массивы имеют фиксированный размер, чтобы взять часть массива, нужно создать новый массив:
- `copyOf()` копирует весь массив, `copyOf(n)` копирует первые `n` элементов
- `copyOfRange(from, to)` копирует элементы от индекса `from` до `to` **не включая**
- `sliceArray(range)` копирует элементы по индексам диапазона, включая оба конца
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
