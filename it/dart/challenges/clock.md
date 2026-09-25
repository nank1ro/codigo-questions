---
language: dart
exerciseType: 1
difficulty: 2
title: Orologio
---

# --description--

Un orologio a 24 ore mostra l'ora del giorno come `HH:MM`, partendo da `00:00` subito dopo la mezzanotte e arrivando a `23:59` un minuto prima della mezzanotte successiva. Entrambe le parti sono sempre scritte con due cifre, così nove minuti dopo le undici del mattino si legge `11:09`.

Un giorno intero dura 1440 minuti. Quando l'orologio supera `23:59` riparte da `00:00` e ricomincia il giorno, e riavvolgendolo all'indietro oltre `00:00` si torna a `23:59`.

# --instructions--

Scrivi una funzione `clockTime` che riceve due numeri interi, `hours` e `minutes`, e restituisce la lettura di un orologio a 24 ore come stringa `"HH:MM"`, con entrambe le parti portate a due cifre.

Esempi:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Ciascuno dei due numeri può essere negativo, oppure più grande di quanto un orologio reale consenta.
- Calcola il numero totale di minuti come `hours * 60 + minutes`, poi riporta quel totale nell'intervallo da `0` a `1439`, così l'orologio riparte in entrambe le direzioni.
- `clockTime(24, 0)` è esattamente un giorno, quindi si legge `"00:00"`.

# --seed--

```dart
String clockTime(int hours, int minutes) {
  
}
```

# --before-asserts--

```dart
import 'package:dart_runner/main.dart';
import 'package:test/test.dart';

void main() {
  group('MainTest -', () {
```

# --asserts--

Le otto del mattino si legge `08:00`

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

Le cifre singole vengono portate a due cifre, così nove minuti dopo le undici si legge `11:09`

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

Esattamente un giorno intero di ore fa ripartire l'orologio da `00:00`

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

I minuti oltre 60 vengono riportati nelle ore

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

Un'ora negativa riavvolge l'orologio all'indietro oltre la mezzanotte

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

Anche un numero di minuti negativo riavvolge l'orologio all'indietro

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

Più di un giorno intero all'indietro continua a ripartire

```dart
  test('test7', () {
    expect(clockTime(-25, 0), "23:00", reason: '--err-t7--');
  });
```

# --after-asserts--

```dart
  }, timeout: Timeout(const Duration(seconds: 1)));
}
```

# --solutions--

```dart
String clockTime(int hours, int minutes) {
  // Il % di Dart è il modulo euclideo, quindi un totale negativo è già
  // riportato in avanti in 0..1439.
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
