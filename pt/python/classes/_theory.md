Python é uma linguagem de programação orientada a objetos, o que significa que ela manipula construtos de programação chamados objetos.
Você pode pensar em um objeto como uma única estrutura de dados que contém dados bem como funções; as funções de um objeto são chamadas de seus métodos.
Por exemplo, quando você chama:
```python
dict_name.items()
```
Python verifica se `my_dict` tem um método `items()` (que todos os dicionários têm) e executa esse método se o encontrar.

---

A basic class consists only of the `class` keyword and the name of the class, for example:
```python
class ClassName:
    pass
```

---

Vamos substituir `pass` por outra coisa.
O método `__init__()` é necessário para classes, e é usado para __inicializar__ os objetos que ele cria.
`__init__()` sempre leva pelo menos um argumento, `self`, que se refere ao objeto sendo criado.
Você pode pensar em `__init__()` como o método que inicia cada objeto que a classe cria.

---

É claro que o método `__init__()` pode usar mais parâmetros além de `self`

---

O primeiro argumento `__init__()` é usado para se referir ao objeto de instância, e por convenção, esse argumento é chamado de `self`.
Se você adicionar argumentos adicionais (por exemplo, `gender` e `legs` para seu animal) definindo cada um desses como `self.gender` e `self.legs` no corpo de `__init__()`, fará com que, quando você criar um objeto de instância da sua classe `Animal`, precise dar a cada instância um gender e legs, e esses serão associados à instância específica que você criar

---

Definir uma classe não cria um objeto.
Para fazer isso, precisamos criar uma __instância__ de uma classe
