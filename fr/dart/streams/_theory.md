Un `Future` représente une **seule** valeur qui arrive plus tard. Un **Stream** représente une **suite** de valeurs qui arrivent au fil du temps : appuis de touches, morceaux d'un fichier, messages d'un serveur. Chaque valeur s'appelle un **événement**, et après le dernier événement le stream est **terminé**.

La façon la plus simple de construire un stream est `Stream.fromIterable`, qui émet chaque élément d'une liste, l'un après l'autre :

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

Pour consommer les événements un par un, tu utilises une boucle **`await for`**. Comme `await`, elle n'est autorisée que dans une fonction marquée `async`, donc `main` devient `Future<void> main() async`. Le corps de la boucle s'exécute une fois par événement et la boucle se termine quand le stream est terminé :

```dart
Future<void> main() async {
  final names = Stream.fromIterable(['Ada', 'Linus']);
  await for (final name in names) {
    print(name);
  }
  // Ada
  // Linus
}
```

Une boucle `for` classique ne marche pas ici : un `Stream` n'est pas un `Iterable`, ses valeurs ne sont pas toutes disponibles d'un coup.

---

`Stream.fromIterable` a besoin de toutes les valeurs d'avance. Pour **produire** les valeurs une à une, écris un **générateur asynchrone** : une fonction dont le corps est marqué `async*` et dont le type de retour est `Stream<T>`. À l'intérieur, `yield` envoie un événement au stream :

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

Le corps ne s'exécute pas quand tu appelles `countTo(3)` : il s'exécute paresseusement, au fur et à mesure que l'auditeur demande des valeurs, et le stream est terminé quand le corps se termine.

Pour rassembler tous les événements dans une `List`, appelle `toList()`. Elle renvoie un `Future<List<T>>`, donc tu l'attends avec `await` :

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

Une boucle `await for` peut faire plus qu'afficher : elle peut mettre à jour une variable déclarée avant la boucle. Une fonction qui consomme un stream et calcule un résultat doit être marquée `async`, et elle renvoie un `Future` de ce résultat :

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

La fonction n'atteint le `return` qu'une fois le stream terminé, donc l'appelant obtient la valeur finale quand il attend le future :

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

Tout stream finit par se terminer. Pour un générateur `async*`, le stream est **terminé** dès que le corps de la fonction se termine, qu'il soit arrivé à la fin ou qu'il ait rencontré un `return`. Une boucle `await for` sur un stream terminé s'arrête, et tout future de `toList()` se complète.

Un stream ne redémarre pas et ne répète pas ses valeurs : une fois terminé, il reste terminé.

---

`await for` met en pause la fonction courante jusqu'à ce que le stream soit terminé. Quand tu veux réagir aux événements **sans attendre**, appelle `listen` et passe une callback : elle est invoquée une fois par événement, et le code qui suit `listen` s'exécute tout de suite.

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` accepte aussi un paramètre nommé `onDone`, une fonction sans arguments appelée quand le stream se termine :

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

Un générateur `async*` peut transmettre **tous les événements d'un autre stream** avec `yield*` (yield-star). C'est comme une boucle `await for` qui émet chaque valeur, en une seule ligne :

```dart
Stream<int> ones() async* {
  yield 1;
  yield 1;
}

Stream<int> sequence() async* {
  yield 0;
  yield* ones();
  yield 2;
}
// sequence() emits 0, 1, 1, 2
```

Le stream extérieur continue avec ses propres `yield` une fois le stream intérieur terminé.

---

Comme `Iterable`, un `Stream` possède des méthodes qui construisent un **nouveau stream** à partir d'un stream existant :

- `map` transforme chaque événement
- `where` ne garde que les événements qui satisfont une condition
- `take` s'arrête après un nombre donné d'événements

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

Ces méthodes sont **paresseuses** : rien ne s'exécute tant que personne n'écoute le stream résultant. Elles peuvent être chaînées, et le stream source n'est jamais modifié.

---

Comme `where`, `map` et `take` renvoient chacune un stream, tu peux les chaîner et terminer par `toList()` pour obtenir le résultat sous forme de liste. Seul le `toList()` final a besoin d'un `await`, puisque c'est le seul appel qui renvoie un `Future` :

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

En plus de `toList()`, un stream propose d'autres méthodes qui **consomment** tous ses événements et renvoient un seul `Future` :

- `first` et `last` se complètent avec le premier ou le dernier événement
- `length` se complète avec le nombre d'événements
- `join(separator)` se complète avec tous les événements joints en une seule `String`
- `reduce(combine)` combine les événements deux par deux en une seule valeur

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` appelle `combine` avec le résultat obtenu jusque-là et l'événement suivant. Elle lève une exception si le stream est vide, ne l'utilise donc que lorsqu'au moins un événement est garanti.

