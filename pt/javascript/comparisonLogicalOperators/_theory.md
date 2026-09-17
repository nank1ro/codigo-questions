Vamos começar com o operador de comparação **igual** `==`.
Ele retorna um **booleano** (`true` ou `false`) indicando se duas expressões são iguais, por exemplo:
```javascript
console.log(2 == 2);
// imprime true
console.log(2 == 3);
// imprime false
```

---

Vamos continuar com o operador de comparação **diferente** `!=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se duas expressões **NÃO** são iguais, por exemplo:
```javascript
console.log(2 != 2);
// imprime false
console.log(2 != 3);
// imprime true
```
É exatamente o oposto do operador *igual*

---

Vamos continuar com o operador de comparação **maior que** `>`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressão é maior que a outra, por exemplo:
```javascript
console.log(2 > 2);
// imprime false
console.log(3 > 2);
// imprime true
```

---

Vamos continuar com o operador de comparação **menor que** `<`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressão é menor que a outra, por exemplo:
```javascript
console.log(2 < 2);
// imprime false
console.log(2 < 3);
// imprime true
```

---

Vamos continuar com o operador de comparação **maior ou igual a** `>=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressão é maior ou igual a outra, por exemplo:
```javascript
console.log(2 >= 2);
// imprime true
console.log(3 >= 2);
// imprime true
console.log(3 >= 4);
// imprime false
```

---

Vamos continuar com o operador de comparação **menor ou igual a** `<=`.
Ele retorna um **booleano** (`true` ou `false`) indicando se uma expressão é menor ou igual a outra, por exemplo:
```javascript
console.log(2 <= 2);
// imprime true
console.log(3 <= 2);
// imprime false
console.log(3 <= 4);
// imprime true
```

---

Agora vamos ver os operadores **lógicos**, começando pelo primeiro chamado __AND__ `&&`.
Ele retorna o primeiro operando que resulta em *false* ou o último se todos forem *true*.
```javascript
console.log(2 == 2 && 2 == 3);
// imprime false
console.log(1 == 1 && 1 == 1.0);
// imprime true
```

---

Vamos continuar com o operador lógico **ou** `||`.
Ele retorna o primeiro operando que resulta em *true* ou o último se todos forem *false*.
```javascript
console.log(2 == 2 || 2 == 3);
// imprime true
console.log(1 == 2 || 1 == 3);
// imprime false
```

---

Vamos finalizar com o operador lógico **not** `!`.
Ele retorna um booleano que é o inverso do estado lógico de uma expressão.
```javascript
console.log(!true);
// imprime false
console.log(!false);
// imprime true
console.log(!(2 == 2));
// imprime false
```

---

O `==` compara os dois lados depois de convertê-los para um tipo comum, então `"5" == 5` é `true`. O operador estrito `===` pula essa conversão e exige que os tipos também sejam iguais.
```javascript
console.log("5" == 5);  // true
console.log("5" === 5); // false
```

---

O `!=` converte antes de comparar, assim como o `==`, então `"5" != 5` é `false`. Seu equivalente estrito `!==` trata uma string e um número como diferentes, não importa o que contenham.
```javascript
console.log("5" !== 5); // true
```

---

Quando os dois lados são strings, o `>` as compara caractere por caractere na ordem do código, e não pelo tamanho, então `"b" > "a"` é `true` e `"apple" > "ant"` também é `true`.

---

O `>=` é satisfeito por qualquer uma das duas metades do seu nome: `8 >= 8` é `true` porque os dois valores são iguais, enquanto o mais estrito `8 > 8` é `false`.

---

Toda comparação envolvendo `NaN` retorna `false`, até mesmo as opostas: `NaN < 3` e `NaN >= 3` são ambas `false`, então um `<` que falha nem sempre significa que o lado esquerdo é maior.

---

Quando um lado é uma string e o outro é um número, o `<=` converte a string para número primeiro, então `"7" <= 8` é `true`.
