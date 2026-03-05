Fangen wir mit dem **gleich**-Operator `==` an.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob zwei Ausdrücke gleich sind, z. B.:
```swift
print(2 == 2) // true
print(2 == 3) // false
```

---

Lassen Sie uns mit dem **ungleich**-Operator `!=` fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob zwei Ausdrücke **NICHT** gleich sind, z. B.:
```swift
print(2 != 2) // false
print(2 != 3) // true
```
Es ist genau das Gegenteil des *gleich*-Operators

---

Lassen Sie uns mit dem **größer als**-Operator `>` fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck größer als der andere ist, z. B.:
```swift
print(2 > 2) // false
print(3 > 2) // true
```

---

Lassen Sie uns mit dem **kleiner als**-Operator `<` fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck kleiner als der andere ist, z. B.:
```swift
print(2 < 2) // false
print(2 < 3) // true
```

---

Lassen Sie uns mit dem **größer als oder gleich**-Operator `>=` fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck größer als oder gleich dem anderen ist, z. B.:
```swift
print(2 >= 2) // true
print(3 >= 2) // true
print(3 >= 4) // false
```

---

Lassen Sie uns mit dem **kleiner als oder gleich**-Operator `<=` fortfahren.
Er gibt einen **booleschen Wert** (`true` oder `false`) zurück, der angibt, ob ein Ausdruck kleiner als oder gleich dem anderen ist, z. B.:
```swift
print(2 <= 2) // true
print(3 <= 2) // false
print(3 <= 4) // true
```

---

Lassen Sie uns nun die **logischen** Operatoren betrachten. Fangen wir mit dem ersten an, der sogenannte __UND__-Operator `&&`.
Er gibt den ersten Operanden zurück, der zu *false* evaluiert, oder den letzten, wenn alle *true* sind.
```swift
print(2 == 2 && 2 == 3) // false
print(1 == 1 && 1 == 1.0) // true
```

---

Lassen Sie uns mit dem **oder**-Operator `||` fortfahren.
Er gibt den ersten Operanden zurück, der zu *true* evaluiert, oder den letzten, wenn alle *false* sind.
```swift
print(2 == 2 || 2 == 3) // true
print(1 == 2 || 1 == 3) // false
```

---

Lassen Sie uns mit dem **nicht**-Operator `!` abschließen.
Er gibt einen booleschen Wert zurück, der das Gegenteil des logischen Zustands eines Ausdrucks ist.
```swift
print(!true) // false
print(!false) // true
print(!(2 == 2)) // false
```
