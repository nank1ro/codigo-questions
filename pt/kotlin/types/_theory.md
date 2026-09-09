Todo valor em Kotlin tem um **tipo**, que informa ao compilador que tipo de dado ele é e o que você pode fazer com ele.
Os tipos básicos são:
- `Int`: um número inteiro, como `42` ou `-7`
- `Long`: um número inteiro que pode ser muito maior do que um `Int`
- `Double`: um número com parte decimal, como `3.14`
- `Float`: um número decimal que usa metade da memória de um `Double`, mas é menos preciso
- `Char`: um único caractere entre aspas simples, como `'a'`
- `Boolean`: ou `true` ou `false`
- `String`: um texto entre aspas duplas, como `"Hello"`

Como você viu nas lições de variáveis, você pode declarar o tipo explicitamente com dois pontos depois do nome:
```kotlin
val age: Int = 36
val name: String = "Ada"
```
Um valor de um tipo não pode ser armazenado em uma variável de outro tipo: `val age: Int = "36"` é um erro de compilação.

---

Na maioria das vezes você não escreve o tipo: o Kotlin **infere** o tipo a partir do valor que você atribui, seguindo algumas regras de literais:
- um número inteiro, como `42`, é um `Int`
- um número com ponto decimal, como `3.14`, é um `Double`
- um texto entre aspas duplas é uma `String`
- um caractere entre aspas simples é um `Char`
- `true` e `false` são `Boolean`
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
Para verificar o que o Kotlin inferiu, você pode imprimir o nome do tipo de qualquer valor com `::class.simpleName`:
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
Um literal decimal nunca é inferido como `Float`: `val ratio = 0.5` é um `Double`.

---

Um `Int` pode armazenar números inteiros até cerca de dois bilhões, mais precisamente até `Int.MAX_VALUE`, que é `2147483647`.
Um literal inteiro grande demais para um `Int` é automaticamente inferido como um `Long`, e você pode forçar um `Long` para qualquer literal com o sufixo `L`:
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
Da mesma forma, o sufixo `f` transforma um literal decimal em um `Float`: `val ratio = 0.5f`.
Números longos são difíceis de ler, então o Kotlin permite colocar sublinhados `_` em qualquer lugar entre os dígitos; eles são ignorados pelo compilador:
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

O Kotlin nunca converte entre tipos numéricos por conta própria quando você atribui um valor, nem mesmo de um tipo menor para um maior: armazenar um `Int` em uma variável `Long` ou `Double` é um erro de compilação.
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
Todo tipo numérico tem **funções de conversão** que constroem um novo valor do tipo que você precisa: `toInt()`, `toLong()`, `toDouble()`, `toFloat()` e, para obter texto, `toString()`.
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
Ir de um decimal para um número inteiro **trunca**: `toInt()` simplesmente descarta a parte decimal, então `3.99.toInt()` é `3` e `(-3.99).toInt()` é `-3`.

---

Os tipos dos operandos decidem como a divisão funciona. Quando ambos são `Int`, o operador `/` realiza a **divisão inteira**: o resultado é um `Int` e o resto é descartado.
Quando pelo menos um operando é um `Double`, o `/` realiza a divisão de ponto flutuante e mantém a parte decimal:
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
Então, para obter um resultado decimal a partir de duas variáveis `Int`, você deve converter pelo menos uma delas **antes** de dividir: `(7 / 2).toDouble()` é `3.0`, porque a divisão inteira já aconteceu.

---

Quando uma função deve retornar um resultado decimal calculado a partir de números inteiros, converta os operandos para `Double` antes de dividir e declare o tipo de retorno como `Double`:
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
Lembre-se de que `sum()` e `size` de uma `List<Int>` também são valores `Int`, então eles precisam da mesma conversão.

---

Todo `Char` é armazenado como um número, o seu **código**. A propriedade `code` fornece o `Int` por trás de um caractere, e `toChar()` faz o oposto, transformando um `Int` no `Char` com aquele código:
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
As letras têm códigos consecutivos, então somar ao código avança ao longo do alfabeto.
Note que o código de `'7'` é `55`, e não `7`: para ler o dígito que um `Char` representa, use `digitToInt()`, que retorna `7`.

---

Como o código de um `Char` é um `Int`, você pode fazer aritmética com ele e converter o resultado de volta para um `Char`. É assim que você avança ao longo do alfabeto:
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
O Kotlin também permite somar um `Int` diretamente a um `Char`: `'a' + 1` é `'b'`, e a diferença entre dois caracteres `'d' - 'a'` é o `Int` `3`.

---

Um texto digitado por um usuário sempre chega como uma `String`, mesmo quando parece um número. Para fazer cálculos com ele, você deve fazer o **parse**: `toInt()` transforma `"42"` no `Int` `42`, e `toDouble()` transforma `"3.5"` no `Double` `3.5`.
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
Nem todo texto é um número: `"4x2".toInt()` lança uma `NumberFormatException` e interrompe o programa.
As alternativas seguras `toIntOrNull()` e `toDoubleOrNull()` retornam `null` em vez de lançar a exceção, então, como você aprendeu nas lições de nulidade, você pode fornecer um valor padrão com `?:`:
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()` só funciona quando o texto inteiro é um número inteiro válido, com um sinal opcional:
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
Para texto decimal, use `toDoubleOrNull()`, que aceita `"3.5"` e retorna um `Double?` da mesma maneira.

---

Um `Int` tem um tamanho fixo, então ele tem um menor e um maior valor: `Int.MIN_VALUE` é `-2147483648` e `Int.MAX_VALUE` é `2147483647`.
Ultrapassar o limite **não** gera um erro: o valor silenciosamente **dá a volta** para o outro extremo do intervalo, um comportamento chamado overflow.
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
Quando um resultado pode exceder dois bilhões, use um `Long`, cujo limite `Long.MAX_VALUE` é cerca de nove quintilhões. Lembre-se de converter antes da operação: `Int.MAX_VALUE.toLong() + 1` é `2147483648`.

---

Um `Double` armazena decimais em binário, então alguns valores não podem ser representados exatamente e pequenos erros aparecem nos últimos dígitos:
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
Para exibir um número fixo de decimais, use `String.format` com uma string de formato: `"%.2f"` significa "um número decimal com 2 dígitos depois do ponto". O resultado é uma `String`, arredondada para essa quantidade de dígitos:
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any` é o tipo no topo da hierarquia: todo valor em Kotlin é um `Any`, então uma variável do tipo `Any` pode conter um `Int`, uma `String`, um `Boolean` ou qualquer outra coisa.
Para descobrir o que ela realmente contém, você usa o operador `is`, que retorna `true` quando o valor tem aquele tipo:
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
Uma vez que a verificação passou, o compilador faz um **smart cast** do valor: dentro do `if` (ou do ramo do `when`) você pode usá-lo como aquele tipo, sem necessidade de conversão:
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
