Les variables sont des conteneurs pour stocker des valeurs de données.
Chaque variable en JavaScript est un objet.
Pour créer une variable, nous devons lui donner un **nom** en gardant à l'esprit qu'il ne doit pas contenir d'espaces.
Une variable est créée au moment où vous lui attribuez une valeur pour la première fois.
En JavaScript, vous déclarez des constantes avec les mots-clés `let` ou `const` et des variables avec le mot-clé `var`.
La valeur d'une constante ne peut pas être modifiée une fois définie, tandis qu'une variable peut être définie à une valeur différente à l'avenir.
Un exemple de création d'une variable nommée `x` est :
```javascript
var x = 1;
```
De cette façon, nous avons assigné la valeur `1` à la variable nommée `x`.
Si nous affichons la variable `x`, nous récupérons le nombre `1` :
```javascript
console.log(x);
// prints 1
```

---

Les variables sont appelées de cette façon parce que la valeur qu'elles stockent peut changer.
Nous pouvons mettre à jour `x` en utilisant `=` et en lui donnant une nouvelle valeur.
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

Nous pouvons également donner aux variables les valeurs d'autres variables.
Ici, nous pouvons donner à la variable `y` la valeur de `x`
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

When we update a variable, it forgets its previous value.
Ici, nous pouvons afficher la variable `x` deux fois et voir comment sa valeur se met à jour.
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

En JavaScript, les variables chaîne peuvent être déclarées en utilisant à la fois des guillemets doubles et simples :
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

Si nous voulons un nom de variable avec plusieurs mots, nous utilisons **camelCase**.
C'est la pratique d'écrire des phrases de telle sorte que chaque mot au milieu de la phrase commence par une majuscule
