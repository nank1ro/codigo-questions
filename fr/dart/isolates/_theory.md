Chaque ligne de Dart que tu as écrite jusqu'ici s'exécute dans un **isolate** : un thread avec sa propre mémoire et sa propre boucle d'événements. Un programme démarre avec un seul isolate, l'isolate *main*, et peut en démarrer d'autres.

Ce qui rend les isolates spéciaux, c'est qu'ils ne partagent **rien**. Deux isolates ne voient jamais le même objet, donc il n'y a ni verrou, ni situation de course, ni valeur à moitié mise à jour. Ils communiquent uniquement en s'échangeant des **copies** de messages.

La façon la plus courte d'utiliser un second isolate est **`Isolate.run`**. Elle prend une fonction, l'exécute sur un isolate tout neuf et te rend un `Future` avec son résultat :

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` vit dans la bibliothèque `dart:isolate`, donc le fichier doit commencer par `import 'dart:isolate';`. Pendant que le nouvel isolate calcule, l'isolate main reste libre : c'est du vrai **parallélisme**, le travail se passe sur un autre cœur de processeur.

---

La fonction que tu donnes à `Isolate.run` peut **capturer** des variables de son environnement. Ces valeurs sont copiées dans le nouvel isolate avec la fonction, donc le calcul peut dépendre de son appelant :

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` renvoie un `Future` de ce que la fonction renvoie, donc `triple` peut simplement le renvoyer : pas besoin d'`async` ni d'`await` quand on se contente de transmettre le future.

L'intérêt de déplacer le travail vers un autre isolate est que les longs calculs ne gèlent plus l'isolate main. Une boucle qui tourne pendant une seconde bloque tout quand elle s'exécute sur l'isolate main ; dans `Isolate.run` elle s'exécute ailleurs et l'isolate main continue de traiter ses propres événements.

---

Seules les **données** sont copiées entre isolates ; pas le **code**. Chaque isolate d'un programme peut déjà voir toutes les fonctions de premier niveau et toutes les classes de ce programme, donc le calcul confié à `Isolate.run` peut librement les appeler :

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

Ce qui voyage, c'est le `text` capturé à l'aller et l'`int` résultant au retour, chacun une copie. Le schéma est toujours le même : garde la fonction lourde où elle est, et enveloppe l'**appel** dans `Isolate.run`.

---

`await` et `Isolate.run` résolvent deux problèmes différents, et il vaut la peine de les distinguer.

`await` te donne de la **concurrence** sur un seul isolate : pendant qu'une fonction attend un minuteur ou un serveur, l'isolate exécute d'autre code en attente. Rien ne s'exécute au même instant, l'isolate cesse simplement de rester inactif. C'est le bon outil pour attendre.

`Isolate.run` te donne du **parallélisme** : un second isolate sur un second cœur de processeur, qui exécute son propre code au même instant que le premier. C'est le bon outil pour calculer.

```dart
await Future.delayed(const Duration(seconds: 1)); // waiting: no core is busy
await Isolate.run(() => hugeCalculation());       // computing: another core is busy
```

Attendre un calcul lent ne t'aide pas du tout : `await bigSum()` exécute quand même `bigSum` sur l'isolate courant et le bloque jusqu'à la dernière ligne. Seul un second isolate déplace ce travail ailleurs.

---

`Isolate.run` est le raccourci pour un résultat unique. Quand tu veux un isolate qui continue de tourner et qui rend compte plus d'une fois, démarre-le toi-même avec **`Isolate.spawn`** et donne-lui un moyen de répondre.

Ce moyen, c'est une paire de ports. Une **`ReceivePort`** est une boîte aux lettres : tu la crées de ton côté et tu lis les messages qui arrivent. Son **`sendPort`** est l'adresse de cette boîte aux lettres, et c'est la seule chose dont l'autre isolate a besoin pour répondre.

```dart
import 'dart:isolate';

void sayHello(SendPort port) {
  port.send('hi');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(sayHello, receivePort.sendPort);
  final message = await receivePort.first;
  print(message); // hi
}
```

`Isolate.spawn` prend la fonction à exécuter et l'unique message à lui passer, ici le `SendPort`. De l'autre côté, `send` dépose une valeur dans la boîte aux lettres, et `await receivePort.first` attend le premier message puis ferme le port.

---

La fonction donnée à `Isolate.spawn` s'appelle le **point d'entrée**. Elle doit être une fonction de premier niveau (ou statique) qui prend exactement un paramètre : le message que `Isolate.spawn` lui passe.

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

Les messages qui arrivent dans un `ReceivePort` ont le type statique `dynamic`, car n'importe quelle valeur pouvait avoir été envoyée. Quand tu sais ce que l'autre isolate envoie, fais un cast :

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

Un isolate démarré suit toujours les mêmes quatre étapes : ouvrir la boîte aux lettres, démarrer le worker avec son adresse, attendre la réponse, l'utiliser.

```dart
import 'dart:isolate';

void worker(SendPort port) {
  port.send('done');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(worker, receivePort.sendPort);
  print(await receivePort.first);
}
```

Le `await` devant `Isolate.spawn` attend que l'isolate *démarre*, pas qu'il termine son travail : le résultat arrive plus tard, par le port.

---

`Isolate.spawn` passe exactement **un** message au point d'entrée, et le worker a généralement besoin à la fois d'un `SendPort` pour répondre et de données à traiter. L'astuce habituelle est de tout regrouper dans une seule `List` et de la déballer de l'autre côté :

```dart
void multiply(List<Object> message) {
  final port = message[0] as SendPort;
  final value = message[1] as int;
  port.send(value * 2);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(multiply, <Object>[receivePort.sendPort, 21]);
  print(await receivePort.first); // 42
}
```

