En JavaScript une fonction est une **valeur** : tu peux la stocker dans une variable, la mettre dans un tableau et la passer à une autre fonction en argument. Une fonction qui reçoit une fonction en argument, ou qui en renvoie une, s'appelle une **fonction d'ordre supérieur**. La fonction passée s'appelle un **callback**, car celui qui la reçoit *la rappelle* quand il en a besoin :
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
Remarque que `shout` est passée **sans parenthèses** : `twice(shout, "hi")` transmet la fonction elle-même, alors que `twice(shout("hi"), "hi")` appellerait d'abord `shout` et passerait son résultat, la chaîne `"HI!"`, qui ne peut pas être appelée.

---

Les fonctions d'ordre supérieur permettent de séparer *ce qu'il faut faire avec chaque élément* de *la façon de parcourir les éléments*. La partie qui parcourt est écrite une seule fois, et le callback décide du reste :
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
Le callback reçoit un élément à la fois. Cela peut être une fonction fléchée écrite en ligne, comme ci-dessus, ou n'importe quelle fonction stockée dans une variable. C'est exactement ainsi que fonctionnent en interne les méthodes de tableau que tu vas découvrir ensuite.

---

La méthode intégrée `map` fait ce que fait `transform` : elle appelle le callback pour chaque élément et rassemble les résultats dans un **nouveau tableau**. `forEach` appelle aussi le callback pour chaque élément, mais ne rassemble rien et renvoie toujours `undefined` ; utilise-la uniquement pour les effets de bord, comme afficher :
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
Une erreur courante est de stocker le résultat de `forEach` ou d'enchaîner une autre méthode après : il n'y a rien à enchaîner, car elle renvoie `undefined`. Règle simple : utilise `map` quand tu as besoin des nouvelles valeurs, `forEach` quand tu veux seulement *faire* quelque chose.

---

Deux autres méthodes d'ordre supérieur couvrent la plupart des besoins quotidiens.
`filter(callback)` renvoie un nouveau tableau contenant uniquement les éléments pour lesquels le callback renvoie `true` ; un callback qui répond oui ou non de cette manière s'appelle un **prédicat**.
`reduce(callback, initialValue)` combine tous les éléments en une seule valeur : le callback reçoit l'**accumulateur** (le résultat obtenu jusque-là) et l'élément courant, et renvoie le nouvel accumulateur. Le second argument de `reduce` est l'accumulateur de départ :
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
Comme `filter` et `map` renvoient des tableaux, tu peux les enchaîner et terminer par `reduce` : `numbers.filter(...).map(...).reduce(...)`.

---

Trois méthodes répondent à des questions sur un tableau à l'aide d'un prédicat :
- `find(predicate)` renvoie le **premier** élément pour lequel le prédicat vaut `true`, ou `undefined` s'il n'y en a aucun
- `some(predicate)` renvoie `true` si **au moins un** élément satisfait le prédicat
- `every(predicate)` renvoie `true` si **tous** les éléments le satisfont (et `true` pour un tableau vide)
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
Toutes trois s'arrêtent dès que la réponse est connue, elles ne regardent donc jamais plus d'éléments que nécessaire.

---

`sort(compare)` trie un tableau **sur place** à l'aide d'un callback qui reçoit deux éléments et renvoie un nombre négatif quand le premier doit venir en premier, un nombre positif quand c'est le second, ou `0` quand ils sont égaux. Pour les nombres, `(a, b) => a - b` trie par ordre croissant et `(a, b) => b - a` par ordre décroissant.
Sans comparateur, `sort()` convertit chaque élément en **chaîne** et les compare caractère par caractère, donc `10` vient avant `9` parce que `"1"` est inférieur à `"9"` :
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
Comme `sort` modifie le tableau, trie une copie quand tu as aussi besoin de l'ordre d'origine : `[...numbers].sort(...)`. Pour les chaînes, utilise `(a, b) => a.localeCompare(b)` comme comparateur, qui ordonne le texte alphabétiquement.

---

Le comparateur peut regarder n'importe quelle partie des éléments, donc un tableau d'objets se trie selon l'une de leurs propriétés simplement en comparant cette propriété :
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
Trier la copie laisse `items` dans son ordre d'origine.

---

Une fonction d'ordre supérieur peut aussi **renvoyer** une fonction. La fonction renvoyée se souvient des variables de l'endroit où elle a été créée, même après la fin de la fonction externe : c'est ce qu'on appelle une **closure**.
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
Chaque appel à `makeMultiplier` crée une nouvelle fonction avec son propre `factor`. C'est ainsi que l'on construit une famille de fonctions similaires à partir d'un seul modèle. La même chose peut s'écrire avec des fonctions fléchées : `const makeMultiplier = (factor) => (n) => n * factor;`.

