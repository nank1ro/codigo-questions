Uma **expressão regular** (ou **regex**) é um pequeno padrão que descreve uma forma de texto. Você a usa para responder perguntas como "esta string contém um número?" ou "onde aparece a palavra `cat`?".

Em JavaScript a forma mais curta de escrever uma é um **regex literal**: o padrão entre duas barras.
```javascript
const pattern = /cat/;
```
Caracteres comuns em um padrão correspondem a si mesmos, então `/cat/` corresponde às três letras `c`, `a`, `t` em qualquer lugar dentro de uma string.

A coisa mais simples que você pode fazer com um padrão é perguntar se ele aparece em uma string. O método **`test`** recebe o texto e retorna `true` ou `false`:
```javascript
console.log(/cat/.test("the cat sleeps"));
// imprime true
console.log(/cat/.test("the dog sleeps"));
// imprime false
```
Note que `test` procura o padrão *em algum lugar* da string; a string inteira não precisa corresponder.

---

Os padrões se tornam úteis quando descrevem um *tipo* de caractere em vez de um caractere exato. Algumas **sequências de escape** cobrem a maioria das necessidades:
- `\d` qualquer dígito, de `0` a `9`
- `\w` qualquer caractere de palavra: uma letra, um dígito ou `_`
- `\s` qualquer espaço em branco: um espaço, uma tabulação, uma quebra de linha

```javascript
console.log(/\d/.test("room 12"));
// imprime true
console.log(/\d/.test("lobby"));
// imprime false
```
Um **quantificador** diz quantas vezes o trecho anterior pode se repetir. O mais comum é `+`, que significa "um ou mais":
```javascript
console.log(/\d+/.test("42"));
// imprime true
```
Então `/\d/` corresponde a um único dígito e `/\d+/` corresponde a uma sequência de dígitos. Para um `test` simples os dois se comportam da mesma forma, porque ambos precisam de apenas um dígito presente.

---

Um literal como `/\d+/` é fixo depois que você o escreve. Quando o padrão precisa ser **construído em tempo de execução**, use o **construtor `RegExp`**, que recebe o padrão como string:
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// imprime true
```
Há uma armadilha. Dentro de uma string, uma barra invertida inicia uma sequência de escape da *string*, então ela desaparece antes que a regex a veja. Para colocar uma barra invertida real no padrão você deve duplicá-la:
```javascript
const digits = new RegExp("\\d+");
// o mesmo padrão que /\d+/
```
Escrever `new RegExp("\d+")` em vez disso produz o padrão `/d+/`, que corresponde à letra `d`, não a um dígito.

Prefira o literal quando o padrão é conhecido ao escrever o código; ele é mais curto e não precisa de barras invertidas duplicadas.

---

Mais dois blocos de construção permitem descrever quase qualquer forma de texto.

Uma **classe de caracteres** é um conjunto de caracteres entre colchetes; ela corresponde a exatamente um deles. Um traço escreve um intervalo, e um `^` no início nega o conjunto:
```javascript
/[aeiou]/   // uma vogal
/[a-z]/     // uma letra minúscula
/[A-Z0-9]/  // uma letra maiúscula ou um dígito
/[^0-9]/    // um caractere que não é um dígito
```
**Quantificadores** dizem quantas vezes o trecho anterior se repete: `+` um ou mais, `*` zero ou mais, `?` zero ou um, e `{n}` exatamente `n` vezes.

Por fim, **âncoras** ligam o padrão às extremidades do texto: `^` significa "comece aqui" e `$` significa "termine aqui". Sem elas um padrão pode corresponder em qualquer lugar dentro da string, então `/\d{2}/.test("abc12def")` é `true`. Com ambas as âncoras a string inteira precisa corresponder:
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// imprime false
console.log(/^\d{2}$/.test("12"));
// imprime true
```

---

`test` apenas diz sim ou não. Para obter o próprio texto correspondido, chame **`match`** na string:
```javascript
const match = "order 42 shipped".match(/\d+/);
```
Quando nada corresponde, `match` retorna `null`. Quando algo corresponde, ele retorna um resultado semelhante a um array:
- `match[0]` é o texto que foi correspondido
- `match.index` é a posição onde a correspondência começa
- `match.input` é a string inteira que foi pesquisada

```javascript
console.log(match[0]);
// imprime 42
console.log(match.index);
// imprime 6
```
Como o resultado pode ser `null`, verifique-o antes de ler `match[0]`.

---

Como `match` retorna `null` quando o padrão está ausente, ler `match[0]` direto lança `TypeError: Cannot read properties of null`. Proteja-o:
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
O operador de coalescência nula escreve a mesma proteção em uma linha, porque `match?.[0]` é `undefined` quando `match` é `null`:
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

Parênteses ao redor de uma parte de um padrão criam um **grupo de captura**: o texto que essa parte correspondeu é guardado à parte para que você possa lê-lo depois.

