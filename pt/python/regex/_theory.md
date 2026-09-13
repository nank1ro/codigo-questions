Uma **expressão regular** (regex) é uma pequena linguagem de padrões que descreve texto. O Python a fornece no módulo padrão `re`:
```python
import re
```

`re.search(pattern, text)` procura o padrão em qualquer lugar do texto. Ela retorna um **objeto de correspondência** quando encontra algo, e `None` quando não encontra. `match.group()` devolve o pedaço de texto que correspondeu:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

Dois pedaços do padrão fazem o trabalho aqui. `\d` significa *qualquer dígito*, e `+` significa *um ou mais do item anterior*, então `\d+` pode ser lido como "um ou mais dígitos". Outras abreviações úteis são `\w` (uma letra, dígito ou underscore) e `\s` (um espaço, tabulação ou nova linha).

Os padrões são escritos como **raw strings**, com um `r` antes das aspas. Em uma string Python normal, a barra invertida inicia uma sequência de escape, então `"\d"` é um aviso prestes a acontecer e `"\n"` se tornaria uma nova linha real em vez dos dois caracteres que o motor de regex espera. O prefixo `r` devolve à barra invertida o papel de caractere comum, então `r"\d"` é exatamente o que o motor recebe. Sempre use `r"..."` para padrões.

---

`re.search` varre o texto inteiro, mas `re.match` só tenta o padrão no **começo**:
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

Ambas retornam `None` quando nada corresponde, e um objeto de correspondência é sempre truthy, então a maneira usual de perguntar "houve correspondência?" é um simples `if`:
```python
if re.search(r"\d", text):
    print("there is a digit")
```
Quando um `True` ou `False` real é necessário, compare com `is not None` ou envolva a chamada em `bool(...)`.

---

Existe um terceiro ponto de entrada, `re.fullmatch`, que só tem sucesso quando o padrão cobre o texto **inteiro**, do primeiro ao último caractere. É a ferramenta certa para validação:
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

Assim, as três funções diferem apenas em onde o padrão pode ficar: `re.match` no começo do texto, `re.search` em qualquer lugar do texto e `re.fullmatch` no texto inteiro.

---

Um objeto de correspondência carrega mais do que o texto correspondido. Além de `.group()`, ele oferece a posição da correspondência dentro da string original:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` é o índice do primeiro caractere correspondido, `.end()` é o índice logo após o último, e `.span()` retorna ambos como uma tupla. Isso significa que `text[match.start():match.end()]` é sempre igual a `match.group()`.

Como `re.search` pode retornar `None`, ler `.group()` direto levanta um `AttributeError` quando nada correspondeu; verifique o resultado primeiro.

---

Parênteses dentro de um padrão criam um **grupo de captura**: uma parte da correspondência que pode ser lida por si só. Os grupos são numerados da esquerda para a direita, começando em `1`:
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` é a correspondência inteira, exatamente como `match.group()`, e `match.groups()` retorna todos os grupos como uma tupla. Pedir um número de grupo que não existe levanta um `IndexError`.

---

Contar parênteses para encontrar o grupo `3` cansa rápido. Um grupo pode receber um nome com `(?P<name>...)` e depois ser lido com `match.group("name")`:
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` retorna todos os grupos nomeados como um dicionário. Grupos nomeados mantêm seu número também, então `match.group(1)` ainda funciona.

O exemplo também usa um **quantificador** com chaves: `\d{2}` significa exatamente dois dígitos, `\d{2,4}` significa entre dois e quatro, e `\d{2,}` significa dois ou mais. Eles são a versão precisa de `+` (um ou mais), `*` (zero ou mais) e `?` (zero ou um).

---

Colchetes definem uma **classe de caracteres**: um conjunto de caracteres, qualquer um dos quais é aceito naquela posição. `[aeiou]` corresponde a uma vogal, `[0-9]` a um dígito e `[a-z]` a uma letra minúscula. Um `^` logo após o colchete de abertura inverte o significado, então `[^0-9]` corresponde a qualquer coisa que *não* seja um dígito.

Fora de uma classe, `^` e `$` são **âncoras**: `^` prende o padrão ao começo do texto e `$` ao final. Com `re.fullmatch` as âncoras são implícitas, e é por isso que a validação fica mais legível com ele:
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` para na primeira correspondência. `re.findall(pattern, text)` coleta **todas** as correspondências em vez disso, e as retorna como uma lista de strings:
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
A lista fica vazia quando nada corresponde, então não há `None` para verificar: é possível iterar sobre ela ou medi-la com `len(...)` direto. Note que `findall` retorna strings simples, não objetos de correspondência, então as posições não estão disponíveis.

