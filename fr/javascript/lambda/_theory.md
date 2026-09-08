Une fonction n'a pas besoin d'un nom. Une **expression de fonction** crée une fonction comme une valeur, que vous pouvez stocker dans une variable et appeler à travers elle :
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Une **fonction fléchée** est une manière plus courte d'écrire la même chose : retirez le mot-clé `function` et placez une « grosse flèche » `=>` entre la liste des paramètres et le corps :
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Les fonctions fléchées sont généralement stockées dans une `const`, de sorte que le nom ne peut pas être réassigné par erreur, et sont appelées exactement comme n'importe quelle autre fonction.

---

Les fonctions fléchées deviennent plus courtes dans deux cas courants.
Lorsque le corps est une **expression unique**, vous pouvez omettre les accolades et le mot-clé `return` : la valeur de l'expression est renvoyée automatiquement (un **retour implicite**) :
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
Lorsqu'il y a **exactement un paramètre**, vous pouvez aussi omettre les parenthèses autour de celui-ci :
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
Avec zéro paramètre ou avec deux ou plus, les parenthèses sont obligatoires : `() => 42` et `(a, b) => a + b`.

---

Il y a un piège avec le retour implicite. Une fonction fléchée dont le corps commence par `{` est lue comme un **corps de bloc**, jamais comme un littéral objet :
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
Ici `{ name: name }` est un bloc contenant l'étiquette `name:` suivie de l'expression `name`. Rien n'est renvoyé, donc l'appel donne `undefined`.
Pour renvoyer un littéral objet sur une seule ligne, enveloppez-le dans des **parenthèses** afin que JavaScript le traite comme une expression :
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

Envelopper le littéral objet dans des parenthèses est la manière standard de construire des objets avec une fonction fléchée d'une seule ligne, par exemple lorsque vous transformez quelques valeurs en enregistrement :
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
Une fonction fléchée sans paramètre commence par une paire de parenthèses vide `()` :
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

Les fonctions fléchées brillent vraiment en tant que **callbacks** : des fonctions passées comme arguments à d'autres fonctions. Les méthodes d'array en sont l'exemple le plus courant.
`map(callback)` renvoie un nouvel array avec le résultat du callback pour chaque élément, et `filter(callback)` renvoie un nouvel array avec uniquement les éléments pour lesquels le callback renvoie `true` :
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
Les deux renvoient un nouvel array et laissent l'original intact, vous pouvez donc les chaîner : `numbers.filter(...).map(...)`.

---

Deux autres méthodes d'array prennent un callback.
`forEach(callback)` appelle le callback une fois par élément et ne renvoie rien ; utilisez-le pour des effets de bord tels que l'affichage.
`reduce(callback, initialValue)` réduit l'array en une seule valeur : le callback reçoit la valeur accumulée jusqu'à présent et l'élément courant, et renvoie la nouvelle valeur accumulée :
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)` trie un array sur place en utilisant un callback qui reçoit deux éléments et renvoie un nombre négatif lorsque le premier doit venir en premier, un nombre positif lorsque le second doit venir en premier, ou `0` lorsqu'ils sont égaux. Pour les nombres, `(a, b) => a - b` trie dans l'ordre croissant et `(a, b) => b - a` dans l'ordre décroissant.
`find(callback)` renvoie le premier élément pour lequel le callback renvoie `true`, ou `undefined` s'il n'y en a aucun :
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

Les paramètres des fonctions fléchées prennent en charge les mêmes fonctionnalités que les paramètres des fonctions régulières.
Une **valeur par défaut** est utilisée lorsque l'argument est omis ou est `undefined` :
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
Notez qu'un paramètre avec une valeur par défaut a toujours besoin des parenthèses, même lorsqu'il est le seul : `name = "World" => ...` est une erreur de syntaxe.

---

Un **paramètre du reste** `...name` rassemble un nombre quelconque d'arguments dans un array, et cela fonctionne aussi dans les fonctions fléchées :
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
Les fonctions régulières ont également un objet `arguments` caché, semblable à un array, qui contient tous les arguments qu'elles ont reçus. Les fonctions fléchées, **non** : à l'intérieur d'une flèche, `arguments` fait référence aux `arguments` de la fonction englobante ou n'existe pas du tout. Chaque fois que vous avez besoin de « tous les arguments » dans une fonction fléchée, utilisez un paramètre du reste.

---

Une fonction se souvient des variables de la portée où elle a été **créée**, même après que cette portée a fini de s'exécuter. Cela s'appelle une **fermeture**.
L'exemple classique est un créateur de compteur : chaque appel à `makeCounter` crée un nouveau `count` et renvoie une fonction fléchée qui continue d'utiliser ce même `count` :
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
Personne d'autre ne peut lire ou réinitialiser `count` : il vit uniquement à l'intérieur de la fonction renvoyée. Un second appel à `makeCounter()` crée un compteur indépendant avec son propre `count`.

---

Puisqu'une fonction est une valeur, une fonction fléchée peut **renvoyer une autre fonction fléchée**. Chaîner deux flèches est une manière compacte d'écrire une fonction qui construit des fonctions :
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
Lisez-la de gauche à droite : `makeAdder` prend `amount` et renvoie `(n) => n + amount`, une fonction fléchée qui capture `amount` à travers une fermeture. `makeAdder(1)(5)` appelle immédiatement la fonction renvoyée.
