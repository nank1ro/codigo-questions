permitir's empezar con el **equal** `==` comparison operador.
It devuelve un **booleano** (`verdadero` o `falso`) stating whether dos expresiones son equal, Por ejemplo:
```swift
print(2 == 2) // verdadero
print(2 == 3) // falso
```

---

Continuemos con el **no equal** `!=` comparison operador.
It devuelve un **booleano** (`verdadero` o `falso`) stating whether dos expresiones son **no** equal, Por ejemplo:
```swift
print(2 != 2) // falso
print(2 != 3) // verdadero
```
It es exactly el opposite de el *equal* operador

---

Continuemos con el **Mayor que** `>` comparison operador.
It devuelve un **booleano** (`verdadero` o `falso`) stating whether uno expresion es Mayor que el other, Por ejemplo:
```swift
print(2 > 2) // falso
print(3 > 2) // verdadero
```

---

Continuemos con el **Menor que** `<` comparison operador.
It devuelve un **booleano** (`verdadero` o `falso`) stating whether uno expresion es Menor que el other, Por ejemplo:
```swift
print(2 < 2) // falso
print(2 < 3) // verdadero
```

---

Continuemos con el **Mayor o igual que** `>=` comparison operador.
It devuelve un **booleano** (`verdadero` o `falso`) stating whether uno expresion es Mayor que o equal el other, Por ejemplo:
```swift
print(2 >= 2) // verdadero
print(3 >= 2) // verdadero
print(3 >= 4) // falso
```

---

Continuemos con el **Menor o igual que** `<=` comparison operador.
It devuelve un **booleano** (`verdadero` o `falso`) stating whether uno expresion es Menor o igual que el other, Por ejemplo:
```swift
print(2 <= 2) // verdadero
print(3 <= 2) // falso
print(3 <= 4) // verdadero
```

---

ahora Veamos el **logical** operadores, permitir's empezar con el primero llamo __AND__ `&&`.
It devuelve el primero operand ese evaluates un *falso* o el ultimo uno si todos son *verdadero*.
```swift
print(2 == 2 && 2 == 3) // falso
print(1 == 1 && 1 == 1.0) // verdadero
```

---

Continuemos con el **o** `||` logical operador.
It devuelve el primero operand ese evaluates un *verdadero* o el ultimo uno si todos son *falso*.
```swift
print(2 == 2 || 2 == 3) // verdadero
print(1 == 2 || 1 == 3) // falso
```

---

permitir's finish con el **no** `!` logical operador.
It devuelve un booleano ese es el reverse de el logical state de un expression.
```swift
print(!true) // falso
print(!false) // verdadero
print(!(2 == 2)) // falso
```
