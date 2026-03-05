Nous savons comment répéter du code en utilisant une boucle `while`.
Comme ce programme qui répète les instructions pour afficher `bonjour`
```javascript
var counter = 0;

while (counter < 5) {
    console.log("hello");
    counter++;
}
```
Mais nous pouvons faire la même chose avec les boucles `for` :
```javascript
for (let i = 0; i < 5; i++) {
    console.log("hello");
}
```

---

Dans une boucle `for`, nous pouvons spécifier combien de fois nous voulons que notre boucle s'exécute

---

Nous pouvons utiliser `<` pour boucler jusqu'au nombre suivant exclu, ou `<=` pour boucler jusqu'au nombre suivant inclus

---

La variable appelée `i` est la variable compteur.
Nous pouvons lui donner le nom que nous voulons.
Elle compte à quelle répétition de la boucle nous en sommes actuellement.

---

En JavaScript, nous avons aussi la boucle `forEach`.
En fait, `forEach` appelle la fermeture donnée sur chaque élément de la séquence dans le même ordre qu'une boucle `for` :
```javascript
// this is an array, we'll see about that soon
let numbers = [1, 3, 5, 7, 9];
numbers.forEach((num) => console.log(num));}
```
L'utilisation de la méthode `forEach` se distingue d'une boucle `for` de deux manières importantes :
1. Les instructions `break` ou `continue` ne peuvent pas être utilisées pour quitter l'appel actuel de la fermeture du corps ou pour sauter les appels suivants.
2. L'utilisation de l'instruction `return` dans la fermeture du corps ne fera que quitter la fermeture et non la portée externe, et elle ne sautera pas les appels suivants.
NOTE : `=>` s'appelle _fonction fléchée_ et c'est une syntaxe de fonction plus courte ES6 qui remplace les accolades {} et retourne la valeur (si nécessaire)
