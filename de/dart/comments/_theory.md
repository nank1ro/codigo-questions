> Bevor ich beginne, wollte ich dir sagen, dass ich mich sehr freue, dir Dart beizubringen.
Mit dieser Nachricht nutze ich die Gelegenheit, dir mitzuteilen, dass die App, die du verwendest, genau in Dart mit dem Flutter-Framework geschrieben wurde. Daher ist es eine Ehre für mich, mein Fachwissen in dieser Sprache mit dir zu teilen.

Dart ermöglicht es dir wie viele andere Programmiersprachen auch, deinen Code zu dokumentieren.
Dies ermöglicht es dir, beliebigen Text neben dem Code zu schreiben.
Kommentare werden vom Compiler ignoriert.

Dart unterstützt _einzeilige_ Kommentare, _mehrzeilige_ Kommentare und _Dokumentations_-Kommentare.

So schreibst du einen _einzeiligen_ Kommentar:
```dart
// Dies ist ein Kommentar. Er wird nicht ausgeführt.
```

---

Du kannst mehrere _einzeilige_ Kommentare hintereinander schreiben, um _mehrzeilige_ Kommentare zu schreiben.
```dart
// Dies ist ein
// mehrzeiliger Kommentar
```

---

Du kannst auch Kommentarblöcke oder _mehrzeilige_ Kommentare erstellen.
_Mehrzeilige_ Kommentare beginnen mit `/*` und enden mit `*/`.
```dart
/*
This is a multi-line
comment
*/
```

---

Neben diesen beiden Möglichkeiten, Kommentare zu schreiben, unterstützt Dart auch _Dokumentations_-Kommentare.

_Dokumentations_-Kommentare sind mehrzeilige oder einzeilige Kommentare, die mit `///` oder `/**` beginnen. Die Verwendung von `///` auf aufeinanderfolgenden Zeilen hat den gleichen Effekt wie ein mehrzeiliger Dokumentations-Kommentar.

_Dokumentations_-Kommentare sind sehr nützlich, da sie es ermöglichen, Dokumentation zu generieren.
Du wirst _Dokumentations_-Kommentare zu deinem Code hinzufügen wollen, um klarzumachen, was ein bestimmter Codeblock tut.

Innerhalb eines _Dokumentations_-Kommentars löst der Analyzer Namen, die in eckigen Klammern stehen, als Verweise auf andere API-Elemente auf.
Mit eckigen Klammern kann man sich auf _Klassen_, _Methoden_, _Felder_, _Variablen_, _Funktionen_ und _Parameter_ beziehen.

Hier ist ein Beispiel:
```dart
/// Ein domestiziertes südamerikanisches Kamelartiges (Lama glama).
///
/// Genau wie jedes andere Tier müssen Lamas essen,
/// vergiss also nicht, ihnen mit [feed] etwas [Food] zu geben.
class Llama {
  String? name;

  /// Füttert deinen Lama mit [food].
  ///
  /// Ein typischer Lama frisst einen Heuballen pro Woche.
  void feed(Food food) {
    // ...
  }

  /// Trainiert deinen Lama mit einer [activity] für
  /// [timeLimit] Minuten.
  void exercise(Activity activity, int timeLimit) {
    // ...
  }
}
```

In der generierten Dokumentation wird `[feed]` zu einem Link zur Dokumentation der Methode `feed`, und `[Food]` wird zu einem Link zur Dokumentation der Klasse `Food`.
`[activity]` und `[timeLimit]` werden hingegen zu Links zur Dokumentation von `activity` bzw. `timeLimit`.
