Uma **string** é uma sequência de caracteres entre aspas, como `"hello"` ou `'hello'`.
Toda string tem uma propriedade `length` que informa quantos caracteres ela contém:
```javascript
let greeting = "hello";
console.log(greeting.length);
// prints 5
```
Espaços e pontuação também contam como caracteres.

---

Cada caractere de uma string tem um **índice**, começando em `0`.
Você pode ler um único caractere com colchetes ou com o método `charAt()`:
```javascript
let word = "hello";
console.log(word[0]);
// prints h
console.log(word.charAt(1));
// prints e
```
O último caractere está no índice `length - 1`:
```javascript
console.log(word[word.length - 1]);
// prints o
```

---

Strings possuem muitos **métodos** integrados. Dois dos mais simples alteram a caixa de todas as letras:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// prints HELLO
console.log(word.toLowerCase());
// prints hello
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
// prints true
console.log(file.startsWith("ph"));
// prints true
console.log(file.endsWith(".jpg"));
// prints false
```
A comparação diferencia maiúsculas de minúsculas: `"Hello".includes("h")` é `false`.

---

O método `indexOf()` retorna o índice onde um trecho de texto aparece **pela primeira vez** na string.
Se o texto não for encontrado, ele retorna `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// prints 2
console.log(word.indexOf("z"));
// prints -1
```

---

O método `slice(start, end)` extrai um trecho de uma string, do índice `start` até (mas sem incluir) o índice `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// prints Java
console.log(word.slice(4));
// prints Script
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
// prints 45
```
