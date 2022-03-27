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
