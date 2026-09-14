---
language: javascript
exerciseType: 1
difficulty: 2
title: Ordenação por bolha
---

# --description--

A ordenação por bolha é um dos algoritmos de ordenação mais simples. Ela percorre uma lista e compara cada par de elementos adjacentes, trocando-os sempre que estão na ordem errada. Depois de cada passagem completa, o maior valor restante "borbulhou" até a sua posição final, e a lista está ordenada assim que uma passagem termina sem uma única troca.

# --instructions--

Escreva uma função chamada `bubbleSort` que receba um array de números inteiros e devolva um **novo** array com os mesmos valores ordenados em ordem crescente. O array passado não deve ser modificado.

Você deve implementar o algoritmo de ordenação por bolha por conta própria, comparando e trocando elementos adjacentes. Não use uma função de ordenação da biblioteca padrão.

A sua função também deve funcionar com um array vazio, um array com um único elemento, um array já ordenado, valores repetidos e números negativos.

Exemplo de chamada de função:
```javascript
console.log(bubbleSort([3, 1, 2]));
// prints [ 1, 2, 3 ]
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

// Returns true if two arrays are equal and in the same order
var arraysMatch = function (arr1, arr2) {
    // Check if the arrays are the same length
    if (arr1.length !== arr2.length) return false;

    // Check if all items exist and are in the same order
    for (var i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }

    // Otherwise, return true
    return true;
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function bubbleSort(arr) {
  
}
```

# --asserts--

Um array vazio deve devolver um array vazio

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

Um array com um único elemento deve permanecer igual

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

Um array já ordenado deve manter a mesma ordem

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

Um array ordenado ao contrário deve ser colocado em ordem crescente

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

Todos os valores repetidos devem ser mantidos

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

Os números negativos devem ser ordenados antes dos positivos

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

Um array misto mais longo deve ser ordenado em ordem crescente

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

O array passado não deve ser modificado

```javascript
const original = [3, 1, 2];
bubbleSort(original);
tryCatch(arraysMatch(original, [3, 1, 2]));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function bubbleSort(arr) {
  const result = [...arr];
  let end = result.length;
  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 1; i < end; i++) {
      if (result[i - 1] > result[i]) {
        const temp = result[i - 1];
        result[i - 1] = result[i];
        result[i] = temp;
        swapped = true;
      }
    }
    end--;
  }
  return result;
}
```
