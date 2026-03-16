**Funkcja** to wielokrotnie używany blok kodu, który wykonuje określone zadanie. W Dart funkcję definiuje się podając typ zwracanej wartości, nazwę i nawiasy `()`.

Gdy funkcja nie zwraca żadnej wartości, jej typ zwracany to `void`:

```dart
void sayHello() {
  print("Hello!");
}
```

Wywołujesz funkcję, pisząc jej nazwę i nawiasy `()`:

```dart
sayHello(); // prints Hello!
```

---

Funkcje mogą **zwracać wartość** do miejsca wywołania. Deklarujesz typ zwracanej wartości przed nazwą funkcji i używasz słowa kluczowego `return`, aby odesłać wartość:

```dart
int getAge() {
  return 25;
}
```

Typ przed nazwą funkcji (`int`) mówi Dartowi, jaki rodzaj wartości funkcja zwróci. Możesz używać `String`, `int`, `double`, `bool` i innych.

---

Funkcje mogą przyjmować **parametry** — wartości przekazywane podczas wywoływania funkcji. Parametry deklaruje się wewnątrz nawiasów, podając ich typ i nazwę:

```dart
int square(int n) {
  return n * n;
}

void main() {
  print(square(4)); // prints 16
}
```

Każdy parametr ma typ (`int`) i nazwę (`n`). Wiele parametrów oddziela się przecinkami.

---

Dart obsługuje **funkcje strzałkowe** z użyciem składni `=>`. Gdy ciało funkcji jest pojedynczym wyrażeniem, możesz je skrócić za pomocą `=>` zamiast `{ return ...; }`:

```dart
// Zwykła funkcja
int double(int n) {
  return n * 2;
}

// Funkcja strzałkowa — ten sam wynik
int double(int n) => n * 2;
```

Funkcje strzałkowe sprawiają, że kod jest bardziej zwięzły. `=>` zastępuje zarówno nawiasy klamrowe, jak i słowo kluczowe `return`.

---

Dart obsługuje **nazwane parametry** — parametry umieszczone w nawiasach klamrowych `{}`. Nazwane parametry muszą być wywoływane po nazwie i mogą mieć wartości domyślne lub być oznaczone jako `required`:

```dart
void printInfo({required String name, int age = 0}) {
  print("$name is $age years old");
}

void main() {
  printInfo(name: "Alice", age: 30);
  // prints Alice is 30 years old
}
```

Nazwane parametry poprawiają czytelność kodu, szczególnie gdy funkcja ma wiele parametrów.
