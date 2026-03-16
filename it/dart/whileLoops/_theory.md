Un ciclo `while` ripete un blocco di codice finché una condizione è `true`.

```dart
int i = 0;
while (i < 3) {
  print(i);
  i++;
}
```

Il ciclo controlla la condizione **prima** di ogni iterazione. Quando `i < 3` diventa `false`, il ciclo si ferma.

---

Una variabile contatore controlla quante volte viene eseguito un ciclo `while`.

```dart
int count = 0;
while (count < 5) {
  count++;
}
print(count); // 5
```

Il contatore parte da `0`, e il ciclo lo incrementa a ogni iterazione finché `count < 5` è `false`.

---

Un ciclo `do-while` è simile a un ciclo `while`, ma **esegue sempre il corpo almeno una volta** — la condizione viene verificata *dopo* ogni iterazione.

```dart
int i = 0;
do {
  print(i);
  i++;
} while (i < 3);
```

Anche se la condizione è `false` fin dall'inizio, il corpo viene eseguito una volta.

---

La condizione di un ciclo `while` può contenere qualsiasi espressione booleana. Non appena la condizione restituisce `false`, il ciclo termina.

```dart
int n = 100;
while (n > 1) {
  n ~/= 2;
}
print(n); // 0
```

Qui, `n` viene dimezzato a ogni iterazione usando la divisione intera (`~/`).

---

La parola chiave `break` esce immediatamente da un ciclo, indipendentemente dalla condizione del ciclo.

```dart
int i = 0;
while (true) {
  if (i == 3) break;
  print(i);
  i++;
}
```

Senza `break`, il ciclo `while (true)` verrebbe eseguito all'infinito. Qui si ferma quando `i` raggiunge `3`.
