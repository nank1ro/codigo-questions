Une **chaîne de caractères** (string) est une séquence de caractères entourée de guillemets, comme `"hello"` ou `'hello'`.
Chaque chaîne possède une propriété `length` qui indique combien de caractères elle contient :
```javascript
let greeting = "hello";
console.log(greeting.length);
// affiche 5
```
Les espaces et la ponctuation comptent aussi comme des caractères.

---

Chaque caractère d'une chaîne a un **index**, en commençant à `0`.
Tu peux lire un caractère unique avec des crochets ou avec la méthode `charAt()` :
```javascript
let word = "hello";
console.log(word[0]);
// affiche h
console.log(word.charAt(1));
// affiche e
```
Le dernier caractère se trouve à l'index `length - 1` :
```javascript
console.log(word[word.length - 1]);
// affiche o
```

---

Les chaînes disposent de nombreuses **méthodes** intégrées. Deux des plus simples changent la casse de chaque lettre :
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// affiche HELLO
console.log(word.toLowerCase());
// affiche hello
```
Ces deux méthodes ne prennent aucun argument, alors n'oublie pas les parenthèses.

---

Pour vérifier si une chaîne contient une autre chaîne, utilise ces méthodes, qui renvoient toutes un booléen :
- `includes(text)` vaut `true` si `text` apparaît n'importe où
- `startsWith(text)` vaut `true` si la chaîne commence par `text`
- `endsWith(text)` vaut `true` si la chaîne se termine par `text`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// affiche true
console.log(file.startsWith("ph"));
// affiche true
console.log(file.endsWith(".jpg"));
// affiche false
```
La comparaison est sensible à la casse : `"Hello".includes("h")` vaut `false`.

---

La méthode `indexOf()` renvoie l'index où un morceau de texte apparaît **pour la première fois** dans la chaîne.
Si le texte n'est pas trouvé, elle renvoie `-1` :
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// affiche 2
console.log(word.indexOf("z"));
// affiche -1
```

---

La méthode `slice(start, end)` extrait une partie d'une chaîne, de l'index `start` jusqu'à (sans l'inclure) l'index `end` :
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// affiche Java
console.log(word.slice(4));
// affiche Script
```
Si tu omets `end`, l'extrait va jusqu'à la fin de la chaîne.
Un index négatif compte à partir de la fin : `word.slice(-3)` vaut `"ipt"`.
La méthode `substring(start, end)` fonctionne de la même façon, mais n'accepte pas d'index négatifs.

---

`indexOf()` et `slice()` fonctionnent bien ensemble : trouve où se trouve quelque chose, puis découpe la chaîne à cet endroit.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// affiche 45
```

---

La méthode `split(separator)` découpe une chaîne en un **tableau** de morceaux, en coupant à chaque `separator` :
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// affiche [ 'I', 'like', 'JavaScript' ]
```
L'opération inverse est la méthode de tableau `join(separator)`, qui recolle les morceaux en une chaîne :
```javascript
console.log(words.join("-"));
// affiche I-like-JavaScript
```

---

La saisie utilisateur contient souvent des espaces superflus. La méthode `trim()` renvoie une copie de la chaîne dont les espaces ont été supprimés aux **deux** extrémités :
```javascript
let input = "   hello   ";
console.log(input.trim());
// affiche hello
```
`trimStart()` supprime uniquement les espaces au début et `trimEnd()` uniquement ceux à la fin.
Les espaces au milieu de la chaîne ne sont jamais touchés.

---

La méthode `replace(search, replacement)` renvoie une nouvelle chaîne dans laquelle la **première** occurrence de `search` est remplacée par `replacement` :
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// affiche blue red
```
Pour remplacer **chaque** occurrence, utilise `replaceAll()` :
```javascript
console.log(text.replaceAll("red", "blue"));
// affiche blue blue
```

---

La méthode `repeat(count)` renvoie la chaîne répétée `count` fois :
```javascript
console.log("ab".repeat(3));
// affiche ababab
console.log("ab".repeat(0));
// affiche une chaîne vide
```

---

La méthode `padStart(targetLength, padString)` ajoute `padString` au **début** de la chaîne jusqu'à atteindre `targetLength` caractères. `padEnd()` fait la même chose à la fin :
```javascript
console.log("7".padStart(3, "0"));
// affiche 007
console.log("Tea".padEnd(6, "."));
// affiche Tea...
```
Si la chaîne est déjà assez longue, elle est renvoyée inchangée.
Les nombres n'ont pas de méthodes de chaîne, alors convertis-les d'abord avec `String(number)`.

---

Deux chaînes sont égales avec `===` seulement si elles ont exactement les mêmes caractères, dans la même casse :
```javascript
console.log("hello" === "hello");
// affiche true
console.log("hello" === "Hello");
// affiche false
```
Les opérateurs `<` et `>` comparent les chaînes par ordre alphabétique, caractère par caractère.
Les majuscules viennent avant les minuscules, donc `"Zoo" < "apple"` vaut `true`.

---

Les chaînes sont **immuables** : une fois créée, une chaîne ne peut jamais être modifiée.
Assigner à un index ne fait rien, et chaque méthode de chaîne renvoie une **nouvelle** chaîne au lieu de modifier l'originale :
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// affiche hello
word.toUpperCase();
console.log(word);
// affiche hello
```
Pour conserver un résultat, réassigne-le à la variable :
```javascript
word = word.toUpperCase();
```

---

Appeler `split("")` avec un séparateur vide transforme une chaîne en un tableau de ses caractères individuels.
Les tableaux ont une méthode `reverse()`, donc tu peux inverser une chaîne en la découpant, en l'inversant et en la recollant :
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// affiche cba
```
