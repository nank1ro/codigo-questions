Certaines opérations prennent du temps : lire un fichier, appeler un serveur, attendre un minuteur. Dart ne bloque pas le programme pendant leur exécution. À la place, une telle fonction renvoie un **`Future<T>`** : la promesse qu'une valeur de type `T` sera disponible **plus tard**.

Le future le plus simple est celui qui possède déjà sa valeur, construit avec `Future.value` :

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

Pour extraire la valeur d'un future, tu l'**`await`**es. `await` met en pause la fonction courante jusqu'à ce que le future soit terminé, puis te donne la valeur brute. Ce n'est autorisé que dans une fonction marquée **`async`**, donc `main` devient `Future<void> main() async` :

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

Sans `await`, `n` serait le `Future` lui-même, et `print(n)` afficherait `Instance of 'Future<int>'` au lieu du nombre.

---

Marquer une fonction `async` fait deux choses : cela autorise `await` dans le corps, et cela fait **renvoyer un `Future`** à la fonction. Ce que tu renvoies avec `return` devient la valeur avec laquelle le future se termine, donc le type de retour déclaré est `Future<T>` même si le corps renvoie un `T` brut :

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

Tu n'as pas besoin de `Future.value` ici : le mot-clé `async` emballe la valeur renvoyée pour toi.

---

`Future.value` se termine immédiatement. Pour simuler un travail qui prend du temps, utilise **`Future.delayed`** : il prend une `Duration` et une fonction, attend la durée, puis se termine avec ce que la fonction renvoie :

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` se construit avec des paramètres nommés comme `seconds`, `milliseconds` ou `minutes`. Dans une fonction `async`, tu peux aussi attendre un délai seul, sans valeur, juste pour faire une pause :

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

Les deux styles sont courants ; le second se lit comme du code séquentiel ordinaire.

---

Garde bien en tête les deux faces d'un future :

- une fonction `async` **déclare** `Future<T>` et **renvoie** un `T` brut : l'emballage est automatique
- un appelant qui fait `await` sur un `Future<T>` **reçoit** un `T` brut : le déballage est automatique

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

Écrire `int count() async` est une erreur : une fonction `async` doit déclarer un type de retour `Future` (ou `void`).

---

`await` n'est pas la seule façon d'utiliser un future. Tu peux aussi enregistrer un **callback** avec **`then`** : la fonction que tu passes est appelée avec la valeur dès que le future se termine. Contrairement à `await`, `then` ne met **pas** en pause la fonction courante, donc le code qui suit s'exécute d'abord :

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

Même un future construit avec `Future.value` ne livre sa valeur qu'une fois le code courant terminé, c'est pourquoi `waiting` est affiché en premier. `then` fonctionne dans n'importe quelle fonction, `async` ou non.

---

Dans une fonction `async`, `await` te permet d'écrire des étapes asynchrones comme s'il s'agissait de code séquentiel ordinaire. Chaque `await` attend son future, et la ligne suivante ne s'exécute qu'une fois la valeur disponible :

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` peut aussi s'utiliser directement dans une expression : `return await width() * await height();` donne le même résultat.

---

Quand une fonction rencontre un `await`, elle se **met en pause** à cette ligne et le reste du programme continue. Les lignes après l'`await` ne s'exécutent qu'une fois le future terminé. Lire une fonction `async` de haut en bas te donne donc l'ordre exact de ses effets :

```dart
Future<int> load() async {
  await Future.delayed(const Duration(milliseconds: 5));
  return 7;
}

Future<void> main() async {
  print('loading');
  final n = await load();
  print('value: $n');
  print('done');
}
// loading
// value: 7
// done
```

---

Un future peut aussi se terminer par une **erreur**. Quand une fonction `async` lève une exception, celle-ci ne s'échappe pas immédiatement : elle devient l'erreur du future renvoyé. Celui qui fait `await` sur ce future voit l'erreur levée au niveau de l'`await`, elle peut donc être traitée avec un `try`/`catch` ordinaire :

```dart
Future<int> parseLater(String s) async {
  await Future.delayed(const Duration(milliseconds: 5));
  return int.parse(s); // throws FormatException for 'abc'
}

Future<int> orZero(String s) async {
  try {
    return await parseLater(s);
  } catch (e) {
    return 0;
  }
}
```

L'`await` à l'intérieur du `try` est essentiel : `return parseLater(s);` remettrait le future à l'appelant **sans attendre**, l'erreur arriverait donc alors que le bloc `try` est déjà terminé et le `catch` ne s'exécuterait jamais.

---

Les erreurs voyagent avec le future, pas par la pile d'appels. Appeler une fonction `async` qui lève une exception ne fait jamais planter l'appelant à lui seul : l'erreur est stockée dans le future renvoyé et apparaît plus tard, à l'endroit où le future est attendu. Un `try`/`catch` doit donc entourer l'**`await`**, pas l'appel qui a créé le future.

