---
language: javascript
exerciseType: 1
difficulty: 2
title: Recherche binaire
---

# --description--

La recherche binaire trouve une valeur dans une collection **triée** en divisant à plusieurs reprises la plage de recherche par deux : regarde l'élément du milieu et, si ce n'est pas celui que tu cherches, continue dans la moitié gauche lorsque la valeur cherchée est plus petite ou dans la moitié droite lorsqu'elle est plus grande.

Comme chaque étape écarte la moitié des éléments restants, la recherche binaire atteint la réponse en quelques comparaisons même sur de très grandes collections, alors que vérifier les éléments un par un coûterait autant d'étapes qu'il y a d'éléments.

# --instructions--

Écris une fonction `binarySearch` qui prend un tableau d'entiers trié par ordre croissant et un entier cherché, et renvoie l'index de la valeur cherchée dans le tableau, ou `-1` lorsque la valeur n'est pas présente.

Le tableau ne contient jamais de doublons, l'index est donc toujours unique. Le tableau peut aussi être vide. Ta fonction doit utiliser la recherche binaire, en divisant la plage de recherche par deux à chaque étape, et non un parcours linéaire.

Exemple d'appel de fonction :
```javascript
console.log(binarySearch([1, 3, 5, 7], 5));
// prints 2
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

Rechercher dans un tableau vide doit renvoyer -1

```javascript
tryCatch(binarySearch([], 7) === -1);
```

Rechercher 5 dans `[5]` doit renvoyer 0

```javascript
tryCatch(binarySearch([5], 5) === 0);
```

Rechercher 9 dans `[5]` doit renvoyer -1

```javascript
tryCatch(binarySearch([5], 9) === -1);
```

Le premier élément -9 du tableau de 12 éléments doit être trouvé à l'index 0

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9) === 0);
```

Le dernier élément 78 du tableau de 12 éléments doit être trouvé à l'index 11

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78) === 11);
```

L'élément 15 doit être trouvé à l'index 6

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15) === 6);
```

L'élément 22 doit être trouvé à l'index 7

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22) === 7);
```

La valeur 12, qui se situe entre 11 et 15, doit renvoyer -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12) === -1);
```

Une valeur cherchée plus petite que tous les éléments doit renvoyer -1

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100) === -1);
```

Une valeur cherchée plus grande que tous les éléments doit renvoyer -1

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
