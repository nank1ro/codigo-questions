---
language: javascript
exerciseType: 1
difficulty: 2
title: Codificação run-length
---

# --description--

A codificação run-length é um dos truques de compressão mais antigos que existem: em vez de escrever o mesmo caractere repetidas vezes, você escreve quantas vezes ele se repete e, em seguida, o próprio caractere.

Uma máquina de fax que digitaliza uma página quase inteira em branco encontra longos trechos de pixels idênticos, de modo que uma fileira de doze `W` percorre a linha como o `12W`, bem mais curto. Quando um caractere aparece apenas uma vez, não há nada a ganhar ao contá-lo, então ele é copiado sozinho.

# --instructions--

Escreva uma função `encodeRun` que recebe uma string `text` e retorna a sua codificação em run-length.

Cada sequência do mesmo caractere repetido duas ou mais vezes se torna o comprimento da sequência escrito em decimal, seguido desse caractere. Uma sequência de comprimento um é copiada como o único caractere, sem nenhum número na frente.

Exemplos:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- O texto contém apenas letras maiúsculas de `A` a `Z` e espaços.
- Uma sequência com mais de nove caracteres usa sua contagem decimal completa, de modo que doze `W` se tornam `12W` e nunca `9W3W`.
- Espaços são caracteres comuns: eles são contados e codificados exatamente como as letras.
- A string vazia é codificada como a string vazia.

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function encodeRun(text) {
  
}
```

# --asserts--

A string vazia é codificada como a string vazia

```javascript
tryCatch(encodeRun("") === "");
```

Um único caractere é copiado como ele mesmo

```javascript
tryCatch(encodeRun("A") === "A");
```

Uma string sem repetições passa inalterada

```javascript
tryCatch(encodeRun("ABCDE") === "ABCDE");
```

Uma sequência de dois se torna a contagem seguida do caractere

```javascript
tryCatch(encodeRun("AA") === "2A");
```

O exemplo misto "AABCCCDEEEE" se torna "2AB3CD4E"

```javascript
tryCatch(encodeRun("AABCCCDEEEE") === "2AB3CD4E");
```

Uma sequência de doze usa sua contagem decimal completa, então o resultado começa com "12W"

```javascript
tryCatch(encodeRun("WWWWWWWWWWWWBWW") === "12WB2W");
```

Sequências de espaços são codificadas exatamente como sequências de letras

```javascript
tryCatch(encodeRun("  HI  ") === "2 HI2 ");
```

Uma sequência de dez é escrita como "10A", nunca como duas sequências menores

```javascript
tryCatch(encodeRun("AAAAAAAAAA") === "10A");
```

Caracteres únicos alternados são todos copiados como eles mesmos

```javascript
tryCatch(encodeRun("ABABAB") === "ABABAB");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function encodeRun(text) {
  let result = "";
  let i = 0;

  while (i < text.length) {
    let run = 1;
    while (i + run < text.length && text[i + run] === text[i]) {
      run++;
    }
    if (run > 1) {
      result += run;
    }
    result += text[i];
    i += run;
  }

  return result;
}
```
