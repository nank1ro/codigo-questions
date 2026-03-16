L'**operatore di addizione** `+` aggiunge due valori insieme.

```dart
int a = 3;
int b = 4;
int sum = a + b; // 7
```

Puoi usare `+` con valori `int` o `double`.

---

L'**operatore di sottrazione** `-` sottrae un valore da un altro.

```dart
int a = 10;
int b = 4;
int diff = a - b; // 6
```

Il risultato può essere negativo se il secondo operando è più grande del primo.

---

L'**operatore di moltiplicazione** `*` moltiplica due valori insieme.

```dart
int a = 5;
int b = 6;
int product = a * b; // 30
```

Moltiplicare un `int` per un altro `int` produce un `int`. Moltiplicare con un `double` produce un `double`.

---

L'**operatore di divisione** `/` divide un valore per un altro. In Dart, `/` **restituisce sempre un `double`**, anche quando il risultato è un numero intero.

```dart
int a = 10;
int b = 4;
double result = a / b; // 2.5

double exact = 10 / 2; // 5.0  (not 5!)
```

Usa sempre una variabile `double` per memorizzare il risultato di `/`.

---

L'**operatore di divisione intera** `~/` divide due numeri e **tronca** il risultato a un intero (scarta qualsiasi parte decimale).

```dart
int a = 10;
int b = 3;
int result = a ~/ b; // 3  (not 3.333...)
```

Usa `~/` quando hai bisogno di un quoziente intero senza resto.
