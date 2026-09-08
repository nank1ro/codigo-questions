Uma **enumeração** (ou *enum*) é um tipo comum para um pequeno grupo de valores relacionados e fixos: os dias da semana, os naipes de um baralho, os possíveis estados de um pedido.
Diferentemente de muitas linguagens, o JavaScript **não** possui a palavra-chave `enum`. O substituto idiomático é um objeto simples cujas propriedades são os membros, passado para `Object.freeze()` para que ninguém possa alterá-lo depois:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
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
// prints done
```
Uma vez congelado, o objeto também não pode receber novas propriedades, e `Object.isFrozen(obj)` informa se um objeto foi congelado:
```javascript
console.log(Object.isFrozen(Status));
// prints true
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
// prints s
console.log(Size.MEDIUM);
// prints undefined
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
// prints true
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
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
Combinar `Object.values()` com o método de array `includes()` é a forma padrão de verificar se um valor arbitrário, por exemplo um lido da entrada do usuário, é um membro válido:
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```
