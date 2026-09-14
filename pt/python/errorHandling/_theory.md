Uma **exceção** é a forma do Python dizer que uma instrução não pode ser executada. Dividir por zero, converter `"abc"` em um inteiro ou ler uma chave inexistente de um dicionário levantam uma. Quando nada a trata, o programa para ali mesmo e imprime um **traceback**:
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
O traceback lista as linhas que estavam em execução, e a última linha informa o **tipo da exceção** (`ZeroDivisionError`) e sua mensagem (`division by zero`). Essa última linha é a primeira a ser lida.

Para manter o programa vivo, coloque a instrução arriscada em um bloco `try` e descreva a recuperação em um bloco `except`:
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
O Python executa o bloco `try`; se a exceção nomeada for levantada, ele salta direto para o bloco `except` correspondente e continua com o restante do programa.

---

O bloco `try` para na **primeira** instrução que levanta uma exceção; as linhas seguintes a ela são puladas e o controle passa para o bloco `except`. Nada no bloco `try` é desfeito, então mantenha-o o mais curto possível:
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
Um `return` dentro de `except` funciona como qualquer outro `return`, o que torna `try`/`except` uma forma natural de devolver um valor alternativo em vez de quebrar.

---

Uma exceção que nenhum bloco `except` corresponde continua se propagando: para fora da linha, para fora da função que a executou, para fora do chamador dela, e assim por diante. Se nada a capturar antes do topo do programa, o Python imprime o traceback e o processo termina com um status de saída diferente de zero. As linhas após a instrução que falhou nunca rodam.

---

Uma cláusula `except` captura apenas o tipo que ela nomeia, e suas subclasses. Esse é o ponto: todo o resto continua se propagando, então um bug que você não esperava ainda aparece como um traceback em vez de ser engolido.

`int(text)` levanta **`ValueError`** quando o texto não descreve um número inteiro, então esse é o tipo a nomear ao ler entrada do usuário:
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
Nomear `ValueError` aqui é uma decisão, não uma formalidade: `int(None)` levanta `TypeError`, que esta função deliberadamente **não** captura, porque passar `None` é um erro de programação e deve ser visto.

---

Escolher o tipo mais estreito que cobre a falha que você espera é o que torna o tratamento de erros confiável. Uma função que lê texto deve se recuperar de texto inválido (`ValueError`), mas não deve esconder o fato de ter sido chamada com o tipo errado de argumento (`TypeError`) — esse erro pertence ao chamador, então deixe-o passar.

---

Um bloco `try` pode ser seguido por **várias** cláusulas `except`, cada uma tratando uma falha diferente com uma recuperação diferente. O Python compara a exceção levantada contra elas de cima para baixo e executa a **primeira** que corresponder; as outras são puladas:
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
Como a primeira correspondência vence, a ordem importa quando os tipos são relacionados: uma cláusula para um tipo geral colocada acima de uma cláusula para um tipo mais específico sempre venceria, deixando a cláusula específica inalcançável.

---

Quando várias falhas merecem a **mesma** recuperação, listá-las como uma tupla em uma única cláusula é mais curto do que repetir o bloco:
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
Os parênteses são obrigatórios: `except ValueError, ZeroDivisionError:` é um erro de sintaxe no Python 3. Uma tupla ainda é uma lista explícita de tipos.

---

`except:` sem nenhum tipo depois dele é um **bare except**. Ele corresponde a tudo, incluindo exceções que não têm nada a ver com a operação que você estava protegendo, então a regra é simples: sempre nomeie os tipos dos quais você realmente pode se recuperar.

---

Uma exceção é um objeto, e `as` o vincula a um nome para que o manipulador possa examiná-lo:
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)` — que é o que `print(e)` e um slot de f-string usam — retorna a mensagem com que a exceção foi construída, e `type(e).__name__` retorna o nome da classe como texto. O nome vinculado por `as` só existe dentro do bloco `except`; o Python o apaga quando o bloco termina.

---

Um bloco `try` pode ser seguido por um bloco `else`, que roda **apenas quando o bloco `try` terminou sem levantar exceção**:
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
Colocar `print(number * 2)` dentro do bloco `try` também funcionaria, mas então um `ValueError` levantado pela própria impressão seria confundido com uma falha de conversão. O `else` mantém o bloco `try` reduzido à única instrução protegida, e guarda tudo o que deve acontecer em caso de sucesso.

---

Um bloco `finally` roda **não importa o que aconteça**: depois de um bloco `try` concluído sem erros, depois de um bloco `except`, mesmo enquanto uma exceção que ninguém capturou se propaga, e mesmo quando o bloco `try` ou `except` executa um `return`:
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
Os dois caminhos imprimem `done` antes que o valor saia da função. Essa garantia é a razão de ser do `finally`: fechar um arquivo, liberar um lock, restaurar uma configuração. A forma completa é `try` / `except` / `else` / `finally`; um `try` precisa de pelo menos um `except` ou um `finally`, e o `else` só funciona junto com um `except`.

---

O seu próprio código também pode levantar exceções, com a instrução `raise` seguida de um objeto de exceção:
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` para a função imediatamente, exatamente como uma falha embutida faria. Retornar um valor de erro em vez disso — `-1`, `None`, `False` — é fácil para um chamador esquecer; uma exceção não pode ser ignorada por acidente.

Escolha o tipo que descreve o problema: `ValueError` quando o argumento tem o tipo certo, mas um valor impossível, `TypeError` quando ele tem o tipo errado por completo. O texto passado para a exceção é sua mensagem.

---

Um punhado de exceções embutidas cobre a maioria das falhas do dia a dia:

| Exceção | Levantada quando | Exemplo |
|---|---|---|
| `ValueError` | o tipo está certo, mas o valor é impossível | `int("abc")` |
| `TypeError` | o tipo em si está errado | `"x" + 1` |
| `ZeroDivisionError` | uma divisão ou módulo tem divisor zero | `1 / 0` |
| `KeyError` | um dicionário não tem tal chave | `{"a": 1}["b"]` |
| `IndexError` | o índice de uma sequência está fora do intervalo | `[1, 2][5]` |

Usar uma destas em vez de inventar um novo tipo mantém seus erros legíveis para qualquer pessoa que conheça Python.
