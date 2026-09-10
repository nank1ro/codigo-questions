Os operadores de comparação comparam dois valores e retornam um **booleano**, `True` ou `False`: `==` igual, `!=` diferente, `<` menor que, `>` maior que, `<=` menor ou igual, `>=` maior ou igual:
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
O resultado pode ser armazenado numa variável ou exibido diretamente. Um único `=` é uma atribuição, não uma comparação.

---

Os operadores de comparação não se limitam a números. As strings são comparadas caractere a caractere usando seus pontos de código, então `"apple" < "banana"` é `True` e, como toda letra maiúscula vem antes das minúsculas, `"Zoo" < "apple"` também é `True`. Listas e tuplas são comparadas elemento a elemento da mesma forma:
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
Uma comparação é uma expressão, então uma função pode fazer `return a < b` diretamente em vez de envolvê-la num `if`.

---

As comparações podem ser **encadeadas**: `1 < x < 10` verifica que `x` é maior que `1` **e** menor que `10`, exatamente como `1 < x and x < 10`, mas `x` é avaliado apenas uma vez:
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
Quaisquer operadores de comparação podem ser encadeados e cada um se aplica aos seus dois vizinhos: `a < b == c` significa `a < b and b == c`. Ler uma cadeia como um intervalo, `low < x < high`, é o uso mais comum.

---

Os operadores lógicos combinam booleanos. `and` é `True` apenas quando ambos os lados são `True`, `or` quando pelo menos um lado é, e `not` inverte um único valor:
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
As comparações têm precedência maior que os operadores lógicos, então `age >= 18 and member` não precisa de parênteses. Os parênteses são necessários para agrupar um `or` dentro de um `and`: `a and (b or c)`.

---

Quando `not`, `and` e `or` aparecem numa mesma expressão, Python aplica primeiro `not`, depois `and`, depois `or`. Assim `a or b and c` significa `a or (b and c)`, e `not a == b` significa `not (a == b)`:
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
Quando se pretende um agrupamento diferente, adicione parênteses; eles também tornam a expressão mais fácil de ler.

---

Todo valor tem um **valor de verdade**. `bool(value)` retorna `False` para `0`, `0.0`, `None`, a string vazia `""` e contêineres vazios como `[]`, `{}` e `set()`; qualquer outro valor é verdadeiro, incluindo `"0"` e `[0]`:
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`, `while`, `and`, `or` e `not` usam essa regra, então `if items:` verifica que a lista não está vazia e `not name` verifica que a string está vazia; não é preciso escrever `len(items) > 0` nem `name == ""`.

---

Como `if value:` já aplica o valor de verdade, comparar com `== True` ou `== False` é desnecessário e pode até estar errado: `2 == True` é `False`, e ainda assim `2` é verdadeiro. Teste o próprio valor:
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` e `or` nem sempre retornam `True` ou `False`: eles retornam um de seus **operandos**. `a and b` retorna `a` se for falso, caso contrário `b`; `a or b` retorna `a` se for verdadeiro, caso contrário `b`:
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
O resultado é verdadeiro ou falso exatamente quando a expressão inteira é, e é por isso que `if a and b:` continua funcionando. Um uso comum é um valor padrão: `name = user_input or "guest"`.

---

Os operadores lógicos são de **curto-circuito**: `and` para assim que um operando é falso e `or` assim que um é verdadeiro, porque o resultado já é conhecido. Os operandos restantes nunca são avaliados, então se forem chamadas de função elas não são executadas:
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` compara **valores**; `is` compara **identidade**, ou seja, se ambos os nomes se referem exatamente ao mesmo objeto. Duas listas iguais construídas separadamente são `==` mas não `is`:
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` serve para singletons como `None`, `True` e `False`: escreva `value is None` ou `value is not None`, nunca `value == None`, porque uma classe pode definir `==` para retornar qualquer coisa. Usar `is` com números ou strings não é confiável e Python avisa sobre isso.

---

A avaliação em curto-circuito é uma forma segura de **proteger** uma operação que falharia com alguns valores. Em `word is not None and len(word) < 4`, `len(word)` só é executado quando `word` não é `None`, então a chamada nunca lança um erro. A proteção deve vir primeiro:
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
Tenha em mente que `and` retorna um operando: `word and len(word) < 4` dá `None` para `None` e `""` para a string vazia, não `False`. Proteja com uma comparação de verdade quando for necessário um booleano.

---

O operador `in` verifica **pertencimento**: se um elemento está numa lista, tupla ou conjunto, se uma substring está numa string, ou se uma chave está num dicionário. `not in` é a sua negação:
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
Ambos retornam um booleano e se leem como inglês, o que os torna a forma preferida de testar pertencimento em vez de escrever um laço.
