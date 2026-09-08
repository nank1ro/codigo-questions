JavaScript tem duas maneiras diferentes de dizer "não há valor aqui".
`undefined` significa que um valor **nunca foi fornecido**. Uma variável declarada sem valor contém `undefined`, e o mesmo acontece com uma propriedade que não existe em um objeto:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` é um valor que **você** atribui de propósito para dizer "vazio, e eu sei disso":
```javascript
let owner = null;
console.log(owner);
// prints null
```
Assim, `undefined` geralmente é a linguagem informando que algo está faltando, enquanto `null` é o programador afirmando que algo está intencionalmente vazio.

---

Funções produzem `undefined` em mais duas situações.
Quando você chama uma função com **menos argumentos** do que ela declara, os parâmetros ausentes contêm `undefined`:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
Quando uma função termina **sem um `return`** (ou com um simples `return;`), chamá-la resulta em `undefined`:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
Observe que passar `null` explicitamente não é o mesmo que omitir o argumento: `greet(null)` imprime `null`, porque `null` é um valor real que foi entregue à função.

---

O operador `typeof` retorna o tipo de um valor como uma string. Para `undefined` ele responde `"undefined"`, como você esperaria:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
Para `null`, porém, ele responde `"object"`. Este é um bug da primeiríssima versão de JavaScript que nunca foi corrigido, porque código demais depende dele:
```javascript
console.log(typeof null);
// prints object
```
Portanto, `typeof` é uma maneira confiável de detectar `undefined`, mas não `null`. Para verificar `null`, compare diretamente com ele: `value === null`.

---

Como `null` e `undefined` se comparam entre si? Depende do operador.
A igualdade **frouxa** `==` os trata como a mesma coisa, e os considera diferentes de qualquer outro valor, incluindo `0`, `""` e `false`:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
A igualdade **estrita** `===` também compara o tipo, e `null` e `undefined` têm tipos diferentes:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

Na maioria das vezes você não se importa *qual* dos dois marcadores de "sem valor" você recebeu: você só quer saber se há um valor.
Como `null == undefined` é `true` e nada mais é frouxamente igual a `null`, a comparação `value == null` é a construção idiomática padrão para capturar **ambos** de uma vez:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
Este é o único caso em que `==` é preferível a `===`: escrever `value === null || value === undefined` faz exatamente o mesmo trabalho, apenas mais longo.
Valores como `0`, `""` e `false` *não* são `null`: são valores reais que por acaso são falsy.

---

Ler uma propriedade de `null` ou `undefined` é um erro que interrompe o programa:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` é `undefined`, e `undefined` não tem propriedades. O operador de **encadeamento opcional** (optional chaining) `?.` resolve isso: se o valor à sua esquerda for `null` ou `undefined`, a expressão inteira para e avalia como `undefined` em vez de lançar um erro:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
Quando o lado esquerdo tem um valor, `?.` se comporta exatamente como um `.` normal. Você pode encadear vários: `user.address?.street?.name` retorna `undefined` assim que qualquer elo estiver faltando.

---

O encadeamento opcional não se limita a propriedades com ponto. Há mais duas formas.
`?.[]` lê um elemento ou uma chave computada apenas quando o lado esquerdo tem um valor:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` chama uma função apenas quando ela existe, o que é útil para callbacks opcionais:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
Em todas as formas, a verificação se aplica ao valor **imediatamente antes** do `?.`: `post?.tags?.[0]` é seguro mesmo quando o próprio `post` é `null` ou `undefined`.

---

Quando você sabe que um valor pode estar ausente, geralmente quer um **padrão** em seu lugar. Dois operadores fazem isso, e eles diferem no que consideram "ausente".
`a || b` retorna `b` sempre que `a` for **falsy**: não apenas `null` e `undefined`, mas também `0`, `""`, `false` e `NaN`.
O operador de **coalescência nula** (nullish coalescing) `a ?? b` retorna `b` apenas quando `a` é `null` ou `undefined`, e mantém qualquer outro valor:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
Use `??` quando `0`, `""` ou `false` forem valores legítimos que devem ser mantidos, e `||` quando você realmente quiser substituir todo valor falsy.

---

Um padrão muito comum é "preencher esta propriedade apenas se ela ainda não estiver definida". Escrito com `??`, ele repete o nome:
```javascript
options.timeout = options.timeout ?? 1000;
```
O operador de **atribuição nula** (nullish assignment) `??=` faz o mesmo em um passo: ele atribui o lado direito apenas quando o lado esquerdo está atualmente `null` ou `undefined`, e deixa qualquer outro valor intocado:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` permanece `0` porque `0` não é nullish; `timeout` não existia, então recebe `1000`. A mesma ideia existe para `||` como `||=`, que sobrescreve todo valor falsy.

---

Um **parâmetro padrão** dá a um parâmetro um valor quando quem chama não fornece um. A regra é precisa: o padrão é usado apenas quando o argumento é `undefined`, o que inclui omiti-lo. Passar `null` **não** aciona o padrão, porque `null` é um valor:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
Parâmetros padrão seguem a regra do `undefined`, enquanto `??` cobre tanto `null` quanto `undefined`: escolha o que corresponder à forma como sua função será chamada.

---

O encadeamento opcional e a proteção `== null` funcionam bem juntos: o encadeamento lê o valor aninhado sem lançar erro, e a proteção decide o que fazer quando o resultado está ausente:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
Dentro do último `return` um `.` simples é seguro, porque a proteção já provou que todos os elos existem.

---

Muitos métodos embutidos relatam "nada encontrado" retornando `undefined`. O método de array `find(callback)` é o exemplo típico: ele retorna o primeiro elemento para o qual o callback é `true`, ou `undefined` quando nenhum elemento corresponde:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
Ler `found.price` aqui lançaria um erro, então `?.` e `??` são os companheiros naturais do `find`:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null` e `undefined` se comportam de forma diferente quando um objeto é convertido para JSON com `JSON.stringify()`.
JSON tem um valor `null` mas não tem `undefined`, então uma propriedade cujo valor é `undefined` é simplesmente **omitida**, enquanto uma propriedade `null` é mantida:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
Dentro de arrays as posições não podem desaparecer, então `undefined` se torna `null` lá:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

Verificar `obj.key === undefined` não consegue distinguir duas situações: a propriedade não existe, ou ela existe e contém o valor `undefined`.
`Object.hasOwn(obj, key)` responde apenas à primeira pergunta: ele retorna `true` quando o objeto tem sua **própria** propriedade chamada `key`, seja qual for seu valor:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
"Própria" significa declarada no próprio objeto: membros herdados como `toString` estão disponíveis em todo objeto, mas `Object.hasOwn(config, "toString")` é `false`.