Os grupos aparecem depois de `match[0]`, numerados da esquerda para a direita pelo seu parêntese de abertura:
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// imprime 2026-09-12
console.log(match[1]);
// imprime 2026
console.log(match[3]);
// imprime 12
```
Então `match[0]` é sempre a correspondência inteira, e `match[1]`, `match[2]`, ... são os grupos. Um grupo que faz parte de um padrão que não corresponde de forma alguma faz todo o `match` retornar `null`.

---

Capture apenas o que você precisa. Um grupo não é apenas uma forma de ler um trecho depois; ele também diz ao leitor qual parte do padrão importa. Em um padrão de hora em que você quer apenas os minutos, agrupe somente os minutos e deixe o resto sem agrupar:
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// imprime 35
```
O padrão inteiro ainda precisa corresponder, então as horas e os segundos ainda são obrigatórios; eles simplesmente não são capturados. Menos grupos significam menos números para controlar quando você lê `match[1]`, `match[2]` e assim por diante.

---

Contar parênteses cansa, e adicionar um grupo no meio de um padrão renumera tudo que vem depois. Um **grupo nomeado** evita ambos os problemas: escreva `?<name>` logo depois do parêntese de abertura e leia o trecho de `match.groups`:
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// imprime 2026
console.log(match.groups.month);
// imprime 09
```
Grupos nomeados ainda são numerados, então `match[1]` continua funcionando, mas `match.groups.year` diz o que o valor significa. Quando o padrão não tem nenhum grupo nomeado, `match.groups` é `undefined`.

---

Tudo até aqui parou na primeira correspondência. **Flags**, escritas depois da barra de fechamento de um literal, mudam isso e outros detalhes da busca:
- `g` global: encontra toda correspondência, não apenas a primeira
- `i` ignora maiúsculas e minúsculas, então `/cat/i` também corresponde a `Cat` e `CAT`

Com a flag `g`, `match` se comporta de forma diferente: ele retorna um array simples das **strings** correspondidas, sem `index` e sem grupos, ou `null` quando não há correspondência:
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// imprime [ '1', '22', '333' ]
console.log(numbers.length);
// imprime 3
```
Flags podem ser combinadas em qualquer ordem, como em `/cat/gi`. Com o construtor `RegExp` elas vão no segundo argumento: `new RegExp("\\d+", "g")`.

---

A flag `g` lhe dá cada string correspondida, mas ela descarta os grupos. Quando você precisa dos grupos de *toda* correspondência, use **`matchAll`**. Ele retorna um iterador de objetos de correspondência completos, cada um exatamente como o resultado de um `match` simples:
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// imprime a -> 1
// imprime b -> 2
```
`matchAll` exige a flag `g`; sem ela, ele lança um `TypeError`. Como ele retorna um iterador, espalhe-o com `[...text.matchAll(pattern)]` quando quiser um array real, e note que ele não produz nada quando o padrão nunca corresponde.

---

**`replace`** retorna uma nova string com a correspondência trocada por outra coisa. A string original nunca é alterada.
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// imprime the dog sleeps
```
Dentro da string de substituição algumas sequências têm um significado especial:
- `$1`, `$2`, ... o texto capturado pelo grupo 1, grupo 2, ...
- `$<name>` o texto capturado por um grupo nomeado
- `$&` a correspondência inteira

É isso que faz de `replace` uma ferramenta de reescrita e não apenas uma troca:
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// imprime 12/09/2026
```
Sem a flag `g` apenas a **primeira** correspondência é substituída.

---

Para reescrever **toda** correspondência em vez da primeira você tem duas opções:
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// imprime a# b#
console.log("a1 b2".replaceAll(/\d/g, "#"));
// imprime a# b#
```
**`replaceAll`** é o mais claro dos dois, e ele também aceita uma string simples como padrão. Quando você fornece uma regex, essa regex **deve** ter a flag `g`, caso contrário ele lança um `TypeError`; isso é exatamente o que evita o bug silencioso de escrever `replace` e corrigir apenas a primeira correspondência.

---

A substituição não precisa ser uma string. Quando você passa uma **função**, ela é chamada uma vez por correspondência e tudo o que ela retorna é inserido no lugar dessa correspondência.

A função recebe primeiro a correspondência inteira, depois cada grupo de captura:
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// imprime 5 5

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// imprime Ann Lee
```
Esta é a única forma de calcular a substituição a partir do texto correspondido, o que `$1` sozinho não consegue fazer.

---

**`split`** corta uma string em um array. Recebendo uma string simples ele corta nesse texto exato, mas recebendo uma regex ele corta em cada correspondência do padrão, o que permite que uma única chamada trate separadores que variam:
```javascript
console.log("a, b;c".split(", "));
// imprime [ 'a', 'b;c' ]
console.log("a, b;c".split(/[,;]\s*/));
// imprime [ 'a', 'b', 'c' ]
```
Os separadores em si não fazem parte do resultado. Cuidado com um separador no início ou no fim da string: ele produz uma string vazia no array, porque há um campo vazio desse lado.

---

Uma última flag completa o conjunto. Por padrão `^` e `$` significam o início e o fim da **string inteira**, então um padrão ancorado com `^` só pode corresponder no comecinho, mesmo quando o texto tem várias linhas.

A flag **`m`** (multiline) muda isso: `^` e `$` então também correspondem logo depois e logo antes de cada quebra de linha, então cada linha é ancorada por si mesma:
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// imprime [ 'note a' ]
console.log(text.match(/^note.*/gm));
// imprime [ 'note a', 'note c' ]
```
Dois detalhes importam aqui. Por padrão o `.` não corresponde a uma quebra de linha (apenas a flag `s` muda isso), então `.*` para no fim da linha por si só. E `match` com a flag `g` retorna `null`, não um array vazio, quando nada corresponde, então combine-o com `?? []` quando você promete retornar um array.
