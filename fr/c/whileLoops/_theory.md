Souvent en programmation, nous devons répéter un bloc de code, par exemple:
```c
printf("2 seconds\n");
printf("3 seconds\n");
printf("4 seconds\n");
printf("5 seconds\n");
```
Cela produit la sortie suivante:
```c
2 seconds
3 seconds
4 seconds
5 seconds
```
Évidemment, pour de longues déclarations, nous passerions beaucoup de temps à écrire le code, mais heureusement, nous pouvons utiliser des boucles.
Apprenons la boucle `while`, en obtenant la même sortie que ci-dessus.
```c
int count = 2;
while (count <= 5) {
    printf("%d seconds\n", count);
    count++;
}
```
Nous avons créé une variable `count` en assignant `2`, la valeur initiale.
Ensuite, nous avons utilisé la déclaration `while` qui exécutera le bloc de code jusqu'à ce que la condition `count <= 5` soit `true`.
À l'intérieur du bloc de code, nous ne devons **PAS** oublier d'ajouter la ligne `count++;`.
Elle incrémente la valeur `count`, sinon, notre boucle sera infinie

---

Pour contrôler le nombre de fois qu'une boucle `while` se répète, nous commençons par une variable définie à un nombre.
Nous appelons cette variable une variable compteur

---

Ensuite, nous utilisons une comparaison dans la condition pour comparer la variable `counter` à un nombre.

---

À l'intérieur du bloc de code, pour arrêter la boucle `while`, nous incrémentons la variable `counter`.

---

L'ordre dans lequel vous écrivez le code affecte la sortie.
