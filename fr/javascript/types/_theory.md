Chaque valeur en JavaScript possède un **type**. Il existe sept types **primitifs** :
- `number` pour n'importe quel nombre, comme `42` ou `3.14`
- `string` pour du texte, comme `"Ana"`
- `boolean` pour `true` et `false`
- `undefined` pour une valeur qui n'a jamais été fournie
- `null` pour une valeur volontairement vide
- `bigint` pour des nombres entiers de n'importe quelle taille, comme `9007199254740993n`
- `symbol` pour des identifiants uniques créés avec `Symbol()`

Tout le reste (tableaux, fonctions, objets créés avec `{}`, dates...) est un `object`.
L'opérateur `typeof` vous indique le type d'une valeur, sous forme de chaîne :
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript est **à typage dynamique** : une variable n'a pas de type propre, seule la valeur qu'elle contient actuellement en a un. La même variable peut contenir un nombre maintenant et une chaîne plus tard, et `typeof` suit la valeur :
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
C'est pratique, mais cela signifie aussi qu'une fonction peut recevoir une valeur d'un type inattendu, donc vérifier avec `typeof` est une première étape courante. Comme `typeof` renvoie une chaîne, vous comparez son résultat avec une chaîne :
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof` a quelques réponses qui surprennent.
Les fonctions obtiennent leur propre réponse, `"function"`, même si ce sont des objets :
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
Les tableaux n'obtiennent **pas** leur propre réponse : ils sont simplement `"object"`, tout comme `{}` :
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
Et `typeof null` vaut `"object"`, un bug historique qui n'a jamais été corrigé. `typeof` distingue donc bien les primitives et les fonctions, mais il ne sait pas différencier un tableau, un objet et `null`.

---

Vous pouvez convertir une valeur vers un autre type **explicitement** en appelant le type comme une fonction :
- `Number(value)` convertit en nombre : `Number("42")` vaut `42`
- `String(value)` convertit en chaîne : `String(42)` vaut `"42"`
- `Boolean(value)` convertit en booléen : `Boolean("")` vaut `false`

Le résultat est une toute nouvelle valeur ; l'originale n'est pas modifiée :
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
Convertir explicitement rend votre intention visible : quiconque lit `Number(input)` sait que `input` était du texte.

---

`Number()` est strict : la chaîne entière doit être un nombre, sinon le résultat est `NaN` ("Not a Number") :
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()` et `parseFloat()` sont plus tolérants : ils lisent les chiffres depuis le début de la chaîne, ignorent les espaces de début et s'arrêtent au premier caractère qui ne fait pas partie d'un nombre. `parseInt` ne garde que la partie entière :
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
Quand la chaîne ne commence pas par quelque chose qui peut débuter un nombre (un signe optionnel, puis un chiffre), ils renvoient aussi `NaN` :
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN` est la seule valeur qui n'est pas égale à elle-même, donc `x === NaN` est toujours `false` ; pour la détecter, utilisez `Number.isNaN(x)`.

---

Il existe deux façons de demander « est-ce que ceci est `NaN` ? », et elles répondent à des questions différentes.
L'ancienne fonction globale `isNaN(value)` **convertit** d'abord `value` en nombre, puis vérifie. Elle répond donc `true` pour tout ce qui ne peut pas devenir un nombre, même si ce n'est pas du tout `NaN` :
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)` ne convertit **pas** : elle vaut `true` uniquement quand `value` est réellement le nombre `NaN` :
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
Préférez `Number.isNaN`, et convertissez d'abord si vous voulez savoir si une conversion a échoué.

---

JavaScript convertit aussi **implicitement**, et l'opérateur `+` est celui qui provoque le plus souvent des surprises. Si l'un des deux côtés est une chaîne, `+` **concatène** et l'autre côté est converti en chaîne :
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
Tous les autres opérateurs arithmétiques convertissent les deux côtés en **nombres** :
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
Additionner des valeurs qui viennent de texte (saisie utilisateur, fichiers, URL) peut donc construire silencieusement une chaîne au lieu d'une somme. Convertissez avec `Number()` avant d'additionner, par sécurité.

