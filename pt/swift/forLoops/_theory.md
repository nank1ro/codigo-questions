Sabemos como repetir código usando um loop `while`.
Como este programa que repete instruções para exibir `hello`
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

Em um loop `for` podemos especificar quantas vezes gostaríamos que nosso loop fosse executado

---

Podemos usar `..<` para fazer loop até o próximo número excluído, ou `...` para fazer loop até o próximo número incluído

---

A variável chamada `i` é a variável contadora.
Podemos dar a ela o nome que quisermos.
Ela conta em qual repetição do loop estamos atualmente

---

A função `stride()` retorna uma sequência de números.
Ela requer os parâmetros _from_, _to_ e _by_.
Esta é a sintaxe da função:
```swift
stride(from:to:by:)
```
Lembre-se que o valor `to` é excluído

---

Com a função `stride()` também podemos usar intervalos fechados, usando:
```swift
stride(from:through:by:)
```
Neste caso o valor `through` é incluído

---

Em Swift também temos o loop `forEach`.
Na verdade, `forEach` chama a closure fornecida em cada elemento da sequência na mesma ordem que um loop `for-in`:
```swift
// isto é um array, veremos sobre isso em breve
let numbers: [Int] = [1, 3, 5, 7, 9]
numbers.forEach { num in
    print(num)
}
```
Usar o método `forEach` é diferente de um loop `for-in` em duas formas importantes:
1. A instrução `break` ou `continue` não pode ser usada para sair da chamada atual do corpo da closure ou para pular chamadas subsequentes.
2. Usar a instrução `return` no corpo da closure só sairá da closure e não do escopo externo, e não pulará chamadas subsequentes.
