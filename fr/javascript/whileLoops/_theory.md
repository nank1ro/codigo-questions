Souvent en programmation, nous avons besoin de répéter un bloc de code, par exemple :
```javascript
console.log("2 seconds");
console.log("3 seconds");
console.log("4 seconds");
console.log("5 seconds");
```
Cela produit la sortie suivante :
```javascript
2 seconds
3 seconds
4 seconds
5 seconds
```
Évidemment, pour les longues déclarations, nous passerions beaucoup de temps à écrire le code, mais heureusement, nous pouvons utiliser des boucles.
Apprenons la boucle `while`, en obtenant la même sortie ci-dessus.
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
Donc nous avons créé une variable `count` en assignant `2`, la valeur initiale.
Ensuite, nous avons utilisé l'instruction `while` qui exécutera le bloc de code jusqu'à ce que la condition `count <= 5` soit `true`.
Dans le bloc de code, nous ne devons **PAS** oublier d'ajouter la ligne `count += 1`.
Il incrémente la valeur `count`, sinon, notre boucle sera infinie

---

Pour contrôler le nombre de fois qu'une boucle `while` se répète, nous commençons par une variable définie sur un nombre.
Nous appelons cette variable une variable de compteur

---

Ensuite, nous utilisons une comparaison dans la condition pour comparer la variable `counter` à un nombre.

---

Dans le bloc de code, pour arrêter la boucle `while`, nous incrémentons la variable `counter`.

---

L'ordre dans lequel vous écrivez le code affecte la sortie.

---

En JavaScript, nous avons aussi la variation **do-while** de la boucle `while`.
Il effectue un seul passage dans le bloc de boucle en premier, _avant_ de considérer la condition de la boucle.
Il continue ensuite à répéter la boucle jusqu'à ce que la condition soit `false`.
