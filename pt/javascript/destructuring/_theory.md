Ler valores de um array um índice por vez é trabalhoso:
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
A **desestruturação** faz o mesmo trabalho em uma linha. À esquerda de `=` você escreve um padrão que se parece com o próprio array, e cada nome dentro dele recebe o elemento na mesma posição:
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// imprime 3 7
```
O padrão não precisa cobrir o array inteiro: elementos extras são simplesmente ignorados, e um nome sem elemento correspondente se torna `undefined`.

---

A desestruturação é mais útil bem onde um array chega: um argumento de função, ou o resultado de uma chamada. Em vez de manter o array por perto e indexá-lo em todo lugar, você o desempacota uma vez e dá às partes nomes reais:
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// imprime 5
```
Nada é copiado ou alterado no array original, o padrão apenas lê a partir dele.

---

Às vezes apenas um elemento no fundo do array importa. Você pode deixar uma posição vazia no padrão, mantendo a vírgula que a separa: essa posição vazia é chamada de **buraco**, e ela pula o elemento sem dar nome a ele:
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// imprime 64
```
Conte as vírgulas, não os nomes: cada vírgula move o padrão uma posição para frente, haja ou não um nome antes dela.

---

Um array nem sempre é tão longo quanto o padrão espera. Escrever `= value` após um nome dá a ele um **valor padrão** (default), usado sempre que o array não tem nada naquela posição:
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// imprime 1920 1080
```
O valor padrão é avaliado apenas quando é necessário, então pode até ser uma chamada de função, e um valor padrão pode ser dado a qualquer posição, não apenas à última.

---

Um padrão também pode ficar à esquerda de uma atribuição simples, sem `const` ou `let` na frente, e então ele escreve em variáveis que já existem. Isso transforma a troca de dois valores em uma única linha, sem variável temporária:
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// imprime 2 1
```
O lado direito é construído primeiro, então ambos os valores antigos já estão seguros dentro do array temporário quando a atribuição acontece. Atenção ao ponto e vírgula na linha anterior: uma linha que começa com `[` seria lida como um índice do que veio antes.

---

Objetos também podem ser desestruturados, com chaves em vez de colchetes. Aqui a posição não significa nada: cada nome é comparado com a **chave** de mesma grafia:
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// imprime Ada 36
```
Trocar `age` e `name` de lugar no padrão não muda nada, e chaves que o padrão não menciona são simplesmente deixadas de lado. Um nome sem chave correspondente se torna `undefined`.

---

Padrões de objeto e valores padrão se combinam exatamente como os de array, o que os torna uma forma organizada de ler um objeto de configuração cujas chaves podem ou não estar lá:
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// imprime dark en
```
Como o padrão inteiro é uma única instrução, uma função pode desempacotar tudo o que precisa do seu argumento já na sua primeira linha.

---

Um padrão de objeto nomeia suas variáveis de acordo com as chaves, o que é desconveniente quando as chaves são crípticas ou já estão em uso. Escrever `key: newName` **renomeia** a variável:
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// imprime Ada 1815
```
Leia como "pegue `n`, chame de `name`". Os dois-pontos não declaram um tipo, e `n` em si nunca é criado como variável, apenas `name` é. Um nome renomeado ainda pode receber um valor padrão, escrito depois dele: `{ n: name = "unknown" }`.

---

Valores padrão têm uma regra que surpreende todo mundo: eles se aplicam **apenas** a `undefined`. Uma chave que existe e contém `null`, `0`, `""` ou `false` é um valor real, então o padrão a recebe e o valor padrão nunca é usado:
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// imprime 0
```
`null` se comporta da mesma forma que `0` aqui, embora muitas vezes signifique "sem valor" em uma resposta de API. Quando `null` também deve ser substituído, desestruture primeiro e recorra ao `??` depois.

---

Quando uma chave contém outro objeto ou um array, o padrão pode simplesmente continuar e descrever essa forma também:
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// imprime London
```
Cuidado com o que essa linha cria: `address: { city }` significa "entre em `address`", não "me dê `address`", então apenas `city` se torna uma variável. Para obter ambos, mencione a chave duas vezes: `const { address, address: { city } } = user;`. Padrões de array e de objeto se aninham livremente entre si, como em `{ tags: [first] }`.

---

Pegar a cabeça de um array e manter a cauda é uma necessidade tão comum que os padrões têm uma sintaxe própria para isso. Três pontos na frente do último nome o tornam um **elemento rest**, e ele coleta todos os elementos restantes em um novo array:
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// imprime a [ 'b', 'c' ]
```
Um elemento rest deve vir por último no padrão e não pode ter um valor padrão: quando nada sobra, ele é simplesmente um array vazio.

---

Padrões de objeto também têm um rest, e nele ele coleta todas as chaves que o padrão não mencionou em um novo objeto:
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// imprime { name: 'Ada', city: 'London' }
```
Esta é a forma mais curta de construir uma cópia de um objeto sem uma de suas chaves: o original nunca é tocado, e o objeto rest é um novo contendo os valores restantes.

---

Um padrão pode substituir o nome de um parâmetro em uma declaração de função, de modo que o desempacotamento acontece no momento da chamada:
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// imprime 12
```
Dentro do corpo não há nenhuma variável de objeto, apenas `width` e `height`. Quem chama passa um objeto, mas a assinatura documenta exatamente quais chaves a função lê, e as chaves podem chegar em qualquer ordem.

---

Um parâmetro desestruturado com valores padrão forma um objeto de opções elegante, mas ainda quebra quando quem chama não passa nada: ler uma chave de `undefined` lança um `TypeError`. Dar ao padrão inteiro um valor padrão `{}` resolve isso:
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// imprime guest/false
```
Leia a linha de fora para dentro: `= {}` fornece um objeto vazio quando o argumento está ausente, e cada valor padrão interno então preenche sua própria chave.

---

`Object.entries(obj)` transforma um objeto em um array de pares `[key, value]`. Coloque um padrão de array no cabeçalho de um loop `for...of` e cada par é desempacotado conforme o loop executa:
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// imprime ada is 36
// imprime bob is 41
```
Esta é a forma legível de percorrer um objeto: sem índice, sem busca, apenas os dois nomes que interessam. `Object.keys` e `Object.values` dão apenas um lado cada, `Object.entries` dá ambos.

---

Tudo o que foi visto até agora pertence a uma única sintaxe, então as peças se combinam livremente: um padrão de objeto pode aninhar outro padrão de objeto, que pode conter uma chave renomeada com um valor padrão, ao lado de um padrão de array terminando em um elemento rest. Uma linha então descreve toda a forma que uma função espera:
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// imprime Post [js] +2
```
Mantenha legível: um padrão que não cabe mais em um par de linhas é geralmente um sinal de que a função está pedindo demais.
