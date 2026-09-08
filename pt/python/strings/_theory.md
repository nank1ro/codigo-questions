Uma **string** é um pedaço de texto: uma sequência de caracteres entre aspas.
O Python aceita aspas simples `'...'` e duplas `"..."`, e elas funcionam exatamente da mesma forma:
```python
name = 'Ada'
language = "Python"
```
A escolha importa quando o próprio texto contém uma aspa.
Um apóstrofo dentro de aspas simples terminaria a string cedo demais, então use aspas duplas nesse caso:
```python
print("It's sunny")  # It's sunny
```

---

A função embutida `len()` retorna o **comprimento** de uma string, ou seja, quantos caracteres ela contém.
Espaços e pontuação também contam como caracteres:
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

Cada caractere de uma string tem uma posição chamada **índice**.
Os índices começam em `0`, não em `1`: o primeiro caractere está no índice `0`, o segundo no índice `1`, e assim por diante.
Escreva o índice entre colchetes depois da string para ler um único caractere:
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
Pedir um índice que não existe, como `word[6]`, gera um `IndexError`.

---

Os índices também podem ser **negativos**: eles contam a partir do final da string.
`-1` é o último caractere, `-2` o anterior a ele, e assim por diante:
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
Isso é útil porque você não precisa saber o comprimento da string para chegar ao seu final.

---

Um **fatiamento** (slice) extrai uma parte de uma string.
Escreva `[início:fim]` entre colchetes: o caractere em `início` é incluído, o de `fim` é **excluído**:
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
Você pode omitir o `início` para fatiar desde o começo, ou o `fim` para fatiar até o final:
```python
print(word[:2])  # py
print(word[2:])  # thon
```
Fatiar nunca gera um erro: um `fim` maior que o comprimento simplesmente para no último caractere.

---

Você já sabe que `+` junta duas strings (**concatenação**).
O operador `*` **repete** uma string um determinado número de vezes:
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
A repetição é uma forma rápida de desenhar separadores e padrões simples.

---

O operador `in` verifica se uma string **contém** outra.
Ele retorna `True` ou `False`, então se encaixa naturalmente dentro de um `if`:
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` faz a verificação oposta.

---

Strings vêm com muitos **métodos** embutidos: funções chamadas com um ponto depois da string.
`upper()` retorna o texto em letras maiúsculas, `lower()` em letras minúsculas:
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
Note que os métodos **retornam uma nova string**: a `word` original não é alterada.
`lower()` é frequentemente usado para comparar textos ignorando maiúsculas e minúsculas: `"Yes".lower() == "yes"`.

---

Strings são **imutáveis**: uma vez criada, seus caracteres não podem ser alterados.
Atribuir a um índice gera um `TypeError`:
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
Para "mudar" uma string, você constrói uma nova, por exemplo com fatiamentos e concatenação, e a armazena na variável:
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

O texto digitado por usuários costuma ter espaços extras ao redor.
O método `strip()` retorna uma cópia da string **sem espaços em branco no início e no final** (espaços, tabulações e quebras de linha):
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
Espaços no meio do texto são mantidos.
`lstrip()` remove apenas o lado esquerdo e `rstrip()` apenas o lado direito.

---

`split()` divide uma string em uma **lista** de pedaços.
Sem argumentos, ela divide por espaços em branco; com um argumento, ela divide por esse separador:
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` faz o oposto: cola os itens de uma lista em uma única string.
Ele é chamado no **separador**, e a lista é o argumento:
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` retorna uma cópia da string onde **toda** ocorrência de `old` é substituída por `new`:
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
Como as strings são imutáveis, lembre-se de armazenar o resultado se quiser mantê-lo.

---

`find(sub)` retorna o **índice** da primeira ocorrência de `sub`, ou `-1` se não for encontrado:
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` retorna **quantas vezes** `sub` aparece:
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` e `endswith(suffix)` retornam `True` ou `False` dependendo de como a string começa ou termina:
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
Essa é a forma usual de verificar extensões de arquivo, protocolos ou prefixos.

---

Alguns caracteres não podem ser digitados diretamente dentro de uma string.
Uma **sequência de escape** é uma barra invertida `\` seguida de uma letra ou símbolo que representa um caractere especial:

- `\n` uma nova linha
- `\t` uma tabulação
- `\"` uma aspa dupla dentro de uma string com aspas duplas
- `\'` uma aspa simples dentro de uma string com aspas simples
- `\\` uma barra invertida literal

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
imprime:
```
Line 1
Line 2
She said "hi"
```
Cada sequência de escape conta como **um** caractere, mesmo que você digite dois.

---

Uma string que se estende por **várias linhas** pode ser escrita com **aspas triplas** `"""..."""` (ou `'''...'''`).
Cada quebra de linha dentro das aspas se torna parte da string, então você não precisa de `\n`:
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
imprime:
```
Roses are red,
Violets are blue
```
Strings com aspas triplas também podem conter aspas simples e duplas livremente.

---

Como todo método de string retorna uma nova string, você pode **encadear** métodos um após o outro.
Cada chamada trabalha sobre o resultado da anterior:
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
Um fatiamento também aceita um terceiro valor, o **passo**.
O passo `-1` percorre a string de trás para frente, que é o truque clássico para invertê-la:
```python
print("abc"[::-1])  # cba
```

---

Um **slug** é uma versão de um título amigável para URLs: minúsculas, sem espaços ao redor, e palavras separadas por traços, como `hello-world`.
Construir um é apenas um encadeamento dos métodos que você aprendeu: `strip()`, `lower()` e `replace()`.
