Une **méthode d'ordre supérieur** est une méthode qui prend une fonction en argument. Les collections de Dart en offrent beaucoup, et la fonction que vous passez est généralement une fonction anonyme écrite avec la syntaxe fléchée `(x) => ...`.

`map` est la plus courante : elle appelle la fonction sur chaque élément et produit les résultats, un pour chaque élément, en laissant la collection d'origine intacte :

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

Remarquez les **parenthèses** dans la sortie. `map` ne retourne pas une `List` : elle retourne un `Iterable`, une séquence que vous pouvez parcourir. Pour obtenir une véritable liste, appelez **`toList()`** dessus :

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

Des crochets dans la sortie sont le signe que vous regardez une `List`, des parenthèses un simple `Iterable`.

---

`where` prend une fonction qui retourne un `bool`, appelée un **prédicat**, et ne garde que les éléments pour lesquels elle répond `true`. L'ordre des éléments survivants ne change jamais :

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

Comme `map`, `where` retourne un `Iterable` et ne modifie jamais la collection d'origine, c'est donc encore `toList()` qui transforme le résultat en `List`.

Dans les autres langages cette méthode s'appelle `filter` ; en Dart c'est `where`.

---

La fonction donnée à `map` n'est pas obligée de retourner le même type que les éléments qu'elle reçoit. Transformer une liste de chaînes en leurs longueurs fait d'une `List<String>` un `Iterable<int>`, que `toList()` transforme ensuite en `List<int>` :

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

Le résultat a toujours **exactement autant d'éléments que l'original**, dans le même ordre : `map` transforme des éléments, il n'en ajoute ni n'en supprime aucun.

---

Certaines méthodes d'ordre supérieur répondent à une question sur la collection au lieu d'en construire une nouvelle. Elles prennent un prédicat et retournent un `bool` :

- `any` vaut `true` quand **au moins un** élément satisfait le prédicat
- `every` vaut `true` quand **tous** les éléments le satisfont

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

Toutes deux s'arrêtent dès que la réponse est certaine : `any` au premier élément qui correspond, `every` au premier qui ne correspond pas.

Sur une collection vide, `any` vaut `false` et `every` vaut `true` : il n'y a aucun élément pour prouver la première, et aucun pour casser la seconde.

---

`map` et `where` sont **paresseuses** : les appeler ne fait rien. Elles retournent un `Iterable` qui se souvient de la source et de la fonction, et la fonction n'est appelée que lorsque quelque chose parcourt le résultat, un élément à la fois.

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // rien n'est encore calculé
print(doubled.first);                      // ne calcule que 2
```

C'est `toList()` qui **matérialise** la séquence : il la parcourt du début à la fin et stocke chaque résultat dans une véritable `List`.

La paresse a deux conséquences qu'il vaut la peine de retenir. Un `Iterable` paresseux est recalculé chaque fois que vous l'itérez, donc le matérialiser une seule fois avec `toList()` coûte moins cher quand vous avez besoin des valeurs plus d'une fois. Et il continue de regarder la collection d'origine, donc modifier cette collection change ce que l'`Iterable` produit :

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` combine toute une collection en une **seule valeur**. Elle prend deux arguments : la valeur de départ de l'**accumulateur**, et une fonction qui reçoit l'accumulateur jusque-là et l'élément suivant, et retourne le nouvel accumulateur :

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

Ici `acc` commence à `0`, puis devient `1`, `3`, `6` et enfin `10`.

L'accumulateur n'est pas obligé d'être un nombre, ni du même type que les éléments : partir de `''` et ajouter du texte construit une `String` à partir d'une liste de n'importe quoi.

Un détail à garder à l'esprit : Dart déduit le type de l'accumulateur à partir de la valeur de départ **et** de l'endroit où le résultat est utilisé. À l'intérieur de `print(...)` le type attendu est inconnu, donc stockez d'abord le résultat dans une variable (ou écrivez `fold<int>(...)`), sinon le compilateur se plaint de ne pas pouvoir utiliser `+` sur l'accumulateur.

---

`reduce` est la version plus courte de `fold`. Elle ne prend pas de valeur de départ : le **premier élément** sert d'accumulateur de départ, et la fonction s'exécute pour chaque élément restant :

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

Comme il n'y a pas de valeur de départ, le résultat a toujours le **même type que les éléments**, et appeler `reduce` sur une collection vide lève une `StateError` : il n'y a pas de premier élément pour commencer. `fold` n'a pas ce problème, c'est pourquoi c'est le choix le plus sûr par défaut.

`reduce` est à son avantage quand vous cherchez un élément parmi d'autres, comme le plus grand :

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` retourne le **premier** élément correspondant à un prédicat, au lieu de tous :

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

Quand rien ne correspond, il n'y a pas d'élément à retourner, donc `firstWhere` lève une `StateError`. Pour donner une réponse plutôt qu'une erreur, passez l'argument nommé **`orElse`** : une fonction sans paramètre qui produit la valeur de repli.

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` est une fonction, pas une simple valeur, donc elle n'est appelée que lorsque la recherche échoue. Écrire `orElse: 'none'` ne compile pas.

---

Quand la fonction que vous donnez à `map` retourne une collection pour chaque élément, vous obtenez une séquence de collections. **`expand`** fait le même travail, puis réunit le tout en une seule séquence à plat :

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

