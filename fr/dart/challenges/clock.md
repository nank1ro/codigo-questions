---
language: dart
exerciseType: 1
difficulty: 2
title: Horloge
---

# --description--

Une horloge 24 heures affiche l'heure de la journée sous la forme `HH:MM`, commençant à `00:00` juste après minuit et se terminant à `23:59` une minute avant le minuit suivant. Les deux parties sont toujours écrites avec deux chiffres, ainsi neuf minutes après onze heures du matin se lit `11:09`.

Une journée entière dure 1440 minutes. Lorsque l'horloge dépasse `23:59`, elle repasse à `00:00` et recommence la journée, et la remonter en arrière avant `00:00` la fait atterrir sur `23:59`.

# --instructions--

Écrivez une fonction `clockTime` qui prend deux nombres entiers, `hours` et `minutes`, et retourne l'affichage d'une horloge 24 heures sous la forme de la chaîne `"HH:MM"`, les deux parties étant complétées sur deux chiffres.

Exemples :
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Chacun des deux nombres peut être négatif ou plus grand que ce qu'une véritable horloge permet.
- Calculez le nombre total de minutes avec `hours * 60 + minutes`, puis ramenez ce total dans la plage de `0` à `1439` afin que l'horloge boucle dans les deux sens.
- `clockTime(24, 0)` correspond exactement à une journée, donc l'affichage est `"00:00"`.

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

Huit heures du matin se lit `08:00`

```dart
  test('test1', () {
    expect(clockTime(8, 0), "08:00", reason: '--err-t1--');
  });
```

Les chiffres uniques sont complétés sur deux chiffres, ainsi neuf minutes après onze heures se lit `11:09`

```dart
  test('test2', () {
    expect(clockTime(11, 9), "11:09", reason: '--err-t2--');
  });
```

Exactement une journée entière d'heures repasse à `00:00`

```dart
  test('test3', () {
    expect(clockTime(24, 0), "00:00", reason: '--err-t3--');
  });
```

Les minutes au-delà de 60 se reportent sur les heures

```dart
  test('test4', () {
    expect(clockTime(25, 160), "03:40", reason: '--err-t4--');
  });
```

Une heure négative remonte l'horloge en arrière au-delà de minuit

```dart
  test('test5', () {
    expect(clockTime(-1, 15), "23:15", reason: '--err-t5--');
  });
```

Un nombre de minutes négatif remonte également l'horloge en arrière

```dart
  test('test6', () {
    expect(clockTime(0, -90), "22:30", reason: '--err-t6--');
  });
```

Plus d'une journée entière en arrière continue de boucler

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
  // Le % de Dart est le modulo euclidien, donc un total négatif est déjà
  // ramené en avant dans 0..1439.
  final total = (hours * 60 + minutes) % 1440;

  final hh = (total ~/ 60).toString().padLeft(2, '0');
  final mm = (total % 60).toString().padLeft(2, '0');
  return '$hh:$mm';
}
```
