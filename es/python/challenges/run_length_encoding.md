---
language: python
exerciseType: 1
difficulty: 2
title: Codificación por longitud de serie
---

# --description--

La codificación por longitud de serie es uno de los trucos de compresión más antiguos que existen: en lugar de escribir el mismo carácter una y otra vez, escribes cuántas veces se repite y luego el propio carácter.

Una máquina de fax que escanea una página casi en blanco se encuentra con largas tiras de píxeles idénticos, así que una fila de doce `W` viaja por la línea como el mucho más corto `12W`. Cuando un carácter aparece solo una vez no hay nada que ganar contándolo, así que se copia tal cual.

# --instructions--

Escribe una función `encode_run` que reciba una cadena `text` y devuelva su forma codificada por longitud de serie.

Cada serie del mismo carácter repetido dos o más veces se convierte en la longitud de la serie escrita en decimal, seguida de ese carácter. Una serie de longitud uno se copia como el único carácter, sin ningún número delante.

Ejemplos:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- El texto contiene solo letras mayúsculas de la `A` a la `Z` y espacios.
- Una serie de más de nueve caracteres usa su conteo decimal completo, así que doce `W` se convierten en `12W` y nunca en `9W3W`.
- Los espacios son caracteres ordinarios: se cuentan y se codifican exactamente igual que las letras.
- La cadena vacía se codifica como la cadena vacía.

# --seed--

```python
def encode_run(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

La cadena vacía se codifica como la cadena vacía

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

Un solo carácter se copia tal cual

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

Una cadena sin repeticiones pasa sin cambios

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

Una serie de dos se convierte en el conteo seguido del carácter

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

El ejemplo mixto "AABCCCDEEEE" se convierte en "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

Una serie de doce usa su conteo decimal completo, así que el resultado empieza con "12W"

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

Las series de espacios se codifican igual que las series de letras

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

Una serie de diez se escribe como "10A", nunca como dos series más cortas

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

Los caracteres sueltos que se alternan se copian todos tal cual

```python
    def test9(self):
        self.assertEqual(encode_run("ABABAB"), "ABABAB", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def encode_run(text):
    result = ""
    i = 0

    while i < len(text):
        run = 1
        while i + run < len(text) and text[i + run] == text[i]:
            run += 1
        if run > 1:
            result += str(run)
        result += text[i]
        i += run

    return result
```
