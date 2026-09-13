Um **comentário** é uma nota escrita dentro do código-fonte para as pessoas que o leem. O Python ignora completamente os comentários, então eles nunca mudam o que o programa faz.

O único tipo de comentário que o Python tem é o **comentário de linha única**: ele começa com `#` e vai até o fim da linha.
```python
# Greets the user
print("Hello")
```
Use comentários para explicar para que serve um trecho de código, ou por que ele foi escrito daquela forma.

---

Um comentário não precisa de uma linha só para ele: ele pode vir depois do código na mesma linha. Esse é um **comentário inline**, e é um bom lugar para uma nota curta sobre aquela instrução específica:
```python
retries = 3  # give up after three attempts
```
Tudo, de `#` até o fim da linha, é ignorado, enquanto o código antes dele roda normalmente.

O guia de estilo do Python, a **PEP 8**, pede um pouco de espaçamento aqui: pelo menos **dois espaços** entre o código e o `#`, e **um espaço** depois do `#`. Um comentário em uma linha própria precisa apenas do espaço depois do `#`.

---

Como o Python descarta completamente os comentários, adicionar ou apagar um comentário nunca muda o que um programa faz. Só roda o código que **não** está comentado.

Isso faz do `#` um jeito rápido de desligar uma linha de código sem apagá-la. Isso se chama **comentar o código**:
```python
total = 10
# total = total + 5
print(total)  # prints 10
```
A segunda linha agora é um comentário, então `total` continua `10`. Remover o `#` traz a linha de volta à vida.

Comentar o código é útil enquanto você experimenta, mas lembre-se de limpar depois: código que fica comentado por muito tempo só confunde quem for ler em seguida.

---

Muitas linguagens têm um segundo tipo de comentário, um **comentário em bloco** que se estende por várias linhas, como `/* ... */`. O Python não tem essa sintaxe: o `#` é tudo o que existe.

Quando uma explicação precisa de mais de uma linha, coloque um `#` na frente de cada linha:
```python
# Prints the welcome banner.
# Called once when the app starts.
print("Welcome!")
```
O mesmo truque comenta várias linhas de código de uma vez: um `#` por linha. Qualquer editor pode adicionar ou remover esses `#` de uma seleção inteira com um único atalho, então isso custa menos do que parece.

---

Você verá com frequência uma **string com aspas triplas** usada como se fosse um comentário em bloco:
```python
"""
This looks like a comment,
but it is a string.
"""
print("done")
```
Uma string entre `"""` e `"""` pode se estender por várias linhas, e uma string escrita sozinha é uma instrução válida: o Python a constrói, não faz nada com ela e a descarta. Nada é impresso, então o resultado parece um comentário.

Mas não é. É uma string literal, então as regras de aspas continuam valendo: uma aspa sem par ou um `"""` perdido dentro dela quebra o programa, enquanto dentro de um comentário `#` tudo é permitido. Ela também pode se tornar uma docstring por acidente, se acabar sendo a primeira instrução de um arquivo, de uma classe ou de uma função. Em qualquer outro lugar ela simplesmente não vai a lugar nenhum: o CPython descarta a instrução inteira ao compilar.

Então, para desligar código, use `#`. A string com aspas triplas tem seu próprio trabalho, que começa no próximo exercício.

---

Quando uma string é a **primeira instrução** dentro de uma função, o Python a trata como a documentação dessa função. Ela se chama **docstring**:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"
```
Por convenção, uma docstring é escrita entre aspas duplas triplas, `"""`, mesmo quando cabe em uma linha, para que possa crescer depois sem trocar as aspas.

Escreva o resumo na terceira pessoa, como se descrevesse a função: "Returns...", "Adds...", "Checks...". A docstring deve vir antes de qualquer outra instrução no corpo, caso contrário é apenas uma string comum.

---

Uma docstring não é descartada: o Python a guarda no atributo `__doc__` da função, para que o programa possa ler a própria documentação enquanto roda:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"

print(greet.__doc__)  # Returns the greeting for name.
```
Quando uma função não tem docstring, `__doc__` é `None`. É isso que `help(greet)` imprime, e o que um editor mostra quando você passa o mouse sobre o nome.

---

Um arquivo também pode ser documentado. Uma string escrita como a **primeiríssima instrução do arquivo**, antes de qualquer import ou definição, é a **docstring do módulo**: ela diz para que serve o arquivo inteiro.
```python
"""Tools for working with rectangles."""

def area(width, height):
    """Returns the area of a rectangle."""
    return width * height
```
Só a primeira instrução conta. Um comentário pode ficar acima dela, mas qualquer código real no meio transforma a string de volta em uma string comum e inútil.

---

As classes funcionam da mesma forma: uma string colocada como a primeira instrução do corpo de uma classe é a docstring dessa classe, e ela é guardada em `__doc__`:
```python
class Point:
    """A point on a grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point.__doc__)  # A point on a grid.
