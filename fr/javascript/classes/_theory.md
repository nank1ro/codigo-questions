JavaScript est un langage de programmation orienté objet, ce qui signifie qu'il manipule des constructions de programmation appelées objets.
Vous pouvez penser à un objet comme une structure de données unique qui contient des données ainsi que des fonctions ; les fonctions d'un objet sont appelées ses méthodes.
Par exemple, lorsque vous appelez :
```javascript
arrayName.push("value");
```
JavaScript vérifie si `arrayName` a une méthode `push()` (que tous les tableaux ont) et exécute cette méthode s'il la trouve.

---

Les _classes_ sont des constructions polyvalentes et flexibles qui deviennent les blocs de construction de votre code de programme.
Une classe de base n'est composée que du mot-clé `class` et de son nom, par exemple :
```javascript
class ClassName {
    // class definition
}
```

---

Mettez quelque chose à l'intérieur de notre classe `Animal`
Pour ajouter des paramètres, nous devons utiliser le `constructor` par défaut

---

La définition d'une classe ne crée pas d'objet.
Pour ce faire, nous devons créer une __instance__ d'une classe.
En JavaScript, pour créer une nouvelle instance d'une classe, nous utilisons toujours le mot-clé `new` avant le nom de la classe.
Si vous voulez assigner une valeur par défaut à un paramètre, faites-le dans la liste des paramètres du constructeur

---

Lorsqu'une classe a ses propres fonctions, ces fonctions sont appelées des __méthodes__.

---

JavaScript nous permet de créer une classe comme enfant d'une autre, en utilisant le mot-clé `extends`

---

Vous pouvez accéder aux propriétés d'une instance en utilisant la _syntaxe pointée_.
En syntaxe pointée, vous écrivez le nom de la propriété immédiatement après le nom de l'instance, séparé par un point `.`, sans espaces :
```javascript
someInstance.someProperty
```
En utilisant la même syntaxe, nous pouvons également mettre à jour la valeur d'une propriété
