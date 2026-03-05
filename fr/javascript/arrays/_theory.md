Les tableaux (arrays) sont un type de données que vous pouvez utiliser pour stocker une collection de différents éléments d'information en tant que séquence sous un seul nom de variable.
Un tableau stocke plusieurs valeurs d'un ou plusieurs types et utilise des **indexes** pour distinguer ces valeurs.
Vous pouvez assigner des éléments à un tableau avec une expression de la forme:
```javascript
var arrayName = [item1, item2];
```

---

Vous pouvez accéder à un élément individuel du tableau par son index.
Un index est comme une adresse qui identifie la place de l'élément dans le tableau.
L'index apparaît directement après le nom du tableau, entre les crochets, comme ceci:
```javascript
arrayName[index];
```
Les indices du tableau commencent par `0`, **pas** `1`! Vous accédez au premier élément d'un tableau comme ceci: `arrayName[0]`.
Le deuxième élément d'un tableau est à l'index 1: `arrayName[1]`.

---

Un index de tableau se comporte comme n'importe quel autre nom de variable.
Il peut être utilisé pour accéder ainsi que pour assigner des valeurs.
Vous avez vu comment accéder à un index de tableau comme ceci:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
Voici comment fonctionne une affectation:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

Tout comme les chaînes de caractères, les tableaux ont une **length**.
La longueur d'un tableau est le nombre d'éléments qu'il contient

---

Un tableau n'a pas besoin d'avoir une longueur fixe.
Vous pouvez ajouter des éléments à la fin d'un tableau à tout moment!
Pour ajouter un élément à un tableau, nous utilisons la fonction `push`:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

Parfois, vous ne voulez accéder qu'à une partie d'un tableau.
Considérez le code suivant:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
D'abord, nous créons un tableau appelé `numbers`.
Ensuite, nous prenons une sous-section du tableau et la stockons dans le tableau slice.
Nous le faisons en définissant les indices que nous voulons inclure après le nom du tableau: `numbers.slice(1, 3)`.
Gardez à l'esprit que l'index de droite est exclu

---

En JavaScript, nous pouvons découper un tableau comme nous le souhaitons!
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
Si votre tranche de tableau inclut le tout premier ou dernier élément d'un tableau, l'index de cet élément n'a pas besoin d'être inclus

---

Les éléments du tableau peuvent être de n'importe quel type.
```javascript
var arrayName = ["one", 2, true];
```
En fait, ci-dessus, nous avons, dans l'ordre, une chaîne, un entier et un booléen.
Mais nous pouvons aussi avoir des tableaux avec des tableaux!

---

Parfois, vous devez rechercher un élément dans un tableau.
En JavaScript, nous pouvons utiliser la méthode `indexOf()`:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
Le code ci-dessus imprime le premier index qui contient la chaîne `"Zac"`, `1` dans ce cas.
Nous pouvons également insérer des éléments dans un tableau à un index spécifique, en utilisant la méthode `splice()`:
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
Le code ci-dessus insère `"Ali"` à l'index `1`, ce qui déplace tout après cet index d'une position vers le bas.
La deuxième valeur `0` signifie _deleteCount_, dans ce cas, nous ne supprimons aucun élément du tableau; mais si nous avions spécifié `1`, la valeur `Zac` aurait été supprimée du tableau

---

En JavaScript, nous pouvons boucler à travers un tableau de manière très simple en utilisant les mots-clés `for..of`:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3
```
Un nom de variable suit le mot-clé `for`, il sera assigné la valeur de chaque élément du tableau à tour de rôle.