---

Une closure garde un lien **vivant** vers la variable, pas une copie de sa valeur. Quand plusieurs fonctions sont créées lors du même appel, elles partagent la même variable, et toute modification faite par l'une est visible par les autres :
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
Personne ne peut lire ou réinitialiser `count` depuis l'extérieur, sauf à travers ces deux fonctions : la variable est **privée**. Un second appel à `makeCounter()` crée un `count` complètement séparé.

---

Comme les fonctions sont des valeurs, tu peux écrire une fonction d'ordre supérieur qui **combine** deux fonctions en une nouvelle. `compose(f, g)` renvoie une fonction qui applique d'abord `g` puis `f` au résultat, comme la notation mathématique *f(g(x))* :
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
L'ordre compte : `compose(f, g)` exécute d'abord `g`, puis `f`. Construire des programmes en collant ainsi de petites fonctions s'appelle la **composition de fonctions**.

---

Une fonction qui renvoie une fonction est aussi la façon naturelle d'**adapter** un callback. Suppose que tu aies un prédicat et qu'il te faille son contraire pour `filter` : au lieu de le réécrire, enveloppe-le :
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
Un `not(predicate)` générique ferait cela pour n'importe quel prédicat : il renvoie une nouvelle fonction qui appelle `predicate` avec le même argument et inverse le résultat avec `!`. Les prédicats de `filter`, `find`, `some` et `every` reçoivent l'élément en premier argument, l'enveloppe n'a donc qu'à transmettre cette seule valeur.

---

L'accumulateur de `reduce` n'est pas forcément un nombre : ce peut être une chaîne, un tableau ou un objet. En partant d'un objet vide `{}`, tu peux compter ou regrouper des choses en une seule passe. N'oublie pas de **renvoyer l'accumulateur** depuis le callback, sinon l'étape suivante reçoit `undefined` :
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` lit le compte actuel, ou `0` quand cette clé n'existe pas encore.

---

Toute fonction possède une méthode `bind` qui renvoie une **nouvelle** fonction avec certaines choses fixées à l'avance. Son premier argument devient le `this` de la nouvelle fonction ; les arguments restants sont placés devant ceux avec lesquels la nouvelle fonction est appelée (une **application partielle**) :
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
Fixer `this` est important pour les méthodes. Quand une méthode est copiée hors de son objet et appelée seule, `this` ne désigne plus l'objet, donc `this.name` devient `undefined`. `bind` le verrouille sur l'objet :
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
La fonction d'origine n'est jamais modifiée : `bind` construit toujours une nouvelle fonction, dont le `name` est le nom d'origine précédé de `bound `.

---

Les vrais programmes combinent ces méthodes en un **pipeline** : filtre les éléments qui t'intéressent, mappe-les vers les valeurs dont tu as besoin, et réduis-les en un résultat. Stocker les tableaux intermédiaires dans des constantes garde chaque étape lisible et permet de les réutiliser :
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` transforme un tableau de chaînes en une seule chaîne dont les éléments sont séparés par une virgule et une espace.

---

Les closures permettent à une fonction renvoyée de garder un **état privé** entre les appels. Un utilitaire classique construit ainsi est `once(fn)` : il renvoie une fonction qui exécute `fn` seulement la première fois qu'elle est appelée, mémorise le résultat, et renvoie ce même résultat à chaque appel suivant sans réexécuter `fn` :
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
L'enveloppe a besoin de deux variables privées : si `fn` a déjà été exécutée, et le résultat mémorisé. Toutes deux vivent dans la closure, invisibles depuis l'extérieur. Pour transmettre à `fn` tous les arguments de l'enveloppe, déclare l'enveloppe avec un paramètre du reste `(...args)` et appelle `fn(...args)`.

---

Tout se rejoint dans `groupBy(items, keyFn)` : une fonction d'ordre supérieur qui reçoit un callback décidant la **clé de groupe** de chaque élément et renvoie un objet associant chaque clé au tableau des éléments ayant cette clé. `reduce` avec un accumulateur objet fait tout le travail :
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
Pour chaque élément, calcule la clé, crée le tableau de cette clé s'il n'existe pas encore (`acc[key] ?? []`), ajoute l'élément et renvoie l'accumulateur. Comme l'appelant choisit `keyFn`, la même fonction regroupe des mots par initiale, des personnes par ville ou des nombres par parité.
