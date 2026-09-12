Certaines opérations ne se terminent pas immédiatement : télécharger un fichier, lire dans une base de données, attendre un minuteur. JavaScript ne se fige pas pendant qu'elles s'exécutent. À la place, il vous remet une **`Promise`** : un objet qui représente une valeur qui sera disponible **plus tard**.

Une fonction marquée **`async`** renvoie toujours une promesse. Ce que la fonction renvoie devient la valeur à l'intérieur de cette promesse :
```javascript
async function fetchNumber() {
  return 42;
}
```
Pour extraire la valeur d'une promesse, vous utilisez **`await`**. Il met la fonction en pause jusqu'à ce que la promesse ait sa valeur, puis vous donne la valeur seule. `await` n'est autorisé qu'à l'intérieur d'une fonction `async` :
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
Sans `await`, `n` serait la promesse elle-même et `console.log(n)` afficherait `Promise { 42 }` au lieu du nombre.

---

Ajouter `async` devant une fonction change ce qu'elle renvoie : le corps calcule toujours une valeur ordinaire, mais l'appelant reçoit une promesse enveloppant cette valeur.
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
Les deux fonctions contiennent le même code ; seule la façon de lire le résultat diffère. `shoutLater("hi")` doit être attendue avec `await` à l'intérieur d'une autre fonction `async` pour redonner `"HI"`.

Marquer une fonction `async` ne coûte rien quand il n'y a rien à attendre, et c'est ce qui permet d'utiliser `await` à l'intérieur plus tard.

---

