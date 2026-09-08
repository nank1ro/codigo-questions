Una **String** è un pezzo di testo: una sequenza di caratteri racchiusa tra virgolette. In Dart puoi usare le virgolette singole `'...'` o le virgolette doppie `"..."`, funzionano esattamente allo stesso modo:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

Scegliere un tipo di virgolette ti permette di usare l'altro tipo all'interno del testo senza doverlo escapare:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

Se ti serve la stessa virgoletta all'interno, mettile davanti un backslash: `'It\'s sunny'`.

---

Due stringhe possono essere unite in una nuova con l'operatore `+`, chiamato **concatenazione**:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart unisce anche due **literal** di stringa scritte una accanto all'altra, senza alcun operatore. È comodo per dividere un testo lungo su più righe:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

Solo le stringhe possono essere concatenate con `+`: `'Age: ' + 30` è un errore di compilazione, perché `30` è un `int`.

---

Invece di concatenare, puoi inserire valori direttamente in una stringa con l'**interpolazione**. Scrivi `$name` per inserire il valore di una variabile, e `${expression}` per inserire il risultato di qualsiasi espressione:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

L'interpolazione funziona con qualsiasi tipo: numeri, booleani e liste vengono convertiti automaticamente in testo, quindi `'Age: $age'` va bene anche se `age` è un `int`.

---

Ogni stringa conosce quanti caratteri contiene tramite la sua proprietà `.length`. Anche gli spazi e la punteggiatura contano come caratteri:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

Puoi leggere un singolo carattere con le parentesi quadre e il suo **indice**, a partire da `0`. Il risultato è una `String` di un solo carattere:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

Leggere un indice fuori dalla stringa (come `word[5]`) genera un errore.

---

Le stringhe in Dart sono **immutabili**: una volta create, una stringa non cambia mai. Metodi come `.toUpperCase()` e `.toLowerCase()` non modificano la stringa originale, **ne restituiscono una nuova**:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

Se vuoi che la variabile contenga il nuovo valore, riassegna il risultato: `word = word.toUpperCase();`.

---

Il testo digitato da un utente spesso ha spazi extra intorno. Il metodo `.trim()` restituisce una copia della stringa senza gli spazi bianchi iniziali e finali (spazi, tab e a capo). `.trimLeft()` e `.trimRight()` li rimuovono solo da un lato:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

Il metodo `.substring(start, end)` restituisce la parte di una stringa dall'indice `start` fino, **senza includerlo**, all'indice `end`. Se ometti `end`, prende tutto fino alla fine della stringa:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

Diversi metodi ti permettono di cercare all'interno di una stringa:

- `.contains(other)` restituisce `true` se `other` appare da qualche parte nella stringa
- `.startsWith(other)` e `.endsWith(other)` controllano l'inizio e la fine
- `.indexOf(other)` restituisce l'indice della prima occorrenza, o `-1` se non viene trovata

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

Sono tutti case-sensitive: `'Dart'.contains('dart')` è `false`.

---

Il metodo `.replaceAll(from, to)` restituisce una nuova stringa in cui **ogni** occorrenza di `from` viene sostituita con `to`. `.replaceFirst(from, to)` sostituisce solo la prima:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

Il metodo `.split(separator)` taglia una stringa in una `List<String>` a ogni occorrenza del separatore. L'opposto è `.join(separator)`, un metodo delle liste che unisce gli elementi in un'unica stringa:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

Chiamare `.split('')` con un separatore vuoto ti dà una lista con ogni singolo carattere.
