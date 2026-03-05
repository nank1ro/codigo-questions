Vous avez peut-être considéré la situation où vous aimeriez réutiliser un morceau de code, juste avec quelques valeurs différentes.
Au lieu de réécrire tout le code, il est beaucoup plus propre de définir une fonction, qui peut ensuite être utilisée à plusieurs reprises.
En Swift, nous utilisons le mot-clé `func` suivi du nom de la fonction :
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

Les parenthèses dans la __définition de fonction__ n'ont pas besoin d'être vides si nous voulons spécifier des paramètres

---

Parfois, nous voulons qu'une fonction __retourne__ une valeur.
Eh bien, il y a le mot-clé `return`.

---

Les fonctions peuvent avoir plusieurs paramètres d'entrée, qui sont écris entre les parenthèses de la fonction, séparés par des virgules.
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

Vous pouvez utiliser un type tuple comme type de retour pour une fonction afin de retourner plusieurs valeurs dans une seule valeur de retour composée.

---

Si vous ne voulez pas d'étiquette d'argument pour un paramètre, écrivez un trait de soulignement `_` à la place d'une étiquette d'argument explicite pour ce paramètre

---

You can define a _default_ value for any parameter in a function by assigning a value to the parameter after that parameter's type.
Si une valeur par défaut est définie, vous pouvez omettre ce paramètre lors de l'appel de la fonction
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

Un _paramètre variadique_ accepte zéro ou plusieurs valeurs d'un type spécifié.
You use a variadic parameter to specify that the parameter can be passed a varying number of input values when the function is called.
Write variadic parameters by inserting three period characters `...` after the parameter's type name.
The values passed to a variadic parameter are made available within the function's body as an array of the appropriate type.
Par exemple, un paramètre variadique avec un nom de `numbers` et un type de `Double...` est rendu disponible dans le corps de la fonction en tant que tableau constant appelé nombres de type `[Double]`

---

Dans les fonctions, nous pouvons ajouter un _commentaire optionnel_ qui explique ce que la fonction fait :
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
We can use `///` for a single line comment and `/** */` for a multi line comment
