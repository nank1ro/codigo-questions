---
language: kotlin
exerciseType: 1
difficulty: 2
title: Checksum de Luhn
---

# --description--

O algoritmo de Luhn é um checksum simples usado para validar números de identificação, como números de cartão de crédito.

Antes de verificar um número, remova todos os espaços da string. A string só é válida se o que restar tiver mais de um caractere e se a string original contiver nada além de dígitos e espaços.

Para fazer a verificação, comece pelo dígito mais à direita e avance para a esquerda, dobrando cada segundo dígito. Quando a duplicação produzir um número maior que 9, subtraia 9 dele. Em seguida, some todos os dígitos: o número só é válido se a soma for divisível por 10.

Por exemplo, `"059"` resulta em `0`, depois `5` dobrado é `10`, que se torna `1`, e depois `9`. A soma deles é `10`, que é divisível por 10, então o número é válido.

# --instructions--

Escreva uma função `isValid` que recebe uma string e retorna `true` quando o número é válido, `false` caso contrário.

- `"4539 3195 0343 6467"` passa no checksum, então o resultado é `true`.
- `"8273 1232 7352 0569"` falha no checksum, então o resultado é `false`.
- `"0"` tem apenas um caractere, então o resultado é `false`.
- `"055-444-285"` contém um caractere que não é um dígito nem um espaço, então o resultado é `false`.

Exemplo de chamada de função:
```kotlin
println(isValid("095 245 88"))
// imprime true
```

# --seed--

```kotlin
fun isValid(value: String): Boolean {
    
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

Um único dígito não é válido.

```kotlin
    tryCatch(isValid("0") == false)
```

Um único dígito com um espaço à esquerda não é válido.

```kotlin
    tryCatch(isValid(" 0") == false)
```

O número `"059"` é válido.

```kotlin
    tryCatch(isValid("059") == true)
```

O número `"59"` é válido.

```kotlin
    tryCatch(isValid("59") == true)
```

O número `"055 444 285"` é válido.

```kotlin
    tryCatch(isValid("055 444 285") == true)
```

O número `"055 444 286"` não é válido.

```kotlin
    tryCatch(isValid("055 444 286") == false)
```

O número `"8273 1232 7352 0569"` não é válido.

```kotlin
    tryCatch(isValid("8273 1232 7352 0569") == false)
```

O número `"4539 3195 0343 6467"` é válido.

```kotlin
    tryCatch(isValid("4539 3195 0343 6467") == true)
```

O número `"1 2345 6789 1234 5678 9012"` não é válido.

```kotlin
    tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

O número `"095 245 88"` é válido.

```kotlin
    tryCatch(isValid("095 245 88") == true)
```

Uma letra torna o número inválido.

```kotlin
    tryCatch(isValid("055a 444 285") == false)
```

Travessões tornam o número inválido.

```kotlin
    tryCatch(isValid("055-444-285") == false)
```

Um caractere de pontuação torna o número inválido.

```kotlin
    tryCatch(isValid(":9") == false)
```

Símbolos tornam o número inválido.

```kotlin
    tryCatch(isValid("055# 444\$ 285") == false)
```

Uma string vazia não é válida.

```kotlin
    tryCatch(isValid("") == false)
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
fun isValid(value: String): Boolean {
    var sum = 0
    var count = 0
    for (i in value.length - 1 downTo 0) {
        val character = value[i]
        if (character == ' ') {
            continue
        }
        if (character < '0' || character > '9') {
            return false
        }
        var digit = character - '0'
        if (count % 2 == 1) {
            digit *= 2
            if (digit > 9) {
                digit -= 9
            }
        }
        sum += digit
        count++
    }
    return count > 1 && sum % 10 == 0
}
```
