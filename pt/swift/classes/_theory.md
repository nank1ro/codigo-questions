Swift e uma linguagem de programacao orientada a objetos, o que significa que ela manipula construcoes de programacao chamadas objetos.
Voce pode pensar em um objeto como uma unica estrutura de dados que contem dados bem como funcoes; as funcoes de um objeto sao chamadas de seus metodos.
Por exemplo, quando voce chama:
```swift
dictName.removeValue(forKey: "keyName")
```
Swift verifica se `dictName` tem um metodo `removeValue()` (que todos os dicionarios tem) e executa esse metodo se o encontrar.

---

_Estruturas_ e _classes_ sao construcoes de proposito geral, flexiveis que se tornam os blocos de construcao do codigo do seu programa.
Uma classe|estrutura basica consiste apenas na palavra-chave `class` ou `struct` e seu nome, por exemplo:
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

Definir uma classe nao cria um objeto.
Para fazer isso, precisamos criar uma __instancia__ de uma classe

---

Quando uma classe tem suas proprias funcoes, essas funcoes sao chamadas de __metodos__.

---

Estruturas e classes em Swift tem muitas coisas em comum. Ambas podem:
- Definir propriedades para armazenar valores
- Definir metodos para fornecer funcionalidade
- Definir subscritos para fornecer acesso aos seus valores usando sintaxe de subscrito
- Definir inicializadores para configurar seu estado inicial
- Ser estendidas para expandir sua funcionalidade alem de uma implementacao padrao
- Conformar com protocolos para fornecer funcionalidade padrao de um certo tipo

Mas as classes tem capacidades adicionais que as estruturas nao tem:
- Heranca permite que uma classe herde as caracteristicas de outra
- Type casting permite que você verifique e interprete o tipo de uma instancia de classe em tempo de execucao
- Deinitializers permitem que uma instancia de classe libere quaisquer recursos que ela atribuiu
- Reference counting permite mais de uma referencia a uma instancia de classe

---

Voce pode acessar as propriedades de uma instancia usando a _sintaxe de ponto_.
Na sintaxe de ponto, voce escreve o nome da propriedade imediatamente apos o nome da instancia, separado por um ponto `.`, sem espacos:
```swift
someInstance.someProperty
```
Usando a mesma sintaxe, tambem podemos atualizar o valor de uma propriedade

---

Uma vantagem das estruturas e que elas possuem um inicializador memberwise gerado automaticamente, que voce pode usar para inicializar as propriedades dos membros de novas instancias de estrutura.
Valores iniciais para as propriedades da nova instancia podem ser passados para o inicializador memberwise por nome
