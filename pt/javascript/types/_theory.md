Todo valor em JavaScript tem um **tipo**. Existem sete tipos **primitivos**:
- `number` para qualquer número, como `42` ou `3.14`
- `string` para texto, como `"Ana"`
- `boolean` para `true` e `false`
- `undefined` para um valor que nunca foi fornecido
- `null` para um valor intencionalmente vazio
- `bigint` para números inteiros de qualquer tamanho, como `9007199254740993n`
- `symbol` para identificadores únicos criados com `Symbol()`

Todo o restante (arrays, funções, objetos criados com `{}`, datas...) é um `object`.
O operador `typeof` informa o tipo de um valor, como uma string:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript é **dinamicamente tipado**: uma variável não tem tipo próprio; apenas o valor que ela contém no momento tem um tipo. A mesma variável pode conter um número agora e uma string depois, e o `typeof` segue o valor:
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
Isso é conveniente, mas também significa que uma função pode receber um valor de um tipo inesperado, então verificar com `typeof` é um primeiro passo comum. Como `typeof` retorna uma string, você compara o resultado com uma string:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

O `typeof` tem algumas respostas que surpreendem as pessoas.
Funções recebem uma resposta própria, `"function"`, embora sejam objetos:
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
Arrays **não** recebem uma resposta própria: eles são apenas `"object"`, assim como `{}`:
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
E `typeof null` é `"object"`, um bug histórico que nunca foi corrigido. Então o `typeof` distingue bem primitivos e funções, mas não consegue diferenciar um array, um objeto e `null`.

---

Você pode converter um valor para outro tipo **explicitamente** chamando o tipo como uma função:
- `Number(value)` converte para um número: `Number("42")` é `42`
- `String(value)` converte para uma string: `String(42)` é `"42"`
- `Boolean(value)` converte para um boolean: `Boolean("")` é `false`

O resultado é um valor completamente novo; o original não é alterado:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
Converter explicitamente deixa sua intenção visível: quem lê `Number(input)` sabe que `input` era texto.

---

`Number()` é rigoroso: a string inteira deve ser um número, caso contrário o resultado é `NaN` ("Not a Number"):
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()` e `parseFloat()` são mais tolerantes: eles leem dígitos a partir do início da string, ignoram espaços à esquerda e param no primeiro caractere que não faz parte de um número. `parseInt` mantém apenas a parte inteira:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
Quando a string não começa com algo que possa iniciar um número (um sinal opcional, seguido de um dígito), eles também retornam `NaN`:
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN` é o único valor que não é igual a si mesmo, então `x === NaN` é sempre `false`; para detectá-lo use `Number.isNaN(x)`.

---

Existem duas maneiras de perguntar "isso é `NaN`?", e elas respondem a perguntas diferentes.
A antiga global `isNaN(value)` primeiro **converte** `value` para um número, depois verifica. Então ela diz `true` para qualquer coisa que não possa se tornar um número, mesmo que não seja `NaN` de fato:
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)` **não** converte: é `true` apenas quando `value` é realmente o número `NaN`:
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
Prefira `Number.isNaN`, e converta primeiro se você quiser saber se uma conversão falhou.

---

JavaScript também converte **implicitamente**, e o operador `+` é onde isso mais causa problemas. Se qualquer um dos lados for uma string, o `+` **concatena** e o outro lado é convertido para uma string:
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
Todos os outros operadores aritméticos convertem os dois lados para **números**:
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
Portanto, somar valores que vêm de texto (entrada do usuário, arquivos, URLs) pode construir silenciosamente uma string em vez de uma soma. Converta com `Number()` antes de somar para ficar seguro.

---

Uma maneira curta de converter uma string para número é o **mais unário**: um `+` colocado na frente de um único valor o converte exatamente como `Number()` faz:
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
É compacto, mas fácil de confundir com adição, então muitas equipes preferem o explícito `Number("5")`.

---

A igualdade **frouxa** `==` converte os dois lados para um tipo comum antes de comparar, seguindo regras difíceis de lembrar:
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
A igualdade **estrita** `===` nunca converte: valores de tipos diferentes simplesmente não são iguais:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
Use `===` (e `!==`) por padrão. A única exceção comum é `value == null`, que verifica `null` e `undefined` juntos.

---

Quando o JavaScript precisa de um boolean, por exemplo em uma condição `if` ou em `Boolean(value)`, ele converte o valor. Apenas oito valores se tornam `false`; eles são chamados de **falsy**:
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` e `NaN`.
**Todo o resto é truthy**, incluindo alguns valores que parecem vazios:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"` é uma string não vazia, então é truthy; um array vazio é um objeto, então também é truthy.

---

Um atalho comum para converter qualquer valor para boolean é a **negação dupla** `!!`: o primeiro `!` converte para boolean e o inverte, o segundo o inverte de volta:
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value` e `Boolean(value)` dão exatamente o mesmo resultado; a forma explícita é mais fácil de ler.

---

JavaScript tem um único tipo `number` para números inteiros e decimais: todo número é um valor de ponto flutuante de 64 bits (um *double*). Então `5` e `5.0` são o mesmo valor, e não existe um tipo inteiro separado:
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
Para perguntar se um número não tem parte fracionária, use `Number.isInteger`:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
Template literals convertem o valor interpolado para uma string com as mesmas regras de `String()`, então `${5.0}` se torna `"5"`, não `"5.0"`.

---

Como os números são doubles, alguns decimais não podem ser armazenados exatamente e pequenos erros aparecem:
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
O método `toFixed(digits)` arredonda um número para `digits` casas decimais, mas retorna uma **string**, o que é bom para exibição e errado para outras contas:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
Para obter um **número** arredondado, converta o resultado de volta com `Number()`:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

Um `number` pode representar números inteiros exatamente apenas até `Number.MAX_SAFE_INTEGER`, que é `9007199254740991`. Além disso, dígitos se perdem:
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
Para números inteiros maiores use `bigint`: escreva o literal com um sufixo `n`, ou converta com `BigInt()`:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
O `console.log` mostra o sufixo `n`; `String(big)` dá os dígitos puros.
Um `bigint` e um `number` não podem ser misturados em aritmética: `big + 1` lança um `TypeError`. Converta um dos lados explicitamente, com `BigInt(count)` ou `Number(big)`.

---

Como o `typeof` responde `"object"` para arrays, objetos e `null`, diferenciá-los requer duas verificações extras.
`Array.isArray(value)` é `true` apenas para arrays:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
Para `null` compare diretamente, `value === null`. Combiná-las dá uma visão completa de qualquer valor:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
Verifique `null` e arrays primeiro, porque o `typeof` simples não consegue distingui-los.

---

Texto vindo de formulários, arquivos ou URLs é sempre uma string, mesmo quando representa um número ou um boolean. Convertê-lo de volta para o tipo certo combina o que você já viu: compare com `"true"` e `"false"` para booleans, e tente `Number()` para números, lembrando que `Number("")` é `0` e que `Number.isNaN` informa quando a conversão falhou:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
Quando nada corresponde, mantenha a string como está.
