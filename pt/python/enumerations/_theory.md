Uma **enumeração** (ou *enum*) define um tipo comum para um grupo de valores relacionados e fixos, como os dias da semana ou as cores de um semáforo.
Em vez de passar strings soltas ou números, você dá a cada valor um **nome**, para que o código fique mais legível e erros de digitação se tornem erros.
Em Python você cria uma enum importando `Enum` do módulo `enum` e declarando uma classe que herda dela.
Cada atributo de classe é um **membro** da enum, com um nome e um valor:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
Por convenção os nomes dos membros são escritos em maiúsculas. Você acessa um membro pela classe, e imprimi-lo mostra os nomes da classe e do membro:
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

Todo membro de uma enum tem dois atributos: `name`, o identificador que você escreveu na classe, e `value`, o valor que você atribuiu a ele:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
O valor pode ser de qualquer tipo, não apenas um inteiro: strings, tuplas e floats são escolhas comuns.
Um membro é um objeto normal, então você pode armazená-lo em uma variável e ler seus atributos depois:
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

Cada membro de uma enum existe **apenas uma vez**: toda vez que você escreve `Color.RED` obtém exatamente o mesmo objeto.
Por esse motivo você pode comparar membros com `is` (identidade) assim como com `==`, e ambos dão o mesmo resultado:
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
Um membro **não** é igual ao seu valor bruto, porque um membro e um número simples são coisas diferentes:
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
É isso que torna enums seguros: um `1` vindo de outro lugar do programa não pode ser confundido com `Color.RED`.

---

Uma classe enum é **iterável**: um loop `for` sobre a classe visita cada membro, na ordem em que foram declarados:
```python
for color in Color:
    print(color.name, color.value)
```
`len()` retorna quantos membros a enum tem, e `list(Color)` constrói uma lista com eles:
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
Dentro de uma lista, os membros são mostrados com seu `repr()`, que inclui o valor entre colchetes angulares.

---

Você pode obter um membro a partir do seu **valor** chamando a classe como uma função, ou a partir do seu **nome** usando colchetes:
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
Ambas são úteis quando o valor ou o nome vem de fora do programa, como um arquivo ou a entrada do usuário.
Se nada corresponder, `Color(9)` gera um `ValueError` e `Color["PINK"]` gera um `KeyError`.

---

Muitas vezes os valores exatos não importam: você só precisa que os membros sejam distintos.
Nesse caso você pode deixar o Python escolher os valores com `auto()`, também importado do módulo `enum`.
Ele atribui `1` ao primeiro membro e depois vai contando:
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

Um membro de um `Enum` simples não pode ser comparado com `<` nem somado a um número.
Quando os membros representam **níveis** que precisam de ordenação, herde de `IntEnum` em vez disso: seus membros também são inteiros, então suportam comparações, aritmética e ordenação:
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.LOW + 1)              # 2
print(int(Priority.MEDIUM))          # 2
```
Um membro de `IntEnum` também é igual ao seu valor inteiro: `Priority.LOW == 1` é `True`.

---

`StrEnum` (disponível desde o Python 3.11) é o equivalente em strings de `IntEnum`: seus membros também são strings, iguais ao seu valor.
Isso os torna convenientes em qualquer lugar onde strings simples sejam esperadas, como chaves de configuração ou parâmetros de API:
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
Ao contrário de um `Enum` simples, converter um membro de `StrEnum` em texto com `str()` ou dentro de uma f-string dá o seu **valor**, não `Mode.DARK`.

---

Uma enum é uma classe, então pode ter **métodos** e **propriedades** como qualquer outra classe.
Dentro deles, `self` é o membro no qual o método foi chamado, então você pode olhar `self.name`, `self.value` ou comparar `self` com outros membros:
```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2

    def can_go(self):
        return self is Light.GREEN

    @property
    def label(self):
        return self.name.lower()

print(Light.GREEN.can_go())  # True
print(Light.RED.label)       # red
```
Qualquer valor simples atribuído no corpo da classe se torna um membro, enquanto funções e propriedades nunca se tornam, não importa onde apareçam.

---

Se dois membros compartilham o mesmo valor, o segundo não é um novo membro, mas um **alias** do primeiro:
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
Aliases são pulados na iteração e não são contados por `len()`.
Normalmente um valor duplicado é um erro. O decorador `unique`, importado de `enum`, faz o Python gerar um `ValueError` assim que uma enum com aliases é declarada:
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

Uma `Flag` é uma enum cujos membros podem ser **combinados**: um valor pode conter vários membros ao mesmo tempo, como um conjunto de opções.
Declare seus membros com `auto()`, que para uma `Flag` atribui potências de dois (`1`, `2`, `4`, ...), para que cada combinação tenha um valor distinto:
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
Use `|` para combinar membros, `in` para verificar se um membro faz parte de uma combinação e `value` para ver o número resultante:
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

Enums combinam naturalmente com a instrução `match` (disponível desde o Python 3.10), que compara um valor com uma série de padrões `case` e executa o primeiro que corresponde:
```python
def action(light):
    match light:
        case Light.RED:
            return "Stop"
        case Light.GREEN:
            return "Go"
        case _:
            return "Slow down"
```
Sempre escreva o membro com sua classe, como `Light.RED`: um nome solto como `case RED:` não compararia nada, apenas capturaria o valor em uma nova variável `RED` e corresponderia a tudo.
O curinga `case _:` é o padrão e deve vir por último, porque qualquer padrão depois dele nunca poderia ser alcançado.

---

Membros de enum são **hashable**, então podem ser usados como chaves de dicionário e como elementos de conjunto.
Um dicionário indexado por uma enum é uma forma limpa de anexar dados a cada membro, e consultá-lo com um membro é mais seguro do que usar uma string solta que poderia estar escrita errado:
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
Como os membros podem aparecer em qualquer coleção, tudo o que você sabe sobre listas, conjuntos e comprehensions funciona com eles também:
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

O valor de um membro pode ser uma **tupla**, o que permite anexar vários dados a cada membro.
Se a enum define um método `__init__`, o Python o chama uma vez por membro, desempacotando a tupla em seus parâmetros, então você pode salvar cada dado em seu próprio atributo:
```python
from enum import Enum

class Planet(Enum):
    EARTH = (5.97, 6371)
    MARS = (0.64, 3390)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

print(Planet.MARS.radius)  # 3390
print(Planet.MARS.value)   # (0.64, 3390)
```
O `value` do membro continua sendo a tupla inteira.

---

Iterar sobre a classe e procurar membros pelo nome funcionam bem juntas quando você processa dados vindos de fora, como linhas de log ou um arquivo.
Uma dictionary comprehension sobre a classe prepara uma entrada por membro, depois `Level[name]` converte cada string recebida no membro correspondente:
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
Como a enum mantém a ordem de declaração, iterar sobre `counts` depois dá os membros nessa mesma ordem.

---

Além de métodos regulares, uma enum pode definir **métodos de classe** com `@classmethod`. Eles recebem a própria classe da enum como `cls`, então são o lugar certo para formas alternativas de encontrar um membro:
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
Junto com `auto()`, métodos, propriedades e consultas, isso permite construir enums que carregam seu próprio comportamento.