Si personne n'attend ni ne traite le future en échec, Dart signale une *unhandled exception* et, dans un programme en ligne de commande, se termine avec une erreur.

---

Avec les callbacks, les erreurs se traitent avec **`catchError`**, le pendant de `then`. Les deux renvoient un nouveau future, ils sont donc généralement chaînés : `then` reçoit la valeur si le future réussit, `catchError` reçoit l'erreur s'il échoue, et un seul des deux callbacks s'exécute :

```dart
Future<String> download() async {
  throw StateError('no network');
}

void main() {
  download()
      .then((data) => print('data: $data'))
      .catchError((e) => print('error: $e'));
  print('requested');
}
// requested
// error: Bad state: no network
```

Un `catchError` placé après `then` attrape aussi les erreurs levées dans le callback de `then`. Comme avec `then`, le code qui suit la chaîne s'exécute d'abord, car les callbacks ne sont invoqués qu'une fois le code courant terminé.

---

Quand plusieurs futures ne dépendent pas les uns des autres, confie-les tous à **`Future.wait`** : il prend une `List<Future<T>>`, les laisse s'exécuter en même temps et renvoie un unique `Future<List<T>>` qui se termine quand **tous** sont finis. Les résultats conservent l'ordre de la liste d'entrée, quel que soit le future terminé en premier :

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` prend `25` millisecondes, car `fast()` n'est appelé qu'une fois `slow()` terminé ; `await Future.wait([slow(), fast()])` prend environ `20`, la durée du plus long.

---

`Future.wait` est l'outil pour « charger plusieurs choses, puis continuer ». La forme typique est : construire la liste des futures, faire `await Future.wait` dessus, puis utiliser la liste obtenue :

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` se termine en premier, mais la liste suit quand même l'ordre des appels : `stock()` en premier, `orders()` en second.

---

Tu n'as pas besoin de `Future.wait` pour exécuter deux futures en même temps. Une fonction `async` commence à s'exécuter dès qu'elle est **appelée**, jusqu'à son premier `await` ; le future que tu récupères est le travail déjà en cours. L'astuce est donc : **appeler d'abord, attendre ensuite** :

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

Compare avec `return await words() / await pages();`, où `pages()` n'est appelé qu'une fois `words()` terminé : même résultat, deux fois plus de temps. Préfère la forme concurrente chaque fois que le second appel n'a pas besoin du résultat du premier.

---

Une erreur se **propage** à travers chaque `await` qui ne l'attrape pas. Si `load()` échoue, `await load()` dans `loadTwice()` lève une exception ; comme `loadTwice` n'a pas de `try`/`catch`, son propre future échoue avec la même erreur ; et ainsi de suite en remontant la chaîne, jusqu'à ce qu'un `await` soit entouré d'un `try`/`catch` :

```dart
Future<int> load() async {
  throw StateError('offline');
}

Future<int> loadTwice() async {
  final n = await load();   // throws here, loadTwice fails too
  return n * 2;             // never runs
}

Future<void> main() async {
  try {
    print(await loadTwice());
  } catch (e) {
    print('failed: $e');    // failed: Bad state: offline
  }
}
```

Cela reproduit la façon dont les exceptions se propagent à travers les appels synchrones : tu les traites une seule fois, au niveau qui sait quoi faire.

---

`Future.wait` suit la même règle : si **l'un** des futures échoue, le future combiné se termine par cette erreur et `await Future.wait(...)` lève une exception. Tu n'obtiens jamais une liste partielle des valeurs réussies. Pour conserver les autres, traite l'erreur dans chaque future individuel, par exemple avec `catchError`, avant de le passer à `Future.wait`.

```dart
Future<int> ok() => Future.value(1);
Future<int> bad() async => throw StateError('nope');

Future<void> main() async {
  try {
    await Future.wait([ok(), bad()]);
  } catch (e) {
    print('failed: $e'); // failed: Bad state: nope
  }
}
```

---

Comme `await` transforme les erreurs d'un future en exceptions ordinaires, tous les motifs `try`/`catch` habituels s'appliquent au code asynchrone, y compris les boucles qui réessaient. Dans un bloc `catch`, **`rethrow`** relance la même erreur, c'est ainsi que l'on abandonne après la dernière tentative :

```dart
Future<String> onceThenGiveUp(Future<String> Function() task) async {
  try {
    return await task();
  } catch (e) {
    print('first attempt failed');
    rethrow; // the caller sees the original error
  }
}
```

Un paramètre de type fonction comme `Future<String> Function() task` reçoit la **fonction** elle-même, pas un future : chaque appel à `task()` démarre une nouvelle tentative.
