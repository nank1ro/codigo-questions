Un **commentaire** est une note écrite à l'intérieur du code source pour les personnes qui le lisent. JavaScript ignore complètement les commentaires, ils ne changent donc jamais ce que fait le programme.

Le commentaire le plus simple est le **commentaire sur une ligne** : il commence par `//` et va jusqu'à la fin de la ligne.
```javascript
// Greets the user
console.log("Hello");
```
Utilise les commentaires pour expliquer à quoi sert un morceau de code, ou pourquoi il a été écrit ainsi. Note que, contrairement à d'autres langages, `#` ne commence **pas** un commentaire en JavaScript.

---

Un commentaire n'a pas besoin de sa propre ligne : il peut suivre le code sur la même ligne. C'est un **commentaire en ligne** (ou commentaire de fin de ligne), et c'est un bon endroit pour une courte note sur cette instruction précise :
```javascript
const retries = 3; // give up after three attempts
```
Tout ce qui va de `//` à la fin de la ligne est ignoré, tandis que le code qui le précède s'exécute normalement.

---

Comme les commentaires sont ignorés, ajouter ou supprimer un commentaire ne change jamais ce que fait un programme. Seul le code qui n'est **pas** commenté s'exécute.

Cela fait de `//` un moyen rapide de désactiver une ligne de code sans la supprimer. On appelle cela **mettre en commentaire** :
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
La deuxième ligne est maintenant un commentaire, donc `total` reste `10`. Enlever le `//` ramène la ligne à la vie.

Mettre en commentaire est pratique pendant que tu expérimentes, mais pense à faire le ménage : du code qui reste commenté longtemps ne fait qu'embrouiller la personne qui le lira ensuite.

---

Quand un commentaire a besoin de plus d'une ligne, JavaScript propose le **commentaire multiligne** (aussi appelé commentaire de bloc) : il commence par `/*` et se termine par `*/`, et tout ce qui se trouve entre les deux est ignoré, y compris les retours à la ligne.
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
Un commentaire de bloc peut aussi être court et tenir sur une seule ligne : `/* like this */`.

---

Quel que soit le type de commentaire que tu utilises, la règle est la même : le texte qu'il contient n'est **pas du code**. Un `console.log` dans un commentaire n'affiche jamais rien, et le code écrit après `//` sur la même ligne ne s'exécute jamais, même quand la ligne commence par du vrai code :
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
Quand tu n'es pas sûr de ce qu'affiche un programme, supprime mentalement tous les commentaires et lis ce qui reste.

---

Contrairement à `//`, qui s'arrête à la fin de la ligne, un commentaire `/*` ne s'arrête qu'au `*/`. Si tu oublies de le fermer, JavaScript considère tout le code qui suit comme faisant partie du commentaire et signale une erreur de syntaxe :
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
`//` et `/* */` fonctionnent tous les deux comme commentaires en ligne, mais avec `/*` assure-toi toujours que le `*/` est bien là.

---

En JavaScript, les commentaires de bloc **ne peuvent pas être imbriqués** : le commentaire se termine au **premier** `*/` rencontré, peu importe combien de `/*` le précédaient.
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
Ici le commentaire se termine juste après `inner`, donc `still a comment */` est lu comme du code et provoque une erreur de syntaxe. Garde-le en tête quand tu mets en commentaire un bloc qui contient déjà un commentaire `/* */` : utilise plutôt `//` sur chaque ligne, ou supprime d'abord le commentaire intérieur.

---

Pour mettre plusieurs lignes en commentaire d'un coup, entoure-les d'un seul commentaire de bloc au lieu d'ajouter `//` à chaque ligne :
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
Comme les lignes à l'intérieur du bloc sont ignorées, `total` ne change jamais. Souviens-toi que cela ne fonctionne que si aucune de ces lignes ne contient un `*/`.

---

