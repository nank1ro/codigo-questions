Algumas operações não terminam imediatamente: baixar um arquivo, ler de um banco de dados, esperar por um temporizador. O JavaScript não congela enquanto elas rodam. Em vez disso, ele lhe entrega uma **`Promise`**: um objeto que representa um valor que estará disponível **mais tarde**.

Uma função marcada com **`async`** sempre retorna uma promise. O que quer que a função retorne se torna o valor dentro dessa promise:
```javascript
async function fetchNumber() {
  return 42;
}
```
Para extrair o valor de uma promise você usa **`await`**. Ele pausa a função até que a promise tenha seu valor e então lhe dá o valor puro. `await` só é permitido dentro de uma função `async`:
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
Sem `await`, `n` seria a própria promise e `console.log(n)` imprimiria `Promise { 42 }` em vez do número.

---

Adicionar `async` na frente de uma função muda o que ela devolve: o corpo ainda calcula um valor comum, mas quem chama recebe uma promise que o envolve.
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
As duas funções contêm o mesmo código; apenas a maneira de ler o resultado muda. `shoutLater("hi")` precisa ser aguardada com `await` dentro de outra função `async` para devolver `"HI"`.

Marcar uma função como `async` não custa nada quando não há nada a esperar, e é isso que permite usar `await` dentro dela mais tarde.

---

