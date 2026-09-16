---
language: javascript
exerciseType: 1
difficulty: 1
title: Distancia de Hamming
---

# --description--

El ADN se escribe como una hebra de nucleótidos, cada uno una sola letra: `A`, `C`, `G` o `T`. Cuando dos hebras de la misma longitud se alinean una junto a la otra, algunas posiciones contienen el mismo nucleótido y otras contienen uno diferente.

El número de posiciones en las que las dos hebras difieren se llama distancia de Hamming, y los biólogos la usan para medir cuán lejos han divergido dos hebras. Alinear `GAGCCTACTAACGGGAT` con `CATCGTAATGACGGCCT` da 7 posiciones que difieren, así que su distancia de Hamming es 7.

# --instructions--

Escribe una función `hammingDistance` que reciba dos hebras de ADN de la misma longitud y devuelva el número de posiciones en las que difieren.

Ejemplos:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Las dos hebras siempre tienen la misma longitud, así que nunca tienes que manejar hebras de longitudes diferentes.
- Dos hebras vacías no difieren en ninguna posición, así que su distancia es 0.

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
function hammingDistance(left, right) {
  
}
```

# --asserts--

Dos hebras vacías no difieren en ninguna posición

```javascript
tryCatch(hammingDistance("", "") === 0);
```

Dos hebras de un solo nucleótido idénticas no tienen ninguna diferencia

```javascript
tryCatch(hammingDistance("A", "A") === 0);
```

Dos hebras de un solo nucleótido diferente difieren en una posición

```javascript
tryCatch(hammingDistance("A", "G") === 1);
```

Dos hebras cortas que difieren en todas las posiciones

```javascript
tryCatch(hammingDistance("AG", "CT") === 2);
```

Dos hebras cortas que difieren solo en la primera posición

```javascript
tryCatch(hammingDistance("AT", "CT") === 1);
```

Un único nucleótido diferente en medio de las hebras

```javascript
tryCatch(hammingDistance("GGACG", "GGTCG") === 1);
```

Los mismos nucleótidos en posiciones diferentes siguen contando como diferencias

```javascript
tryCatch(hammingDistance("TAG", "GAT") === 2);
```

Un par de hebras más largo con cuatro diferencias

```javascript
tryCatch(hammingDistance("GATACA", "GCATAA") === 4);
```

Desplazar una hebra una posición hace que casi todas las posiciones difieran

```javascript
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") === 9);
```

Las dos hebras de la descripción tienen una distancia de siete

```javascript
tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") === 7);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function hammingDistance(left, right) {
  let distance = 0;

  for (let i = 0; i < left.length; i++) {
    if (left[i] !== right[i]) {
      distance++;
    }
  }

  return distance;
}
```
