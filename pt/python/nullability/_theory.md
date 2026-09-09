Às vezes uma variável ainda não tem **nenhum valor** para guardar: um usuário que não fez login, uma busca que não encontrou nada, uma configuração que nunca foi escolhida. O Python representa isso com o valor especial `None`.
`None` é um valor como qualquer outro: você pode atribuí-lo, imprimi-lo e passá-lo para funções. Seu tipo é `NoneType`, e existe exatamente **um** `None` em todo o programa, então cada `None` que você escreve se refere ao mesmo objeto:
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` não é `0`, não é uma string vazia e não é `False`: é um valor distinto que significa "nada aqui".

---

Toda chamada de função produz um valor, mesmo quando a função parece não retornar nada. Uma função **sem** instrução `return`, ou com um `return` vazio, devolve `None`:
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
É por isso que chamar `print(my_list.append(3))` mostra `None`: `append` modifica a lista no lugar e não retorna nada.
Uma função que apenas executa uma ação (imprimir, salvar, modificar uma lista) geralmente retorna `None`, enquanto uma função que calcula algo deve devolvê-lo explicitamente com `return`.

---

Para verificar se uma variável contém `None`, use `is` e `is not`, nunca `==`:
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` pergunta "esses valores são *iguais*?", e qualquer classe pode responder a essa pergunta à sua maneira definindo o método `__eq__`. `is` pergunta "esses são o *mesmo objeto*?", e nada pode mudar a resposta.
Como existe apenas um `None`, `is None` é sempre correto e ligeiramente mais rápido, enquanto `== None` pode dar uma resposta surpreendente para objetos com um `__eq__` personalizado.

---

`None` conta como **falso** em uma condição, então `if not value:` é `True` quando `value` é `None`. É tentador usá-lo como uma verificação de `None`, mas o mesmo teste também é `True` para `0`, `""`, `[]` e todos os outros valores vazios:
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
Quando "nenhum valor" e "valor vazio" devem ser tratados de forma diferente, verifique `is None` primeiro, depois a truthiness:
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
Use `if not value:` apenas quando você realmente quiser tratar `None` e os valores vazios da mesma forma.

---

Um parâmetro pode ter um **valor padrão**, usado quando quem chama omite o argumento. `None` é o padrão usual para "não fornecido":
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
Isso importa para listas e dicionários. Um valor padrão é avaliado **uma vez**, quando a função é definida, então `def add(item, items=[])` compartilha a mesma lista em toda chamada que omite `items`, e os itens se acumulam. A correção é usar `None` como padrão e criar uma lista nova dentro da função:
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

Ler uma chave ausente de um dicionário com `[]` gera um `KeyError`. O método `get` é a alternativa segura: ele retorna o valor quando a chave existe e `None` quando não existe:
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` aceita um segundo argumento, o valor a retornar **no lugar de** `None` quando a chave está ausente:
```python
print(ages.get("Grace", 0))  # 0
```
Esta é a forma mais comum de `None` aparecer no código do dia a dia: uma busca que não encontrou nada.

---

Uma função que retorna um número **ou** `None` deve dizer isso em sua assinatura. Uma **type hint** é uma anotação que documenta o tipo esperado: `name: str` para um parâmetro e `-> int` para o valor de retorno. O Python não impõe as type hints, mas editores e leitores dependem delas:
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` se lê "um `int` ou `None`". A grafia mais antiga `Optional[int]` do módulo `typing` significa exatamente a mesma coisa, e você ainda a encontrará em código existente.
Sempre que ver `| None` em uma assinatura, lembre-se de verificar o resultado antes de usá-lo.

---

Funções que podem receber `None` geralmente começam com uma **guarda**: um `if` que retorna cedo quando não há nada com que trabalhar. O restante da função pode então presumir que o valor está presente, sem aninhar tudo dentro de um `else`:
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
As guardas vêm primeiro, na ordem em que as verificações devem acontecer: você não pode chamar `text.split()` antes de saber que `text` não é `None`.

---

O operador `or` não retorna `True` ou `False`: ele retorna seu operando à **esquerda** quando este é verdadeiro, e seu operando à **direita** caso contrário. Isso dá uma forma de uma linha para fornecer um fallback:
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
A pegadinha é que o `or` olha a truthiness, não o `None`: `0`, `""` e `[]` também são substituídos pelo fallback. Use `x or fallback` apenas quando todo valor vazio também deve se tornar o fallback.

---

Quando `0` ou `""` devem ser mantidos e apenas `None` substituído, o fallback precisa de uma verificação explícita com `is None`. A forma compacta é a **expressão condicional**, `a if condition else b`, que avalia para `a` quando a condição é verdadeira e para `b` caso contrário:
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

Uma lista pode conter `None` junto a valores reais, por exemplo leituras que falharam ou respostas que foram puladas. A maioria das operações não o aceita: `sum([8, None])` gera um `TypeError`.
Filtre os valores `None` com uma list comprehension cuja condição é `is not None`:
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
Usar `if r` em vez disso também descartaria cada `0`, então seja explícito quando zero é uma leitura válida.

---

Uma busca seguida de uma verificação de `None` geralmente precisa de duas linhas: uma para armazenar o resultado, outra para testá-lo. O operador de **expressão de atribuição** `:=`, apelidado de *walrus*, atribui um valor **dentro** de uma expressão, então ambos os passos cabem no `if`:
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
Os parênteses são obrigatórios: sem eles, o `:=` tentaria atribuir a comparação inteira. Depois do `if`, `age` permanece disponível como qualquer outra variável.

---

Nem todo "não encontrado" é relatado com `None`. Algumas funções mais antigas retornam, em vez disso, um valor **sentinela**: um valor normal ao qual é dado um significado especial. O método de string `find` retorna o índice de uma substring, ou `-1` quando ela está ausente:
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
A função `re.match(pattern, text)` do módulo `re` verifica se `text` começa com `pattern`, e retorna um objeto match, ou `None` quando não há correspondência.
`None` é a convenção mais segura: `-1` é um índice válido, então `text[text.find("x")]` silenciosamente retorna o último caractere em vez de falhar, enquanto usar `None` como índice gera um erro imediatamente.

---

`None` não pode ser ordenado: `None < 1` gera um `TypeError`, porque o Python não tem ideia de se "nada" é menor ou maior que um número.
Isso importa quando `None` é usado como valor inicial de uma busca, como "o melhor valor visto até agora, se houver". Toda comparação deve ser protegida por uma verificação `is None` colocada **primeiro**, para que o `or` faça curto-circuito e a comparação seja pulada quando ainda não há nada para comparar:
```python
if best is None or value > best:
    best = value
```
Escrito ao contrário, `value > best or best is None` compararia com `None` na primeira iteração e quebraria.
