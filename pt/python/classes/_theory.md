Python é uma linguagem de programação orientada a objetos, o que significa que ela manipula construções de programação chamadas objetos.
Você pode pensar em um objeto como uma única estrutura de dados que contém dados e também funções; as funções de um objeto são chamadas de seus métodos.
Por exemplo, quando você chama:
```python
dict_name.items()
```
Python verifica se `my_dict` possui um método `items()` (que todos os dicionários possuem) e executa esse método se encontrá-lo.

---

Uma classe básica consiste apenas na palavra-chave `class` e no nome da classe, por exemplo:
```python
class ClassName:
    pass
```

---

Vamos substituir `pass` por outra coisa.
O método `__init__()` é obrigatório para classes, e é usado para __inicializar__ os objetos que ele cria.
`__init__()` sempre recebe pelo menos um argumento, `self`, que se refere ao objeto que está sendo criado.
Você pode pensar em `__init__()` como o método que inicializa cada objeto que a classe cria.

---

Claro, o método `__init__()` pode usar mais parâmetros além de `self`

---

O primeiro argumento de `__init__()` é usado para se referir ao objeto instância, e por convenção, esse argumento é chamado de `self`.
Se você adicionar argumentos adicionais (por exemplo, `gender` e `legs` para o seu animal), definir cada um deles igual a `self.gender` e `self.legs` no corpo de `__init__()` fará com que, ao criar um objeto instância da sua classe `Animal`, você precise fornecer a cada instância um gender e legs, e esses serão associados à instância específica que você criar

---

Definir uma classe não cria um objeto.
Para fazer isso, precisamos criar uma __instância__ de uma classe

---

Quando uma classe tem suas próprias funções, essas funções são chamadas de __métodos__. Você já viu um desses métodos: `__init__()`.
Mas você também pode definir seus próprios métodos!
