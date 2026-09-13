Você já sabe que `extends` torna uma classe filha de outra. O que essa palavra-chave realmente lhe dá é **herança**: a filha recebe de graça todas as propriedades e métodos do pai, e pode adicionar os seus próprios por cima.

A peça que torna a herança útil é o **`super`**. Dentro do construtor de uma filha, `super(...)` chama o construtor do pai, para que o pai possa configurar a parte do objeto que lhe pertence:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
Aqui `super(name)` entrega `name` para `Animal`, que o armazena, e `Dog` só precisa se preocupar com `breed`.

---

Uma classe filha não precisa redefinir nada que o pai já forneça. Os métodos também são herdados, então uma instância da filha pode chamá-los como se fossem seus:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// prints Max makes a sound
```
Quando uma filha declara o seu próprio construtor, chamar `super(...)` nele é **obrigatório**: sem isso o objeto nunca é inicializado e o JavaScript lança um `ReferenceError`. Uma filha sem construtor algum não tem problema, porque o JavaScript escreve um que repassa todos os argumentos ao pai.

---

A regra sobre `super()` é mais rigorosa do que "chame-o em algum lugar". No construtor de uma filha, a palavra `this` não existe até que `super()` tenha executado, porque é o construtor do pai que cria o objeto. Tocar em `this` antes dessa linha lança um erro:
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
Portanto, `super(...)` deve ser a **primeira instrução** de qualquer construtor de filha que use `this`.

---

Quando uma filha define um método que o pai já tem, a versão da filha vence. Isso é chamado de **sobrescrita**:
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// prints Woof
```
A sobrescrita não apaga a versão do pai, apenas a esconde. Dentro do método da filha, `super.methodName(...)` ainda alcança a versão do pai, o que permite estender o comportamento do pai em vez de substituí-lo:
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// prints Woof!
```
Note a diferença: `super(...)` chama o **construtor** do pai, `super.name(...)` chama um **método** do pai.

---

Até agora, toda propriedade era criada dentro do construtor. Um **campo de classe** permite declará-la diretamente no corpo da classe, com um valor inicial opcional:
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// prints 0
```
Os campos são atribuídos a cada nova instância antes de o corpo do construtor executar, então o construtor já pode contar com eles. Um campo sem valor ainda é declarado, apenas começa como `undefined`:
```javascript
class Task {
    done = false;
    title;
}
```
Note a sintaxe: sem `let`, sem `const`, sem `this` na declaração, e a linha termina com ponto e vírgula.

---

A ordem importa quando as classes herdam umas das outras. Uma declaração `class` **não** sofre hoisting da forma como uma `function` sofre: o nome só existe a partir da linha em que a classe é escrita em diante. Portanto, uma classe filha precisa aparecer *depois* do pai que ela estende, caso contrário a cláusula `extends` falha com um `ReferenceError`.

---

Alguns comportamentos pertencem à própria classe, e não a qualquer instância individual. Uma conversão entre duas unidades, por exemplo, não precisa de um objeto sobre o qual trabalhar. Marcar um método como **`static`** o coloca na classe:
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// prints 8
```
Um método estático é chamado no nome da classe, nunca em uma instância: `new MathUtils().double(4)` lança um `TypeError`, porque as instâncias não recebem membros estáticos. Dentro de um método estático, `this` se refere à classe, então um estático pode chamar outro com `this.otherStatic(...)`.

---

`static` funciona em campos também. Uma **propriedade estática** é armazenada uma única vez na classe, e não uma vez por instância, o que a torna o lugar natural para um contador compartilhado ou uma constante:
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// prints 3.14
```
Como há apenas uma cópia, toda instância que a atualiza atualiza o mesmo valor. Dentro de um construtor, você a acessa por meio do nome da classe, `Circle.PI`, e não por meio de `this`: `this.PI` procuraria uma propriedade na instância, não encontraria nada e lhe daria `undefined`.

---

Um uso muito comum de um método estático é uma **fábrica**: um método que constrói uma instância a partir de algum outro formato de dados e a retorna. Ele mantém o `new` em um só lugar e dá à construção um nome que diz o que ela faz:
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// prints 120
```
Uma fábrica pode ser chamada antes que qualquer instância exista, o que um método normal não poderia.

---

Um **getter** é um método que é lido como uma propriedade. Escreva `get` na frente dele e omita os parênteses no local da chamada:
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// prints 12
```
`r.area` executa o método e devolve o seu resultado, então é um número. Adicionar parênteses tentaria chamar esse número, o que falha.

O oposto é um **setter**, declarado com `set`, que executa quando a propriedade é atribuída. Ele recebe exatamente um parâmetro:
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

O verdadeiro valor de um setter é que ele pode recusar. Entre a atribuição e o valor armazenado, você tem a chance de verificar, limitar ou rejeitar o que chega:
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// prints 3, the setter rejected 50
```
Um getter e um setter com o mesmo nome formam uma única propriedade, então eles não podem também ser um campo normal: o valor armazenado vive sob um nome diferente, por convenção o mesmo nome com um sublinhado na frente.

---

O sublinhado no início de `_temperature` é apenas uma convenção: nada impede o mundo exterior de escrever `v._level = 999` e passar direto pelo seu setter. Um **campo privado** é imposto pela linguagem. O seu nome começa com `#`, ele deve ser declarado no corpo da classe e só pode ser lido ou escrito de dentro dessa classe:
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// prints 1234
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
Dois detalhes são fáceis de tropeçar. O `#` faz parte do nome, então você sempre escreve `this.#code`, nunca `this.code`. E um campo privado não aparece em `Object.keys` nem no `console.log` da instância.

---

Os métodos também podem ser privados. Coloque `#` na frente do nome e o método desaparece da superfície pública da classe, continuando chamável a partir de qualquer outro método com `this.#name(...)`:
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// prints $7
```
É assim que você mantém os passos auxiliares fora da API: quem chama vê `print`, não o detalhe de formatação por trás dele. Campos privados e métodos privados, juntos, dão a uma classe um dentro e um fora bem definidos.

---

Imprimir um objeto geralmente dá algo inútil. Sempre que o JavaScript precisa de uma string e recebe um objeto em vez disso, ele chama o método **`toString`** do objeto, e o padrão retorna `[object Object]`. Definir o seu próprio substitui isso:
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// prints $7
```
O mesmo método é usado pela concatenação de strings e por `String(value)`. Se você também quiser um **número** sensato, defina `[Symbol.toPrimitive](hint)`, que recebe `"string"`, `"number"` ou `"default"` e decide o que retornar; quando existe, ele vence o `toString`.

---

O operador **`instanceof`** pergunta se um objeto foi construído a partir de uma classe, ou a partir de qualquer classe que herde dela:
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
O JavaScript não tem uma palavra-chave `abstract`, mas a mesma ideia é escrita à mão: uma classe base define a forma e todo método que uma filha *deve* fornecer simplesmente lança um erro:
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
Uma filha que se esquece de sobrescrever `area` falha ruidosamente na primeira vez em que é usada, em vez de retornar `undefined` silenciosamente.

---

`for...of` e o operador spread `...` não funcionam em qualquer objeto: eles funcionam em **iteráveis**, objetos que fornecem um método armazenado sob a chave especial `Symbol.iterator`. Dê esse método à sua classe e ela entra no clube:
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// prints [ 'a', 'b' ]
```
O `*` na frente do nome o torna um **generator**: uma função que entrega valores um de cada vez com `yield` e pausa entre eles. Essa é a maneira mais curta de satisfazer o protocolo de iteração, e ela funciona para valores que são computados em vez de armazenados.
