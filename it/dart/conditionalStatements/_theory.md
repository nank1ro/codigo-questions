Un'**istruzione `if`** esegue un blocco di codice solo quando una condizione è `true`.

```dart
int age = 20;
if (age >= 18) {
  print('Adult');
}
```

Il codice all'interno delle parentesi graffe viene eseguito solo se la condizione `age >= 18` viene valutata come `true`.

---

Puoi usare `print()` all'interno di un blocco `if` per visualizzare un messaggio quando una condizione è soddisfatta.

```dart
bool isRaining = true;
if (isRaining) {
  print('Take an umbrella');
}
```

Se `isRaining` è `false`, non viene stampato nulla.

---

Un'**istruzione `if-else`** esegue il blocco `if` quando la condizione è `true`, e il blocco `else` quando è `false`.

```dart
int temperature = 10;
if (temperature > 20) {
  print('Warm');
} else {
  print('Cold');
}
// prints: Cold
```

Esattamente uno dei due rami viene sempre eseguito.

---

**`else if`** consente di testare più condizioni in sequenza. Viene eseguito il primo ramo la cui condizione è `true`, e il resto viene saltato.

```dart
int score = 75;
if (score >= 90) {
  print('A');
} else if (score >= 70) {
  print('B');
} else {
  print('C');
}
// prints: B
```

---

L'**operatore ternario** `condition ? expr1 : expr2` è un modo compatto per scrivere una semplice espressione `if-else`.

```dart
int x = 10;
String label = x > 0 ? 'positive' : 'non-positive';
print(label); // positive
```

Se la condizione è `true`, viene usata `expr1`; altrimenti viene usata `expr2`.
