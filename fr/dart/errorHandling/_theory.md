Certaines instructions ne peuvent pas être menées à bien : lire un texte qui n'est pas un nombre, prendre un élément au-delà de la fin d'une liste, demander le premier élément d'une liste vide. Quand cela arrive, Dart **lève** un objet qui décrit l'échec.

Vous pouvez en lever une vous-même avec le mot-clé `throw`. `Exception('message')` construit un objet prêt à l'emploi portant une courte explication :

```dart
throw Exception('no fuel');
```

Un `throw` n'est pas un `return`. Il abandonne l'instruction, la fonction, et chaque appelant au-dessus d'elle, à la recherche de quelque chose qui le gère. Quand rien ne le fait, le programme s'arrête et affiche l'échec :

```
Unhandled exception:
Exception: no fuel
```

Tout ce qui suit le `throw` est ignoré, si bien que les lignes qui auraient dû s'exécuter ne le font jamais. C'est ce dont ce sujet traite : décider où un échec est géré au lieu de le laisser mettre fin au programme.

---

Pour garder le programme en vie, enveloppez l'instruction risquée dans un bloc `try` et décrivez la récupération dans un bloc `catch` :

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

`int.parse` lève une exception quand le texte ne décrit pas un nombre entier. Dart quitte le bloc `try` à la première instruction qui lève, ignore le reste de celui-ci, exécute le bloc `catch`, puis poursuit avec le code qui suit. La variable entre les parenthèses, `e` ici, est l'objet levé lui-même.

Rien de ce qui se trouve dans le bloc `try` n'est annulé, gardez-le donc aussi court que l'échec auquel vous vous attendez.

---

Un `catch` seul attrape tout, ce qui masque aussi les échecs que vous n'aviez pas prévus. Pour n'en gérer qu'une seule sorte, nommez son type dans une clause `on` :

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

`int.parse` lève une **`FormatException`** quand le texte n'est pas un nombre entier, c'est donc le type à nommer lors de la lecture d'une saisie. Une clause `on` correspond à ce type et à ses sous-types, et à rien d'autre : tout autre échec continue de voyager vers l'extérieur et finit par apparaître, au lieu d'être avalé par une récupération qui ne lui était pas destinée.

---

Un bloc `try` peut être suivi de **plusieurs** clauses, chacune se remettant d'un échec différent. Dart compare l'objet levé à chacune de haut en bas et exécute la **première** qui correspond :

```dart
try {
  return names[int.parse(text)];
} on FormatException {
  return 'not a number';
} on RangeError {
  return 'out of range';
} catch (e) {
  return 'unknown problem';
}
```

Lire une liste avec un index qui n'existe pas lève une **`RangeError`**, si bien que les deux échecs de cette seule ligne obtiennent des réponses différentes.

Comme c'est la première correspondance qui gagne, l'ordre compte : une clause pour un type général placée au-dessus d'une plus spécifique gagnerait toujours, laissant la clause spécifique inatteignable. Écrivez les clauses spécifiques en premier, et un `catch` seul en dernier si vous voulez un filet de sécurité.

La clause `on RangeError` ci-dessus n'est là que pour montrer comment plusieurs clauses sont ordonnées. `RangeError` signale une erreur dans le code plutôt qu'une condition que le programme ne pouvait pas contrôler, et un exercice ultérieur explique pourquoi un tel échec doit être prévenu plutôt qu'attrapé.

---

Souvent, la récupération n'a pas besoin du tout de l'objet levé : le type dit déjà tout. Dans ce cas, supprimez la partie `catch` et ne gardez que la clause `on` :

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

Les deux formes ne diffèrent que par l'obtention ou non d'une variable :

- `on FormatException catch (e)` — correspond à ce type et vous donne l'objet dans `e`
- `on FormatException` — correspond à ce type, sans variable
- `catch (e)` — correspond à tout et vous donne l'objet

Omettre une variable inutilisée garde le gestionnaire honnête sur ce qu'il utilise réellement.

---

Un troisième bloc peut suivre les gestionnaires. `finally` s'exécute **dans tous les cas** : après que le bloc `try` s'est terminé normalement, après qu'un gestionnaire a rattrapé l'échec, et aussi quand rien ne correspondait et que l'échec continue de voyager vers l'extérieur.

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

Il s'exécute même avant qu'un `return` ne rende sa valeur, c'est pourquoi le message ci-dessus est affiché avant que l'appelant ne voie le résultat. Cela fait de `finally` l'endroit du travail qui doit avoir lieu dans tous les cas, comme fermer ce que vous avez ouvert.

---

Votre propre code lève des exceptions de la même façon que la bibliothèque. `Exception('message')` construit une exception simple portant une courte explication, et `throw` l'envoie sur sa route :

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

Le message n'est pas perdu : `toString()` réunit le mot `Exception`, deux points et le message, ce qui est exactement ce que le rapport d'exception non gérée affiche.

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

Lever une exception est préférable à retourner une valeur inventée comme `-1` : l'appelant ne peut pas oublier de l'examiner, et la raison voyage avec elle.

---

