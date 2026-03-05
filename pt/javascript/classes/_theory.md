JavaScript é uma linguagem de programação orientada a objetos, o que significa que ela manipula construções de programação chamadas objetos.
Você pode pensar em um objeto como uma única estrutura de dados que contém dados e também funções; as funções de um objeto são chamadas de métodos.
Por exemplo, quando você chama:
```javascript
arrayName.push("value");
```
JavaScript verifica se `arrayName` possui um método `push()` (que todos os arrays possuem) e executa esse método se o encontrar.

---

_Classes_ são construções flexíveis e de uso geral que se tornam os blocos de construção do código do seu programa.
Uma classe básica consiste apenas na palavra-chave `class` e seu nome, por exemplo:
```javascript
class ClassName {
    // class definition
}
```

---

Vamos colocar algo dentro da nossa classe `Animal`
Para adicionar alguns parâmetros, precisamos usar o `constructor` padrão

---

Definir uma classe não cria um objeto.
Para fazer isso, precisamos criar uma __instância__ de uma classe.
Em JavaScript, para criar uma nova instância de uma classe, sempre usamos a palavra-chave `new` antes do nome da classe.
Se você quiser atribuir um valor padrão a um parâmetro, faça isso na lista de nomes de parâmetros do constructor

---

Quando uma classe possui suas próprias funções, essas funções são chamadas de __métodos__.

---

JavaScript nos permite criar uma classe como filha de outra, usando a palavra-chave `extends`

---

Você pode acessar as propriedades de uma instância usando a _sintaxe de ponto_.
Na sintaxe de ponto, você escreve o nome da propriedade imediatamente após o nome da instância, separado por um ponto `.`, sem espaços:
```javascript
someInstance.someProperty
```
Usando a mesma sintaxe, também podemos atualizar o valor de uma propriedade
