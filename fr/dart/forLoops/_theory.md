Une boucle `for` répète un bloc de code un nombre défini de fois. La syntaxe de base est :

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: s'exécute une fois avant le démarrage de la boucle (p. ex. `int i = 0`)

**condition**: vérifiée avant chaque itération ; la boucle s'arrête quand elle est fausse

**update**: s'exécute après chaque itération (p. ex. `i++`)

---

Vous pouvez utiliser la variable de boucle dans le corps pour suivre le compte courant. Par exemple, pour accumuler une somme :

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

Après la boucle, `total` est égal à 15.

---

Une boucle `for` peut compter **à rebours** en utilisant un décrément (`i--`) et une condition `>=` :

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

C'est utile pour les comptes à rebours ou l'itération en sens inverse.

---

La boucle `for-in` itère sur chaque élément d'une collection sans avoir besoin d'un index :

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

À chaque itération, l'élément suivant est assigné à la variable de boucle (`fruit` ici).

---

L'instruction `break` quitte une boucle immédiatement lorsqu'une condition est remplie :

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

C'est utile lorsqu'on recherche une valeur et qu'on veut s'arrêter dès qu'elle est trouvée.
