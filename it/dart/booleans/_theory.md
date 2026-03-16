Un __booleano__ è un tipo di dato che può contenere uno di soli due valori: `true` o `false`.
In Dart, il tipo booleano viene dichiarato con la parola chiave `bool`.

```dart
bool isRaining = true;
```

La variabile `isRaining` memorizza il valore `true`, il che significa che sta piove attualmente.
I valori booleani sono sempre scritti in minuscolo: `true` e `false`.

---

Come qualsiasi altra variabile, puoi stampare un valore booleano con `print()`.
Quando stampi un booleano, Dart restituisce il testo `true` o `false`.

```dart
bool isSunny = true;
print(isSunny); // true
```

---

Una variabile booleana può anche contenere il valore `false`.
Usa `false` quando qualcosa non è il caso.

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

Come `true`, anche `false` deve essere scritto in minuscolo.

---

L'__operatore di negazione__ `!` (anche detto "not") inverte un valore booleano.
Applicare `!` a `true` dà `false`, e applicare `!` a `false` dà `true`.

```dart
bool isActive = true;
print(!isActive); // false
```

Questo è utile quando vuoi verificare l'opposto di una condizione.

---

I booleani sono usati in tutta la programmazione per rappresentare condizioni e guidare le decisioni.
Ogni volta che il tuo programma ha bisogno di decidere tra due possibilità, è coinvolto un booleano.

Esempi:
- L'utente è connesso? (`isLoggedIn`)
- La porta è aperta? (`isDoorOpen`)
- L'ordine è stato spedito? (`isShipped`)
