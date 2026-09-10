Um **comentário** é uma nota escrita dentro do código-fonte para quem o lê. O JavaScript ignora completamente os comentários, por isso eles nunca mudam o que o programa faz.

O comentário mais simples é o **comentário de uma linha**: começa com `//` e vai até o final da linha.
```javascript
// Greets the user
console.log("Hello");
```
Use comentários para explicar para que serve um trecho de código, ou por que ele foi escrito daquela forma. Note que, ao contrário de outras linguagens, `#` **não** inicia um comentário em JavaScript.

---

Um comentário não precisa de uma linha só para ele: pode vir depois do código na mesma linha. Esse é um **comentário em linha** (ou comentário final), e é um bom lugar para uma nota curta sobre aquela instrução específica:
```javascript
const retries = 3; // give up after three attempts
```
Tudo o que vai de `//` até o final da linha é ignorado, enquanto o código antes dele é executado normalmente.

---

Como os comentários são ignorados, adicionar ou apagar um comentário nunca muda o que um programa faz. Só o código que **não** está comentado é executado.

Isso faz de `//` uma forma rápida de desligar uma linha de código sem apagá-la. Isso se chama **comentar** o código:
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
A segunda linha agora é um comentário, então `total` continua `10`. Remover o `//` traz a linha de volta à vida.

Comentar código é prático enquanto você experimenta, mas lembre-se de limpar: código que fica comentado por muito tempo só confunde quem for lê-lo depois.

---

Quando um comentário precisa de mais de uma linha, o JavaScript oferece o **comentário de várias linhas** (também chamado de comentário de bloco): começa com `/*` e termina com `*/`, e tudo o que estiver entre eles é ignorado, incluindo as quebras de linha.
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
Um comentário de bloco também pode ser curto e ficar em uma única linha: `/* like this */`.

---

Seja qual for o tipo de comentário que você usar, a regra é a mesma: o texto dentro dele **não é código**. Um `console.log` dentro de um comentário nunca imprime nada, e o código escrito depois de `//` na mesma linha nunca é executado, mesmo quando a linha começa com código de verdade:
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
Quando não tiver certeza do que um programa imprime, apague mentalmente todos os comentários e leia o que sobrou.

---

Ao contrário de `//`, que para no fim da linha, um comentário `/*` só para no `*/`. Se você esquecer de fechá-lo, o JavaScript trata todo o código seguinte como parte do comentário e reporta um erro de sintaxe:
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
Tanto `//` quanto `/* */` funcionam como comentários em linha, mas com `/*` certifique-se sempre de que o `*/` está lá.

---

Em JavaScript, comentários de bloco **não podem ser aninhados**: o comentário termina no **primeiro** `*/` que encontra, não importa quantos `/*` vieram antes.
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
Aqui o comentário termina logo depois de `inner`, então `still a comment */` é lido como código e causa um erro de sintaxe. Tenha isso em mente quando comentar um bloco que já contém um comentário `/* */`: use `//` em cada linha, ou remova antes o comentário interno.

---

Para comentar várias linhas de uma vez, envolva-as em um único comentário de bloco em vez de adicionar `//` a cada linha:
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
Como as linhas dentro do bloco são ignoradas, `total` nunca muda. Lembre-se de que isso só funciona quando nenhuma dessas linhas contém um `*/`.

---

O JavaScript tem um terceiro tipo de comentário, o **comentário de documentação**, escrito no formato **JSDoc**: um comentário de bloco que começa com `/**` (dois asteriscos) colocado diretamente acima de uma função. Dentro dele, as linhas normalmente começam com ` * ` e **tags** especiais que começam com `@` descrevem a função:
- `@param {type} name description` para cada parâmetro
- `@returns {type} description` para o valor retornado

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
Para o JavaScript é apenas um comentário, mas os editores o leem e o mostram como texto de ajuda de `greet`, junto com o tipo escrito entre chaves (`{number}`, `{string}`, `{boolean}`, `{number[]}`...).

---

A primeira linha de um comentário JSDoc é o **resumo**: uma frase curta que diz o que a função faz. Escreva-a na terceira pessoa, como se estivesse descrevendo a função: "Returns...", "Adds...", "Checks...". Depois liste as tags, uma por linha:
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
O comentário deve ficar logo acima da declaração, sem linha em branco entre eles, senão os editores não o associam à função.

---

Um comentário JSDoc também é um **contrato**: ele diz a quem chama a função o que passar e o que esperar de volta, antes mesmo de o corpo ser escrito. Ler o comentário muitas vezes basta para implementar a função:
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
Cada `@param` corresponde a um parâmetro, na mesma ordem, e `@returns` descreve todos os resultados possíveis.

---

A ordem dentro de um comentário JSDoc é sempre a mesma: primeiro o resumo, depois um `@param` por parâmetro na ordem em que são declarados, e por último `@returns`. A abertura `/**` e o fechamento ` */` envolvem tudo, e o comentário fica diretamente acima da função que descreve:
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

Um arquivo JavaScript pode começar com uma linha especial chamada **shebang** (ou hashbang): `#!` seguido do caminho do programa que deve executar o arquivo. Em sistemas do tipo Unix, isso permite executar um script diretamente do terminal, como `./hello.js`, sem digitar `node` antes:
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
O JavaScript ignora essa linha exatamente como um comentário, mas apenas quando ela é a **primeiríssima linha** do arquivo: em qualquer outro lugar, `#!` é um erro de sintaxe. `/usr/bin/env node` significa "encontre o `node` neste sistema e use-o".

---

Um bom comentário explica **por que** o código faz algo, não **o que** ele faz. O código já mostra o que acontece; repetir isso em palavras só acrescenta ruído e fica desatualizado assim que o código muda:
```javascript
// set timeout to 30
const timeout = 30;
```
O motivo por trás do número é o que quem lê não consegue adivinhar:
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
Se um comentário apenas repete a linha abaixo dele, apague-o ou substitua-o pelo motivo.

---

Alguns comentários seguem uma convenção que os editores entendem. Os **marcadores** mais comuns são:
- `// TODO: ...` sinaliza algo que ainda precisa ser escrito
- `// FIXME: ...` sinaliza código que se sabe estar errado e que precisa ser corrigido

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Para o JavaScript são comentários comuns; os editores os listam para que o trabalho pendente seja fácil de encontrar. Um `TODO` normalmente fica ao lado de um substituto provisório que mantém o código funcionando até que a implementação real seja escrita. Quando você concluir o trabalho, substitua o provisório e remova o marcador na mesma alteração: um `TODO` desatualizado é enganoso.

---

Um `FIXME` é diferente de um `TODO`: o código já existe, mas sabe-se que está errado. Um bom `FIXME` diz qual é o bug e, quando possível, dá um exemplo que o mostra, para que a próxima pessoa possa corrigi-lo rapidamente. Assim como no `TODO`, apague o marcador quando o bug estiver corrigido, mas mantenha o comentário JSDoc, que continua verdadeiro.
