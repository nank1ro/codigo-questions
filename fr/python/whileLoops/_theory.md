Souvent en programmation, nous devons répéter un bloc de code, par exemple :
```python
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
Ceci produit la sortie suivante :
```python
2 seconds
3 seconds
4 seconds
5 seconds
```
Évidemment, pour les longues déclarations, nous dépensionsnous beaucoup de temps à écrire le code, mais heureusement, nous pouvons utiliser des boucles.
Apprenons la boucle `while`, obtenant la même sortie ci-dessus.
```python
count = 2
while (count <= 5):
    print(f"{count} seconds")
    count += 1
```
Donc, nous avons créé une variable `count` en assignant `2`, la valeur initiale.
Ensuite, nous avons utilisé l'instruction `while` qui exécutera le bloc de code jusqu'à ce que la condition `count <= 5` soit `True`.
À l'intérieur du bloc de code, nous ne devons **pas** oublier d'ajouter la ligne `count += 1`.
Elle incrémente la valeur `count`, sinon, notre boucle sera infinie

---

Pour contrôler le nombre de fois qu'une boucle `while` se répète, nous commençons par une variable définie à un nombre.
Nous appelons cette variable une variable de compteur

---

Ensuite, nous utilisons une comparaison dans la condition pour comparer la variable `counter` à un nombre.

---

À l'intérieur du bloc de code, pour arrêter la boucle `while`, nous incrémentons la variable `counter`.

---

L'ordre dans lequel vous écrivez le code affecte la sortie.