---

Un moyen rapide de convertir une chaîne en nombre est le **plus unaire** : un `+` placé devant une seule valeur la convertit exactement comme le fait `Number()` :
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
C'est compact, mais facile à confondre avec une addition, donc beaucoup d'équipes préfèrent le `Number("5")` explicite.

---

L'égalité **large** `==` convertit les deux côtés vers un type commun avant de comparer, en suivant des règles difficiles à retenir :
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
L'égalité **stricte** `===` ne convertit jamais : des valeurs de types différents ne sont tout simplement pas égales :
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
Utilisez `===` (et `!==`) par défaut. La seule exception courante est `value == null`, qui vérifie `null` et `undefined` ensemble.

---

Quand JavaScript a besoin d'un booléen, par exemple dans une condition `if` ou dans `Boolean(value)`, il convertit la valeur. Seules huit valeurs deviennent `false` ; elles sont appelées **falsy** :
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` et `NaN`.
**Tout le reste est truthy**, y compris certaines valeurs qui semblent vides :
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"` est une chaîne non vide, donc elle est truthy ; un tableau vide est un objet, donc il est truthy aussi.

---

Un raccourci courant pour convertir n'importe quelle valeur en booléen est la **double négation** `!!` : le premier `!` convertit en booléen et inverse la valeur, le deuxième l'inverse à nouveau :
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value` et `Boolean(value)` donnent exactement le même résultat ; la forme explicite est plus facile à lire.

---

JavaScript possède un seul type `number` pour les nombres entiers et décimaux : chaque nombre est une valeur flottante 64 bits (un *double*). Donc `5` et `5.0` sont la même valeur, et il n'y a pas de type entier séparé :
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
Pour savoir si un nombre n'a pas de partie fractionnaire, utilisez `Number.isInteger` :
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
Les chaînes de modèle convertissent la valeur interpolée en chaîne avec les mêmes règles que `String()`, donc `${5.0}` devient `"5"`, pas `"5.0"`.

---

Comme les nombres sont des doubles, certains décimaux ne peuvent pas être stockés exactement et de petites erreurs apparaissent :
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
La méthode `toFixed(digits)` arrondit un nombre à `digits` décimales, mais elle renvoie une **chaîne**, ce qui convient pour l'affichage mais est incorrect pour des calculs ultérieurs :
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
Pour obtenir un **nombre** arrondi, reconvertissez le résultat avec `Number()` :
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

Un `number` ne peut représenter exactement des nombres entiers que jusqu'à `Number.MAX_SAFE_INTEGER`, qui vaut `9007199254740991`. Au-delà, des chiffres se perdent :
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
Pour des nombres entiers plus grands, utilisez `bigint` : écrivez le littéral avec un suffixe `n`, ou convertissez avec `BigInt()` :
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
`console.log` affiche le suffixe `n` ; `String(big)` donne les chiffres seuls.
Un `bigint` et un `number` ne peuvent pas être mélangés en arithmétique : `big + 1` lève une `TypeError`. Convertissez explicitement l'un des deux côtés, avec `BigInt(count)` ou `Number(big)`.

---

Comme `typeof` répond `"object"` pour les tableaux, les objets et `null`, les distinguer nécessite deux vérifications supplémentaires.
`Array.isArray(value)` vaut `true` uniquement pour les tableaux :
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
Pour `null`, comparez directement, `value === null`. Les combiner donne une image complète de n'importe quelle valeur :
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
Vérifiez d'abord `null` et les tableaux, car le `typeof` simple ne peut pas les distinguer.

---

Le texte provenant de formulaires, de fichiers ou d'URL est toujours une chaîne, même quand il représente un nombre ou un booléen. Le reconvertir vers le bon type combine ce que vous avez vu : comparez avec `"true"` et `"false"` pour les booléens, et essayez `Number()` pour les nombres, en vous rappelant que `Number("")` vaut `0` et que `Number.isNaN` vous dit quand la conversion a échoué :
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
Quand rien ne correspond, gardez la chaîne telle quelle.