JavaScript possède un troisième type de commentaire, le **commentaire de documentation**, écrit au format **JSDoc** : un commentaire de bloc qui commence par `/**` (deux astérisques) placé directement au-dessus d'une fonction. À l'intérieur, les lignes commencent en général par ` * ` et des **balises** spéciales commençant par `@` décrivent la fonction :
- `@param {type} name description` pour chaque paramètre
- `@returns {type} description` pour la valeur de retour

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
Pour JavaScript ce n'est qu'un commentaire, mais les éditeurs le lisent et l'affichent comme texte d'aide de `greet`, avec le type écrit entre accolades (`{number}`, `{string}`, `{boolean}`, `{number[]}`...).

---

La première ligne d'un commentaire JSDoc est le **résumé** : une courte phrase qui dit ce que fait la fonction. Écris-la à la troisième personne, comme si tu décrivais la fonction : "Returns...", "Adds...", "Checks...". Ensuite, liste les balises, une par ligne :
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
Le commentaire doit se trouver juste au-dessus de la déclaration, sans ligne vide entre les deux, sinon les éditeurs ne le rattachent pas à la fonction.

---

Un commentaire JSDoc est aussi un **contrat** : il indique à celui qui appelle la fonction ce qu'il doit passer et ce qu'il obtiendra en retour, avant même que le corps ne soit écrit. Lire le commentaire suffit souvent pour implémenter la fonction :
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
Chaque `@param` correspond à un paramètre, dans le même ordre, et `@returns` décrit tous les résultats possibles.

---

L'ordre à l'intérieur d'un commentaire JSDoc est toujours le même : d'abord le résumé, puis un `@param` par paramètre dans l'ordre où ils sont déclarés, puis `@returns` en dernier. L'ouverture `/**` et la fermeture ` */` entourent le tout, et le commentaire se place directement au-dessus de la fonction qu'il décrit :
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

Un fichier JavaScript peut commencer par une ligne spéciale appelée **shebang** (ou hashbang) : `#!` suivi du chemin du programme qui doit exécuter le fichier. Sur les systèmes de type Unix, cela permet de lancer un script directement depuis le terminal, comme `./hello.js`, sans taper `node` d'abord :
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript ignore cette ligne exactement comme un commentaire, mais seulement quand c'est la **toute première ligne** du fichier : ailleurs, `#!` est une erreur de syntaxe. `/usr/bin/env node` signifie "trouve `node` sur ce système et utilise-le".

---

Un bon commentaire explique **pourquoi** le code fait quelque chose, pas **ce** qu'il fait. Le code montre déjà ce qui se passe ; le répéter avec des mots ajoute du bruit et devient obsolète dès que le code change :
```javascript
// set timeout to 30
const timeout = 30;
```
La raison derrière ce nombre est ce qu'un lecteur ne peut pas deviner :
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
Si un commentaire ne fait que répéter la ligne en dessous, supprime-le ou remplace-le par la raison.

---

Certains commentaires suivent une convention que les éditeurs comprennent. Les **marqueurs** les plus courants sont :
- `// TODO: ...` signale quelque chose qui reste à écrire
- `// FIXME: ...` signale du code que l'on sait faux et qui doit être corrigé

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Pour JavaScript ce sont des commentaires ordinaires ; les éditeurs les répertorient pour que le travail en attente soit facile à trouver. Un `TODO` se trouve souvent à côté d'un bouchon qui garde le code fonctionnel jusqu'à ce que la vraie implémentation soit écrite. Quand tu termines le travail, remplace le bouchon et supprime le marqueur dans la même modification : un `TODO` périmé est trompeur.

---

Un `FIXME` est différent d'un `TODO` : le code existe déjà, mais on sait qu'il est faux. Un bon `FIXME` dit quel est le bug et, quand c'est possible, donne un exemple qui le montre, pour que la personne suivante puisse le corriger rapidement. Comme pour `TODO`, supprime le marqueur une fois le bug corrigé, mais garde le commentaire JSDoc, qui reste vrai.
