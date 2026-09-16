---
language: javascript
exerciseType: 1
difficulty: 2
title: Chiffre de César
---

# --description--

Jules César protégeait ses lettres privées avec l'une des plus anciennes astuces de la cryptographie : il remplaçait chaque lettre d'un message par la lettre située un nombre fixe de positions plus loin dans l'alphabet. Avec un décalage de 3, `a` devient `d`, `b` devient `e` et `c` devient `f`.

L'alphabet se comporte comme un cercle, ainsi les lettres de la fin reviennent au début : avec un décalage de 3, `x` devient `a`, `y` devient `b` et `z` devient `c`.

Tout ce qui n'est pas une lettre, comme un espace, une virgule, un point d'exclamation ou un chiffre, traverse le chiffrement sans être modifié.

# --instructions--

Écrivez une fonction `caesarCipher` qui prend un message `text` et un nombre entier `shift`, et retourne le message encodé.

Exemples :
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- Le message est toujours en minuscules, vous n'avez donc jamais à gérer de lettres majuscules.
- Les caractères qui ne sont pas des lettres conservent leur place et leur valeur.
- Le décalage n'est jamais négatif. Un décalage de `0` laisse le message inchangé, et il en va de même pour un décalage de `26`.

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

Un décalage de 3 transforme "hello" en "khoor"

```javascript
tryCatch(caesarCipher("hello", 3) === "khoor");
```

La fin de l'alphabet revient au début, ainsi "xyz" devient "abc"

```javascript
tryCatch(caesarCipher("xyz", 3) === "abc");
```

Un décalage de 0 laisse le message inchangé

```javascript
tryCatch(caesarCipher("abc", 0) === "abc");
```

Un décalage de 26 correspond à un tour complet de l'alphabet, le message est donc inchangé

```javascript
tryCatch(caesarCipher("abc", 26) === "abc");
```

La ponctuation et les espaces passent sans être modifiés

```javascript
tryCatch(caesarCipher("codigo, rocks!", 5) === "htinlt, wthpx!");
```

Un message vide reste vide

```javascript
tryCatch(caesarCipher("", 4) === "");
```

Les espaces entre les lettres isolées sont conservés

```javascript
tryCatch(caesarCipher("a b c", 1) === "b c d");
```

Les chiffres ne sont pas décalés, même avec un décalage de 25

```javascript
tryCatch(caesarCipher("abc 123!", 25) === "zab 123!");
```

Un décalage de 13 encode une phrase entière

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
