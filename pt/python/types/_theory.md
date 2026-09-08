Todo valor em Python tem um **tipo** que diz que tipo de dado ele é e o que você pode fazer com ele.
Os tipos básicos integrados são:
- `int`, um número inteiro como `42` ou `-3`
- `float`, um número com parte decimal como `3.5`
- `str`, um texto como `"hello"`
- `bool`, um dos dois valores `True` e `False`
- `NoneType`, o tipo do valor especial `None`, que significa "nenhum valor"

A função integrada `type()` retorna o tipo de um valor. Ao imprimi-lo, é exibido o nome da classe:
```python
print(type(42))     # <class 'int'>
print(type("hi"))   # <class 'str'>
```
Você nunca escreverá `NoneType` você mesmo: `type(None)` o retorna, mas o nome não é um integrado como os outros quatro.

---

`type()` retorna a classe de um valor, então você pode compará-la com um nome de classe usando `is`:
```python
age = 30
print(type(age) is int)  # True
```
Na maioria das vezes, porém, você só quer saber **se** um valor é de um certo tipo. Essa é a função de `isinstance(value, cls)`, que retorna `True` ou `False`:
```python
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```
O segundo argumento também pode ser uma **tupla** de classes: o resultado é `True` se o valor pertencer a qualquer uma delas:
```python
print(isinstance(2.5, (int, float)))  # True
```

---

Python é **dinamicamente tipado**: o tipo pertence ao **valor**, não à variável.
Uma variável é apenas um nome ligado a um valor, e você pode ligá-lo a um valor de um tipo diferente a qualquer momento:
```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"
print(type(x))  # <class 'str'>
```
Nenhuma declaração e nenhuma conversão são necessárias: o valor antigo é simplesmente esquecido.
Isso é conveniente, mas também significa que o tipo de uma variável só é conhecido quando o programa roda, então misturar tipos por engano aparece como um erro em tempo de execução, não antes.

---

Você já conhece os operadores aritméticos. O que importa aqui é o **tipo do resultado**.
Combinar um `int` com um `float` resulta em um `float`, mesmo quando a parte decimal é zero:
```python
print(3 + 0.5)   # 3.5
print(2 * 1.0)   # 2.0
```
A **divisão verdadeira** `/` sempre retorna um `float`, mesmo quando os números se dividem exatamente:
```python
print(10 / 5)    # 2.0
print(7 / 2)     # 3.5
```
A **divisão inteira** `//` arredonda o resultado para baixo até o número inteiro mais próximo (então `-7 // 2` é `-4`) e retorna um `int` quando ambos os operandos são inteiros. Junto com o resto `%`, ela divide uma quantidade em partes inteiras:
```python
print(7 // 2)    # 3
print(7 % 2)     # 1
```

---

Os valores não mudam de tipo por conta própria: para transformar um valor em outro tipo você chama o nome do tipo como uma função. Isso é chamado de **conversão** (ou *casting*):
```python
print(int("42"))      # 42
print(float("3.5"))   # 3.5
print(str(7))         # '7'
print(int(3.9))       # 3
```
`int()` e `float()` leem números escritos como texto, que é o que você obtém da entrada do usuário ou de arquivos. `str()` transforma qualquer coisa em texto, para que possa ser juntada com `+` a outras strings.
Note que `int(3.9)` não arredonda: ela descarta a parte decimal.

---

Uma conversão pode falhar. `int("abc")` não consegue produzir um número, então ela gera um `ValueError` e o programa para:
```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError as well: "3.5" is not a whole number
```
Para manter o programa em execução você pode capturar o erro com `try` / `except`: o código no bloco `try` roda, e se ele gerar o erro nomeado, o bloco `except` roda em seu lugar:
```python
try:
    number = int(text)
except ValueError:
    number = 0
```
Quando a conversão tem sucesso, o bloco `except` é pulado.

---

Todo valor pode ser interpretado como um booleano. `bool()` converte um valor em `True` ou `False`, e a mesma regra é aplicada quando um valor é usado diretamente em um `if`.
Os valores que contam como **falsos** são os "vazios":
- o número `0` (e `0.0`)
- a string vazia `""`
- coleções vazias como `[]`, `{}`, `()` e `set()`
- `None`

Qualquer valor não vazio é **verdadeiro**, incluindo números negativos e strings que apenas parecem vazias, como `"0"` ou `" "`:
```python
print(bool(0))     # False
print(bool(-1))    # True
print(bool(""))    # False
print(bool("0"))   # True
```
É por isso que `if name:` é uma forma comum de verificar que uma string não está vazia.

---

