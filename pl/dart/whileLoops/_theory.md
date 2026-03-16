Pętla `while` powtarza blok kodu tak długo, jak warunek jest `true`.

```dart
int i = 0;
while (i < 3) {
  print(i);
  i++;
}
```

Pętla sprawdza warunek **przed** każdą iteracją. Gdy `i < 3` staje się `false`, pętla się zatrzymuje.

---

Zmienna licznikowa kontroluje, ile razy pętla `while` się wykonuje.

```dart
int count = 0;
while (count < 5) {
  count++;
}
print(count); // 5
```

Licznik zaczyna od `0`, a pętla zwiększa go przy każdej iteracji, dopóki `count < 5` nie stanie się `false`.

---

Pętla `do-while` jest podobna do pętli `while`, ale **zawsze wykonuje ciało przynajmniej raz** — warunek jest sprawdzany *po* każdej iteracji.

```dart
int i = 0;
do {
  print(i);
  i++;
} while (i < 3);
```

Nawet jeśli warunek jest `false` od początku, ciało wykona się raz.

---

Warunek pętli `while` może zawierać dowolne wyrażenie logiczne. Gdy tylko warunek przyjmuje wartość `false`, pętla się kończy.

```dart
int n = 100;
while (n > 1) {
  n ~/= 2;
}
print(n); // 0
```

Tutaj `n` jest dzielone przez dwa przy każdej iteracji przy użyciu dzielenia całkowitego (`~/`).

---

Słowo kluczowe `break` natychmiast przerywa pętlę, niezależnie od jej warunku.

```dart
int i = 0;
while (true) {
  if (i == 3) break;
  print(i);
  i++;
}
```

Bez `break` pętla `while (true)` działałaby w nieskończoność. Tutaj zatrzymuje się, gdy `i` osiągnie `3`.
