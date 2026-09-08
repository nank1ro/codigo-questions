Vous savez déjà déclarer une fonction avec un nom, telle que `void sayHello() { ... }`. Dart vous permet également d'écrire une fonction **sans nom** : une **fonction anonyme**. Elle a les mêmes parties qu'une fonction nommée (des paramètres entre parenthèses et un corps entre accolades), mais sans type de retour ni nom :

```dart
(String name) {
  print('Hello, $name!');
}
```

Comme elle n'a pas de nom, la façon habituelle de l'utiliser est de la stocker dans une variable, puis d'appeler la variable comme une fonction :

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

Notez le `;` après l'accolade fermante : l'affectation est une instruction normale.

---

Une fonction anonyme peut prendre des paramètres et `return` une valeur, exactement comme une fonction nommée. Le type de retour n'est pas écrit : Dart l'**infère** à partir des instructions `return` du corps.

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

Lorsque le corps est une seule expression, une fonction anonyme peut utiliser la **syntaxe fléchée** `=>`, tout comme une fonction nommée. La flèche remplace les accolades et le mot-clé `return` :

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

Cette forme courte est de loin la façon la plus courante d'écrire des fonctions anonymes en Dart.

---

Les fonctions sont des valeurs, elles ont donc un type. Le type d'une fonction s'écrit avec le **type de retour**, puis le mot-clé `Function`, puis les **types des paramètres** entre parenthèses :

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

Lorsque la variable est typée de cette façon, les types des paramètres peuvent être omis dans la fonction anonyme, car Dart les infère du type déclaré :

```dart
int Function(int, int) add = (a, b) => a + b;
```

Le type seul `Function` accepte n'importe quelle fonction, quels que soient ses paramètres et son type de retour, mais il n'indique pas à Dart comment l'appeler.

---

Comme un type de fonction est un type normal, une fonction peut prendre **une autre fonction en paramètre**. Dans le corps, le paramètre est appelé comme n'importe quelle fonction :

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

Ici, l'appelant décide de ce que fait `apply` en passant une fonction anonyme comme second argument.

---

De nombreuses méthodes des collections Dart prennent une fonction en argument, et les fonctions anonymes sont la façon naturelle d'en passer une. La plus simple est `forEach`, qui appelle la fonction donnée une fois pour chaque élément d'une liste :

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

Le type du paramètre est inféré de la liste, donc `fruit` est un `String` sans avoir à l'écrire.

---

Deux autres méthodes très courantes qui prennent une fonction anonyme sont `map` et `where` :

- `map` transforme chaque élément avec la fonction et retourne les nouvelles valeurs
- `where` ne garde que les éléments pour lesquels la fonction retourne `true`

Les deux retournent un `Iterable` paresseux ; appelez `toList()` pour transformer le résultat en une `List` :

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

Comme `map` et `where` retournent tous deux un `Iterable`, leurs appels peuvent être **chaînés** l'un après l'autre. Chaque étape reçoit le résultat de la précédente, et `toList()` est appelé une fois à la fin :

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort` réordonne une liste sur place. Par défaut, il utilise l'ordre naturel des éléments, mais vous pouvez passer une fonction anonyme qui **compare deux éléments** et retourne un nombre négatif, zéro ou un nombre positif. `compareTo` donne exactement un tel nombre, c'est donc le bloc de construction habituel :

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

En échangeant `a` et `b` dans la comparaison, l'ordre est inversé.

---

`reduce` combine tous les éléments d'une liste en une seule valeur. Sa fonction anonyme prend deux paramètres : la valeur **accumulée jusqu'ici** et l'**élément suivant**, et retourne la nouvelle valeur accumulée. Le premier élément est utilisé comme point de départ :

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

`reduce` lève une erreur sur une liste vide, puisqu'il n'y a pas de premier élément pour commencer.

---

Une fonction peut aussi **retourner une fonction**. Le type de retour est alors un type de fonction, et le corps retourne une fonction anonyme :

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

Remarquez que la fonction retournée utilise toujours `amount`, un paramètre de `makeAdder`, même après que `makeAdder` a terminé. Une fonction qui se souvient ainsi des variables qui l'entourent est appelée une **fermeture** (closure).

---

Une fermeture ne fait pas que lire les variables qu'elle capture : elle peut aussi les **modifier**, et les modifications sont conservées entre les appels. Cela permet de garder un état privé sans classe :

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

Chaque appel à `makeTimer()` crée une toute nouvelle variable `seconds`, donc deux minuteurs ne partagent jamais leur compteur.
