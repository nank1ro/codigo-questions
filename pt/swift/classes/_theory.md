Swift é uma linguagem de programação orientada a objetos, o que significa que ela manipula construções de programação chamadas objetos.
Você pode pensar em um objeto como uma única estrutura de dados que contém dados e também funções; as funções de um objeto são chamadas de seus métodos.
Por exemplo, quando você chama:
```swift
dictName.removeValue(forKey: "keyName")
```
Swift verifica se `dictName` tem um método `removeValue()` (que todos os dicionários possuem) e executa esse método se o encontrar.

---

_Estruturas_ e _classes_ são construções flexíveis e de propósito geral que se tornam os blocos de construção do código do seu programa.
Uma classe|struct básica consiste apenas na palavra-chave `class` ou `struct` e seu nome, por exemplo:
```swift
class ClassName {
    // class definition
}
struct ClassName {
    // structure definition
}
```

---

Vamos colocar algo dentro da nossa classe `Animal`

---

Definir uma classe não cria um objeto.
Para fazer isso, precisamos criar uma __instância__ de uma classe

---

Quando uma classe possui suas próprias funções, essas funções são chamadas de __métodos__.

---

Estruturas e classes em Swift têm muitas coisas em comum. Ambas podem:
- Definir propriedades para armazenar valores
- Definir métodos para fornecer funcionalidade
- Definir subscripts para fornecer acesso aos seus valores usando a sintaxe de subscript
- Definir inicializadores para configurar seu estado inicial
- Ser estendidas para expandir sua funcionalidade além de uma implementação padrão
- Conformar-se a protocolos para fornecer funcionalidade padrão de um determinado tipo

Mas as classes têm capacidades adicionais que as estruturas não possuem:
- Herança permite que uma classe herde as características de outra
- Conversão de tipo permite verificar e interpretar o tipo de uma instância de classe em tempo de execução
- Desinicializadores permitem que uma instância de classe libere quaisquer recursos que tenha atribuído
- Contagem de referência permite mais de uma referência a uma instância de classe

---

Você pode acessar as propriedades de uma instância usando a _sintaxe de ponto_.
Na sintaxe de ponto, você escreve o nome da propriedade imediatamente após o nome da instância, separados por um ponto `.`, sem espaços:
```swift
someInstance.someProperty
```
Usando a mesma sintaxe, também podemos atualizar o valor de uma propriedade

---

Uma vantagem das estruturas é que possuem um inicializador memberwise gerado automaticamente, que você pode usar para inicializar as propriedades de membro de novas instâncias da estrutura.
Os valores iniciais para as propriedades da nova instância podem ser passados para o inicializador memberwise pelo nome
