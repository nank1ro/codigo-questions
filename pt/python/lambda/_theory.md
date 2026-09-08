Às vezes você precisa de uma função minúscula usada apenas uma vez, por exemplo para dobrar um número.
Escrever um bloco `def` completo para isso parece pesado demais.
O Python oferece uma forma mais curta: a expressão **lambda**, uma função _anônima_ escrita em uma única linha:
```python
lambda x: x * 2
```
A sintaxe é `lambda parâmetros: expressão`.
Uma lambda não tem nome, mas você pode armazená-la em uma variável e chamá-la como qualquer outra função:
```python
double = lambda x: x * 2
print(double(4))  # 8
```

---

Note que o corpo da lambda não tem a palavra-chave `return`.
O corpo é uma **única expressão**, e seu valor é retornado automaticamente:
```python
square = lambda n: n * n
print(square(3))  # 9
```

---

Uma lambda pode receber **mais de um parâmetro**.
Separe-os com vírgulas, exatamente como em uma função `def`:
```python
power = lambda base, exp: base ** exp
print(power(2, 3))  # 8
```

---

Como o corpo deve ser uma única expressão, uma lambda **não pode conter instruções**.
Nada de `return`, blocos `if`, loops ou atribuições:
```python
# SyntaxError
increment = lambda x: return x + 1
```
Se você precisar de algo assim, escreva uma função `def` normal.

---

Os parâmetros de uma lambda também aceitam **valores padrão**:
```python
greet = lambda name="World": f"Hello, {name}!"
print(greet())       # Hello, World!
print(greet("Ana"))  # Hello, Ana!
```

---

Você nem precisa armazenar uma lambda: pode **chamá-la imediatamente**.
Envolva a lambda em parênteses e depois adicione os argumentos:
```python
print((lambda x: x + 1)(4))  # 5
```

---

É como argumentos para outras funções que as lambdas realmente brilham.
`sorted()` aceita um parâmetro `key`: uma função chamada em cada item, cujo resultado decide a ordem.
Uma lambda é perfeita para isso:
```python
words = ["banana", "kiwi", "apple"]
print(sorted(words, key=lambda w: len(w)))
# ['kiwi', 'apple', 'banana']
```

---

A lambda usada em `key` pode escolher qualquer parte de um item.
Para uma lista de listas, `lambda p: p[1]` ordena pelo segundo elemento de cada lista interna.

---

`map()` aplica uma função a **todos os itens** de uma lista.
Ela retorna um _objeto map_ especial, então envolva-o em `list()` para ver os valores:
```python
nums = [1, 2, 3]
doubled = list(map(lambda n: n * 2, nums))
print(doubled)  # [2, 4, 6]
```

---

`filter()` mantém apenas os itens para os quais a função retorna `True`:
```python
nums = [5, 12, 8, 20]
big = list(filter(lambda n: n > 10, nums))
print(big)  # [12, 20]
```

---

Imprimir um objeto `map` diretamente não mostra seus valores: você obtém algo como `<map object at 0x7f2b1c>`.
Apenas `list()` (ou um laço) o transforma nos valores esperados.

---

As lambdas não se limitam a funções embutidas: **suas próprias funções** também podem receber uma função como parâmetro e chamá-la.
```python
def apply(func, value):
    return func(value)

print(apply(lambda x: x * 10, 3))  # 30
```

---

`max()` e `min()` também aceitam uma função `key`, assim como `sorted()`:
```python
words = ["hi", "hello", "hey"]
print(max(words, key=lambda w: len(w)))  # hello
```

---

**Quando você deve preferir `def`?**
Uma lambda é ótima para uma função curta e descartável passada como argumento.
Se a lógica precisar de um nome, de várias linhas, de uma docstring, ou for reutilizada em muitos lugares, uma função `def` é mais clara.
Um último truque: `sorted()` também aceita `reverse=True` para obter os maiores valores primeiro:
```python
print(sorted([3, 1, 2], reverse=True))  # [3, 2, 1]
```
