---
language: javascript
exerciseType: 1
difficulty: 1
title: Gouttes de pluie
---

# --description--

Votre tâche est de convertir un nombre en une chaîne qui contient les sons de gouttes de pluie correspondant à certains facteurs potentiels.
Un facteur est un nombre qui divise uniformément un autre nombre sans laisser de reste.
Le moyen le plus simple de vérifier si un nombre est un facteur d'un autre est d'utiliser l'opération modulo.
Les règles des gouttes de pluie sont les suivantes :

- a 3 comme facteur, ajouter 'Pling' au résultat.
- a 5 comme facteur, ajouter 'Plang' au résultat.
- a 7 comme facteur, ajouter 'Plong' au résultat.
- n'a pas 3, 5 ou 7 comme facteur, le résultat doit être les chiffres du nombre.

# --instructions--

Écrivez une fonction qui retourne la chaîne correcte, exemples :

- 28 a 7 comme facteur, mais pas 3 ou 5, donc le résultat serait `"Plong"`.
- 30 a à la fois 3 et 5 comme facteurs, mais pas 7, donc le résultat serait `"PlingPlang"`.
- 34 n'est pas factorisé par 3, 5 ou 7, donc le résultat serait `"34"`.

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

Le son pour 1 est "1"

```javascript
tryCatch(convert(1) === "1");
```

Le son pour 3 est "Pling"

```javascript
tryCatch(convert(3) === "Pling");
```

Le son pour 5 est "Plang"

```javascript
tryCatch(convert(5) === "Plang");
```

Le son pour 7 est "Plong"

```javascript
tryCatch(convert(7) === "Plong");
```

Le son pour 6 est "Pling"

```javascript
tryCatch(convert(6) === "Pling");
```

Le son pour 8 est "8"

```javascript
tryCatch(convert(8) === "8");
```

Le son pour 9 est "Pling"

```javascript
tryCatch(convert(9) === "Pling");
```

Le son pour 10 est "Plang"

```javascript
tryCatch(convert(10) === "Plang");
```

Le son pour 14 est "Plong"

```javascript
tryCatch(convert(14) === "Plong");
```

Le son pour 15 est "PlingPlang"

```javascript
tryCatch(convert(15) === "PlingPlang");
```

Le son pour 21 est "PlingPlong"

```javascript
tryCatch(convert(21) === "PlingPlong");
```

Le son pour 25 est "Plang"

```javascript
tryCatch(convert(25) === "Plang");
```

Le son pour 27 est "Pling"

```javascript
tryCatch(convert(27) === "Pling");
```

Le son pour 35 est "PlangPlong"

```javascript
tryCatch(convert(35) === "PlangPlong");
```

Le son pour 49 est "Plong"

```javascript
tryCatch(convert(49) === "Plong");
```

Le son pour 52 est "52"

```javascript
tryCatch(convert(52) === "52");
```

Le son pour 105 est "PlingPlangPlong"

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

Le son pour 3125 est "Plang"

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
