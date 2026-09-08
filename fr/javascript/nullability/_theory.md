JavaScript possède deux façons différentes de dire « il n'y a pas de valeur ici ».
`undefined` signifie qu'une valeur n'a **jamais été fournie**. Une variable déclarée sans valeur contient `undefined`, et il en va de même pour une propriété qui n'existe pas dans un objet :
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` est une valeur que **vous** assignez délibérément pour dire « vide, et je le sais » :
```javascript
let owner = null;
console.log(owner);
// prints null
```
Donc `undefined` est généralement le langage qui vous signale qu'il manque quelque chose, tandis que `null` est le programmeur qui déclare que quelque chose est intentionnellement vide.

---

Les fonctions produisent `undefined` dans deux autres situations.
Quand vous appelez une fonction avec **moins d'arguments** qu'elle n'en déclare, les paramètres manquants valent `undefined` :
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
Quand une fonction se termine **sans `return`** (ou avec un simple `return;`), l'appeler donne `undefined` :
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
Notez que passer `null` explicitement n'est pas la même chose que d'omettre l'argument : `greet(null)` affiche `null`, car `null` est une véritable valeur qui a été transmise à la fonction.

---

L'opérateur `typeof` renvoie le type d'une valeur sous forme de chaîne. Pour `undefined`, il répond `"undefined"`, comme on pourrait s'y attendre :
```javascript
let city;
console.log(typeof city);
// prints undefined
```
Pour `null`, en revanche, il répond `"object"`. C'est un bug présent depuis la toute première version de JavaScript et qui n'a jamais été corrigé, car trop de code en dépend :
```javascript
console.log(typeof null);
// prints object
```
`typeof` est donc un moyen fiable de détecter `undefined`, mais pas `null`. Pour vérifier `null`, comparez directement avec lui : `value === null`.

---

Comment `null` et `undefined` se comparent-ils entre eux ? Cela dépend de l'opérateur.
L'égalité **faible** `==` les considère comme la même chose, et les juge différents de toute autre valeur, y compris `0`, `""` et `false` :
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
L'égalité **stricte** `===` compare également le type, et `null` et `undefined` ont des types différents :
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

La plupart du temps, peu importe *laquelle* des deux marques « pas de valeur » vous avez reçue : vous voulez simplement savoir si une valeur est présente.
Comme `null == undefined` vaut `true` et que rien d'autre n'est faiblement égal à `null`, la comparaison `value == null` est l'idiome standard pour détecter **les deux** d'un coup :
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
C'est le seul cas où `==` est préféré à `===` : écrire `value === null || value === undefined` fait exactement le même travail, seulement plus long.
Des valeurs comme `0`, `""` et `false` ne sont *pas* `null` : ce sont de véritables valeurs qui se trouvent être falsy.

---

Lire une propriété de `null` ou `undefined` est une erreur qui arrête le programme :
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` est `undefined`, et `undefined` n'a pas de propriétés. L'opérateur de **chaînage optionnel** `?.` résout ce problème : si la valeur à sa gauche est `null` ou `undefined`, toute l'expression s'arrête et vaut `undefined` au lieu de lever une erreur :
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
Quand le côté gauche a bien une valeur, `?.` se comporte exactement comme un `.` normal. Vous pouvez en chaîner plusieurs : `user.address?.street?.name` renvoie `undefined` dès qu'un maillon manque.

---

Le chaînage optionnel ne se limite pas aux propriétés avec un point. Il existe deux autres formes.
`?.[]` lit un élément ou une clé calculée seulement quand le côté gauche a une valeur :
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` appelle une fonction seulement quand elle existe, ce qui est pratique pour les callbacks optionnels :
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
Dans toutes les formes, la vérification s'applique à la valeur **juste avant** le `?.` : `post?.tags?.[0]` est sûr même quand `post` lui-même est `null` ou `undefined`.

---

Une fois que vous savez qu'une valeur peut être absente, vous voulez généralement une valeur **par défaut** à sa place. Deux opérateurs font cela, et ils diffèrent par ce qu'ils considèrent comme « absent ».
`a || b` renvoie `b` dès que `a` est **falsy** : pas seulement `null` et `undefined`, mais aussi `0`, `""`, `false` et `NaN`.
L'opérateur de **coalescence nullish** `a ?? b` renvoie `b` seulement quand `a` est `null` ou `undefined`, et conserve toute autre valeur :
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
Utilisez `??` quand `0`, `""` ou `false` sont des valeurs légitimes qui doivent être conservées, et `||` quand vous voulez vraiment remplacer toute valeur falsy.

---

Un motif très courant est « remplir cette propriété seulement si elle n'est pas encore définie ». Écrit avec `??`, il répète le nom :
```javascript
options.timeout = options.timeout ?? 1000;
```
L'opérateur d'**affectation nullish** `??=` fait la même chose en une étape : il affecte le côté droit seulement quand le côté gauche vaut actuellement `null` ou `undefined`, et laisse toute autre valeur intacte :
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` reste `0` car `0` n'est pas nullish ; `timeout` n'existait pas, il reçoit donc `1000`. La même idée existe pour `||` sous la forme `||=`, qui écrase toute valeur falsy.

---

Un **paramètre par défaut** donne une valeur à un paramètre quand l'appelant n'en fournit pas. La règle est précise : la valeur par défaut n'est utilisée que lorsque l'argument est `undefined`, ce qui inclut son omission. Passer `null` ne déclenche **pas** la valeur par défaut, car `null` est une valeur :
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
Les paramètres par défaut suivent la règle du `undefined`, tandis que `??` couvre à la fois `null` et `undefined` : choisissez celui qui correspond à la façon dont votre fonction sera appelée.

---

Le chaînage optionnel et la garde `== null` fonctionnent bien ensemble : la chaîne lit la valeur imbriquée sans lever d'erreur, et la garde décide quoi faire quand le résultat est absent :
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
Dans le dernier `return`, un simple `.` est sûr, car la garde a déjà prouvé que chaque maillon existe.

---

De nombreuses méthodes intégrées signalent « rien trouvé » en renvoyant `undefined`. La méthode de tableau `find(callback)` en est l'exemple typique : elle renvoie le premier élément pour lequel le callback vaut `true`, ou `undefined` quand aucun élément ne correspond :
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
Lire `found.price` ici lèverait une erreur, donc `?.` et `??` sont les compagnons naturels de `find` :
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null` et `undefined` se comportent différemment quand un objet est converti en JSON avec `JSON.stringify()`.
Le JSON possède une valeur `null` mais pas d'`undefined`, donc une propriété dont la valeur est `undefined` est simplement **omise**, tandis qu'une propriété `null` est conservée :
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
Dans les tableaux, les positions ne peuvent pas disparaître, donc `undefined` y devient `null` :
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

Vérifier `obj.key === undefined` ne permet pas de distinguer deux situations : la propriété n'existe pas, ou elle existe et contient la valeur `undefined`.
`Object.hasOwn(obj, key)` répond uniquement à la première question : il renvoie `true` quand l'objet possède sa **propre** propriété nommée `key`, quelle que soit sa valeur :
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
« Propre » signifie déclarée sur l'objet lui-même : les membres hérités tels que `toString` sont disponibles sur chaque objet, mais `Object.hasOwn(config, "toString")` vaut `false`.
