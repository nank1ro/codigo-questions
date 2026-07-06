Une **fonction** est un bloc de code réutilisable qui effectue une tâche spécifique. En Dart, on définit une fonction avec un type de retour, un nom et une paire de parenthèses `()`.

Lorsqu'une fonction ne retourne aucune valeur, son type de retour est `void` :

```dart
void sayHello() {
  print("Hello!");
}
```

On appelle la fonction en écrivant son nom suivi de `()` :

```dart
sayHello(); // prints Hello!
```

---

Les fonctions peuvent **retourner une valeur** à l'appelant. On déclare le type de retour avant le nom de la fonction et on utilise le mot-clé `return` pour renvoyer la valeur :

```dart
int getAge() {
  return 25;
}
```

Le type avant le nom de la fonction (`int`) indique à Dart quel type de valeur la fonction retournera. On peut utiliser `String`, `int`, `double`, `bool` et d'autres.

---

Les fonctions peuvent accepter des **paramètres** — des valeurs passées lors de l'appel de la fonction. Les paramètres sont déclarés entre les parenthèses avec leur type et leur nom :

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

Chaque paramètre a un type (`int`) et un nom (`n`). Les paramètres multiples sont séparés par des virgules.

---

Dart prend en charge les **fonctions fléchées** avec la syntaxe `=>`. Lorsque le corps d'une fonction est une seule expression, on peut le raccourcir avec `=>` à la place de `{ return ...; }` :

```dart
// Fonction normale
int double(int n) {
  return n * 2;
}

// Fonction fléchée — même résultat
int double(int n) => n * 2;
```

Les fonctions fléchées rendent le code plus concis. Le `=>` remplace à la fois les accolades et le mot-clé `return`.

---

Dart prend en charge les **paramètres nommés** — des paramètres entourés d'accolades `{}`. Les paramètres nommés doivent être appelés par leur nom et peuvent avoir des valeurs par défaut ou être marqués `required` :

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

Les paramètres nommés améliorent la lisibilité, surtout quand une fonction a de nombreux paramètres.
