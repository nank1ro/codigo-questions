Iniziamo con l'operatore di comparazione **uguale** `==`.
Restituisce un valore **booleano** (`true` o `false`) affermando se due espressioni sono uguali, ad esempio:
```swift
print(2 == 2) // true
print(2 == 3) // false
```

---

Continuiamo con l'operatore di comparazione **non uguale** `!=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se due espressioni **NON** sono uguali, ad esempio:
```swift
print(2 != 2) // false
print(2 != 3) // true
```
E' esattamente l'opposto dell'operatore *uguale*

---

Continuiamo con l'operatore di comparazione **maggiore di** `>`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' maggiore dell'altra, per esempio:
```swift
print(2 > 2) // false
print(3 > 2) // true
```

---

Continuiamo con l'operatore di comparazione **minore di** `<`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' minore dell'altra, per esempio:
```swift
print(2 < 2) // false
print(2 < 3) // true
```

---

Continuiamo con l'operatore di comparazione **maggiore di o uguale a** `>=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' maggiore o uguale all'altra, per esempio:
```swift
print(2 >= 2) // true
print(3 >= 2) // true
print(3 >= 4) // false
```

---

Continuiamo con l'operatore di comparazione **minore di o uguale a** `<=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' minore o uguale all'altra, per esempio:
```swift
print(2 <= 2) // true
print(3 <= 2) // false
print(3 <= 4) // true
```

---

Ora vediamo gli operatori **logici**, iniziamo con il primo chiamato __AND__ `&&`.
L'operatore restituisce il primo operando che e' uguale a *false* o l'ultimo se tutti sono *true*.
```swift
print(2 == 2 && 2 == 3) // false
print(1 == 1 && 1 == 1.0) // true
```

---

Continuiamo con l'operatore logico **or** `||`.
L'operatore restituisce il primo operando che e' uguale a *true* o l'ultimo se tutti sono *false*.
```swift
print(2 == 2 || 2 == 3) // true
print(1 == 2 || 1 == 3) // false
```

---

Concludiamo con l'operatore logico **not** `!`.
L'operatore restituisce un valore booleano che e' il contrario dello stato logico di un'espressione.
```swift
print(!true) // false
print(!false) // true
print(!(2 == 2)) // false
```
