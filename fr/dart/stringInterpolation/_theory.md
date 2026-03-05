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

We can also insert variables after the dollar signs to show their value

---

We can use curly brackets to insert values as often as we like using the string interpolation

---

Inside the `${}` we can also put conditions, for example:
```dart
print("The answer is ${true ? "correct": "wrong"}");
// prints The answer is correct
```

---

Interpolation de chaînes is best used in print statements, but we can also store them in variables like normal strings.
