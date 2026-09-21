---
language: kotlin
exerciseType: 1
difficulty: 3
title: Corchetes coincidentes
---

# --description--

El texto que contiene código, matemáticas o marcado está lleno de corchetes, y cada corchete de apertura necesita uno de cierre de la misma clase. Una cadena está equilibrada cuando sus corchetes se emparejan y se anidan como las capas de una cebolla: `{[()]}` está equilibrada, mientras que `{[(])}` no lo está, porque el par redondo se cierra antes que el par cuadrado dentro del cual se encuentra.

Aquí cuentan tres pares: paréntesis `()`, corchetes `[]` y llaves `{}`. Todos los demás caracteres de la cadena se ignoran. Un corchete de cierre debe cerrar el último corchete que se haya abierto y que aún siga abierto, y cuando la cadena termina no debe quedar ningún corchete abierto.

# --instructions--

Escribe una función `isBalanced` que tome una cadena y devuelva `true` cuando todos los corchetes que contiene estén emparejados y anidados correctamente, y `false` en caso contrario.

Ejemplos:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Una cadena vacía está equilibrada.
- Los caracteres que no son corchetes se ignoran.
- Un corchete de cierre debe corresponder al último corchete que se haya abierto y que aún siga abierto.
- No debe quedar ningún corchete abierto cuando la cadena termina.

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

Una cadena vacía está equilibrada

```kotlin
    tryCatch(isBalanced("") == true)
```

Un solo par de paréntesis está equilibrado

```kotlin
    tryCatch(isBalanced("()") == true)
```

Los tres tipos de pares anidados unos dentro de otros están equilibrados

```kotlin
    tryCatch(isBalanced("{[()]}") == true)
```

Los corchetes mezclados con otro texto siguen estando equilibrados

```kotlin
    tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Los pares colocados uno al lado del otro están equilibrados

```kotlin
    tryCatch(isBalanced("()[]{}") == true)
```

Una cadena sin ningún corchete está equilibrada

```kotlin
    tryCatch(isBalanced("no brackets in here at all") == true)
```

Un par cruzado no está equilibrado

```kotlin
    tryCatch(isBalanced("{[(])}") == false)
```

Un corchete de apertura que nunca se cierra no está equilibrado

```kotlin
    tryCatch(isBalanced("(") == false)
```

Un corchete de cierre antes de cualquier corchete de apertura no está equilibrado

```kotlin
    tryCatch(isBalanced(")(") == false)
```

Los pares cruzados en lo profundo de la cadena no están equilibrados

```kotlin
    tryCatch(isBalanced("(([]{[}]))") == false)
```

Un corchete de cierre que sobra al final no está equilibrado

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
