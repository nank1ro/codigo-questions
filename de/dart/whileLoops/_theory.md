Eine `while`-Schleife wiederholt einen Codeblock, solange eine Bedingung `true` ist.

```dart
int i = 0;
while (i < 3) {
  print(i);
  i++;
}
```

Die Schleife prüft die Bedingung **vor** jeder Iteration. Wenn `i < 3` `false` wird, hält die Schleife an.

---

Eine Zählervariable steuert, wie oft eine `while`-Schleife ausgeführt wird.

```dart
int count = 0;
while (count < 5) {
  count++;
}
print(count); // 5
```

Der Zähler beginnt bei `0`, und die Schleife erhöht ihn bei jeder Iteration, bis `count < 5` `false` ist.

---

Eine `do-while`-Schleife ähnelt einer `while`-Schleife, aber sie **führt den Rumpf immer mindestens einmal aus** — die Bedingung wird *nach* jeder Iteration geprüft.

```dart
int i = 0;
do {
  print(i);
  i++;
} while (i < 3);
```

Selbst wenn die Bedingung von Anfang an `false` ist, wird der Rumpf einmal ausgeführt.

---

Eine `while`-Schleifenbedingung kann jeden booleschen Ausdruck enthalten. Sobald die Bedingung `false` ergibt, endet die Schleife.

```dart
int n = 100;
while (n > 1) {
  n ~/= 2;
}
print(n); // 0
```

Hier wird `n` bei jeder Iteration durch ganzzahlige Division (`~/`) halbiert.

---

Das Schlüsselwort `break` beendet eine Schleife sofort, unabhängig von der Schleifenbedingung.

```dart
int i = 0;
while (true) {
  if (i == 3) break;
  print(i);
  i++;
}
```

Ohne `break` würde die `while (true)`-Schleife ewig laufen. Hier hält sie an, wenn `i` den Wert `3` erreicht.
