Uma **enumeração** (ou *enum*) é um tipo comum para um pequeno grupo de valores relacionados e fixos: os dias da semana, os naipes de um baralho, os possíveis estados de um pedido.
Diferentemente de muitas linguagens, o JavaScript **não** possui a palavra-chave `enum`. O substituto idiomático é um objeto simples cujas propriedades são os membros, passado para `Object.freeze()` para que ninguém possa alterá-lo depois:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// imprime red
```
Por convenção, o objeto é declarado com `const`, seu nome começa com letra maiúscula e os nomes dos membros são escritos em `UPPER_CASE`, exatamente como as outras constantes.

---

O valor armazenado em cada membro fica a seu critério. **Strings** são a escolha mais comum porque são legíveis quando impressas, registradas em log ou salvas em um arquivo:
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// imprime done
```
Uma vez congelado, o objeto também não pode receber novas propriedades, e `Object.isFrozen(obj)` informa se um objeto foi congelado:
```javascript
console.log(Object.isFrozen(Status));
// imprime true
```

---

Afinal, por que congelar o objeto? Um objeto congelado rejeita qualquer alteração: atribuir a um membro existente, adicionar um novo ou excluir um não tem efeito algum.
A forma como a rejeição se manifesta depende do modo em que seu código é executado:
- no **modo não estrito** (sloppy mode, o padrão para scripts simples) a atribuição é **silenciosamente ignorada**
- no **modo estrito** (strict mode, arquivos que começam com `"use strict"`, módulos ES e corpos de classe) ela **lança** um `TypeError`

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// imprime s
console.log(Size.MEDIUM);
// imprime undefined
```
De qualquer forma, a enumeração mantém os valores que você definiu, que é exatamente o que se espera de um conjunto de constantes.

---

Os membros também podem conter **números**. Valores numéricos são úteis quando os membros têm uma ordem natural, pois é possível compará-los com os operadores usuais:
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// imprime true
```
A contrapartida é a legibilidade: imprimir `Priority.HIGH` mostra `3`, o que informa muito menos do que a string `"high"` informaria.

---

Como uma enumeração é apenas um objeto, os utilitários de objeto de sempre permitem inspecioná-la:
- `Object.keys(Enum)` retorna um array com os **nomes** dos membros
- `Object.values(Enum)` retorna um array com os **valores** dos membros
- `Object.entries(Enum)` retorna um array de pares `[nome, valor]`

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// imprime [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// imprime [ 'red', 'blue' ]
```
Combinar `Object.values()` com o método de array `includes()` é a forma padrão de verificar se um valor arbitrário, por exemplo um lido da entrada do usuário, é um membro válido:
```javascript
console.log(Object.values(Color).includes("red"));
// imprime true
console.log(Object.values(Color).includes("pink"));
// imprime false
```

---

As enumerações combinam naturalmente com a instrução `switch`, que compara um valor com uma lista de rótulos `case` e executa o código do primeiro que corresponder.
Cada ramo termina com `return` ou `break`, e o ramo opcional `default` é executado quando nada corresponde:
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// imprime go
```
Sempre compare com os membros (`Light.RED`), nunca com os valores brutos (`"red"`): se o valor mudar algum dia, o `switch` continua funcionando.

---

Ir de um valor de volta ao nome do seu membro é chamado de **busca reversa**. Percorra os nomes com `Object.keys()` e escolha o primeiro cujo valor corresponda, usando o método de array `find()`, que retorna o primeiro elemento para o qual o callback é `true` (ou `undefined` se nenhum for encontrado):
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// imprime HIGH
```
`Priority[key]` lê o membro cujo nome está armazenado na variável `key`, a mesma notação de colchetes usada para qualquer objeto.

---

Membros do tipo string têm uma fraqueza: qualquer string com o mesmo texto é aceita como membro.
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// imprime true
```
Quando você quiser membros que sejam iguais **apenas** a si mesmos, use um `Symbol`. `Symbol(description)` cria um valor totalmente novo, diferente de qualquer outro símbolo, mesmo um criado com a mesma descrição:
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// imprime true
console.log(Suit.HEARTS === Symbol("hearts"));
// imprime false
console.log(typeof Suit.HEARTS);
// imprime symbol
```
O texto que você passa é apenas um rótulo para depuração; você pode lê-lo de volta com a propriedade `description` (`Suit.HEARTS.description` é `"hearts"`).

---

Os valores de uma enumeração costumam ser usados como **chaves** de outro objeto, por exemplo para mapear cada membro a um rótulo ou a um preço. Dentro de um objeto literal, envolver uma chave em colchetes `[ ]` avalia a expressão e usa seu resultado como chave (uma **chave computada**). Isso funciona tanto com membros do tipo string quanto do tipo symbol:
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// imprime Completed
```
Sem os colchetes, `Status.DONE: "Completed"` seria um erro de sintaxe, e `"Status.DONE"` seria apenas uma chave string comum.

---

Quando cada membro precisa de várias informações ou de métodos próprios, uma **classe** pode desempenhar o papel da enumeração. Cada membro é uma instância da classe, armazenada em uma propriedade `static`, ou seja, uma propriedade que pertence à própria classe em vez de a cada instância:
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// imprime Earth
```
Chame `Object.freeze(Planet)` depois da classe para impedir que alguém adicione ou substitua membros, e congele cada instância no construtor com `Object.freeze(this)` para que os próprios membros permaneçam somente leitura.
