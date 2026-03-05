Les types vous permettent de catégoriser tous les différents types de données que vous utilisez dans votre code.
En Dart, un __type__ est un moyen de dire au compilateur commentaire vous allez utiliser un morceau de données donné.
Voici un exemple de types que Dart supporte :
- int
- String
- double
- dynamic
- num

Dart supporte beaucoup d'autres types. Ceux énumérés sont les principaux que vous utiliserez.

---

Il est possible de définir explicitement le type d'une variable, par exemple :
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

Les variables avec un type explicite peuvent également être des constantes, ajoutez simplement le mot clé `const` ou `final` avant le type :
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> Remarque : Les données mutables vous permettent de les modifier quand vous le souhaitez de manière facile. Cependant, de nombreux programmeurs expérimentés apprécient les avantages des données immuables. Quand une valeur est immuable, vous pouvez faire confiance au fait que personne ne pourra changer la valeur après que vous l'ayez créée. Limiter vos données de cette manière prévient de nombreux bogues difficiles à trouver et facilite la réflexion et le test du programme.

---

Bien qu'il soit possible de noter le type d'une variable, cela est redondant. Vous savez que `10` est de type `int` et `3.14` est de type `double`. Le compilateur Dart est capable de le déduire grâce à l'__inférence de type__. Tous les langages de programmation ne disposent pas de l'_inférence de type_, et c'est ce qui fait de Dart un langage de programmation très puissant.

Vous pouvez simplement supprimer le type des variables, par exemple :
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

Lorsque le type d'une variable n'est pas explicitement noté, Dart essaiera de déduire son type.

---

Il y a une façon programmatique de vérifier le type d'une variable, à savoir avec le mot clé `is` :
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

Comme vous pouvez le voir, Dart a attribué le type `double` à la variable `number`.

---

Le mot-clé `is` vous permet de vérifier si une variable est du type que vous définissez. Mais vous pouvez
 également vérifier si une variable n'est pas du type défini avec le mot-clé `is!`
```dart
final number = 3.14;
print(number is! int); // true
```

---

Une autre option pour voir le type d'une variable à l'_exécution_ est d'utiliser la propriété `runtimeType` qui est disponible pour tous les types.
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

Parfois, vous vous retrouverez dans la situation d'avoir un type, mais d'avoir besoin de le convertir en un autre. Vous pourriez être tenté de faire :

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

Mais Dart se plaindra et vous donnera l'erreur :
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

Certains langages de programmation ne sont pas aussi restrictifs et convertiront silencieusement. L'expérience montre que ce type de conversion implicite silencieuse est une source fréquente de bogues et de problèmes de performance. Dart a désactivé cette fonctionnalité pour éviter ces problèmes.

N'oubliez pas que les ordinateurs comptent sur les programmeurs pour savoir quoi faire. En Dart, cela inclut être explicite sur le type de conversion.

Au lieu d'attendre une conversion implicite de Dart, vous devez dire explicitement que vous voulez que Dart convertisse le type pour vous. Voici comment convertir un nombre `double` en `int` :
```dart
var integer = decimal.toInt();
```

L'affectation indique à Dart, sans équivoque, que vous voulez convertir du type original `double` vers le nouveau type `int`.

> NOTES : Dans ce cas, assigner une valeur décimale à un entier entraîne une perte de précision. La variable `integer` a la valeur __3__ au lieu de __3.14__. C'est pourquoi il est important d'être explicite. Dart veut être sûr de ce que vous faites et vous informe que vous perdrez des informations lors de la conversion.

---

Jusqu'à présent, nous avons vu les opérateurs utilisés indépendamment sur des entiers ou des décimaux. Que se passe-t-il si vous avez
un entier et devez le multiplier par un nombre décimal ? Voyons un exemple :
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius` est de type `int` tandis que `pi` est de type `double`. Quel sera le type de `circumference` ? Dart attribuera le type `double` à la variable `circumference`. C'est le choix le plus sûr car si on l'avait fait de type `int`, cela aurait pu causer une perte de précision.

Si vous voulez un `int` comme résultat, vous devez faire la conversion explicitement :
```dart
const circumference = (2 * pi * radius).toInt();
```

Les parenthèses indiquent à Dart de multiplier d'abord, puis de prendre le résultat et de le convertir en valeur entière. Malheureusement, l'analyseur n'aimera pas ce code :
 > Const variables must be initialized with a constant value.

Le problème est que la méthode `toInt` est une méthode uniquement disponible à l'exécution. Cela signifie que la variable `circumference` ne peut pas être déterminée au moment de la compilation, il n'est donc pas possible que la variable soit constante. Pour corriger, remplacez `const` par `final` :

```dart
final circumference = (2 * pi * radius).toInt();
```

Maintenant `circumference` est une variable __constante d'exécution__ de type `int`.

---

Parfois, vous pouvez avoir une variable avec un type générique, mais vous avez besoin d'une fonctionnalité qui n'existe que dans un sous-type. Si vous êtes sûr que le type de la variable est le sous-type dont vous avez besoin, alors vous pouvez utiliser le mot-clé `as` pour changer son type. Cette procédure est également connue sous le nom de __transtypage__ (type casting), voici un exemple :

```dart
num number = 3;
```

Disons que nous voulons vérifier si le nombre est pair, et la fonctionnalité en question est présente uniquement sur le sous-type `int`.
```dart
print(number.isEven);
```

Le code ci-dessus devrait vous retourner une erreur de type :
> The getter `isEven` isn't defined for the type 'num'.

Le type `num` est un type trop général pour savoir si un nombre est pair ou impair. Seuls les entiers peuvent être pairs ou impairs.
Le problème se pose si `num` contient une valeur `double`, puisque `num` inclut à la fois les types `double` et `int`. Dans ce cas, nous sommes sûrs que __3__ est un entier, donc nous pouvons transtyper en `int`

```dart
final integer = number as int;
print(integer.isEven); // false
```

Le mot-clé `as` amène le compilateur à reconnaître la variable `integer` comme ayant le type `int`. Cela vous permet d'utiliser la propriété `isEven` qui est présente sur les entiers. Puisque le nombre __3__ n'est pas pair, le résultat est false.

Il faut faire attention lors du transtypage. Si vous transtypez incorrectement, vous obtiendrez une erreur à l'exécution :
```dart
num numero = 3;
final decimale = numero as double;
```

Cela fera planter le programme avec l'erreur suivante :
> CastError (type 'int' is not a subtype of type 'double' in type cast)

Le type à l'exécution de `number` est `int` et non `double`. En Dart, vous ne pouvez pas transtyper avec des types de même niveau, comme `int` et `double`. Vous ne pouvez transtyper que des sous-types.
