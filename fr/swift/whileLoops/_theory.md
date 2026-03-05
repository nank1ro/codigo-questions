Souvent en programmation, nous devons répéter un bloc de code, par exemple :
```swift
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
Cela produit la sortie suivante :
```swift
2 seconds
3 seconds
4 seconds
5 seconds
```
Évidemment, pour les longues instructions, nous passerions beaucoup de temps à écrire le code, mais heureusement, nous pouvons utiliser des boucles.
Apprenons la boucle `while`, en obtenant la même sortie ci-dessus.
```swift
var count = 2
while count <= 5 {
    print("\(count) seconds")
    count += 1
}
```
Donc, nous avons créé une variable `count` en assignant `2`, la valeur initiale.
Ensuite, nous avons utilisé l'instruction `while` qui exécutera le bloc de code jusqu'à ce que la condition `count <= 5` soit `true`.
À l'intérieur du bloc de code, nous ne devons **PAS** oublier d'ajouter la ligne `count += 1`.
Il incrémente la valeur `count`, sinon, notre boucle sera infinie

---

To control the times a `while` loop repeats, we start with a variable set to a number.
We call this variable a counter variable

---

Then, we use a comparison in the condition to compare the `counter` variable to a number.

---

Inside the block of code, in order to stop the `while` loop, we increment the `counter` variable.

---

The order you write code affects the output.

---

En Swift, nous avons aussi la variation **repeat-while** de la boucle `while`.
It performs a single pass through the loop block first, _before_ considering the loop's condition.
It then continues to repeat the loop until the condition is `false`.
The __repeat-while__ loop in Swift is analogous to a __do-while__ loop in other languages
