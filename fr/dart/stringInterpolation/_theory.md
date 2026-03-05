Une _interpolation_ de chaîne est un moyen programmatique de générer une chaîne.
En Dart, nous pouvons utiliser le signe `+` (concaténation) pour afficher deux ou plusieurs chaînes ensemble, comme :
```dart
print("Hello " + "Dart!");
// prints "Hello Dart!"
```

---

Mais l'utilisation du signe `+` pour ajouter un nombre comme '10' à une chaîne comme ` "friends"` produit une erreur car ce sont des valeurs d'une sorte différente

---

Interpolation de chaînes allow us to display expressions like adding a string to a number, without any error.
Placing an expression inside `${}` evaluates it.
The return value is converted to a String and inserted into the resulting String

---

Si vous mettez un `$` avant un nom d'identificateur, l'interpolation de chaîne insérera le contenu de cet identificateur dans la `String`

---

Si ce qui suit le signe `$` n'est pas reconnaissable comme un identificateur de programme, vous allez rencontrer une erreur

---

Nous pouvons également insérer des variables après les signes dollar pour afficher leur valeur

---

Nous pouvons utiliser des accolades pour insérer des valeurs autant de fois que nous le souhaitons en utilisant l'interpolation de chaînes

---

À l'intérieur de `${}`, nous pouvons également mettre des conditions, par exemple :
```dart
print("The answer is ${true ? "correct": "wrong"}");
// prints The answer is correct
```

---

L'interpolation de chaînes est idéalement utilisée dans les instructions print, mais nous pouvons également les stocker dans des variables comme des chaînes normales.
