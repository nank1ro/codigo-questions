---
language: javascript
exerciseType: 1
difficulty: 2
title: Tri à bulles
---

# --description--

Le tri à bulles est l'un des algorithmes de tri les plus simples. Il parcourt une liste et compare chaque paire d'éléments adjacents, en les échangeant dès qu'ils sont dans le mauvais ordre. Après chaque passage complet, la plus grande valeur restante a « remonté » jusqu'à sa position finale, et la liste est triée dès qu'un passage se termine sans le moindre échange.

# --instructions--

Écrivez une fonction appelée `bubbleSort` qui prend un tableau d'entiers et retourne un **nouveau** tableau avec les mêmes valeurs triées par ordre croissant. Le tableau passé en paramètre ne doit pas être modifié.

Vous devez implémenter l'algorithme de tri à bulles vous-même, en comparant et en échangeant les éléments adjacents. N'utilisez pas de fonction de tri de la bibliothèque standard.

Votre fonction doit également fonctionner avec un tableau vide, un tableau d'un seul élément, un tableau déjà trié, des valeurs répétées et des nombres négatifs.

Exemple d'appel de fonction :
```javascript
console.log(bubbleSort([3, 1, 2]));
// affiche [ 1, 2, 3 ]
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

Un tableau vide doit retourner un tableau vide

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

Un tableau d'un seul élément doit rester identique

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

Un tableau déjà trié doit conserver le même ordre

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

Un tableau trié à l'envers doit être mis en ordre croissant

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

Toutes les valeurs répétées doivent être conservées

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

Les nombres négatifs doivent être triés avant les positifs

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

Un tableau mixte plus long doit être trié par ordre croissant

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

Le tableau passé en paramètre ne doit pas être modifié

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