Quand la valeur arrive réellement plus tard, vous construisez la promesse vous-même avec **`new Promise`**. Il prend une fonction, qui reçoit un callback **`resolve`** : appelez `resolve(value)` quand la valeur est prête, et la promesse est tenue avec celle-ci.
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` planifie l'exécution de `callback` après `ms` millisecondes et rend la main immédiatement, donc rien n'est bloqué entre-temps.

La fonction passée à `new Promise` s'exécute immédiatement, mais la promesse reste **en attente** jusqu'à ce que `resolve` soit appelé. L'attendre avec `await` donne la valeur :
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

Une promesse est toujours dans l'un des trois états suivants :

- **en attente** : le travail est encore en cours ;
- **tenue** : le travail a réussi et la promesse contient une valeur ;
- **rejetée** : le travail a échoué et la promesse contient une erreur.

Une promesse commence en attente et change d'état au plus une fois. Une fois tenue ou rejetée, elle est **réglée** et ne change plus jamais.

Appeler une fonction `async` n'attend jamais : elle démarre le travail et vous remet immédiatement une promesse en attente, donc la ligne après l'appel s'exécute avant que le travail soit terminé. Cette promesse est un objet normal, pas la valeur qu'elle contient, c'est pourquoi oublier `await` est une erreur si courante.

---

`await` n'est pas la seule façon de lire une promesse. Chaque promesse possède une méthode **`.then(callback)`** : le callback reçoit la valeur dès que la promesse est tenue.
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** construit une promesse déjà tenue avec `value`, ce qui est pratique quand vous avez la valeur sous la main mais devez renvoyer une promesse.

`.then` renvoie une **nouvelle** promesse tenue avec ce que le callback renvoie, donc les appels peuvent être **chaînés**, chaque étape travaillant sur le résultat de la précédente :
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

Une fonction `async` se lit de haut en bas comme n'importe quelle autre fonction : `await` la met simplement en pause jusqu'à ce que la promesse attendue soit tenue, puis l'exécution continue à la ligne suivante.
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
Remarquez la dernière ligne : une fonction `async` doit quand même être **appelée**. Écrire `main` sans les parenthèses définit le travail mais ne le démarre jamais, et rien n'est affiché.

---

Le travail asynchrone peut aussi échouer. La fonction donnée à `new Promise` reçoit un second callback, **`reject`** : appelez `reject(error)` et la promesse devient rejetée au lieu d'être tenue.
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
Rejetez toujours avec un objet `Error` : il porte un `message` et une pile d'appels, ce qu'une simple string ne fait pas.

Un rejet se lit avec **`.catch(callback)`**, l'image miroir de `.then`. **`Promise.reject(error)`** construit une promesse déjà rejetée, tout comme `Promise.resolve` construit une promesse tenue :
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
Appeler à la fois `resolve` et `reject`, ou appeler deux fois, ne change rien : seul le premier appel compte.

---

`.then`, `.catch` et `.finally` sont les maillons d'une même chaîne. Un rejet saute tous les `.then` jusqu'à ce qu'il rencontre un `.catch` ; dès que le callback du `.catch` renvoie une valeur, la chaîne est de nouveau tenue et continue normalement.

**`.finally(callback)`** s'exécute quand la chaîne est réglée, qu'elle ait été tenue ou rejetée. Son callback ne prend aucun argument et sa valeur de retour est ignorée, donc la valeur continue de circuler vers le prochain `.then`. C'est l'endroit idéal pour le nettoyage, comme cacher un indicateur de chargement :
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

À l'intérieur d'une fonction `async`, vous n'avez pas besoin de `.catch`. Attendre une promesse rejetée **lève** l'erreur, donc l'instruction ordinaire `try` / `catch` / `finally` la gère :
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
L'autre sens fonctionne aussi : un `throw` à l'intérieur d'une fonction `async` ne fait pas planter l'appelant, il rejette la promesse que la fonction a renvoyée.
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
Comme dans tout bloc `try`, les lignes après le `await` qui échoue sont ignorées, le bloc `catch` s'exécute, et le bloc `finally` s'exécute dans les deux cas.

---

Un usage courant de `try` / `catch` autour de `await` est de remplacer un échec par une valeur par défaut raisonnable, afin que l'appelant n'ait jamais à traiter l'erreur :
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
Gardez le `await` devant `measure(path)` même si la valeur est renvoyée immédiatement. Sans lui, la promesse quitte la fonction sans jamais passer par le bloc `try`, et un rejet échapperait au `catch`.

---

Quand plusieurs résultats sont nécessaires, les attendre un après l'autre fait perdre du temps : chacun ne démarre que lorsque le précédent est terminé. **`Promise.all(promises)`** prend un array de promesses déjà en cours d'exécution et renvoie une seule promesse tenue avec un array de toutes leurs valeurs :
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
Deux règles méritent d'être retenues :

- les valeurs reviennent **dans l'ordre de l'array**, pas dans l'ordre où elles se sont terminées ;
- si une promesse est rejetée, la promesse renvoyée par `Promise.all` est rejetée immédiatement avec cette première erreur, et les autres valeurs sont perdues.

---

`Promise.all` fonctionne avec un array de n'importe quelle longueur, y compris vide : attendre `Promise.all([])` redonne un array vide immédiatement. Cela permet de passer sans risque une liste construite à l'exécution, sans cas spécial pour « rien à attendre ».
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
L'array qu'il renvoie a toujours exactement autant d'entrées que l'array qu'il a reçu, aux mêmes positions, donc on peut le parcourir comme n'importe quel autre array.

---

La différence entre l'attente **séquentielle** et **parallèle** est décidée par l'*endroit* où vous placez `await` :
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
Dans la première version, le second téléchargement ne démarre qu'une fois le premier terminé, car `await` met la fonction en pause sur cette ligne. Dans la seconde, les deux appels sont faits avant d'attendre quoi que ce soit, donc les deux téléchargements sont déjà en cours pendant que `Promise.all` attend.

Utilisez des `await` séquentiels seulement quand la seconde tâche a vraiment besoin du résultat de la première. Sinon, démarrez tout d'abord et attendez ensemble.

---

`Promise.all` abandonne dès qu'une promesse est rejetée. Quand vous voulez quand même chaque résultat, utilisez **`Promise.allSettled(promises)`** : il n'est jamais rejeté, et il est tenu avec un petit objet par promesse, dans le même ordre :

- `{ status: "fulfilled", value: ... }` pour celles qui ont réussi ;
- `{ status: "rejected", reason: ... }` pour celles qui ont échoué.

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
Lisez `value` seulement quand `status` vaut `"fulfilled"`, et `reason` seulement quand il vaut `"rejected"` : l'autre propriété est simplement absente.

---

**`Promise.race(promises)`** se règle dès que la **première** des promesses se règle, et en copie l'issue : tenu avec la première valeur, ou rejeté avec la première erreur. Les autres ne sont pas annulées, elles continuent de s'exécuter, mais tout ce qu'elles produisent est ignoré.
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
L'usage typique est une échéance : faites une course entre le vrai travail et une promesse qui échoue au bout d'un moment, et vous obtenez soit le résultat, soit une erreur de délai dépassé.

Attention avec un array vide : `Promise.race([])` reste en attente pour toujours, car il n'y a rien qui puisse le régler.

---

En assemblant les dernières pièces, on obtient un petit outil utilisé dans presque toutes les applications réelles : une échéance. Construisez une promesse qui est rejetée après `ms` millisecondes, faites-la courir contre le vrai travail, et celle qui se règle en premier décide de l'issue :
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
Renvoyer une promesse depuis une fonction `async` est très bien : la promesse que la fonction renvoie suit celle-ci, donc l'appelant attend la valeur finale et non une promesse de promesse.
