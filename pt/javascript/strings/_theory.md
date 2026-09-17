Uma **string** é uma sequência de caracteres entre aspas, como `"hello"` ou `'hello'`.
Toda string tem uma propriedade `length` que informa quantos caracteres ela contém:
```javascript
let greeting = "hello";
console.log(greeting.length);
// imprime 5
```
Espaços e pontuação também contam como caracteres.

---

Cada caractere de uma string tem um **índice**, começando em `0`.
Você pode ler um único caractere com colchetes ou com o método `charAt()`:
```javascript
let word = "hello";
console.log(word[0]);
// imprime h
console.log(word.charAt(1));
// imprime e
```
O último caractere está no índice `length - 1`:
```javascript
console.log(word[word.length - 1]);
// imprime o
```

---

Strings possuem muitos **métodos** integrados. Dois dos mais simples alteram a caixa de todas as letras:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// imprime HELLO
console.log(word.toLowerCase());
// imprime hello
```
Ambos os métodos não recebem argumentos, então não esqueça os parênteses.

---

Para verificar se uma string contém outra string, use estes métodos, que retornam um booleano:
- `includes(text)` é `true` se `text` aparecer em qualquer lugar
- `startsWith(text)` é `true` se a string começar com `text`
- `endsWith(text)` é `true` se a string terminar com `text`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// imprime true
console.log(file.startsWith("ph"));
// imprime true
console.log(file.endsWith(".jpg"));
// imprime false
```
A comparação diferencia maiúsculas de minúsculas: `"Hello".includes("h")` é `false`.

---

O método `indexOf()` retorna o índice onde um trecho de texto aparece **pela primeira vez** na string.
Se o texto não for encontrado, ele retorna `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// imprime 2
console.log(word.indexOf("z"));
// imprime -1
```

---

O método `slice(start, end)` extrai um trecho de uma string, do índice `start` até (mas sem incluir) o índice `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// imprime Java
console.log(word.slice(4));
// imprime Script
```
Se você omitir `end`, o trecho vai até o final da string.
Um índice negativo conta a partir do final: `word.slice(-3)` é `"ipt"`.
O método `substring(start, end)` funciona da mesma forma, mas não aceita índices negativos.

---

`indexOf()` e `slice()` funcionam bem juntos: descubra onde algo está e depois corte a string ali.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// imprime 45
```

---

O método `split(separator)` divide uma string em um **array** de pedaços, cortando em cada `separator`:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// imprime [ 'I', 'like', 'JavaScript' ]
```
O oposto é o método de array `join(separator)`, que cola os pedaços de volta em uma string:
```javascript
console.log(words.join("-"));
// imprime I-like-JavaScript
```

---

A entrada do usuário costuma ter espaços extras ao redor. O método `trim()` retorna uma cópia da string com os espaços em branco removidos de **ambas** as extremidades:
```javascript
let input = "   hello   ";
console.log(input.trim());
// imprime hello
```
`trimStart()` remove apenas os espaços do início e `trimEnd()` apenas os do final.
Os espaços no meio da string nunca são alterados.

---

O método `replace(search, replacement)` retorna uma nova string onde a **primeira** ocorrência de `search` é trocada por `replacement`:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// imprime blue red
```
Para substituir **todas** as ocorrências, use `replaceAll()`:
```javascript
console.log(text.replaceAll("red", "blue"));
// imprime blue blue
```

---

O método `repeat(count)` retorna a string repetida `count` vezes:
```javascript
console.log("ab".repeat(3));
// imprime ababab
console.log("ab".repeat(0));
// imprime uma string vazia
```

---

O método `padStart(targetLength, padString)` adiciona `padString` ao **início** da string até que ela atinja `targetLength` caracteres. `padEnd()` faz o mesmo no final:
```javascript
console.log("7".padStart(3, "0"));
// imprime 007
console.log("Tea".padEnd(6, "."));
// imprime Tea...
```
Se a string já for longa o suficiente, ela é retornada sem alterações.
Números não têm métodos de string, então converta-os primeiro com `String(number)`.

---

Duas strings são iguais com `===` somente se tiverem exatamente os mesmos caracteres, na mesma caixa:
```javascript
console.log("hello" === "hello");
// imprime true
console.log("hello" === "Hello");
// imprime false
```
Os operadores `<` e `>` comparam strings em ordem alfabética, caractere por caractere.
Letras maiúsculas vêm antes das minúsculas, então `"Zoo" < "apple"` é `true`.

---

Strings são **imutáveis**: uma vez criada, uma string nunca pode ser alterada.
Atribuir a um índice não faz nada, e todo método de string retorna uma **nova** string em vez de modificar a original:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// imprime hello
word.toUpperCase();
console.log(word);
// imprime hello
```
Para manter um resultado, atribua-o de volta à variável:
```javascript
word = word.toUpperCase();
```

---

Chamar `split("")` com um separador vazio transforma uma string em um array de caracteres individuais.
Arrays têm um método `reverse()`, então você pode inverter uma string dividindo, invertendo e juntando novamente:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// imprime cba
```
