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

---

Alcuni caratteri non possono essere digitati direttamente tra virgolette. Le **sequenze di escape** iniziano con un backslash: `\n` è un a capo, `\t` un tab, `\\` un backslash e `\$` un segno di dollaro letterale (altrimenti `$` avvia un'interpolazione):

```dart
print('one\ntwo');   // stampa one e two su righe separate
print('Cost: \$5');  // Cost: $5
```

Una **raw string** è preceduta da `r`: al suo interno, i backslash e `$` sono caratteri normali, niente viene escapato o interpolato:

```dart
print(r'C:\new\folder'); // C:\new\folder
print(r'Cost: $5');      // Cost: $5
```

Per un testo che si estende su più righe, usa una **stringa multi-riga** delimitata da triple virgolette `'''` o `"""`: gli a capo al suo interno vengono mantenuti.

```dart
var poem = '''
roses are red
violets are blue''';
```

---

Sotto il cofano, ogni carattere di una stringa è memorizzato come un numero, il suo **code unit** (un codice UTF-16). `.codeUnitAt(index)` restituisce il codice di un carattere e `.codeUnits` l'intera lista. `String.fromCharCode(code)` fa il contrario, costruendo una stringa a partire da un codice:

```dart
var word = 'AB';
print(word.codeUnitAt(0));         // 65
print(word.codeUnits);             // [65, 66]
print(String.fromCharCode(67));    // C
```

Lettere consecutive hanno codici consecutivi: `'A'` è 65, `'B'` è 66, e così via.

---

Due stringhe sono uguali con `==` quando contengono esattamente gli stessi caratteri, nello stesso ordine. Il confronto è **case-sensitive** e conta ogni spazio:

```dart
print('dart' == 'dart');    // true
print('Dart' == 'dart');    // false
print('dart ' == 'dart');   // false
```

Per confrontare ignorando maiuscole e minuscole, converti prima entrambi i lati: `a.toLowerCase() == b.toLowerCase()`. Per l'ordinamento, `.compareTo(other)` restituisce un numero negativo, `0` o un numero positivo a seconda che la stringa venga prima, sia uguale, o venga dopo l'altra.

---

Poiché le stringhe sono immutabili, costruire un testo lungo con `+=` in un ciclo crea una nuova stringa a ogni passo. Uno **StringBuffer** raccoglie pezzi di testo in modo efficiente e produce la stringa finale solo quando la richiedi:

- `.write(value)` aggiunge un valore (qualsiasi tipo viene convertito in testo)
- `.writeln(value)` aggiunge il valore seguito da un a capo
- `.toString()` restituisce la stringa costruita finora

```dart
var buffer = StringBuffer();
buffer.write('Hello');
buffer.write(', ');
buffer.writeln('Dart!');
buffer.write(42);
print(buffer.toString()); // Hello, Dart!\n42
```

---

I metodi delle stringhe restituiscono stringhe, quindi possono essere **concatenati** uno dopo l'altro. Combinato con `.split('')`, la proprietà `.reversed` delle liste e `.join()`, questo ti permette di invertire una stringa in un'unica espressione:

```dart
var text = 'Dart';
print(text.split('').reversed.join()); // traD
print(text.toLowerCase().replaceAll('a', '4')); // d4rt
```

Un **palindromo** è un testo che si legge allo stesso modo in avanti e indietro, come `level`.
