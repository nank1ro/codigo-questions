Eine **Funktion** ist ein wiederverwendbarer Codeblock, der eine bestimmte Aufgabe ausführt. In Dart definiert man eine Funktion mit einem Rückgabetyp, einem Namen und einem Klammernpaar `()`.

Wenn eine Funktion keinen Wert zurückgibt, lautet ihr Rückgabetyp `void`:

```dart
void sayHello() {
  print("Hello!");
}
```

Man ruft die Funktion auf, indem man ihren Namen gefolgt von `()` schreibt:

```dart
sayHello(); // prints Hello!
```

---

Funktionen können einen **Wert zurückgeben**. Man deklariert den Rückgabetyp vor dem Funktionsnamen und verwendet das Schlüsselwort `return`, um den Wert zurückzugeben:

```dart
int getAge() {
  return 25;
}
```

Der Typ vor dem Funktionsnamen (`int`) teilt Dart mit, welche Art von Wert die Funktion zurückgibt. Man kann `String`, `int`, `double`, `bool` und weitere verwenden.

---

Funktionen können **Parameter** akzeptieren — Werte, die beim Aufruf der Funktion übergeben werden. Parameter werden innerhalb der Klammern mit ihrem Typ und Namen deklariert:

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

Jeder Parameter hat einen Typ (`int`) und einen Namen (`n`). Mehrere Parameter werden durch Kommas getrennt.

---

Dart unterstützt **Pfeilfunktionen** mit der `=>`-Syntax. Wenn der Funktionsrumpf ein einzelner Ausdruck ist, kann man ihn mit `=>` anstelle von `{ return ...; }` kürzen:

```dart
// Reguläre Funktion
int double(int n) {
  return n * 2;
}

// Pfeilfunktion — gleiche Ergebnis
int double(int n) => n * 2;
```

Pfeilfunktionen machen den Code prägnanter. Das `=>` ersetzt sowohl die geschweiften Klammern als auch das Schlüsselwort `return`.

---

Dart unterstützt **benannte Parameter** — Parameter, die in geschweifte Klammern `{}` eingeschlossen sind. Benannte Parameter müssen beim Aufruf mit ihrem Namen angegeben werden und können Standardwerte haben oder als `required` markiert sein:

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

Benannte Parameter verbessern die Lesbarkeit, besonders wenn eine Funktion viele Parameter hat.
