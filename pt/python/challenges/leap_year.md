---
language: python
exerciseType: 1
difficulty: 3
title: Leap Year
---
# --description--
Em um ano calendário existem exatamente 365.25 dias. Mas, eventualmente, isso levará a confusão porque os humanos normalmente contam por divisibilidade exata de 1 e não com pontos decimais. Então, para evitar o último, foi decidido somar todos os 0.25 dias a cada ciclo de quatro anos e dar a esse ano 366 dias (incluindo 29 de fevereiro como um dia intercalado) e chamá-lo de __ano bissexto__. Os outros três anos no ciclo de quatro anos conteriam apenas 365 dias e __não seriam anos bissextos__.
# --instructions--
```dart
print(leap_year(2000))
// prints true
```
Neste desafio, vamos levá-lo a um novo nível, onde você deve determinar se é um ano bissexto ou não sem o uso da classe `datetime`, __blocos if__, __blocos if-elif__ ou __condicionais__ (`a if b else c`) nem os operadores lógicos __AND__ (`and`) e __OR__ (`or`) com a exceção do operador __NOT__ (`not`).

Retorne `True` se for um ano bissexto, `False` caso contrário.

Exemplo de chamada de função:
# --seed--
```python
def leap_year(year):
    pass
```


# --before-asserts--
```python
import unittest
class CodigoTests(unittest.TestCase):
```



# --asserts--
O uso de `month`, `day`, `if`, `else`, `elif`, `and`, `or` não é permitido.
```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```
O ano `2016` é um ano bissexto.
```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```
O ano `1996` é um ano bissexto.
```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```
O ano `1600` é um ano bissexto.
```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```
O ano `2020` é um ano bissexto.
```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```
O ano `2000` é um ano bissexto.
```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```
O ano `2008` é um ano bissexto.
```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```
O ano `1521` não é um ano bissexto.
```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```
O ano `1800` não é um ano bissexto.
```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```
O ano `2007` não é um ano bissexto.
```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```
O ano `2002` não é um ano bissexto.
```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```
O ano `1979` não é um ano bissexto.
```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```
O ano `2006` não é um ano bissexto.
```python
    def test12(self):
        self.assertEqual(leap_year(2006), False, "--err-t12--")
```



























# --after-asserts--
```python
if __name__ == "__main__":
    unittest.main()
```


# --solutions--
```python
def leap_year(year):
    return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0))
```
```python
def leap_year(year):
    while year % 100 == 0:
        year = year // 100
    return year % 4 == 0
```


