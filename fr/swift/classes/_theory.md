Swift est un langage de programmation orienté objet, ce qui signifie qu'il manipule des constructions de programmation appelées objets.
Vous pouvez penser à un objet comme une structure de données unique qui contient des données ainsi que des fonctions ; les fonctions d'un objet s'appellent ses méthodes.
Par exemple, lorsque vous appelez :
```swift
dictName.removeValue(forKey: "keyName")
```
Swift vérifie si `dictName` a une méthode `removeValue()` (que tous les dictionnaires possèdent) et exécute cette méthode s'il la trouve.

---

Les **structures** et les **classes** sont des constructions à usage général et flexibles qui deviennent les éléments constitutifs du code de votre programme.
Une classe|structure de base consiste uniquement au mot-clé `class` ou `struct` et à son nom, par exemple :
```swift
class ClassName {
    // class definition
}
struct ClassName {
    // structure definition
}
```

---

Mettons quelque chose dans notre classe `Animal`

---

La définition d'une classe ne crée pas un objet.
Pour ce faire, nous devons créer une **instance** d'une classe

---

Quand une classe a ses propres fonctions, ces fonctions s'appellent des **méthodes**.

---

Les structures et les classes en Swift ont beaucoup en commun. Les deux peuvent :
- Définir des propriétés pour stocker des valeurs
- Définir des méthodes pour fournir des fonctionnalités
- Définir des indices pour fournir l'accès à leurs valeurs en utilisant la syntaxe des indices
- Définir des initialiseurs pour configurer leur état initial
- Être étendus pour développer leurs fonctionnalités au-delà d'une implémentation par défaut
- Conformer aux protocoles pour fournir une fonctionnalité standard d'une certaine sorte

Mais les classes ont des capacités supplémentaires que les structures n'ont pas :
- L'héritage permet à une classe d'hériter des caractéristiques d'une autre
- Le transtypage vous permet de vérifier et d'interpréter le type d'une instance de classe lors de l'exécution
- Les déinitialiseurs permettent à une instance de classe de libérer toutes les ressources qu'elle a allouées
- Le comptage des références permet plus d'une référence à une instance de classe

---

Vous pouvez accéder aux propriétés d'une instance en utilisant la _syntaxe pointée_.
En syntaxe pointée, vous écrivez le nom de la propriété immédiatement après le nom de l'instance, séparé par un point `.`, sans espaces :
```swift
someInstance.someProperty
```
En utilisant la même syntaxe, nous pouvons également mettre à jour la valeur d'une propriété

---

Un avantage des structures est qu'elles ont un initialiseur sans paramètres généré automatiquement, que vous pouvez utiliser pour initialiser les propriétés des membres de nouvelles instances de structure.
Les valeurs initiales des propriétés de la nouvelle instance peuvent être passées à l'initialiseur sans paramètres par nom
