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