La liste est copiée à l'aller, donc le worker lit ses propres valeurs. Un `SendPort` est l'une des rares choses qui n'est pas copiée mais partagée : il continue de pointer vers la boîte aux lettres de l'isolate qui l'a créé, et c'est exactement pourquoi il peut servir d'adresse de retour.

---

`first` lit un message et ferme la boîte aux lettres. Un `ReceivePort` est aussi une **`Stream`**, donc pour lire plusieurs messages tu le parcours avec `await for`.

La boucle ne s'arrête jamais d'elle-même : le port reste ouvert à l'affût d'un message qui ne viendra peut-être jamais. Le worker envoie donc une dernière valeur comme signal, souvent `null`, et le code qui écoute réagit en appelant **`close()`**, ce qui termine le stream et la boucle :

```dart
import 'dart:isolate';

void countdown(SendPort port) {
  port.send(3);
  port.send(2);
  port.send(1);
  port.send(null);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(countdown, receivePort.sendPort);
  await for (final message in receivePort) {
    if (message == null) {
      receivePort.close();
    } else {
      print(message);
    }
  }
  print('done');
}
```

---

Ramasser toute une série de messages suit une seule recette : une liste vide avant la boucle, un `add` par vrai message, et `close()` sur le signal qui met fin au stream. Une fois le port fermé, le `await for` se termine et la fonction peut renvoyer :

```dart
Future<List<int>> collect(ReceivePort port) async {
  final values = <int>[];
  await for (final message in port) {
    if (message == null) {
      port.close();
    } else {
      values.add(message as int);
    }
  }
  return values;
}
```

Les messages gardent l'ordre dans lequel ils ont été envoyés, donc la liste que tu construis reflète pas à pas le travail de l'autre isolate.

---

Un `ReceivePort` ouvert compte comme du travail en attente : tant qu'il en existe un, l'isolate qui le possède a une raison de rester en vie et sa boucle d'événements continue d'attendre un message. Dans un programme en ligne de commande, un isolate main avec un port ouvert ne se termine tout simplement **jamais**, et tu dois l'arrêter à la main.

Fermer le port fait donc partie du travail, ce n'est pas une optimisation :

- `await port.first` le ferme pour toi après un message
- `port.close()` le ferme explicitement, ce qu'il te faut après une boucle `await for`

`Isolate.run` n'a aucune de ces corvées de gestion : il crée les ports, les ferme et arrête l'isolate pour toi. Privilégie-le chaque fois qu'un seul résultat te suffit.

---

Une exception levée dans un isolate ne peut pas sauter vers un autre : les deux ont des piles séparées. `Isolate.run` comble ce fossé pour toi en attrapant l'erreur, en la recopiant et en faisant échouer le future renvoyé avec elle. De ton côté, c'est donc une erreur asynchrone ordinaire, attrapée avec `try`/`catch` autour du `await` :

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

Le `await` dans le `try` compte, exactement comme pour n'importe quel autre future : sans lui, le future quitterait le bloc `try` sans être terminé et le `catch` ne s'exécuterait jamais.

Avec `Isolate.spawn`, il n'y a pas un tel pont. Une erreur non attrapée tue l'isolate démarré en silence et le parent continue d'attendre un message qui n'arrivera jamais, ce qui est une raison de plus de penser d'abord à `Isolate.run`.

---

L'erreur qui revient de `Isolate.run` est une **copie** de celle levée de l'autre côté, donc les vérifications habituelles fonctionnent toujours : `catch (e)` te donne l'objet, et `e is FormatException` te dit de quel type d'échec il s'agissait.

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

Ce dont tu ne peux pas être sûr, c'est que la trace de pile pointe vers ton propre isolate : l'erreur a voyagé, pas la pile.

---

Une fois assemblé, un programme `Isolate.run` se lit comme du code séquentiel ordinaire : la ligne avant l'appel s'exécute sur l'isolate main, le calcul s'exécute ailleurs, et la ligne après le `await` s'exécute de nouveau sur l'isolate main, résultat en main.

```dart
import 'dart:isolate';

int twice(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => twice(4));
  print(result);
}
// start
// 8
```

---

Comme les isolates ne partagent aucune mémoire, chaque message est **copié** quand il traverse. Les nombres, les booléens, les strings, `null`, les listes, les maps et la plupart des objets simples peuvent faire le voyage ; quelques choses ne peuvent pas être copiées du tout, comme un socket ouvert, et essayer d'en envoyer un lève une `ArgumentError`.

La conséquence, c'est la règle qui rend les isolates sûrs : après l'envoi, les deux côtés détiennent **deux objets indépendants**. Quoi qu'un isolate fasse à sa copie, c'est invisible pour l'autre.

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // the copy grows
print(numbers);                           // [1, 2, 3]
```

`SendPort` est l'exception qui confirme la règle : il est partagé plutôt que copié, précisément pour qu'il puisse continuer à pointer vers la boîte aux lettres d'origine.

---

Chaque `Isolate.run` démarre son propre isolate, donc plusieurs d'entre eux s'exécutent vraiment au même instant, sur autant de cœurs que la machine en possède. Le schéma est celui que tu connais déjà avec les futures : démarre chaque calcul d'abord, puis attends-les tous avec `Future.wait`, qui garde les résultats dans l'ordre de l'entrée.

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

Démarrer un isolate n'est pas gratuit : cela coûte de la mémoire et quelques millisecondes. Répartir un long calcul sur une poignée d'isolates paie, envoyer mille additions triviales à mille isolates ne paie pas.