Parfois, un gestionnaire n'est pas le bon endroit pour se remettre de l'échec : vous voulez seulement *remarquer* l'échec et le laisser continuer vers l'appelant qui peut réellement le traiter. Le mot-clé `rethrow` fait cela, dans un bloc `catch` ou `on ... catch` :

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow` envoie le **même** objet plus loin, si bien que l'appelant voit l'échec d'origine. Écrire `throw e` à la place fonctionnerait aussi, mais cela redémarre le voyage et perd l'endroit où l'échec s'est produit à l'origine.

Un bloc `finally` dans la même instruction s'exécute tout de même, même sur le chemin de sortie.

---

Une clause `catch` accepte un **second** paramètre :

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

Le premier est l'objet levé, le second est une `StackTrace` : la chaîne des appels qui étaient en cours au moment du `throw`. Elle répond à la question de *l'endroit* d'où venait l'échec, ce que le message seul fait rarement.

Une trace de pile énumère des noms de fichiers, des numéros de ligne et des frames, et elle change selon la compilation et le chemin d'appels. Affichez-la, joignez-la à un rapport, transmettez-la — mais ne la comparez jamais à un texte fixe, et ne faites jamais reposer le comportement du programme sur son contenu. Ne la demandez que lorsque vous allez la consigner dans un journal.

---

`Exception` est une interface, votre propre classe peut donc l'être. Une exception personnalisée donne à l'échec un nom qu'une clause `on` peut sélectionner, et des champs qu'un gestionnaire peut lire :

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

Trois parties méritent d'être gardées : `implements Exception` pour que la classe compte parmi les autres échecs, un champ `final` portant le détail, et un `toString()` redéfini pour que le rapport d'exception non gérée soit lisible. Sans cette redéfinition, Dart affiche le nom de classe seul et le détail est perdu.

---

Dart lève deux familles d'objets, et elles signifient des choses opposées.

Une **`Exception`** décrit une condition que le programme ne pouvait pas contrôler : un texte qui n'était pas un nombre, un fichier qui n'était pas là, un réseau qui n'a rien répondu. `FormatException` en est une. Elles sont attendues, et les attraper est la réponse normale.

Un **`Error`** décrit une erreur dans le code lui-même :

- `ArgumentError` — une fonction a été appelée avec une valeur qu'elle documente comme invalide
- `StateError` — un objet a été utilisé à un moment où il ne peut pas faire ce qui est demandé
- `RangeError` — un index ou une valeur était en dehors de la plage autorisée

Attraper un `Error` masque le bogue au lieu de le corriger. La bonne réponse est de changer le code pour qu'il cesse d'être levé : vérifiez l'argument avant d'appeler, ou utilisez une API qui ne lève pas. C'est pourquoi une clause `on FormatException` est une bonne pratique, alors qu'une clause `on ArgumentError` ne l'est presque jamais.

---

Certaines bibliothèques proposent une version qui ne lève rien du tout. À côté de `int.parse`, Dart a **`int.tryParse`** : la même conversion, mais elle retourne `null` au lieu de lever quand le texte n'est pas un nombre.

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

Le résultat est un `int?`, si bien que l'opérateur `??` le transforme directement en valeur par défaut :

```dart
final port = int.tryParse(text) ?? 8080;
```

Quand l'échec est ordinaire et que vous voulez seulement une valeur de repli, c'est plus court et plus clair qu'un bloc `try`. Gardez `int.parse` pour les cas où un texte incorrect est vraiment un échec que quelqu'un au-dessus doit apprendre.

---

`firstWhere` retourne le premier élément correspondant à un test. Quand rien ne correspond, il n'y a pas d'élément à retourner, alors il lève une `StateError` :

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

Comme `int.tryParse`, la bibliothèque propose une porte de sortie. Le paramètre nommé `orElse` prend une fonction qui produit la valeur à utiliser quand rien ne correspondait :

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

Le choix est le même qu'auparavant : `orElse` quand « rien ne correspond » est un résultat ordinaire, l'appel seul quand cela signifierait que les données sont corrompues et que quelqu'un doit l'apprendre.

---

Le `throw` et le `try` n'ont pas besoin de vivre dans la même fonction. Une fonction qui ne peut pas faire son travail lève, et l'appelant qui sait quoi faire de cela attrape :

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

`ageFromText` n'a pas d'opinion sur la question de savoir si un âge incorrect doit mettre fin au programme, afficher un message ou être ignoré — c'est la décision de l'appelant, et l'appelant est l'endroit où le bloc `try` a sa place. Cette séparation est la raison pour laquelle lever vaut plus que retourner `-1` : l'échec atteint le seul endroit qui peut y répondre.

Rappelez-vous que le bloc `try` s'arrête au premier échec, si bien que les instructions qui suivent l'appel qui échoue sont ignorées elles aussi.

---

L'endroit où se trouve le bloc `try` décide de la quantité de travail qu'un seul échec détruit. Autour d'une boucle, le premier élément incorrect met fin à tout le lot ; **à l'intérieur** de la boucle, seul cet élément est perdu et le reste est quand même traité :

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

C'est la forme du quotidien pour importer un fichier, lire une liste de réglages ou traiter une file de messages : une ligne endommagée ne devrait pas jeter les bonnes. La règle reste la même qu'auparavant — gardez le bloc `try` autour de l'instruction qui peut échouer, et pas plus grand.

---

La dernière pièce est le fait de lever un `Error` à dessein. Une fonction qui documente ce qu'elle accepte devrait refuser tout le reste bruyamment, et `ArgumentError` est l'objet fait pour cela :

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

Le message est accessible via `e.message`, et `toString()` affiche `Invalid argument(s): ` suivi de ce message.

Cela ne contredit pas la règle d'avant. Lever une `ArgumentError` est juste, en attraper une ne l'est pas : elle dit à l'*auteur de l'appelant* que l'appel lui-même est faux, et le correctif est une vérification avant l'appel, pas un gestionnaire autour.
