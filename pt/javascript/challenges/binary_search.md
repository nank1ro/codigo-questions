---
language: javascript
exerciseType: 1
difficulty: 2
title: Busca binária
---

# --description--

A busca binária encontra um valor dentro de uma coleção **ordenada** dividindo o intervalo de busca pela metade repetidamente: olhe o elemento no meio e, se não for o que você procura, continue na metade esquerda quando o alvo for menor ou na metade direita quando o alvo for maior.

Como cada etapa descarta metade dos elementos restantes, a busca binária chega à resposta em poucas comparações, mesmo em coleções muito grandes, enquanto verificar os elementos um por um custaria tantos passos quanto o número de elementos.

# --instructions--

Escreva uma função `binarySearch` que recebe um array de inteiros ordenado em ordem crescente e um inteiro alvo, e retorna o índice do alvo dentro do array, ou `-1` quando o alvo não está presente.

O array nunca contém duplicatas, então o índice é sempre único. O array também pode estar vazio. Sua função deve usar busca binária, dividindo o intervalo de busca pela metade a cada passo, e não uma varredura linear.

Exemplo de chamada da função:
```javascript
console.log(binarySearch([1, 3, 5, 7], 5));
// imprime 2
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
function binarySearch(arr, target) {
  
}
```

# --asserts--

A busca em um array vazio deve retornar -1

```javascript
tryCatch(binarySearch([], 7) === -1);
```

A busca por 5 em `[5]` deve retornar 0

```javascript
tryCatch(binarySearch([5], 5) === 0);
```

A busca por 9 em `[5]` deve retornar -1

```javascript
tryCatch(binarySearch([5], 9) === -1);
```

O primeiro elemento -9 do array de 12 elementos deve ser encontrado no índice 0

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9) === 0);
```

O último elemento 78 do array de 12 elementos deve ser encontrado no índice 11

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78) === 11);
```

O elemento 15 deve ser encontrado no índice 6

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15) === 6);
```

O elemento 22 deve ser encontrado no índice 7

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22) === 7);
```

O valor 12, que está entre 11 e 15, deve retornar -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12) === -1);
```

Um alvo menor que todos os elementos deve retornar -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100) === -1);
```

Um alvo maior que todos os elementos deve retornar -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100) === -1);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) {
      return mid;
    }
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}
```
