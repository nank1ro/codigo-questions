La prise de décision est requise lorsque nous voulons exécuter du code uniquement si une certaine condition est remplie.
Supposons que nous voulions jouer dehors uniquement si le temps est beau.
En programmation, nous pouvons enregistrer une variable booléenne `niceWeather` et effectuer l'action de jouer dehors `if` this variable is `true`, comme :
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```

---

Continuons avec l'exemple précédent.
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```
Nous avons vu que l'instruction `if` exécute le bloc de code uniquement si la condition est `true`.
Une autre chose importante à considérer est représentée par les **crochets ondulés** `{}` qui indiquent un bloc de code.

---

We just saw how to execute a block of code if a condition occurs, now let's see how to execute another block of code if the first condition fails.
We go to play outside if the weather is nice; otherwise, we stay home.
In Swift we can use the `else` statement, comme :
```swift
var niceWeather = true
if niceWeather {
    // play outside
} else {
    // stay home
}
```

---

Let's assume we have another condition to check, like in this example:
```swift
var num = 3
if num == 2 {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else {
    print("do something else")
}
```
et la sortie de ce code est `the number is 3`.
D'abord, vérifions si le nombre est égal à 2, c'est faux.
So let's move on to the second statement and check if `num` is equal to 3, being true we execute the following block of code by printing `the number is 3`

---

Nous pouvons ajouter autant d'instructions `else if` que nous le souhaitons, il n'y a pas de limites
```swift
var num = 4
if (num == 2) {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else if (num == 4) {
    print("the number is 4")
} else if (num == 5) {
    print("the number is 5")
} else if (num == 6) {
    print("the number is 6")
}
```
et la sortie de ce code est `the number is 4`.

---

Nous pouvons également imbriquer une instruction conditionnelle (`if`, `else if` ou `else`) dans une autre instruction conditionnelle, pour créer une structure plus complexe.
```swift
var num = 4
if num < 3 {
    print("the number is lower than 3")
} else {
    if num == 3 {
        print("the number is 3")
    } else if num == 4 {
        print("the number is 4")
    } else {
        print("the number is greather than 4")
    }
}
```
et la sortie de ce code est `the number is 4`.

---

L'opérateur ternaire conditionnel est un opérateur spécial avec trois parties, qui prend la forme `question ? answer1 : answer2`.
It's a shortcut for evaluating one of two expressions based on whether `question` is true or false.
If `question` is true, it evaluates `answer1` and returns its value; otherwise, it evaluates `answer2` and returns its value.
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
Le code abrégé pour le code ci-dessus est :
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
`c` is set equal to `a`, because the condition `a < b` was true

---

L'opérateur _nil-coalescing_ `a ?? b` déverrouille un optionnel `a` s'il contient une valeur, ou retourne une valeur par défaut `b` si `a` est `nil`.
L'expression `a` est toujours de type optionnel.
L'expression `b` doit correspondre au type qui est stocké à l'intérieur de a.
L'opérateur nil-coalescing est une notation abrégée pour le code ci-dessous :
```swift
a != nil ? a! : b
```
