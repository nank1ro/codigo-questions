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

Pour contrôler le nombre de fois qu'une boucle `while` se répète, nous commençons avec une variable définie sur un nombre.
Nous appelons cette variable une variable compteur

---

Ensuite, nous utilisons une comparaison dans la condition pour comparer la variable `counter` à un nombre.

---

À l'intérieur du bloc de code, afin d'arrêter la boucle `while`, nous incrémentons la variable `counter`.

---

L'ordre dans lequel vous écrivez le code affecte la sortie.

---

En Swift, nous avons aussi la variation **repeat-while** de la boucle `while`.
Elle effectue un premier passage dans le bloc de la boucle, _avant_ de considérer la condition de la boucle.
Elle continue ensuite à répéter la boucle jusqu'à ce que la condition soit `false`.
La boucle __repeat-while__ en Swift est analogue à une boucle __do-while__ dans d'autres langages
