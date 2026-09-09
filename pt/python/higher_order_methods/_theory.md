Em Python uma função é um **valor**, assim como um número ou uma string. Você pode armazená-la em uma variável, colocá-la em uma lista ou passá-la para outra função. Apenas os parênteses a chamam: `shout` é a função em si, `shout("hi")` é o seu resultado:
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
Uma função que recebe outra função como parâmetro, ou que retorna uma, é chamada de **função de ordem superior**. Dentro dela, o parâmetro é chamado com parênteses como qualquer outra função:
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

Passar uma função como argumento permite que quem chama decida **o quê** fazer, enquanto a função de ordem superior decide **quantas vezes** ou **sobre o quê**. O parâmetro função pode ser chamado quantas vezes for necessário, e o seu resultado pode ser passado de volta para ele:
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
Qualquer chamável funciona: uma função `def`, uma função embutida como `len` ou uma `lambda`.

---

A função embutida `map(func, iterable)` chama `func` em cada elemento e produz os resultados, um para cada elemento. Ela retorna um *map object* preguiçoso, então envolva-a em `list()` para ver os valores:
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
Qualquer chamável pode ser passado, não apenas uma lambda: uma função embutida como `len`, ou um método retirado da sua classe, como `str.upper`, que recebe a string como seu primeiro argumento:
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

A função embutida `filter(func, iterable)` mantém apenas os elementos para os quais `func` retorna um valor verdadeiro. Como `map`, ela retorna um objeto preguiçoso que deve ser convertido em uma lista:
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
A função passada a `filter` é chamada de **predicado**: ela recebe um elemento e responde a uma pergunta de sim/não sobre ele. Passar `None` em vez de uma função mantém os elementos que são verdadeiros por si mesmos, descartando `0`, `""` e `None`.

---

`sorted(iterable, key=func)` ordena os elementos pelo valor que `func` retorna para cada um deles, sem alterar os próprios elementos. Adicione `reverse=True` para obter os maiores primeiro:
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
A ordenação é **estável**: elementos cujas chaves são iguais mantêm a sua ordem original. A função `key` é chamada uma vez por elemento e os seus resultados são usados apenas para comparar, então a saída ainda contém as palavras originais, não os seus comprimentos.

---

A função `key` pode escolher **qualquer parte** de um elemento. Para uma lista de tuplas, `lambda s: s[1]` ordena pelo segundo item de cada tupla; para uma lista de dicionários, `lambda d: d["age"]` ordena por um valor:
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` e `max` aceitam o mesmo parâmetro `key`, então `max(pairs, key=lambda p: p[1])` retorna `('a', 3)`: a tupla inteira, não apenas o número.

---

Uma função também pode **retornar** uma função. Defina uma função interna com `def` e retorne-a sem chamá-la:
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
A função interna continua usando `greeting` mesmo depois que `make_greeter` terminou: ela **lembra** as variáveis do escopo onde foi criada. Uma função assim é chamada de **closure**. Cada chamada a `make_greeter` cria uma nova closure independente com o seu próprio `greeting`.

---

Uma closure pode ler as variáveis da função que a envolve, mas atribuir a uma delas cria em vez disso uma **nova variável local**. Para atualizar a variável externa, declare-a com `nonlocal` dentro da função interna:
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` procuraria `count` no nível do módulo, onde ela não existe. Com `nonlocal`, cada chamada à função retornada atualiza o mesmo `count`, então a closure carrega estado entre as chamadas, como um pequeno objeto.

---

`reduce(func, iterable, initial)` do módulo `functools` dobra uma sequência em um **único valor**. Ela chama `func` com o resultado até o momento e o próximo elemento, começando de `initial`:
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
Os passos são `0 + 1`, depois `1 + 2`, depois `3 + 3`. Quando `initial` é omitido, o primeiro elemento é usado como valor inicial, mas então uma sequência vazia levanta um `TypeError`, então forneça um valor inicial sempre que a sequência puder estar vazia.

---

`partial(func, *fixed)` de `functools` constrói uma nova função com alguns argumentos **já preenchidos**. Chamar o resultado fornece os restantes:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
Argumentos posicionais dados a `partial` preenchem os primeiros parâmetros; argumentos nomeados fixam um parâmetro pelo nome e ainda podem ser sobrescritos no momento da chamada. Um partial é um chamável comum, então pode ser passado a `map`, `sorted` ou qualquer outra função de ordem superior.

---

`partial` é útil com funções embutidas que recebem opções. `int(text, base=16)` analisa uma string hexadecimal; fixar a base gera um conversor de um argumento que se encaixa no `map`:
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
O objeto partial lembra o que ele envolve: `hex_to_int.func` é `int`, e `hex_to_int.keywords` é `{'base': 16}`.

---

Um **decorator** é uma função de ordem superior que recebe uma função e retorna uma nova que a envolve, geralmente para adicionar comportamento antes ou depois da chamada original:
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` é o nome com o qual a função foi definida. Aplicar o decorator é apenas uma chamada: `greet = announce(greet)`. A sintaxe `@` colocada na linha **acima** de um `def` faz exatamente isso:
```python
@announce
def greet(name):
    return "Hello, " + name
```
O decorator deve ser definido antes de ser usado com `@`, porque a substituição acontece assim que o `def` executa.

---

Um decorator que aceita apenas um argumento tem pouca utilidade. Para envolver **qualquer** função, o wrapper coleta cada argumento posicional em `*args` e cada argumento nomeado em `**kwargs`, e os encaminha sem alterações:
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
Dentro do wrapper, `args` é uma tupla e `kwargs` um dicionário; o `*` e o `**` na chamada os desempacotam de volta em argumentos separados.

---

`any(iterable)` retorna `True` se **pelo menos um** elemento é verdadeiro, `all(iterable)` se **todos** os elementos são. Elas combinam naturalmente com uma **expressão geradora**: uma list comprehension escrita sem os colchetes, que produz os valores um de cada vez em vez de construir uma lista:
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
Como os valores são produzidos preguiçosamente, `any` para no primeiro `True` e `all` no primeiro `False`, sem avaliar o resto. `sum` também aceita uma expressão geradora: `sum(1 for age in ages if age >= 18)` conta os adultos.
