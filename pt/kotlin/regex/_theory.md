Uma **expressão regular** (ou **regex**) é um pequeno padrão que descreve uma forma de texto: "quatro dígitos", "uma palavra seguida de `@`", "qualquer coisa entre aspas". Em Kotlin um padrão é um objeto `Regex`, construído de duas maneiras equivalentes:
```kotlin
val a = Regex("cat")
val b = "cat".toRegex()
```
A maioria dos caracteres em um padrão representa a si mesma, mas algumas são **atalhos**:
- `\d` é qualquer dígito, escrito `"\\d"` em uma string Kotlin porque `\` deve ser escapado
- `[a-z]` é qualquer letra minúscula, e `[abc]` é qualquer um entre `a`, `b` ou `c`
- `+` após um elemento significa "um ou mais dele", então `\d+` é uma sequência de dígitos

A pergunta mais simples que você pode fazer é `matches`, que é `true` apenas quando o padrão descreve a string **inteira**:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("2026")) // true
println(digits.matches("20a6")) // false, the letter is not a digit
```

---

`matches` costuma ser restritivo demais: geralmente você só quer saber se o padrão aparece **em algum lugar** do texto. Isso é `containsMatchIn`:
```kotlin
val digits = Regex("\\d+")
println(digits.matches("order 42"))          // false, the whole string is not digits
println(digits.containsMatchIn("order 42"))  // true, "42" is in there
```
Além de `\d` há mais dois atalhos que você usará constantemente: `\w` é um caractere de palavra (letra, dígito ou `_`) e `\s` é um caractere de espaço em branco. Cada um deles pode ser repetido com um **quantificador**:
- `+` um ou mais
- `*` zero ou mais
- `?` zero ou um
- `{3}` exatamente três, `{2,4}` de dois a quatro

