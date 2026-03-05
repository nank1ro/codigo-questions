---
language: javascript
exerciseType: 1
difficulty: 1
title: Pingos de chuva
---

# --description--

Sua tarefa é converter um número em uma string que contenha sons de pingos de chuva correspondentes a certos fatores potenciais.
Um fator é um número que divide outro número de forma exata, sem deixar resto.
A maneira mais simples de testar se um número é fator de outro é usar a operação de módulo.
As regras dos pingos de chuva são as seguintes:

- tem 3 como fator, adicione 'Pling' ao resultado.
- tem 5 como fator, adicione 'Plang' ao resultado.
- tem 7 como fator, adicione 'Plong' ao resultado.
- não tem 3, 5 ou 7 como fator, o resultado deve ser os dígitos do número.

# --instructions--

Escreva uma função que retorne a string correta, exemplos:

- 28 tem 7 como fator, mas não 3 ou 5, então o resultado seria `"Plong"`.
- 30 tem 3 e 5 como fatores, mas não 7, então o resultado seria `"PlingPlang"`.
- 34 não é divisível por 3, 5 ou 7, então o resultado seria `"34"`.

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
function convert(number) {
  
}
```

# --asserts--

O som para 1 é "1"

```javascript
tryCatch(convert(1) === "1");
```

O som para 3 é "Pling"

```javascript
tryCatch(convert(3) === "Pling");
```

O som para 5 é "Plang"

```javascript
tryCatch(convert(5) === "Plang");
```

O som para 7 é "Plong"

```javascript
tryCatch(convert(7) === "Plong");
```

O som para 6 é "Pling"

```javascript
tryCatch(convert(6) === "Pling");
```

O som para 8 é "8"

```javascript
tryCatch(convert(8) === "8");
```

O som para 9 é "Pling"

```javascript
tryCatch(convert(9) === "Pling");
```

O som para 10 é "Plang"

```javascript
tryCatch(convert(10) === "Plang");
```

O som para 14 é "Plong"

```javascript
tryCatch(convert(14) === "Plong");
```

O som para 15 é "PlingPlang"

```javascript
tryCatch(convert(15) === "PlingPlang");
```

O som para 21 é "PlingPlong"

```javascript
tryCatch(convert(21) === "PlingPlong");
```

O som para 25 é "Plang"

```javascript
tryCatch(convert(25) === "Plang");
```

O som para 27 é "Pling"

```javascript
tryCatch(convert(27) === "Pling");
```

O som para 35 é "PlangPlong"

```javascript
tryCatch(convert(35) === "PlangPlong");
```

O som para 49 é "Plong"

```javascript
tryCatch(convert(49) === "Plong");
```

O som para 52 é "52"

```javascript
tryCatch(convert(52) === "52");
```

O som para 105 é "PlingPlangPlong"

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

O som para 3125 é "Plang"

```javascript
tryCatch(convert(3125) === "Plang");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convert(number) {
  var result = ""
  if (number % 3 == 0) {
    result += "Pling"
  }
  if (number % 5 == 0) {
    result += "Plang"
  }
  if (number % 7 == 0) {
    result += "Plong"
  }
  if (!result) {
    result = number.toString()
  }
  return result
}
```
