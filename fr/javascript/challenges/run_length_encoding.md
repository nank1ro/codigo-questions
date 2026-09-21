---
language: javascript
exerciseType: 1
difficulty: 2
title: Codage par plages
---

# --description--

Le codage par plages est l'une des plus vieilles astuces de compression qui existent : au lieu d'écrire le même caractère encore et encore, on écrit combien de fois il se répète, puis le caractère lui-même.

Un télécopieur qui scanne une page quasiment vide rencontre de longues plages de pixels identiques : une rangée de douze `W` parcourt ainsi la ligne sous la forme bien plus courte `12W`. Quand un caractère n'apparaît qu'une seule fois, le compter n'apporte rien, si bien qu'il est copié tel quel.

# --instructions--

Écrivez une fonction `encodeRun` qui prend une chaîne `text` et retourne sa forme encodée par plages.

Chaque plage du même caractère répété au moins deux fois devient la longueur de cette plage écrite en décimal, suivie de ce caractère. Une plage de longueur un est copiée comme le seul caractère, sans nombre devant lui.

Exemples :
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Le texte ne contient que des lettres majuscules de `A` à `Z` et des espaces.
- Une plage de plus de neuf caractères utilise son comptage décimal complet : douze `W` deviennent donc `12W` et jamais `9W3W`.
- Les espaces sont des caractères ordinaires : elles sont comptées et encodées exactement comme les lettres.
- La chaîne vide s'encode en chaîne vide.

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
function encodeRun(text) {
  
}
```

# --asserts--

La chaîne vide s'encode en chaîne vide

```javascript
tryCatch(encodeRun("") === "");
```

Un caractère seul est copié tel quel

```javascript
tryCatch(encodeRun("A") === "A");
```

Une chaîne sans répétitions passe inchangée

```javascript
tryCatch(encodeRun("ABCDE") === "ABCDE");
```

Une plage de deux devient le comptage suivi du caractère

```javascript
tryCatch(encodeRun("AA") === "2A");
```

L'exemple mixte "AABCCCDEEEE" devient "2AB3CD4E"

```javascript
tryCatch(encodeRun("AABCCCDEEEE") === "2AB3CD4E");
```

Une plage de douze utilise son comptage décimal complet, donc le résultat commence par "12W"

```javascript
tryCatch(encodeRun("WWWWWWWWWWWWBWW") === "12WB2W");
```

Les plages d'espaces sont encodées exactement comme les plages de lettres

```javascript
tryCatch(encodeRun("  HI  ") === "2 HI2 ");
```

Une plage de dix s'écrit "10A", jamais comme deux plages plus courtes

```javascript
tryCatch(encodeRun("AAAAAAAAAA") === "10A");
```

Les caractères isolés qui alternent sont tous copiés tels quels

```javascript
tryCatch(encodeRun("ABABAB") === "ABABAB");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function encodeRun(text) {
  let result = "";
  let i = 0;

  while (i < text.length) {
    let run = 1;
    while (i + run < text.length && text[i + run] === text[i]) {
      run++;
    }
    if (run > 1) {
      result += run;
    }
    result += text[i];
    i += run;
  }

  return result;
}
```
