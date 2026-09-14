---
language: python
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

Escribe una función `is_valid` que tome una cadena y devuelva `True` cuando el número sea válido, `False` en caso contrario.

- `"4539 3195 0343 6467"` pasa la suma de verificación, por lo que el resultado es `True`.
- `"8273 1232 7352 0569"` falla la suma de verificación, por lo que el resultado es `False`.
- `"0"` tiene solo un carácter de longitud, por lo que el resultado es `False`.
- `"055-444-285"` contiene un carácter que no es un dígito ni un espacio, por lo que el resultado es `False`.

Ejemplo de llamada de función:
```python
print(is_valid("095 245 88"))
# prints True
```

# --seed--

```python
def is_valid(value):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Un solo dígito no es válido.

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

Un solo dígito con un espacio inicial no es válido.

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

El número `"059"` es válido.

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

El número `"59"` es válido.

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

El número `"055 444 285"` es válido.

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

El número `"055 444 286"` no es válido.

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

El número `"8273 1232 7352 0569"` no es válido.

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

El número `"4539 3195 0343 6467"` es válido.

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

El número `"1 2345 6789 1234 5678 9012"` no es válido.

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

El número `"095 245 88"` es válido.

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

Una letra hace que el número sea inválido.

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

Los guiones hacen que el número sea inválido.

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

Un carácter de puntuación hace que el número sea inválido.

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

Los símbolos hacen que el número sea inválido.

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

Una cadena vacía no es válida.

```python
    def test_an_empty_string_is_not_valid(self):
        self.assertEqual(is_valid(""), False, "--err-t15--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_valid(value):
    total = 0
    count = 0
    for char in reversed(value):
        if char == ' ':
            continue
        if char < '0' or char > '9':
            return False
        digit = int(char)
        if count % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        count += 1
    return count > 1 and total % 10 == 0
```
