Vamos começar com o operador de comparação **igual** `==`.
Ele retorna um **booleano** (`true` ou `false`) indicando se duas expressões são iguais, por exemplo:
```swift
print(2 == 2) // true
print(2 == 3) // false
```

---

Vamos continuar com o operador de comparação **diferente** `!=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se duas expressões **NÃO** são iguais, por exemplo:
```swift
print(2 != 2) // false
print(2 != 3) // true
```
É exatamente o oposto do operador *igual*

---

Vamos continuar com o operador de comparação **maior que** `>`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressão é maior que a outra, por exemplo:
```swift
print(2 > 2) // false
print(3 > 2) // true
```

---

Vamos continuar com o operador de comparação **menor que** `<`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressão é menor que a outra, por exemplo:
```swift
print(2 < 2) // false
print(2 < 3) // true
```

---

Vamos continuar com o operador de comparação **maior ou igual a** `>=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressão é maior ou igual à outra, por exemplo:
```swift
print(2 >= 2) // true
print(3 >= 2) // true
print(3 >= 4) // false
```

---

Vamos continuar com o operador de comparação **menor ou igual a** `<=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressão é menor ou igual à outra, por exemplo:
```swift
print(2 <= 2) // true
print(3 <= 2) // false
print(3 <= 4) // true
```

---

Agora vamos ver os operadores **lógicos**, começando pelo primeiro chamado __AND__ `&&`.
Ele retorna o primeiro operando que é avaliado como *false* ou o último se todos forem *true*.
```swift
print(2 == 2 && 2 == 3) // false
print(1 == 1 && 1 == 1.0) // true
```

---

Vamos continuar com o operador lógico **ou** `||`.
Ele retorna o primeiro operando que é avaliado como *true* ou o último se todos forem *false*.
```swift
print(2 == 2 || 2 == 3) // true
print(1 == 2 || 1 == 3) // false
```

---

Vamos finalizar com o operador lógico **not** `!`.
Ele retorna um booleano que é o inverso do estado lógico de uma expressão.
```swift
print(!true) // false
print(!false) // true
print(!(2 == 2)) // false
```
