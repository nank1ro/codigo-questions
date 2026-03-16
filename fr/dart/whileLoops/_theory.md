Une boucle `while` répète un bloc de code tant qu'une condition est `true`.

```dart
int i = 0;
while (i < 3) {
  print(i);
  i++;
}
```

La boucle vérifie la condition **avant** chaque itération. Quand `i < 3` devient `false`, la boucle s'arrête.

---

Une variable compteur contrôle le nombre de fois qu'une boucle `while` s'exécute.

```dart
int count = 0;
while (count < 5) {
  count++;
}
print(count); // 5
```

Le compteur commence à `0`, et la boucle l'incrémente à chaque itération jusqu'à ce que `count < 5` soit `false`.

---

Une boucle `do-while` est similaire à une boucle `while`, mais elle **exécute toujours le corps au moins une fois** — la condition est vérifiée *après* chaque itération.

```dart
int i = 0;
do {
  print(i);
  i++;
} while (i < 3);
```

Même si la condition est `false` dès le départ, le corps s'exécute une fois.

---

La condition d'une boucle `while` peut contenir n'importe quelle expression booléenne. Dès que la condition est évaluée à `false`, la boucle se termine.

```dart
int n = 100;
while (n > 1) {
  n ~/= 2;
}
print(n); // 0
```

Ici, `n` est divisé par deux à chaque itération en utilisant la division entière (`~/`).

---

Le mot-clé `break` quitte une boucle immédiatement, indépendamment de la condition de la boucle.

```dart
int i = 0;
while (true) {
  if (i == 3) break;
  print(i);
  i++;
}
```

Sans `break`, la boucle `while (true)` s'exécuterait indéfiniment. Ici, elle s'arrête quand `i` atteint `3`.