`bool` é uma **subclasse** de `int`: `True` se comporta como `1` e `False` como `0` onde quer que um número seja esperado:
```python
print(True + 1)     # 2
print(True == 1)    # True
print(False * 10)   # 0
```
`sum()` soma os itens de uma lista, então somar uma lista de booleanos **conta** quantos são `True`:
```python
answers = [True, False, True]
print(sum(answers))  # 2
```
Por causa da relação de subclasse, `isinstance(True, int)` retorna `True`, enquanto `type(True)` ainda é `bool`.

---

`None` é um valor que existe por conta própria e significa "nada aqui". É o que uma função retorna quando não tem uma instrução `return`, e é um placeholder comum para um valor que ainda não é conhecido.
Como existe apenas um `None`, verifique-o com `is`, não com `==`:
```python
result = None
if result is None:
    print("no result yet")
```
Todo tipo tem um atributo `__name__` com o seu nome como uma string, o que é útil para mensagens:
```python
print(type(3).__name__)     # int
print(type(None).__name__)  # NoneType
```

---

Imprimir um `float` mostra tantos dígitos quantos forem necessários para representá-lo exatamente, o que costuma ser demais:
```python
print(19.999 * 3)  # 59.997
print(10 / 3)      # 3.3333333333333335
```
Dentro de uma f-string você pode adicionar uma **especificação de formato** após dois-pontos. `.2f` significa "número de ponto fixo com 2 casas decimais":
```python
total = 10 / 3
print(f"{total:.2f}")   # 3.33
print(f"{total:.0f}")   # 3
```
O valor é arredondado para o número de casas decimais solicitado, e zeros são adicionados quando necessário: `f"{2.5:.2f}"` dá `2.50`.

---

A formatação apenas muda como um número é exibido. Para obter um **valor** arredondado use a função integrada `round()`:
```python
print(round(3.14159, 2))  # 3.14
print(round(2.71828, 1))  # 2.7
```
Com um único argumento, `round()` arredonda para o número inteiro mais próximo e retorna um `int`; com um número de casas decimais, ela retorna um `float`:
```python
print(round(3.7))     # 4
print(round(3.7, 0))  # 4.0
```
Note que valores exatamente no meio entre dois números são arredondados para o **par**: `round(2.5)` é `2` e `round(3.5)` é `4`.

---

Um `float` é armazenado em binário com um número fixo de bits, então a maioria dos números decimais só pode ser **aproximada**. O erro é minúsculo, mas aparece na aritmética:
```python
print(0.1 + 0.2)   # 0.30000000000000004
```
Por esse motivo você não deve comparar floats por igualdade exata. Arredonde ambos os lados, ou use `math.isclose()`, que verifica que dois números são iguais dentro de uma tolerância minúscula:
```python
import math
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(math.isclose(0.1 + 0.2, 0.3))  # True
```
Os inteiros não têm esse problema: `1 + 2 == 3` é sempre `True`.

---

Ao contrário de muitas linguagens, os inteiros de Python não têm **tamanho máximo**: um `int` cresce para acomodar quantos dígitos forem necessários, então cálculos grandes permanecem exatos:
```python
print(3 ** 100)  # 515377520732011331036461129765621272702107522001
```
Um `float`, por outro lado, mantém apenas cerca de 15 dígitos significativos, então a mesma potência como float perde precisão:
```python
print(3.0 ** 100)  # 5.153775207320113e+47
```
Como `str()` funciona em qualquer `int`, uma forma rápida de contar os dígitos de um número é medir o comprimento do seu texto.

---

Você pode escrever o tipo esperado de uma variável, parâmetro ou valor de retorno como uma **type hint**: dois-pontos após o nome para variáveis e parâmetros, uma seta `->` antes dos dois-pontos para o valor de retorno:
```python
count: int = 3

def greet(name: str) -> str:
    return "Hi " + name
```
Hints são **documentação** para pessoas e para ferramentas como editores: Python **não** as verifica. Este código roda sem reclamar e imprime `hello`:
```python
count: int = "hello"
print(count)
```
Hints deixam claros os tipos pretendidos, mas o valor ainda decide o tipo real.

---

Conversões podem ser combinadas. `int("3.7")` falha, mas `float("3.7")` funciona, e `int()` de um `float` descarta a parte decimal:
```python
number = float("3.7")   # 3.7
print(int(number))      # 3
```
`bool()` segue as regras de truthiness: `bool("")` é `False`, e note que `bool("False")` é `True`, porque é uma string não vazia.

---

Texto vindo de fora é sempre um `str`, e cabe ao seu programa descobrir qual tipo ele realmente contém.
Uma abordagem comum é tentar a conversão **mais estrita** primeiro, e recorrer à seguinte quando ela gerar um `ValueError`:
```python
try:
    value = int(text)
except ValueError:
    value = float(text)
```
Aninhar um segundo `try` dentro do bloco `except` permite recorrer mais uma vez, por exemplo para manter o texto como está.