---

Les méthodes de `Stream` se répartissent en deux groupes :

- les méthodes de **transformation** comme `map`, `where`, `take` et `skip` renvoient un **nouveau `Stream`** et sont paresseuses : aucun événement n'est traité tant que le nouveau stream n'est pas écouté
- les méthodes de **consommation** comme `toList`, `reduce`, `join`, `first`, `last` et `length` écoutent le stream et renvoient un **`Future`** avec le résultat final

Une chaîne ressemble donc à zéro ou plusieurs appels de transformation suivis d'au plus un appel de consommation.

---

Les générateurs produisent des événements depuis l'intérieur d'une fonction. Quand les événements viennent **d'ailleurs** (un bouton, une callback réseau, un autre objet), il te faut un **`StreamController`**. Il vit dans la bibliothèque `dart:async`, le fichier doit donc commencer par `import 'dart:async';`.

Un contrôleur possède un stream et te permet d'y pousser des événements :

```dart
import 'dart:async';

Stream<int> dice() {
  final controller = StreamController<int>();
  controller.add(4);
  controller.add(2);
  controller.close();
  return controller.stream;
}
```

- `add(value)` envoie un événement
- `close()` termine le stream ; l'oublier signifie que les auditeurs attendent pour toujours
- `stream` est le `Stream` que les auditeurs consomment

Les événements ajoutés avant que quiconque écoute sont conservés dans un tampon, le code ci-dessus est donc sûr : un auditeur qui arrive plus tard reçoit quand même `4` et `2`.

---

Un `StreamController` est souvent créé et consommé au même endroit : tu t'abonnes à `controller.stream` avec `listen`, puis tu ajoutes des événements avec `add` et tu fermes le contrôleur avec `close`. Comme `listen` n'attend pas, les événements sont livrés après la fin du code courant, mais toujours dans l'ordre où ils ont été ajoutés :

```dart
import 'dart:async';

void main() {
  final controller = StreamController<int>();
  controller.stream.listen((n) => print('got $n'));
  controller.add(1);
  controller.add(2);
  controller.close();
}
// got 1
// got 2
```

---

Les streams vus jusqu'ici sont à **abonnement unique** : ils n'autorisent qu'un seul auditeur. Appeler `listen`, `await for` ou n'importe quelle méthode de consommation une deuxième fois lève une `StateError` ("Stream has already been listened to").

Pour partager un stream entre plusieurs auditeurs, convertis-le en stream **broadcast** avec `asBroadcastStream()` :

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

Un stream broadcast n'utilise pas de tampon : un auditeur ne reçoit que les événements émis **après** son abonnement. Dans l'exemple, les deux auditeurs s'abonnent avant le premier `await`, donc tous deux reçoivent chaque événement.

---

Un contrôleur peut créer directement un stream broadcast avec le constructeur nommé `StreamController<T>.broadcast()`. Son `stream` accepte n'importe quel nombre d'auditeurs, et chaque événement est livré à tous, dans l'ordre où ils se sont abonnés :

```dart
import 'dart:async';

void main() {
  final controller = StreamController<String>.broadcast();
  controller.stream.listen((msg) => print('first: $msg'));
  controller.stream.listen((msg) => print('second: $msg'));
  controller.add('hi');
  controller.close();
}
// first: hi
// second: hi
```

Comme tout stream broadcast, il n'utilise pas de tampon : les événements ajoutés avant qu'un auditeur s'abonne sont perdus pour cet auditeur.

---

Un stream peut transporter des **erreurs** aussi bien que des valeurs. À l'intérieur d'un générateur `async*`, un `throw` envoie un événement d'erreur et termine le stream ; un `StreamController` peut en envoyer un avec `addError`.

Du côté consommation, une boucle `await for` relance l'erreur à l'endroit de la boucle, tu la gères donc avec un `try`/`catch` ordinaire autour de la boucle :

```dart
Stream<int> risky() async* {
  yield 1;
  throw StateError('sensor offline');
}

Future<void> main() async {
  try {
    await for (final n in risky()) {
      print(n);
    }
  } catch (e) {
    print('caught: $e');
  }
}
// 1
// caught: Bad state: sensor offline
```

Avec `listen`, passe plutôt une callback `onError` : `stream.listen(print, onError: (e) => print('caught: $e'));`
