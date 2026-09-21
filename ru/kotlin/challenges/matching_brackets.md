---
language: kotlin
exerciseType: 1
difficulty: 3
title: Сбалансированные скобки
---

# --description--

Текст, в котором есть код, математика или разметка, полон скобок, и каждой открывающей скобке нужна закрывающая того же вида. Строка сбалансирована, когда её скобки образуют пары и вкладываются друг в друга, как слои луковицы: `{[()]}` сбалансирована, а `{[(])}` — нет, ведь круглая пара закрывается раньше квадратной пары, внутри которой она находится.

Здесь учитываются три пары: круглые `()`, квадратные `[]` и фигурные `{}`. Все остальные символы строки игнорируются. Закрывающая скобка должна закрывать последнюю из ещё открытых скобок, а к концу строки не должно остаться ни одной незакрытой скобки.

# --instructions--

Напишите функцию `isBalanced`, которая принимает строку и возвращает `true`, если все скобки в ней образуют пары и правильно вложены, и `false` в противном случае.

Примеры:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Пустая строка сбалансирована.
- Символы, не являющиеся скобками, игнорируются.
- Закрывающая скобка должна соответствовать последней из ещё открытых скобок.
- К концу строки не должно оставаться ни одной открытой скобки.

# --seed--

```kotlin
fun isBalanced(text: String): Boolean {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Пустая строка сбалансирована

```kotlin
    tryCatch(isBalanced("") == true)
```

Одна пара круглых скобок сбалансирована

```kotlin
    tryCatch(isBalanced("()") == true)
```

Три вида пар, вложенные друг в друга, сбалансированы

```kotlin
    tryCatch(isBalanced("{[()]}") == true)
```

Скобки вперемешку с другим текстом остаются сбалансированными

```kotlin
    tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Пары, стоящие друг за другом, сбалансированы

```kotlin
    tryCatch(isBalanced("()[]{}") == true)
```

Строка вовсе без скобок сбалансирована

```kotlin
    tryCatch(isBalanced("no brackets in here at all") == true)
```

Перекрёстная пара не сбалансирована

```kotlin
    tryCatch(isBalanced("{[(])}") == false)
```

Открывающая скобка, которая никогда не закрывается, не сбалансирована

```kotlin
    tryCatch(isBalanced("(") == false)
```

Закрывающая скобка раньше любой открывающей не сбалансирована

```kotlin
    tryCatch(isBalanced(")(") == false)
```

Перекрёстные пары в глубине строки не сбалансированы

```kotlin
    tryCatch(isBalanced("(([]{[}]))") == false)
```

Лишняя закрывающая скобка в конце строки не сбалансирована

```kotlin
    tryCatch(isBalanced("())") == false)
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun isBalanced(text: String): Boolean {
    val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')
    val stack = ArrayDeque<Char>()

    for (char in text) {
        if (char == '(' || char == '[' || char == '{') {
            stack.addLast(char)
        } else if (pairs.containsKey(char)) {
            if (stack.isEmpty() || stack.removeLast() != pairs[char]) {
                return false
            }
        }
    }

    return stack.isEmpty()
}
```
