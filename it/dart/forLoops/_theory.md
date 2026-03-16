Un ciclo `for` ripete un blocco di codice un numero fisso di volte. La sintassi di base è:

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: viene eseguita una volta prima dell'avvio del ciclo (es. `int i = 0`)

**condition**: verificata prima di ogni iterazione; il ciclo si ferma quando è falsa

**update**: viene eseguita dopo ogni iterazione (es. `i++`)

---

Puoi usare la variabile del ciclo all'interno del corpo per tenere traccia del conteggio corrente. Ad esempio, accumulando una somma:

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

Dopo il ciclo, `total` è uguale a 15.

---

Un ciclo `for` può contare **al contrario** usando un decremento (`i--`) e una condizione `>=`:

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

Questo è utile per i conto alla rovescia o per l'iterazione in senso inverso.

---

Il ciclo `for-in` itera su ogni elemento di una collezione senza bisogno di un indice:

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

Ad ogni iterazione, l'elemento successivo viene assegnato alla variabile del ciclo (`fruit` qui).

---

L'istruzione `break` esce immediatamente da un ciclo quando una condizione è soddisfatta:

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

Questo è utile quando si cerca un valore e si vuole fermarsi non appena viene trovato.
