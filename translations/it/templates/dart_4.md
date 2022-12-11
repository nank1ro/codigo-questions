---
language: dart
exerciseType: 4
---

# --instructions--

Ordina gli elementi per generare il seguente output: `Ciao Dart!`?

# --answers--

```dart
void main() {
```

```dart
    final hello = "Ciao";
```

```dart
    final language = "Dart";
```

```dart
    print("$hello $language!");
```

```dart
}
```

# --solutions--

```dart
void main() {
    final hello = "Ciao";
    final language = "Dart";
    print("$hello $language!");
}
```

```dart
void main() {
    final language = "Dart";
    final hello = "Ciao";
    print("$hello $language!");
}
```

# --output--

Ciao Dart!
