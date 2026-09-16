---
language: kotlin
exerciseType: 1
difficulty: 2
title: Cifrado César
---

# --description--

Julio César protegía sus cartas privadas con uno de los trucos más antiguos de la criptografía: reemplazaba cada letra de un mensaje por la letra que está un número fijo de posiciones más adelante en el alfabeto. Con un desplazamiento de 3, la `a` se convierte en `d`, la `b` se convierte en `e` y la `c` se convierte en `f`.

El alfabeto se comporta como un círculo, así que las letras del final vuelven al principio: con un desplazamiento de 3, la `x` se convierte en `a`, la `y` se convierte en `b` y la `z` se convierte en `c`.

Todo lo que no sea una letra, como un espacio, una coma, un signo de exclamación o un dígito, atraviesa el cifrado sin modificarse.

# --instructions--

Escribe una función `caesarCipher` que reciba un mensaje `text` y un número entero `shift`, y devuelva el mensaje codificado.

Ejemplos:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- El mensaje siempre está en minúsculas, así que nunca tienes que lidiar con letras mayúsculas.
- Los caracteres que no son letras conservan su lugar y su valor.
- El desplazamiento nunca es negativo. Un desplazamiento de `0` deja el mensaje sin cambios, y lo mismo ocurre con un desplazamiento de `26`.

# --seed--

```kotlin
fun caesarCipher(text: String, shift: Int): String {
    
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

Un desplazamiento de 3 convierte "hello" en "khoor"

```kotlin
    tryCatch(caesarCipher("hello", 3) == "khoor")
```

El final del alfabeto da la vuelta, así que "xyz" se convierte en "abc"

```kotlin
    tryCatch(caesarCipher("xyz", 3) == "abc")
```

Un desplazamiento de 0 deja el mensaje sin cambios

```kotlin
    tryCatch(caesarCipher("abc", 0) == "abc")
```

Un desplazamiento de 26 es una vuelta completa al alfabeto, así que el mensaje queda sin cambios

```kotlin
    tryCatch(caesarCipher("abc", 26) == "abc")
```

Los signos de puntuación y los espacios pasan sin cambios

```kotlin
    tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

Un mensaje vacío sigue estando vacío

```kotlin
    tryCatch(caesarCipher("", 4) == "")
```

Los espacios entre letras sueltas se conservan

```kotlin
    tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Los dígitos no se desplazan, ni siquiera con un desplazamiento de 25

```kotlin
    tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

Un desplazamiento de 13 codifica una frase completa

```kotlin
    tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
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
fun caesarCipher(text: String, shift: Int): String {
    val result = StringBuilder()

    for (char in text) {
        if (char in 'a'..'z') {
            result.append('a' + (char - 'a' + shift) % 26)
        } else {
            result.append(char)
        }
    }

    return result.toString()
}
```
