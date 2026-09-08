Un **Set** est une collection de valeurs **uniques** : chaque valeur peut apparaître au plus une fois, et il n'y a pas d'index pour accéder à une valeur par position.
Les sets sont parfaits quand seul importe *quelles* valeurs sont présentes, pas combien de fois ni dans quel ordre.
Vous créez un set vide avec `new Set()`, ajoutez une valeur avec `add(value)` et vérifiez si une valeur est présente avec `has(value)` :
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
```

---

Ajouter une valeur déjà présente dans le set ne fait **rien** : les doublons sont simplement ignorés.
Deux autres éléments essentiels :
- `delete(value)` retire la valeur du set
- `size` est le nombre de valeurs stockées (une propriété, donc sans parenthèses)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
```

---

`add()` renvoie le set lui-même, donc plusieurs appels peuvent être chaînés :
```javascript
let letters = new Set();
letters.add("a").add("b");
```
Que vous chaîniez ou non, une valeur déjà présente n'est jamais ajoutée une seconde fois, donc `size` compte chaque valeur distincte une seule fois.

---

Vous pouvez construire un set en une seule fois en passant un tableau à `new Set()`. Les doublons du tableau sont éliminés, c'est donc le moyen le plus rapide de trouver les valeurs distinctes d'un tableau :
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// prints 3
```
L'opérateur **spread** `...` fonctionne dans l'autre sens et retransforme un set en tableau :
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` fait la même chose.

---

Un set se souvient de l'ordre dans lequel les valeurs ont été ajoutées, et vous pouvez le parcourir avec `for...of` :
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
Les sets ont aussi une méthode `forEach()` qui appelle une fonction pour chaque valeur :
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
