---
language: javascript
exerciseType: 1
difficulty: 3
title: Ano Bissexto
---

# --description--

Em um ano civil há exatamente 365,25 dias. Mas, eventualmente, isso levará a confusão porque os humanos normalmente contam por divisibilidade exata de 1 e não com casas decimais. Então, para evitar isso, decidiu-se somar todos os 0,25 dias a cada ciclo de quatro anos e dar a esse ano 366 dias (incluindo 29 de fevereiro como dia intercalar) e chamá-lo de __ano bissexto__. Os outros três anos no ciclo de quatro anos teriam apenas 365 dias e __não seriam anos bissextos__.

# --instructions--

Neste desafio vamos levar a outro nível, onde você deve determinar se é um ano bissexto ou não sem o uso da classe `Date`, instruções `switch`, __blocos if__, __blocos if-else__ ou __operador ternário__ (`x ? a : b`) nem os operadores lógicos __AND__ (`&&`) e __OR__ (`||`) com a exceção do operador __NOT__ (`!`).

Retorne `true` se for um ano bissexto, `false` caso contrário.

Exemplo de chamada da função:
```javascript
console.log(leapYear(2000));
// prints true
```

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
function leapYear(year) {
  
}
```

# --asserts--

O uso de `Date`, `switch`, `if`, `else`, `&&`, `||` ou `?` não é permitido.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

O ano `2016` é um ano bissexto.

```javascript
tryCatch(leapYear(2016) == true);
```

O ano `1996` é um ano bissexto.

```javascript
tryCatch(leapYear(1996) == true);
```

O ano `1600` é um ano bissexto.

```javascript
tryCatch(leapYear(1600) == true);
```

O ano `2020` é um ano bissexto.

```javascript
tryCatch(leapYear(2020) == true);
```

O ano `2000` é um ano bissexto.

```javascript
tryCatch(leapYear(2000) == true);
```

O ano `2008` é um ano bissexto.

```javascript
tryCatch(leapYear(2008) == true);
```

O ano `1521` não é um ano bissexto.

```javascript
tryCatch(leapYear(1521) == false);
```

O ano `1800` não é um ano bissexto.

```javascript
tryCatch(leapYear(1800) == false);
```

O ano `2007` não é um ano bissexto.

```javascript
tryCatch(leapYear(2007) == false);
```

O ano `2002` não é um ano bissexto.

```javascript
tryCatch(leapYear(2002) == false);
```

O ano `1979` não é um ano bissexto.

```javascript
tryCatch(leapYear(1979) == false);
```

O ano `2006` não é um ano bissexto.

```javascript
tryCatch(leapYear(2006) == false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function leapYear(year) {
  return (year % 4 === 0) ^ ((year % 100 === 0) & (year % 400 !== 0));
}
```

```javascript
function leapYear(year){
   while(year % 100 === 0) {
     year = year / 100;
   }
  return year % 4 === 0; 
}
```