```
Cada método dentro da classe também pode ter sua própria docstring, lida com `Point.__init__.__doc__`. Então os três lugares que aceitam uma docstring são o topo de um módulo, o topo de uma classe e o topo de uma função.

---

Docstrings e comentários `#` parecem semelhantes, mas respondem a perguntas diferentes.

Uma **docstring** é para quem **usa** o código: o que a função faz, o que ela espera e o que ela devolve. Ela sobrevive em `__doc__`, o `help()` a lê, os editores a mostram, e as ferramentas de documentação a coletam.

Um **comentário** é para quem **lê** o código: por que esta linha está escrita dessa forma, o que significa o número estranho, qual bug ele contorna. Ele existe apenas no arquivo-fonte e desaparece quando o programa roda.

```python
def timeout():
    """Returns the number of seconds to wait for the server."""
    # the server drops idle connections after 35 seconds
    return 30
```
Resumindo: a documentação da função vai na docstring, as notas sobre a implementação vão nos comentários.

---

Quando uma linha não é suficiente, uma docstring cresce para um layout fixo, descrito na **PEP 257**: um resumo de uma linha, uma linha em branco, depois os detalhes, e o `"""` de fechamento em uma linha própria.
```python
def to_seconds(minutes):
    """Returns the number of seconds in the given minutes.

    minutes is a whole number and is never negative.
    """
    return minutes * 60
```
A linha em branco importa: as ferramentas mostram a primeira linha sozinha, como uma descrição curta, e guardam o resto para quem quiser ler mais.

---

A docstring precisa ser a **primeira linha do corpo**, acima de todas as outras instruções. Uma string escrita depois do `return`, ou em qualquer outro lugar do corpo, é apenas uma string: `__doc__` continua `None` e nenhuma ferramenta jamais a mostrará.

---

Alguns comentários seguem uma convenção que os editores entendem. Os **marcadores** mais comuns são:
- `# TODO: ...` sinaliza algo que ainda precisa ser escrito
- `# FIXME: ...` sinaliza código que se sabe estar errado e precisa ser corrigido

```python
limit = 10
# TODO: read the limit from the settings
```
Para o Python eles são comentários comuns; os editores os reúnem em um painel dedicado, então o trabalho pendente é fácil de encontrar. Um `TODO` normalmente fica ao lado de um placeholder que mantém o programa rodando até que o código real seja escrito.

Quando você terminar o trabalho, substitua o placeholder e apague o marcador na mesma alteração, para que o comentário nunca minta sobre o estado do código.

---

Um comentário colocado acima de uma função para dizer o que a função faz está no lugar errado. A docstring é o lugar para isso: ela está anexada à função, o `help()` a encontra e os editores a mostram, enquanto um comentário `#` acima do `def` é invisível para todos eles.

```python
# adds a and b
def add(a, b):
    return a + b
```
Mover a mesma frase uma linha para baixo, entre aspas triplas, a transforma em documentação de verdade:
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```

---

O Python procura por `#` apenas no código, nunca dentro de uma **string**. Entre aspas, o `#` é um caractere comum:
```python
print("black is #000000")  # a hex colour
```
O primeiro `#` faz parte do texto, o segundo inicia um comentário de verdade. O mesmo vale para `"""` dentro de um comentário `#`: ali ele é apenas três caracteres de aspas, e não inicia nada.

---

Um bom comentário explica **por que** o código faz algo, não **o que** ele faz. O código já mostra o que acontece; repeti-lo em palavras adiciona ruído e fica desatualizado assim que o código muda:
```python
# set timeout to 30
timeout = 30
```
A razão por trás do número é o que um leitor não consegue adivinhar:
```python
# the server drops idle connections after 35 seconds, so stop earlier
timeout = 30
```
Se um comentário apenas repete a linha abaixo dele, apague-o ou substitua-o pela razão. Os melhores comentários são os que dizem algo que o código não consegue.
