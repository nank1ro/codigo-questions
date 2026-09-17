> Avant de commencer, je tenais à vous dire que je suis très heureux de vous enseigner Dart.
Avec ce message, j'en profite pour vous faire savoir que l'application que vous utilisez a été écrite en Dart, en utilisant le framework Flutter. C'est donc un honneur pour moi de pouvoir partager mon expertise dans ce langage.

Dart, comme beaucoup d'autres langages de programmation, vous permet de documenter votre code.
Cela vous permet d'écrire n'importe quel texte à côté du code.
Les commentaires sont ignorés par le compilateur.

Dart supporte les commentaires _d'une seule ligne_, les commentaires _multi-lignes_ et les commentaires _de documentation_.

Voici comment écrire un commentaire _d'une seule ligne_ :
```dart
// Ceci est un commentaire. Il n'est pas exécuté.
```

---

Vous pouvez empiler des commentaires _d'une seule ligne_ pour écrire des commentaires _multi-lignes_.
```dart
// Ceci est un
// multi-line comment
```

---

Vous pouvez également créer des blocs de commentaires, ou des commentaires _multi-lignes_.
Les commentaires _multi-lignes_ commencent par `/*` et se terminent par `*/`.
```dart
/*
This is a multi-line
comment
*/
```

---

En plus de ces deux façons d'écrire des commentaires, Dart inclut les commentaires _de documentation_.

Les commentaires _de documentation_ sont des commentaires multi-lignes ou d'une seule ligne qui commencent par `///` ou `/**`. L'utilisation de `///` sur des lignes consécutives a le même effet qu'un commentaire de documentation multi-ligne.

Les commentaires _de documentation_ sont très utiles car ils permettent de générer la documentation. 
Vous voudrez ajouter des commentaires _de documentation_ à votre code pour clarifier ce qu'un bloc de code particulier fait.

Dans un commentaire _de documentation_, l'analyseur résout les noms placés entre crochets comme des références à d'autres éléments de l'API.
En utilisant des crochets, on peut se référer à des _classes_, _methods_, _fields_, _variables_, _functions_ et _parameters_.

Voici un exemple :
```dart
/// Un camélidé sud-américain domestiqué (Lama glama).
///
/// Comme tout autre animal, les lamas doivent manger,
/// alors n'oubliez pas de les [feed] avec du [Food].
class Llama {
  String? name;

  /// Nourrit votre lama avec du [food].
  ///
  /// Un lama typique mange une balle de foin par semaine.
  void feed(Food food) {
    // ...
  }

  /// Fait faire de l'exercice à votre lama avec une [activity] pendant
  /// [timeLimit] minutes.
  void exercise(Activity activity, int timeLimit) {
    // ...
  }
}
```

Dans la documentation générée, `[feed]` devient un lien vers la documentation de la méthode `feed`, et `[Food]` devient un lien vers la documentation de la classe `Food`.
Tandis que `[activity]` et `[timeLimit]` deviennent un lien vers la documentation pour `activity` et `timeLimit` respectivement.