Dobrar cada barra invertida fica confuso, então os padrões costumam ser escritos como **strings brutas** com aspas triplas, onde `\` é apenas um caractere:
```kotlin
val digits = Regex("""\d+""") // same as Regex("\\d+")
```

---

`containsMatchIn` diz apenas *se* o padrão está lá. `find` também diz **o quê** e **onde**: ele retorna a primeira correspondência como um `MatchResult`, ou `null` quando não há nada a encontrar.
```kotlin
val match = Regex("""\d+""").find("order 42 shipped")
println(match?.value) // 42
println(match?.range) // 6..7
```
`value` é o texto correspondente e `range` são os índices que ele cobre na string original. Como o resultado é anulável, você o acessa com a chamada segura `?.`, que dá `null` em vez de travar quando nenhuma correspondência foi encontrada:
```kotlin
val none = Regex("""\d+""").find("no numbers")
println(none?.value) // null
```

---

Parênteses em um padrão criam um **grupo de captura**: uma parte da correspondência que você quer ler separadamente. `MatchResult.groupValues` os guarda, com o índice `0` para a correspondência inteira e `1`, `2`, ... para os grupos, da esquerda para a direita:
```kotlin
val date = Regex("""(\d{4})-(\d{2})-(\d{2})""")
val match = date.find("released 2026-09-12 in Rome")
println(match?.groupValues?.get(0)) // 2026-09-12
println(match?.groupValues?.get(1)) // 2026
println(match?.groupValues?.get(2)) // 09
```
Quando não há correspondência alguma, `find` retorna `null` e não há nada a ler, então uma função que extrai um grupo geralmente decide o que retornar nesse caso:
```kotlin
val match = date.find("no date here")
println(match?.groupValues?.get(1) ?: "unknown") // unknown
```

---

Contar parênteses para descobrir que o host é o grupo `2` fica frágil assim que o padrão cresce. Um grupo pode receber um **nome** com `(?<name>...)` e ser lido de `groups` por esse nome:
```kotlin
val email = Regex("""(?<user>\w+)@(?<host>\w+)""")
val match = email.find("write to ann@mail today")
println(match?.groups?.get("user")?.value) // ann
println(match?.groups?.get("host")?.value) // mail
```
`groups` retorna o grupo como um `MatchGroup?`, então você ainda pede o seu `.value`. Um grupo nomeado também é numerado como de costume, então `groupValues[1]` continua funcionando ao lado dele.

---

`find` para na primeira correspondência. `findAll` retorna **todas** as correspondências, como uma `Sequence<MatchResult>`: uma cadeia preguiçosa que você pode tratar como uma lista com `map`, `filter`, `count` e `toList`.
```kotlin
val words = Regex("""\w+""").findAll("one two three")
println(words.count())                    // 3
println(words.map { it.value }.toList())  // [one, two, three]
```
Quando nada corresponde, `findAll` retorna uma sequência vazia em vez de `null`, então não há chamada segura a escrever. Imprimir a sequência em si não é útil, ela mostra o objeto, não as correspondências: transforme-a em uma lista primeiro.

---

`replace` reescreve o texto: ele retorna uma string **nova** onde cada correspondência é trocada pela substituição, deixando o original intacto.
```kotlin
println(Regex("""\d+""").replace("a1 b22", "#")) // a# b#
```
Na string de substituição, `$1`, `$2`, ... representam os grupos capturados daquela correspondência, então você pode reordenar ou reutilizar as partes que correspondeu:
```kotlin
val name = Regex("""(\w+) (\w+)""")
println(name.replace("Ann Lee", "$2 $1")) // Lee Ann
```
`$0` é a correspondência inteira. Se você precisar de um `$` literal na substituição, escape-o como `\$`.
`replace` reescreve **todas** as correspondências, então quando apenas uma string completa deve ser reescrita, ancore o padrão com as **âncoras** `^` (início do texto) e `$` (fim do texto):
```kotlin
println(Regex("""^\w+$""").replace("one two", "x")) // one two, nothing is replaced
```

---

Uma string de substituição só pode reorganizar as partes que recebeu. Quando o novo texto precisa ser **calculado**, passe um lambda para `replace`: ele recebe o `MatchResult` e retorna a string que ocupa o seu lugar.
```kotlin
val digits = Regex("""\d+""")
println(digits.replace("a1 b22") { m -> (m.value.toInt() * 2).toString() }) // a2 b44
```
Dentro do lambda você tem o `MatchResult` completo, então `m.value`, `m.range` e `m.groupValues` estão todos disponíveis. Note que `$1` não tem significado aqui: é um caractere comum em qualquer string que você retornar.

---

`split` corta uma string onde quer que o padrão corresponda e retorna as partes como uma `List<String>`. Diferentemente de dividir em uma string delimitadora fixa, um separador regex pode descrever toda uma família de separadores:
```kotlin
val separators = Regex("""[,;]\s*""")
println(separators.split("a, b;c")) // [a, b, c]
```
Os separadores correspondentes não fazem parte do resultado. Se o texto começa ou termina com um separador, a parte ao lado dele é vazia:
```kotlin
println(Regex("""\s+""").split(" a b")) // [, a, b]
```
`split` aceita um `limit` como segundo argumento para parar após um determinado número de partes, mantendo o restante intacto na última.

---

Padrões diferenciam maiúsculas de minúsculas: `Regex("kotlin")` não corresponde a `"Kotlin"`. Em vez de escrever `[kK][oO]...`, passe uma opção como segundo argumento:
```kotlin
val pattern = Regex("kotlin", RegexOption.IGNORE_CASE)
println(pattern.containsMatchIn("I love Kotlin")) // true
```
A opção pertence ao `Regex`, então todo método desse objeto a obedece: `matches`, `find`, `findAll`, `replace` e `split` igualmente. Outras opções úteis são `RegexOption.MULTILINE`, que faz `^` e `$` corresponderem em cada linha, e `RegexOption.DOT_MATCHES_ALL`. Para combiná-las, passe um conjunto: `Regex("a.b", setOf(RegexOption.IGNORE_CASE, RegexOption.DOT_MATCHES_ALL))`.

---

`Regex("cat")` também corresponde ao `cat` dentro de `catalog`. Para exigir uma palavra inteira, use a **fronteira de palavra** `\b`: ela corresponde à posição vazia entre um caractere de palavra e qualquer outra coisa, incluindo o início e o fim do texto.
```kotlin
println(Regex("""cat""").findAll("cat catalog").count())     // 2
println(Regex("""\bcat\b""").findAll("cat catalog").count()) // 1
```
Um padrão é uma string comum, então pode ser construído a partir de partes em tempo de execução:
```kotlin
val word = "cat"
val pattern = Regex("""\b""" + word + """\b""")
```

---

Os caracteres `. * + ? ( ) [ ] { } | ^ $ \` têm um significado especial dentro de um padrão. O mais traiçoeiro é `.`, que corresponde a **qualquer** caractere, não a um ponto. Para se referir ao próprio caractere, escape-o com uma barra invertida:
```kotlin
println(Regex("""3.14""").matches("3x14"))  // true, the dot matches the x
println(Regex("""3\.14""").matches("3x14")) // false
```
Quando o texto a procurar vem de uma variável e deve ser tomado literalmente, deixe a biblioteca fazer o escape com `Regex.escape`:
```kotlin
val typed = "1+1"
println(Regex(Regex.escape(typed)).containsMatchIn("1+1=2")) // true
```

---

`findAll` e grupos juntos transformam uma linha de texto em dados estruturados. Cada `MatchResult` da sequência carrega o seu próprio `groupValues`, então uma única cadeia pode construir uma lista, um map ou um total:
```kotlin
val pair = Regex("""(\w+)=(\w+)""")
val config = pair.findAll("host=local;port=80").associate { it.groupValues[1] to it.groupValues[2] }
println(config) // {host=local, port=80}
```
`associate` constrói um map a partir dos pares `key to value` retornados pelo lambda. Quando um padrão tem um número fixo de grupos, `destructured` permite desempacotá-los em variáveis nomeadas em vez de lê-los por índice:
```kotlin
val (key, value) = pair.find("host=local")!!.destructured
println(key)   // host
println(value) // local
```

---

Colchetes definem uma **classe de caracteres**: um caractere dentre o conjunto listado. Dentro deles você pode usar intervalos, e um `^` no início nega a classe inteira:
```kotlin
println(Regex("""gr[ae]y""").matches("grey"))  // true
println(Regex("""[a-f0-9]+""").matches("1b3")) // true
println(Regex("""[^0-9]+""").matches("abc"))   // true, no digit allowed
```
Uma classe escolhe apenas entre caracteres individuais. Para escolher entre alternativas inteiras, use `|`, geralmente envolvido em um grupo para que ele não engula o restante do padrão:
```kotlin
println(Regex("""(cat|dog)s?""").matches("dogs")) // true
```

---

Como `findAll` dá uma sequência, os métodos de agregação que você já conhece funcionam em correspondências também: `sumOf`, `maxOfOrNull`, `filter`, `sortedBy`. Extrair números de texto livre é um trabalho de duas etapas: correspondê-los e depois converter o texto em um número.
```kotlin
val total = Regex("""\d+""").findAll("2 apples, 3 pears").sumOf { it.value.toInt() }
println(total) // 5
```

---

Um padrão realista costuma misturar tudo de uma vez: grupos para manter as partes de que você precisa, um `\.` escapado para os pontos literais e uma substituição por lambda para reconstruir o texto em torno deles.
```kotlin
val email = Regex("""(\w+)@(\w+\.\w+)""")
println(email.replace("ping ann@mail.com now") { m -> "<" + m.groupValues[2] + ">" })
// ping <mail.com> now
```
Mantenha os padrões tão simples quanto o trabalho permite: um padrão que tenta descrever todo endereço de e-mail válido é ilegível, enquanto `\w+@\w+\.\w+` é suficiente para encontrar os endereços em uma frase.
