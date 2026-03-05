En Swift, nous pouvons utiliser le signe `+` pour afficher deux chaînes ou plus ensemble, comme :
```swift
print("Hello " + "Swift!") // prints "Hello Swift!"
```

---

Mais l'utilisation du signe `+` pour ajouter un nombre comme '10' à une chaîne comme `"friends"` produit une erreur car ce sont des types de valeurs différents

---

Interpolation de chaîne allow us to display expressions like adding a string to a number, without any error.

---

Chaque instruction d'interpolation de chaîne se compose de deux parties : le `\()` où nous insérons le nombre ou la variable, et la chaîne normale

---

Next, we add the different kind of value in curly braces so it'll display as one print statement. Like here, with `\(5)`

---

Inserting variables like `friends` between the round brackets displays their value too

---

We can use round brackets to insert values as often as we like inside the string interpolation

---

Interpolation de chaînes are best used in print statements, but we can also store them in variables like normal strings.
