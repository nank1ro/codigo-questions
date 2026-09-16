---
language: javascript
exerciseType: 1
difficulty: 2
title: Cifra de César
---

# --description--

Júlio César protegia as suas cartas particulares com um dos truques mais antigos da criptografia: ele substituía cada letra de uma mensagem pela letra que está um número fixo de posições à frente no alfabeto. Com um deslocamento de 3, `a` vira `d`, `b` vira `e` e `c` vira `f`.

O alfabeto funciona como um círculo, então as letras no final voltam para o começo: com um deslocamento de 3, `x` vira `a`, `y` vira `b` e `z` vira `c`.

Qualquer coisa que não seja uma letra, como um espaço, uma vírgula, um ponto de exclamação ou um dígito, atravessa a cifra sem sofrer alterações.

# --instructions--

Escreva uma função `caesarCipher` que receba uma mensagem `text` e um número inteiro `shift`, e retorne a mensagem codificada.

Exemplos:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- A mensagem está sempre em minúsculas, então você nunca precisa lidar com letras maiúsculas.
- Os caracteres que não são letras mantêm o seu lugar e o seu valor.
- O deslocamento nunca é negativo. Um deslocamento de `0` deixa a mensagem inalterada, e o mesmo acontece com um deslocamento de `26`.

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
function caesarCipher(text, shift) {
  
}
```

# --asserts--

Um deslocamento de 3 transforma "hello" em "khoor"

```javascript
tryCatch(caesarCipher("hello", 3) === "khoor");
```

O final do alfabeto dá a volta, então "xyz" vira "abc"

```javascript
tryCatch(caesarCipher("xyz", 3) === "abc");
```

Um deslocamento de 0 deixa a mensagem inalterada

```javascript
tryCatch(caesarCipher("abc", 0) === "abc");
```

Um deslocamento de 26 é uma volta completa no alfabeto, então a mensagem fica inalterada

```javascript
tryCatch(caesarCipher("abc", 26) === "abc");
```

A pontuação e os espaços passam sem sofrer alterações

```javascript
tryCatch(caesarCipher("codigo, rocks!", 5) === "htinlt, wthpx!");
```

Uma mensagem vazia continua vazia

```javascript
tryCatch(caesarCipher("", 4) === "");
```

Os espaços entre letras isoladas são preservados

```javascript
tryCatch(caesarCipher("a b c", 1) === "b c d");
```

Os dígitos não são deslocados, mesmo com um deslocamento de 25

```javascript
tryCatch(caesarCipher("abc 123!", 25) === "zab 123!");
```

Um deslocamento de 13 codifica uma frase inteira

```javascript
tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) === "gur dhvpx oebja sbk whzcf bire gur ynml qbt");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function caesarCipher(text, shift) {
  const a = "a".charCodeAt(0);
  let result = "";

  for (const char of text) {
    const code = char.charCodeAt(0);
    if (char >= "a" && char <= "z") {
      result += String.fromCharCode(a + ((code - a + shift) % 26));
    } else {
      result += char;
    }
  }

  return result;
}
```
