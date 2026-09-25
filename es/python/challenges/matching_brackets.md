---
language: python
exerciseType: 1
difficulty: 3
title: Corchetes coincidentes
---

# --description--

El texto que contiene código, matemáticas o marcado está lleno de corchetes, y cada corchete de apertura necesita uno de cierre de la misma clase. Una cadena está equilibrada cuando sus corchetes se emparejan y se anidan como las capas de una cebolla: `{[()]}` está equilibrada, mientras que `{[(])}` no lo está, porque el par redondo se cierra antes que el par cuadrado dentro del cual se encuentra.

Aquí cuentan tres pares: paréntesis `()`, corchetes `[]` y llaves `{}`. Todos los demás caracteres de la cadena se ignoran. Un corchete de cierre debe cerrar el último corchete que se haya abierto y que aún siga abierto, y cuando la cadena termina no debe quedar ningún corchete abierto.

# --instructions--

Escribe una función `is_balanced` que tome una cadena y devuelva `True` cuando todos los corchetes que contiene estén emparejados y anidados correctamente, y `False` en caso contrario.

Ejemplos:
```
is_balanced("") ➞ True
is_balanced("{[()]}") ➞ True
is_balanced("{what is (42)}[?]") ➞ True
is_balanced("{[(])}") ➞ False
is_balanced("(") ➞ False
is_balanced(")(") ➞ False
```

- Una cadena vacía está equilibrada.
- Los caracteres que no son corchetes se ignoran.
- Un corchete de cierre debe corresponder al último corchete que se haya abierto y que aún siga abierto.
- No debe quedar ningún corchete abierto cuando la cadena termina.

# --seed--

```python
def is_balanced(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Una cadena vacía está equilibrada

```python
    def test1(self):
        self.assertEqual(is_balanced(""), True, "--err-t1--")
```

Un solo par de paréntesis está equilibrado

```python
    def test2(self):
        self.assertEqual(is_balanced("()"), True, "--err-t2--")
```

Los tres tipos de pares anidados unos dentro de otros están equilibrados

```python
    def test3(self):
        self.assertEqual(is_balanced("{[()]}"), True, "--err-t3--")
```

Los corchetes mezclados con otro texto siguen estando equilibrados

```python
    def test4(self):
        self.assertEqual(is_balanced("{what is (42)}[?]"), True, "--err-t4--")
```

Los pares colocados uno al lado del otro están equilibrados

```python
    def test5(self):
        self.assertEqual(is_balanced("()[]{}"), True, "--err-t5--")
```

Una cadena sin ningún corchete está equilibrada

```python
    def test6(self):
        self.assertEqual(is_balanced("no brackets in here at all"), True, "--err-t6--")
```

Un par cruzado no está equilibrado

```python
    def test7(self):
        self.assertEqual(is_balanced("{[(])}"), False, "--err-t7--")
```

Un corchete de apertura que nunca se cierra no está equilibrado

```python
    def test8(self):
        self.assertEqual(is_balanced("("), False, "--err-t8--")
```

Un corchete de cierre antes de cualquier corchete de apertura no está equilibrado

```python
    def test9(self):
        self.assertEqual(is_balanced(")("), False, "--err-t9--")
```

Los pares cruzados en lo profundo de la cadena no están equilibrados

```python
    def test10(self):
        self.assertEqual(is_balanced("(([]{[}]))"), False, "--err-t10--")
```

Un corchete de cierre que sobra al final no está equilibrado

```python
    def test11(self):
        self.assertEqual(is_balanced("())"), False, "--err-t11--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_balanced(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return not stack
```
