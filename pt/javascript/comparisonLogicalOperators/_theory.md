Vamos comecar com o operador de comparacao **igual** `==`.
Ele retorna um **booleano** (`true` ou `false`) indicando se duas expressoes sao iguais, por exemplo:
```javascript
console.log(2 == 2);
// imprime true
console.log(2 == 3);
// imprime false
```

---

Vamos continuar com o operador de comparacao **diferente** `!=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se duas expressoes **NAO** sao iguais, por exemplo:
```javascript
console.log(2 != 2);
// imprime false
console.log(2 != 3);
// imprime true
```
E exatamente o oposto do operador *igual*

---

Vamos continuar com o operador de comparacao **maior que** `>`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressao e maior que a outra, por exemplo:
```javascript
console.log(2 > 2);
// imprime false
console.log(3 > 2);
// imprime true
```

---

Vamos continuar com o operador de comparacao **menor que** `<`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressao e menor que a outra, por exemplo:
```javascript
console.log(2 < 2);
// imprime false
console.log(2 < 3);
// imprime true
```

---

Vamos continuar com o operador de comparacao **maior ou igual a** `>=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressao e maior ou igual a outra, por exemplo:
```javascript
console.log(2 >= 2);
// imprime true
console.log(3 >= 2);
// imprime true
console.log(3 >= 4);
// imprime false
```

---

Vamos continuar com o operador de comparacao **menor ou igual a** `<=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressao e menor ou igual a outra, por exemplo:
```javascript
console.log(2 <= 2);
// imprime true
console.log(3 <= 2);
// imprime false
console.log(3 <= 4);
// imprime true
```

---

Agora vamos ver os operadores **logicos**, comecando pelo primeiro chamado __AND__ `&&`.
Ele retorna o primeiro operando que resulta em *false* ou o ultimo se todos forem *true*.
```javascript
console.log(2 == 2 && 2 == 3);
// imprime false
console.log(1 == 1 && 1 == 1.0);
// imprime true
```

---

Vamos continuar com o operador logico **ou** `||`.
Ele retorna o primeiro operando que resulta em *true* ou o ultimo se todos forem *false*.
```javascript
console.log(2 == 2 || 2 == 3);
// imprime true
console.log(1 == 2 || 1 == 3);
// imprime false
```

---

Vamos finalizar com o operador logico **not** `!`.
Ele retorna um booleano que e o inverso do estado logico de uma expressao.
```javascript
console.log(!true);
// imprime false
console.log(!false);
// imprime true
console.log(!(2 == 2));
// imprime false
```
