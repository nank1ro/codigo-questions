Iniziamo con l'operatore di comparazione **uguale** `==`.
Restituisce un valore **booleano** (`true` o `false`) affermando se due espressioni sono uguali, ad esempio:
```javascript
console.log(2 == 2); 
// stampa true
console.log(2 == 3);
// stampa false
```

---

Continuiamo con l'operatore di comparazione **non uguale** `!=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se due espressioni **NON** sono uguali, ad esempio:
```javascript
console.log(2 != 2);
// stampa false
console.log(2 != 3); 
// stampa true
```
E' esattamente l'opposto dell'operatore *uguale*

---

Continuiamo con l'operatore di comparazione **maggiore di** `>`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' maggiore dell'altra, per esempio:
```javascript
console.log(2 > 2);
// stampa false
console.log(3 > 2);
// stampa true
```

---

Continuiamo con l'operatore di comparazione **minore di** `<`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' minore dell'altra, per esempio:
```javascript
console.log(2 < 2);
// stampa false
console.log(2 < 3);
// stampa true
```

---

Continuiamo con l'operatore di comparazione **maggiore di o uguale a** `>=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' maggiore o uguale all'altra, per esempio:
```javascript
console.log(2 >= 2); 
// stampa true
console.log(3 >= 2);
// stampa true
console.log(3 >= 4);
// stampa false
```

---

Continuiamo con l'operatore di comparazione **minore di o uguale a** `<=`.
Restituisce un valore **booleano** (`true` o `false`) affermando se un'espressione e' minore o uguale all'altra, per esempio:
```javascript
console.log(2 <= 2); 
// stampa true
console.log(3 <= 2);
// stampa false
console.log(3 <= 4);
// stampa true
```

---

Ora vediamo gli operatori **logici**, iniziamo con il primo chiamato __AND__ `&&`.
L'operatore restituisce il primo operando che e' uguale a *false* o l'ultimo se tutti sono *true*.
```javascript
console.log(2 == 2 && 2 == 3);
// stampa false
console.log(1 == 1 && 1 == 1.0);
// stampa true
```

---

Continuiamo con l'operatore logico **or** `||`.
L'operatore restituisce il primo operando che e' uguale a *true* o l'ultimo se tutti sono *false*.
```javascript
console.log(2 == 2 || 2 == 3);
// stampa true
console.log(1 == 2 || 1 == 3);
// stampa false
```

---

Concludiamo con l'operatore logico **not** `!`.
L'operatore restituisce un valore booleano che e' il contrario dello stato logico di un'espressione.
```javascript
console.log(!true);
// stampa false
console.log(!false);
// stampa true
console.log(!(2 == 2));
// stampa false
```

---

`==` confronta i suoi due lati dopo averli convertiti in un tipo comune, quindi `"5" == 5` è `true`. L'operatore stretto `===` salta questa conversione e richiede che anche i tipi corrispondano.
```javascript
console.log("5" == 5);  // true
console.log("5" === 5); // false
```

---

`!=` converte prima di confrontare, proprio come `==`, quindi `"5" != 5` è `false`. La sua controparte stretta `!==` tratta una stringa e un numero come diversi qualunque cosa contengano.
```javascript
console.log("5" !== 5); // true
```

---

Quando entrambi i lati sono stringhe, `>` le confronta carattere per carattere seguendo l'ordine dei codici anziché la lunghezza, quindi `"b" > "a"` è `true` e anche `"apple" > "ant"` è `true`.

---

`>=` è soddisfatto da entrambe le metà del suo nome: `8 >= 8` è `true` perché i due valori sono uguali, mentre il più rigido `8 > 8` è `false`.

---

Ogni confronto che coinvolge `NaN` restituisce `false`, anche quelli opposti: `NaN < 3` e `NaN >= 3` sono entrambi `false`, quindi un `<` fallito non significa sempre che il lato sinistro sia maggiore.

---

Quando un lato è una stringa e l'altro un numero, `<=` converte prima la stringa in un numero, quindi `"7" <= 8` è `true`.