---

Quando a posição ou os grupos de cada correspondência são necessários, `re.finditer(pattern, text)` é a chamada certa: ela percorre o texto e produz um **objeto de correspondência** para cada correspondência, uma de cada vez:
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` produz um iterador, não uma lista, então ele pode ser usado em um loop `for` ou em uma comprehension. Enquanto `findall` dá apenas o texto, `finditer` dá tudo o que um objeto de correspondência sabe.

---

`findall` muda de comportamento quando o padrão contém grupos de captura. Com exatamente um grupo, ele retorna o conteúdo desse grupo em vez da correspondência inteira, e com dois ou mais ele retorna uma tupla de grupos para cada correspondência:
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
Vale a pena lembrar: adicionar parênteses a um padrão apenas para agrupar muda silenciosamente o que `findall` retorna. `re.finditer` nunca se comporta assim, porque um objeto de correspondência sempre mantém tanto a correspondência completa quanto os grupos.

---

`re.sub(pattern, replacement, text)` retorna uma nova string na qual cada correspondência foi substituída. Strings são imutáveis, então o texto original permanece intacto:
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

A substituição pode se referir aos grupos de captura com `\1`, `\2`, ... (ou `\g<name>` para um grupo nomeado), o que torna reordenar texto uma tarefa de uma linha. A substituição também é uma raw string, pela mesma razão da barra invertida:
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
Um argumento `count` limita quantas correspondências são substituídas: `re.sub(r"\d", "#", "1 2 3", count=1)` resulta em `# 2 3`.

---

A substituição dada a `re.sub` também pode ser uma **função**. Ela é chamada uma vez por correspondência, recebe o objeto de correspondência e deve retornar a string a ser colocada em seu lugar. É assim que uma substituição pode depender do que foi correspondido:
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
A função é passada pelo nome, sem parênteses: escrever `shout(match)` a chamaria imediatamente em vez de entregá-la a `re.sub`.

---

`str.split` só consegue cortar em um separador fixo. `re.split(pattern, text)` corta em qualquer coisa que o padrão descreva, que é o que uma entrada bagunçada geralmente precisa:
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
Escrever o separador como `[,;\s]+` faz com que toda uma sequência de vírgulas, ponto e vírgula e espaços conte como um único corte, em vez de deixar strings vazias entre eles.

Um argumento `maxsplit` para depois de um determinado número de cortes, deixando o resto do texto no último elemento: `re.split(r"\s+", "a b c", maxsplit=1)` resulta em `['a', 'b c']`.

---

Cada chamada a `re.search` ou `re.findall` precisa primeiro procurar a string do padrão em um cache interno. `re.compile(pattern)` pula essa busca e retorna um **objeto de padrão** que carrega os mesmos métodos:
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
O texto é o único argumento que resta, porque o padrão já está incorporado ao objeto. Compilar compensa quando o mesmo padrão é usado muitas vezes, por exemplo dentro de um loop, e também dá ao padrão um nome que explica o que ele corresponde.

---

**Flags** mudam como um padrão é aplicado. Toda função em `re` as aceita como um argumento `flags`, e `re.compile` as armazena no objeto de padrão:
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
As duas mais usadas são `re.IGNORECASE`, que faz as letras corresponderem em qualquer caixa, e `re.MULTILINE`, que faz `^` e `$` corresponderem ao começo e ao fim de cada linha em vez do texto inteiro. Várias flags são combinadas com `|`, como em `re.IGNORECASE | re.MULTILINE`.

Uma flag muda apenas as regras de correspondência: o texto retornado é sempre o texto que realmente estava lá, com sua caixa original.
