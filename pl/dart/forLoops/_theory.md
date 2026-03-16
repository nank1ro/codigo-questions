Pętla `for` powtarza blok kodu określoną liczbę razy. Podstawowa składnia to:

```dart
for (initialization; condition; update) {
  // body
}
```

**initialization**: wykonywana raz przed rozpoczęciem pętli (np. `int i = 0`)

**condition**: sprawdzana przed każdą iteracją; pętla zatrzymuje się, gdy jest fałszywa

**update**: wykonywana po każdej iteracji (np. `i++`)

---

Możesz używać zmiennej pętli wewnątrz ciała, aby śledzić bieżący licznik. Na przykład, akumulowanie sumy:

```dart
int total = 0;
for (int i = 1; i <= 5; i++) {
  total += i;
}
```

Po pętli `total` wynosi 15.

---

Pętla `for` może liczyć **wstecz** używając dekrementacji (`i--`) i warunku `>=`:

```dart
for (int i = 5; i >= 1; i--) {
  print(i); // 5, 4, 3, 2, 1
}
```

Jest to przydatne przy odliczaniu wstecz lub iteracji odwrotnej.

---

Pętla `for-in` iteruje po każdym elemencie kolekcji bez potrzeby używania indeksu:

```dart
List<String> fruits = ['apple', 'banana', 'cherry'];
for (var fruit in fruits) {
  print(fruit);
}
```

Każda iteracja przypisuje kolejny element do zmiennej pętli (tutaj `fruit`).

---

Instrukcja `break` natychmiast kończy pętlę, gdy spełniony jest warunek:

```dart
for (int i = 0; i < 10; i++) {
  if (i == 5) break; // stops at 5
  print(i);
}
```

Jest to przydatne, gdy szukamy wartości i chcemy zatrzymać się po jej znalezieniu.
