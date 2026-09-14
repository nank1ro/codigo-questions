---
language: javascript
exerciseType: 1
difficulty: 2
title: Suma de verificación de Luhn
---

# --description--

El algoritmo de Luhn es una suma de verificación simple que se usa para validar números de identificación, como los números de tarjetas de crédito.

Antes de comprobar un número, elimina todos los espacios de la cadena. La cadena solo es válida si lo que queda tiene más de un carácter y la cadena original no contiene nada más que dígitos y espacios.

Para realizar la comprobación, comienza desde el dígito de más a la derecha y avanza hacia la izquierda, duplicando cada segundo dígito. Cuando duplicar produce un número mayor que 9, réstale 9. Luego suma todos los dígitos: el número solo es válido si la suma es divisible por 10.

Por ejemplo, `"059"` da `0`, luego `5` duplicado es `10`, que se convierte en `1`, luego `9`. Su suma es `10`, que es divisible por 10, por lo que el número es válido.

# --instructions--

Escribe una función `isValid` que tome una cadena y devuelva `true` cuando el número sea válido, `false` en caso contrario.

- `"4539 3195 0343 6467"` pasa la suma de verificación, por lo que el resultado es `true`.
- `"8273 1232 7352 0569"` falla la suma de verificación, por lo que el resultado es `false`.
- `"0"` tiene solo un carácter de longitud, por lo que el resultado es `false`.
- `"055-444-285"` contiene un carácter que no es un dígito ni un espacio, por lo que el resultado es `false`.

Ejemplo de llamada de función:
```javascript
console.log(isValid("095 245 88"));
// prints true
```

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function isValid(value) {
  
}
```

# --asserts--

Un solo dígito no es válido.

```javascript
tryCatch(isValid("0") === false);
```

Un solo dígito con un espacio inicial no es válido.

```javascript
tryCatch(isValid(" 0") === false);
```

El número `"059"` es válido.

```javascript
tryCatch(isValid("059") === true);
```

El número `"59"` es válido.

```javascript
tryCatch(isValid("59") === true);
```

El número `"055 444 285"` es válido.

```javascript
tryCatch(isValid("055 444 285") === true);
```

El número `"055 444 286"` no es válido.

```javascript
tryCatch(isValid("055 444 286") === false);
```

El número `"8273 1232 7352 0569"` no es válido.

```javascript
tryCatch(isValid("8273 1232 7352 0569") === false);
```

El número `"4539 3195 0343 6467"` es válido.

```javascript
tryCatch(isValid("4539 3195 0343 6467") === true);
```

El número `"1 2345 6789 1234 5678 9012"` no es válido.

```javascript
tryCatch(isValid("1 2345 6789 1234 5678 9012") === false);
```

El número `"095 245 88"` es válido.

```javascript
tryCatch(isValid("095 245 88") === true);
```

Una letra hace que el número sea inválido.

```javascript
tryCatch(isValid("055a 444 285") === false);
```

Los guiones hacen que el número sea inválido.

```javascript
tryCatch(isValid("055-444-285") === false);
```

Un carácter de puntuación hace que el número sea inválido.

```javascript
tryCatch(isValid(":9") === false);
```

Los símbolos hacen que el número sea inválido.

```javascript
tryCatch(isValid("055# 444$ 285") === false);
```

Una cadena vacía no es válida.

```javascript
tryCatch(isValid("") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isValid(value) {
  var sum = 0
  var count = 0
  for (var i = value.length - 1; i >= 0; i--) {
    var code = value.charCodeAt(i)
    if (code === 32) {
      continue
    }
    if (code < 48 || code > 57) {
      return false
    }
    var digit = code - 48
    if (count % 2 === 1) {
      digit *= 2
      if (digit > 9) {
        digit -= 9
      }
    }
    sum += digit
    count++
  }
  return count > 1 && sum % 10 === 0
}
```