Quando o valor realmente chega mais tarde, você constrói a promise você mesmo com **`new Promise`**. Ela recebe uma função, que por sua vez recebe um callback **`resolve`**: chame `resolve(value)` quando o valor estiver pronto e a promise será cumprida com ele.
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` agenda o `callback` para rodar após `ms` milissegundos e retorna imediatamente, então nada fica bloqueado enquanto isso.

A função passada para `new Promise` roda imediatamente, mas a promise permanece **pending** até que `resolve` seja chamado. Aguardá-la com `await` dá o valor:
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

Uma promise está sempre em um de três estados:

- **pending**: o trabalho ainda está em andamento;
- **fulfilled**: o trabalho teve sucesso e a promise contém um valor;
- **rejected**: o trabalho falhou e a promise contém um erro.

Uma promise começa como pending e muda de estado no máximo uma vez. Assim que é fulfilled ou rejected, ela está **settled** e nunca mais muda.

Chamar uma função `async` nunca espera: ela inicia o trabalho e lhe entrega uma promise pending imediatamente, então a linha após a chamada roda antes de o trabalho terminar. Essa promise é um objeto normal, não o valor dentro dela, e é por isso que esquecer o `await` é um erro tão comum.

---

`await` não é a única maneira de ler uma promise. Toda promise tem um método **`.then(callback)`**: o callback recebe o valor assim que a promise é cumprida.
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** constrói uma promise que já está cumprida com `value`, o que é útil quando você tem o valor em mãos mas precisa retornar uma promise.

`.then` retorna uma **nova** promise cumprida com o que quer que o callback retorne, então as chamadas podem ser **encadeadas**, cada passo trabalhando sobre o resultado do anterior:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

Uma função `async` é lida de cima para baixo como qualquer outra função: `await` simplesmente a pausa até que a promise aguardada seja cumprida, então a execução continua na linha seguinte.
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
Note a última linha: uma função `async` ainda precisa ser **chamada**. Escrever `main` sem os parênteses define o trabalho mas nunca o inicia, e nada é impresso.

---

O trabalho assíncrono também pode falhar. A função dada a `new Promise` recebe um segundo callback, **`reject`**: chame `reject(error)` e a promise se torna rejeitada em vez de cumprida.
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
Sempre rejeite com um objeto `Error`: ele carrega uma `message` e um stack trace, o que uma string pura não faz.

Uma rejeição é lida com **`.catch(callback)`**, o espelho de `.then`. **`Promise.reject(error)`** constrói uma promise que já está rejeitada, assim como `Promise.resolve` constrói uma cumprida:
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
Chamar `resolve` e `reject` juntos, ou duas vezes, não muda nada: apenas a primeira chamada conta.

---

`.then`, `.catch` e `.finally` são elos da mesma corrente. Uma rejeição pula todos os `.then` até encontrar um `.catch`; assim que o callback do `.catch` retorna um valor, a corrente é cumprida novamente e continua normalmente.

**`.finally(callback)`** roda quando a corrente se estabelece, não importando se foi cumprida ou rejeitada. Seu callback não recebe argumento e seu valor de retorno é ignorado, então o valor continua fluindo para o próximo `.then`. É o lugar para limpeza, como esconder um spinner:
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

Dentro de uma função `async` você não precisa de `.catch`. Aguardar com `await` uma promise rejeitada **lança** o erro, então a instrução comum `try` / `catch` / `finally` o trata:
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
O outro caminho também funciona: um `throw` dentro de uma função `async` não quebra quem a chamou, ele rejeita a promise que a função retornou.
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
Como em qualquer bloco `try`, as linhas após o `await` que falha são puladas, o bloco `catch` roda, e o bloco `finally` roda nos dois casos.

---

Um uso comum de `try` / `catch` em torno de `await` é substituir uma falha por um padrão razoável, para que quem chama nunca precise lidar com o erro:
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
Mantenha o `await` na frente de `measure(path)` mesmo que o valor seja retornado imediatamente. Sem ele, a promise sai da função sem nunca passar pelo bloco `try`, e uma rejeição escaparia do `catch`.

---

Quando vários resultados são necessários, aguardá-los um após o outro desperdiça tempo: cada um só começa quando o anterior terminou. **`Promise.all(promises)`** recebe um array de promises que já estão rodando e retorna uma única promise cumprida com um array com todos os seus valores:
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
Duas regras valem a pena memorizar:

- os valores voltam **na ordem do array**, não na ordem em que terminaram;
- se qualquer promise for rejeitada, a promise retornada por `Promise.all` é rejeitada imediatamente com esse primeiro erro, e os outros valores são perdidos.

---

`Promise.all` funciona com um array de qualquer tamanho, incluindo um vazio: aguardar `Promise.all([])` devolve um array vazio imediatamente. Isso torna seguro passar uma lista construída em tempo de execução, sem um caso especial para "não há nada a esperar".
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
O array que ela devolve sempre tem exatamente tantos elementos quanto o array que recebeu, nas mesmas posições, então ele pode ser percorrido como qualquer outro array.

---

A diferença entre esperar de forma **sequencial** e **paralela** é decidida por *onde* você coloca o `await`:
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
Na primeira versão, o segundo download só começa quando o primeiro terminou, porque `await` pausa a função naquela linha. Na segunda, as duas chamadas são feitas antes de qualquer `await`, então os dois downloads já estão rodando enquanto `Promise.all` espera.

Use `await` sequenciais apenas quando a segunda tarefa realmente precisar do resultado da primeira. Caso contrário, inicie tudo primeiro e aguarde tudo junto.

---

`Promise.all` desiste assim que uma promise é rejeitada. Quando você quer todos os resultados de qualquer forma, use **`Promise.allSettled(promises)`**: ela nunca é rejeitada e é cumprida com um pequeno objeto por promise, na mesma ordem:

- `{ status: "fulfilled", value: ... }` para as que tiveram sucesso;
- `{ status: "rejected", reason: ... }` para as que falharam.

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
Leia `value` apenas quando `status` for `"fulfilled"`, e `reason` apenas quando for `"rejected"`: a outra propriedade simplesmente não existe.

---

**`Promise.race(promises)`** se estabelece assim que a **primeira** das promises se estabelece, e copia o seu resultado: cumprida com o primeiro valor, ou rejeitada com o primeiro erro. As outras não são canceladas, elas continuam rodando, mas o que quer que produzam é ignorado.
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
O uso típico é um prazo: faça uma corrida entre o trabalho real e uma promise que falha depois de um tempo, e você recebe ou o resultado ou um erro de timeout.

Cuidado com um array vazio: `Promise.race([])` fica pending para sempre, porque não há nada que possa estabelecê-la.

---

Juntando as últimas peças temos uma pequena ferramenta usada em quase toda aplicação real: um prazo. Construa uma promise que é rejeitada após `ms` milissegundos, faça uma corrida entre ela e o trabalho real, e a que se estabelecer primeiro decide o resultado:
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
Retornar uma promise de uma função `async` é válido: a promise que a função devolve a acompanha, então quem chama aguarda o valor final e não uma promise de uma promise.
