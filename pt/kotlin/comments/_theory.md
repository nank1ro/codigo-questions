Um **comentário** é uma nota escrita dentro do código-fonte para as pessoas que o leem. O compilador ignora completamente os comentários, então eles nunca mudam o que o programa faz.

O comentário mais simples é o **comentário de linha única**: ele começa com `//` e vai até o fim da linha.
```kotlin
// Cumprimenta o usuário
println("Hello")
```
Use comentários para explicar para que serve um trecho de código, ou por que ele foi escrito daquela forma.

---

Um comentário não precisa de uma linha própria: ele pode vir depois do código na mesma linha. Este é um **comentário de fim de linha**, e é um bom lugar para uma nota curta sobre aquela instrução específica:
```kotlin
val retries = 3 // desiste depois de três tentativas
```
Tudo, de `//` até o fim da linha, é ignorado, enquanto o código antes dele roda como de costume.

---

Como o compilador remove os comentários completamente, adicionar ou apagar um comentário nunca muda o que um programa faz. Apenas o código que **não** está comentado roda.

Isso torna o `//` uma forma rápida de desligar uma linha de código sem apagá-la. Isso se chama **comentar** o código:
```kotlin
var total = 10
// total = total + 5
println(total) // imprime 10
```
A segunda linha agora é um comentário, então `total` continua `10`. Remover o `//` traz a linha de volta à vida.

Comentar código é útil enquanto você experimenta, mas lembre-se de limpar depois: código que fica comentado por muito tempo só confunde quem for lê-lo em seguida.

---

Quando um comentário precisa de mais de uma linha, o Kotlin oferece o **comentário de múltiplas linhas** (também chamado de comentário em bloco): ele começa com `/*` e termina com `*/`, e tudo no meio é ignorado, incluindo quebras de linha.
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
Um comentário em bloco também pode ser curto e ficar em uma única linha: `/* like this */`.

---

Diferentemente do `//`, que para no fim da linha, um comentário `/*` só para no `*/`. Se você esquecer de fechá-lo, o compilador trata todo o código seguinte como parte do comentário e reporta um erro:
```kotlin
val width = 10 /* em centímetros
println(width) // ainda dentro do comentário: erro, o comentário nunca é fechado
```
Tanto `//` quanto `/* */` funcionam como comentários de fim de linha, mas com `/*` sempre verifique se o `*/` está lá.

---

Em Java um comentário em bloco não pode conter outro comentário em bloco, mas em Kotlin eles **podem ser aninhados**: cada `/*` deve ser fechado pelo seu próprio `*/`, e o comentário só termina quando o mais externo é fechado.
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
Aqui `still a comment */` faz parte do comentário externo, então apenas `done` é impresso. É isso que permite comentar um bloco inteiro de código mesmo quando esse bloco já contém um comentário `/* */`.

---

Para comentar várias linhas de uma vez, envolva-as em um único comentário em bloco em vez de adicionar `//` a cada linha:
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // imprime 100
```
Graças ao aninhamento, isso funciona mesmo quando uma dessas linhas já contém um comentário `/* */`.

---

Um uso comum dos comentários em bloco é o **comentário de cabeçalho**: um bloco curto colocado diretamente acima de uma função que diz o que ela faz e o que seus parâmetros significam.
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
Quem chama `toSeconds` pode ler o cabeçalho em vez do corpo. Mantenha o cabeçalho junto à função para que sejam atualizados juntos.

---

O Kotlin tem um terceiro tipo de comentário, o **comentário de documentação**, escrito em um formato chamado **KDoc**: ele começa com `/**` (uma barra e dois asteriscos) e termina com `*/`, e é colocado diretamente acima de uma função, uma classe ou uma propriedade.
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
Para o compilador é apenas um comentário, mas ferramentas como o IntelliJ IDEA o leem e o exibem como texto de ajuda para `greet`. O `*` no início das linhas internas é apenas uma convenção que mantém o bloco alinhado. Dentro do KDoc você pode usar Markdown, e colchetes como `[name]` viram links para aquele parâmetro.

---

A primeira linha de um comentário de documentação é o **resumo**: uma frase curta que diz o que a função faz. Escreva-a na terceira pessoa, como se descrevesse a função: "Returns...", "Adds...", "Checks...".
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
O comentário deve ficar diretamente acima da declaração, sem nenhuma outra instrução no meio, caso contrário as ferramentas não o associam à função.

---

Depois do resumo, um comentário de documentação pode descrever os parâmetros e o valor retornado com **tags KDoc**, que sempre começam com `@`:
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
`@param` é seguido pelo nome do parâmetro e depois pela sua descrição; há um `@param` por parâmetro. `@return` descreve o valor que a função devolve. A ordem é sempre a mesma: primeiro o resumo, depois as tags `@param`, depois `@return`.

---

Uma função com mais de um parâmetro recebe uma tag `@param` para cada um deles, escritas na mesma ordem dos parâmetros:
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
Uma tag ainda é apenas um comentário: se você renomear um parâmetro e esquecer a tag, nada quebra, mas a documentação começa a mentir. Atualize o KDoc junto com a assinatura.

---

O compilador procura comentários apenas no código, nunca dentro de um **literal de string**. Entre aspas duplas, `//` e `/* */` são caracteres comuns:
```kotlin
println("50 // 2") // prints 50 // 2
```
O primeiro `//` faz parte do texto, o segundo inicia um comentário de verdade. Isso surpreende as pessoas com mais frequência em endereços web, que contêm `//` logo depois do protocolo.

---

Alguns comentários seguem uma convenção que os editores entendem. Os **marcadores** mais comuns são:
- `// TODO: ...` sinaliza algo que ainda precisa ser escrito
- `// FIXME: ...` sinaliza código que se sabe estar errado e deve ser corrigido

```kotlin
val limit = 10
// TODO: lê o limite das configurações
```
Para o compilador são comentários comuns; o IntelliJ IDEA os reúne em uma janela de ferramentas dedicada, para que o trabalho pendente seja fácil de encontrar. Um `TODO` geralmente fica ao lado de um placeholder que mantém o código compilando até que a implementação real seja escrita. Quando concluir o trabalho, substitua o placeholder e remova o marcador na mesma alteração, para que o comentário nunca minta sobre o estado do código.

---

Um `FIXME` é diferente de um `TODO`: o código já existe, mas se sabe que está errado. Um bom `FIXME` diz qual é o bug e, quando possível, dá um exemplo que o demonstra, para que a próxima pessoa possa corrigi-lo rapidamente. Assim como no `TODO`, apague o marcador assim que o bug for corrigido, mas mantenha o comentário de documentação, que continua verdadeiro.

---

Um bom comentário explica **por que** o código faz algo, e não **o que** ele faz. O código já mostra o que acontece; repeti-lo em palavras só adiciona ruído e fica desatualizado assim que o código muda:
```kotlin
// define timeout como 30
val timeout = 30
```
O motivo por trás do número é o que um leitor não consegue adivinhar:
```kotlin
// o servidor encerra conexões ociosas depois de 35 segundos, então pare antes
val timeout = 30
```
Se um comentário apenas repete a linha abaixo dele, apague-o ou substitua-o pelo motivo. Os melhores comentários são os que dizem algo que o código não consegue.
