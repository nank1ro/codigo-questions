Les variables sont des conteneurs pour stocker des valeurs.
Chaque variable en Dart est un objet (`Object`).
Pour créer une variable, nous devons lui donner un __nom__ en tenant compte du fait qu'elle ne doit pas contenir d'espaces.
Jetez un œil à ce qui suit :

```dart
int number = 1;
```

Cette déclaration crée une variable appelée `number` de type `int`.
Elle définit ensuite la valeur de la variable au nombre `1`.
La partie `int` de la déclaration est connue sous le nom __d'annotation de type__ et indique à Dart explicitement le type de la variable.

---

Dans l'exemple précédent, nous avons vu la création d'une variable :

```dart
int number = 1;
```

Ne vous laissez pas tromper par le symbole `=`.
Ce n'est pas le symbole d'égalité comme en mathématiques, mais il est connu sous le nom d'__opérateur d'affectation__ car il assigne une valeur à la variable.
Le signe d'égalité, en revanche, est `==`.

---

Si vous voulez changer la valeur d'une variable, il suffit de lui assigner une valeur différente du même type :

```dart
int number = 1;
number = 2;
```

---

Le type `int` permet de stocker des nombres entiers.
Pour enregistrer des nombres décimaux, nous pouvons utiliser le type `double` :

```dart
double pi = 3.14159;
```

Cet exemple est similaire au précédent. Cette fois, cependant, la variable est de type `double`, un type qui permet de stocker des nombres décimaux avec une haute précision.

---

Dart est un langage __type-safe__.
Cela signifie que lorsque vous attribuez un type à une variable, vous ne pouvez pas le changer après. Voici un exemple :

```dart
int integerNumber = 1;
integerNumber = 3.14159; // Error
```

3.14159` est de type `double`, mais vous avez déjà défini `integerNumber` avec le type `int`.

Bien sûr, il peut parfois être utile d'attribuer des types connexes à la même variable. Par exemple, vous pourriez vouloir une variable `integerNumber` qui accepte à la fois les nombres `int` et `double`, comme ici :

```dart
num number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // Error
```

À la fois `int` et `double` étendent `num`, donc les deux types sont acceptés.
Cependant, si nous essayons d'attribuer une `String`, le compilateur retourne une erreur.

---

Si vous aimez vivre dangereusement, nous pouvons complètement ignorer la __sécurité de type__ du langage en utilisant le type `dynamic`.
Cela vous permet d'assigner n'importe quel type de valeur à la variable.

```dart
dynamic number;
number = 1; // OK
number = 3.14159; // OK
number = '10'; // OK
```

Cette approche est fortement déconseillée car les erreurs ne sont plus interceptées par l'_analyseur_ du code, mais uniquement à l'_exécution_ (lorsque le programme est en cours d'exécution).

---

Dart supporte l'__inférence de type__.
Il n'est pas nécessaire d'indiquer le type d'une variable car Dart peut déduire son type.
Le mot-clé `var` indique à Dart d'utiliser le type le plus approprié.

```dart
var number = 5;
```

Il n'est pas nécessaire de dire à Dart que le nombre `5` est de type `int`.
Dart déduit le type et fait de `number` un type `int`.

---

Dart supporte deux types différents de "_variables_" dont la valeur ne change jamais. Elles sont déclarées avec les mots-clés `const` et `final`.
Commençons par voir ce que signifie `const`.

## const (constantes)

Les variables dont vous pouvez changer la valeur sont connues sous le nom de __données mutables__. Les données mutables sont souvent surutilisées et peuvent présenter des problèmes. Il est facile de perdre la trace de tous les points dans le code qui peuvent changer la valeur d'une variable.

Pour cette raison, vous devriez utiliser des `const`antes au lieu de `var`iables chaque fois que possible. Ces variables qui ne peuvent pas changer de valeur sont également appelées __données immuables__.

Pour créer une constante en Dart, nous utilisons le mot-clé `const` :

```dart
const number = 5;
```

Tout comme `var`, Dart avec l'__inférence de type__ détermine que `number` est de type `int`.

---

Lorsque vous avez déclaré une variable constante, vous ne pouvez plus changer sa valeur. Par exemple :

```dart
const number = 2;
number = 3; // Error
```

Ce code produit l'erreur :
> Constant variables can't be assigned a value.

C'est-à-dire qu'il n'est pas possible de changer la valeur d'une variable constante.

---

Vous vous retrouverez souvent dans la situation de vouloir utiliser une constante mais de ne pas connaître la valeur au moment de la compilation. Vous ne connaîtrez la valeur qu'après le démarrage de l'exécution du programme.
Ce type de constante est connu sous le nom de __constante d'exécution__.

En Dart, `const` est uniquement utilisé pour les __constantes de compilation__ pour les valeurs qui peuvent être déterminées par le compilateur avant l'exécution du programme.

Si vous ne pouvez pas créer une variable constante parce que vous ne connaissez pas sa valeur au moment de la compilation, alors vous devez utiliser le mot-clé `final` pour faire de la variable une __constante d'exécution__.

Il y a de nombreuses raisons pour lesquelles vous ne pouvez pas connaître la valeur d'une variable avant l'exécution du programme. Par exemple, vous devriez obtenir la valeur depuis le serveur, ou la demander à l'utilisateur.

---

Voici un exemple de valeur qui ne peut être obtenue qu'à l'exécution :

```dart
final currentHour = DateTime.now().hour;
```

`DateTime.now()` est une fonction pour obtenir la date et l'heure actuelles au moment de l'exécution du code.
Avec le champ `hour`, nous accédons au nombre d'heures écoulées depuis le début de la journée.

Puisque la valeur de `hour` est différente selon le moment où le code est exécuté, cela peut être défini comme une valeur d'_exécution_.

Si vous essayez de changer la valeur d'une variable `final`, vous obtenez une erreur.
