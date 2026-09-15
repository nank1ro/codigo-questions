Alguns trabalhos não terminam imediatamente: baixar um arquivo, ler de um banco de dados, esperar por um temporizador. Se um programa simplesmente parasse e esperasse, nada mais poderia acontecer nesse meio-tempo. O Swift resolve isso com **funções assíncronas**.

Uma função marcada como **`async`** tem permissão para pausar no meio e retomar depois. A palavra-chave vem depois da lista de parâmetros, antes da seta:
```swift
func fetchNumber() async -> Int {
    return 42
}
```
Chamá-la também é diferente: você deve escrever **`await`** na frente da chamada. O `await` marca o ponto exato em que o programa pode pausar e lhe entrega o valor puro quando a função termina:
```swift
let n = await fetchNumber()
print(n)
// imprime 42
```
Em um script Swift o nível superior já suporta `await`, então você pode chamar funções assíncronas diretamente, sem nenhuma configuração extra. Esquecer `async` ou `await` é um erro de compilação, não um bug silencioso.

---

Uma função assíncrona ainda é uma função comum: ela pode receber parâmetros e retornar um valor de qualquer tipo. Apenas duas coisas mudam, a palavra-chave `async` na assinatura e o `await` em cada local de chamada:
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// imprime 10.0
```
O valor retornado é um `Double` normal, não um wrapper: depois que o `await` termina, você trabalha com ele exatamente como de costume.

---

Funções assíncronas geralmente são construídas umas sobre as outras. Dentro de uma função `async` você pode usar `await` em qualquer outra função `async`, e o resultado é usado como qualquer valor normal:
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// imprime 15
```
O `await` só é permitido dentro de um contexto assíncrono: uma função `async`, ou o nível superior de um script. Uma função comum, não `async`, não pode usar `await` em nada.

---

Um trabalho que acontece ao longo do tempo frequentemente falha: um servidor está fora do ar, um arquivo está ausente, a entrada está errada. Tal função é marcada como **`async throws`** e é chamada com **`try await`**:
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
Para tratar o erro, você envolve a chamada em um bloco `do` e o captura:
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// imprime could not load
```
A ordem das palavras-chave é fixa: `try` vem primeiro, depois `await`.

---

Quando você não se importa com o *motivo* pelo qual a chamada falhou, `try?` é mais curto do que um bloco `do`. Ele transforma uma chamada que lança erros em um **opcional**: o valor em caso de sucesso, `nil` em caso de falha. Combinado com `await`, escreve-se `try? await`:
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
Como o resultado é opcional, ele se encaixa diretamente em um `if let`:
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
Use `try? await` para um fallback rápido, e `do` / `catch` quando o erro em si importa.

---

Várias chamadas `await` escritas uma após a outra rodam **sequencialmente**: a segunda chamada nem sequer começa até que a primeira tenha retornado. O código é lido de cima para baixo, exatamente como um código comum:
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
É isso que você quer quando a segunda chamada precisa do resultado da primeira. Quando as chamadas são independentes, esperar por uma antes de iniciar a outra é tempo desperdiçado, e os próximos exercícios mostram como evitar isso.

---

Para executar duas chamadas independentes ao mesmo tempo, declare-as com **`async let`**. O trabalho começa imediatamente, e o programa continua sem esperar:
```swift
async let left = step("A")
async let right = step("B")
```
O valor ainda não está disponível, então você não pode usar a vinculação diretamente: você deve aguardá-la com `await` no ponto em que finalmente precisar dela. Um `await` na frente da expressão cobre cada `async let` dentro dela:
```swift
let both = await left + right
```
Se cada chamada leva um segundo, a versão sequencial precisa de dois segundos, enquanto a versão com `async let` precisa de cerca de um, porque as duas chamadas se sobrepõem.

---

Quando você precisa dos resultados separadamente, reúna várias vinculações `async let` em uma tupla e aplique `await` à tupla inteira de uma vez:
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
As duas chamadas já estavam em execução; o único `await` espera até que a mais lenta das duas termine. Lembre-se de que `async let` apenas inicia o trabalho: um `async let` que você nunca aguarda é cancelado e implicitamente aguardado quando o escopo termina.

---

`async let` está vinculado ao escopo em que é escrito. Para iniciar um trabalho concorrente e manter uma referência a ele, use uma **`Task`**. A closure passada para `Task { }` roda por conta própria, e a tarefa pode ser armazenada, passada adiante ou retornada:
```swift
let job = Task {
    return await double(21)
}
```
O resultado é lido mais tarde com **`.value`**, que é aguardado com `await`:
```swift
print(await job.value)
// imprime 42
```
O tipo da referência diz o que ela produz e o que ela pode lançar: `Task<Int, Never>` é uma tarefa que retorna um `Int` e nunca lança erros. Ao contrário de `async let`, uma `Task` pode ser criada a partir de código comum, não assíncrono.

---

`Task.sleep` pausa a tarefa atual por um tempo sem bloquear mais nada. Ela pode ser interrompida, então é uma chamada assíncrona que lança erros e precisa de `try await`. A duração é informada com auxiliares como `.seconds`, `.milliseconds` ou `.nanoseconds`:
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
Essa é a maneira padrão de simular um trabalho lento em um exemplo, em vez de uma chamada de rede real. Note que ela não congela o programa: enquanto uma tarefa dorme, as outras continuam executando.

---

Agora a diferença entre sequencial e concorrente é mensurável. Suponha que `work` dorme um segundo antes de retornar:
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
Aguardar as chamadas uma por uma leva cerca de **dois** segundos, porque a segunda espera só começa quando a primeira termina:
```swift
let a = await work(1)
let b = await work(2)
```
Iniciá-las com `async let` leva cerca de **um** segundo, porque as duas esperas se sobrepõem:
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
Escrever `await work(1) + await work(2)` em uma única linha não muda nada: as duas chamadas ainda são avaliadas uma após a outra. A concorrência vem de `async let` ou de tarefas, nunca de como a linha é formatada.

---

`async let` funciona quando você sabe quantas chamadas existem enquanto escreve o código. Para uma lista cujo tamanho só é conhecido em tempo de execução, use um **grupo de tarefas**.

`withTaskGroup(of:)` abre um grupo, `addTask` inicia uma tarefa filha por item, e o grupo é então lido com `for await`, que entrega os resultados à medida que terminam:
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self` declara o que cada tarefa filha retorna. Toda a chamada `withTaskGroup` é uma única expressão, então ela precisa de um único `await` na frente, e ela não retorna até que cada tarefa filha tenha terminado.

---

Um grupo de tarefas lhe entrega os resultados na **ordem de conclusão**, não na ordem em que as tarefas foram adicionadas. A tarefa filha mais rápida chega primeiro, então coletar valores em um array produz uma ordem imprevisível.

Quando a ordem importa, há duas correções. Se os valores podem simplesmente ser reordenados, ordene-os no final:
```swift
return values.sorted()
```
Se cada resultado pertence a uma posição, faça cada tarefa retornar um par `(index, value)` e escreva-o em um array preparado:
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
Uma soma, um máximo ou uma contagem não precisa de nenhuma das correções, porque a ordem dos valores não muda a resposta.
