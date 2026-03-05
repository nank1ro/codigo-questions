Sabemos como repetir codigo usando um loop `while`.
Como neste programa que repete instrucoes para exibir `hello`
```swift
var counter = 0

while counter < 5 {
    print("hello")
    counter += 1;
}
```
Mas podemos fazer o mesmo com loops `for`:
```swift
for i in 0..<5 {
    print("hello")
}
```

---

Em um loop `for` podemos especificar quantas vezes queremos que nosso loop execute

---

Podemos usar `..<` para iterar ate o proximo numero excluido, ou `...` para iterar ate o proximo numero incluido

---

A variavel chamada `i` e a variavel contadora.
Podemos dar a ela o nome que quisermos.
Ela conta em qual repeticao do loop estamos atualmente

---

A funcao `stride()` retorna uma sequencia de numeros.
Ela requer os parametros _from_, _to_ e _by_.
Esta e a sintaxe da funcao:
```swift
stride(from:to:by:)
```
Tenha em mente que o valor `to` e excluido

---

Com a funcao `stride()` tambem podemos usar intervalos fechados, usando:
```swift
stride(from:through:by:)
```
Neste caso, o valor `through` e incluido

---

Em Swift tambem temos o loop `forEach`.
Na verdade, `forEach` chama a closure fornecida em cada elemento da sequencia na mesma ordem que um loop `for-in`:
```swift
// this is an array, we'll see about that soon
let numbers: [Int] = [1, 3, 5, 7, 9]
numbers.forEach { num in
    print(num)
}
```
Usar o metodo `forEach` e diferente de um loop `for-in` de duas maneiras importantes:
1. As instrucoes `break` ou `continue` nao podem ser usadas para sair da chamada atual da closure ou para pular chamadas subsequentes.
2. Usar a instrucao `return` na closure apenas saira da closure e nao do escopo externo, e nao pulara chamadas subsequentes.