L'ordre est préservé : tout ce que produit le premier élément vient d'abord, puis tout ce que produit le deuxième, et ainsi de suite.

Comme la collection retournée peut avoir n'importe quelle taille, `expand` est aussi le moyen de produire **plus ou moins** d'éléments que ceux du départ : retourner une liste vide pour un élément l'élimine simplement.

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` garde les `n` **premiers** éléments et `skip(n)` les jette. Ni l'une ni l'autre ne prend de fonction, mais toutes deux retournent un `Iterable` paresseux, donc elles s'insèrent naturellement entre les autres méthodes d'ordre supérieur :

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

Demander plus d'éléments qu'il n'y en a n'est pas une erreur : vous obtenez simplement ce qui existe, ou un résultat vide.

`takeWhile` et `skipWhile` sont les versions avec un prédicat. Elles prennent ou abandonnent des éléments depuis le début **tant que** le prédicat est vrai, et s'arrêtent au premier élément qui le fait échouer, même si des éléments plus loin pourraient à nouveau correspondre :

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart n'a pas de méthode `sorted`. `sort` appartient à `List`, elle réordonne la liste **sur place** et ne retourne rien :

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

Comme elle retourne `void`, vous ne pouvez pas du tout utiliser le résultat : `final sorted = numbers.sort();` donne une valeur que le compilateur refuse de vous laisser lire. L'idiome pour une **copie** ordonnée est `toList()` suivi de la cascade `..sort()` : `toList()` fait la copie, et `..` exécute `sort` dessus tout en rendant la copie elle-même.

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], inchangée
```

`sort` accepte aussi un **comparateur** : une fonction de deux éléments retournant un nombre négatif quand le premier vient avant le second, `0` quand ils sont égaux, et un nombre positif sinon. `compareTo` produit exactement cela, donc trier selon n'importe quelle clé tient en une ligne :

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` et `reduce` se ressemblent, et choisir entre les deux revient à deux questions : la collection peut-elle être vide, et le résultat a-t-il le même type que les éléments ?

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String à partir de Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int à partir de Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` ne peut jamais donner que le type d'un élément, parce qu'elle part d'un élément. `fold` part d'une valeur que vous choisissez, donc l'accumulateur peut être un `int` qui compte, une `String` qui grandit, ou même une `List` en cours de construction. Et comme cette valeur de départ existe déjà, une collection vide est simplement la réponse que `fold` retourne inchangée, tandis que `reduce` n'a rien à retourner et lève une erreur.

---

Chacune de ces méthodes retourne un `Iterable`, et chaque `Iterable` possède à nouveau les mêmes méthodes. C'est ce qui permet de les **enchaîner** : tout un calcul se lit comme un pipeline de gauche à droite, chaque étape travaillant sur ce que la précédente a produit.

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

Seule la dernière étape a besoin de `toList()` : l'appeler au milieu construirait une liste que personne ne garde.

Le type change le long de la chaîne, et donc ce que reçoit la fonction suivante : après un `where` sur une `List<String>` vous avez encore des chaînes, mais après `map((w) => w.length)` l'étape suivante voit des nombres.

Comme chaque étape est paresseuse, l'ordre compte pour le travail effectué, et pas seulement pour le résultat : filtrer d'abord avec `where` signifie que `map` est appelée sur moins d'éléments.

---

Rien de spécial dans ces méthodes : elles ont simplement **une fonction en paramètre**, et vos propres fonctions peuvent faire de même. Le type d'un paramètre de fonction s'écrit comme le type de retour, puis `Function`, puis les types des paramètres entre parenthèses :

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

L'appelant décide **ce qui** se passe, la fonction décide **sur quoi**. Notez comment `operation` est passée directement à `map` : une valeur de fonction peut être transmise comme n'importe quelle autre valeur.

L'argument peut être une fonction anonyme, ou le **nom** d'une fonction existante, écrit sans parenthèses. Ajouter les parenthèses l'appellerait au lieu de la passer :

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

Une fonction peut aussi **retourner** une fonction. Le type de retour s'écrit exactement comme un type de paramètre de fonction, et la valeur retournée est généralement une fonction anonyme :

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` ne multiplie rien : elle construit et rend une nouvelle fonction qui multiplie par `3`. Cette fonction est ensuite stockée, appelée, ou passée à `map` comme n'importe quelle autre :

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

La fonction retournée se souvient encore de `factor` après que `multiplier` a terminé. Une fonction qui garde les variables de la portée où elle a été créée est appelée une **fermeture** (closure), et c'est ce qui rend possibles les fabriques de fonctions comme celle-ci.

---

Mis bout à bout, ces méthodes remplacent la plupart des boucles écrites à la main. Un pipeline se lit généralement en trois étapes : **sélectionner** les éléments avec `where`, les **transformer** avec `map`, puis les **combiner** avec `fold` :

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

Comme `fold` choisit sa propre valeur de départ, il peut aussi terminer une chaîne avec un type qui n'a rien à voir avec les éléments, comme une `String` construite morceau par morceau :

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

Chaque étape reste courte et dit ce qu'elle fait, et c'est la vraie raison de les préférer à une boucle qui fait les trois à la fois.
