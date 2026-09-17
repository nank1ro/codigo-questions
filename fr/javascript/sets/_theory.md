Un **Set** est une collection de valeurs **uniques** : chaque valeur peut apparaître au plus une fois, et il n'y a pas d'index pour accéder à une valeur par position.
Les sets sont parfaits quand seul importe *quelles* valeurs sont présentes, pas combien de fois ni dans quel ordre.
Vous créez un set vide avec `new Set()`, ajoutez une valeur avec `add(value)` et vérifiez si une valeur est présente avec `has(value)` :
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// affiche true
console.log(colors.has("green"));
// affiche false
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
// affiche 2
tags.delete("css");
console.log(tags.size);
// affiche 1
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
// affiche 3
```
L'opérateur **spread** `...` fonctionne dans l'autre sens et retransforme un set en tableau :
```javascript
let unique = [...distinct];
console.log(unique);
// affiche [ 1, 2, 3 ]
```
`Array.from(distinct)` fait la même chose.

---

Un set se souvient de l'ordre dans lequel les valeurs ont été ajoutées, et vous pouvez le parcourir avec `for...of` :
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// affiche 3
// affiche 1
// affiche 2
```
Les sets ont aussi une méthode `forEach()` qui appelle une fonction pour chaque valeur :
```javascript
nums.forEach((n) => console.log(n * 10));
// affiche 30
// affiche 10
// affiche 20
```

---

`delete(value)` renvoie `true` quand la valeur a été retirée et `false` quand elle n'était pas dans le set.
Pour retirer **toutes** les valeurs d'un coup, appelez `clear()` :
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// affiche true
console.log(cart.delete("pen"));
// affiche false
cart.clear();
console.log(cart.size);
// affiche 0
```

---

Un set détermine si deux valeurs sont "identiques" avec presque la même règle que `===` (sauf que `NaN` est considéré comme égal à lui-même). Pour les chaînes et les nombres, cela compare le contenu, mais **les objets sont comparés par référence** : deux littéraux d'objet avec des champs identiques sont deux valeurs différentes.
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// affiche 1
people.add({ name: "Alice" });
console.log(people.size);
// affiche 2
```
Seul le fait de rajouter exactement le même objet est ignoré.

---

Combiner spread et `filter()` vous donne les opérations classiques de la théorie des ensembles. Chacune construit une **nouvelle** collection et laisse les originaux inchangés :
- **union**, chaque valeur présente dans `a`, dans `b` ou dans les deux : `new Set([...a, ...b])`
- **intersection**, seulement les valeurs présentes dans **les deux** : `[...a].filter((x) => b.has(x))`
- **différence**, les valeurs de `a` qui ne sont **pas** dans `b` : `[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// affiche [ 1, 2, 3, 4 ]
console.log([...a].filter((x) => b.has(x)));
// affiche [ 3 ]
console.log([...a].filter((x) => !b.has(x)));
// affiche [ 1, 2 ]
```
Les moteurs JavaScript récents fournissent aussi `a.union(b)`, `a.intersection(b)` et `a.difference(b)` directement sur les sets, mais les versions avec spread et filter fonctionnent partout.

---

Pour conserver la même interface que `Map`, un set propose les méthodes d'itération `values()`, `keys()` et `entries()`.
Comme un set n'a pas de clés, `keys()` n'est qu'un autre nom pour `values()`, et `entries()` produit chaque valeur **deux fois**, sous forme de paire `[value, value]` :
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// affiche [ 'a', 'b' ]
console.log([...letters.entries()]);
// affiche [ [ 'a', 'a' ], [ 'b', 'b' ] ]
```
En pratique vous en avez rarement besoin : `for...of` et spread parcourent déjà directement les valeurs.

---

`new Set()` accepte n'importe quel **itérable**, pas seulement des tableaux. Une chaîne est itérable caractère par caractère, ce qui vous donne les caractères distincts d'un texte :
```javascript
let letters = new Set("hello");
console.log([...letters]);
// affiche [ 'h', 'e', 'l', 'o' ]
```
