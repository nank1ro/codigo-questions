Kotlin tem um tipo Booleano básico, chamado `Boolean`.
Valores booleanos são referidos como lógicos, porque podem ser apenas true ou false.
Você pode avaliar qualquer expressão em Kotlin e obter uma de duas respostas, `true` ou `false`.

---

Podemos armazenar o valor booleano `true` em uma variável, assim como um número ou uma string.

---

O valor oposto de `true` é `false`

---

Valores booleanos também podem ser negados usando `!` antes deles, por exemplo:
```kotlin
println(!true) // imprime false
println(!false) // imprime true
```

---

Também podemos criar expressões booleanas usando `&&` (_and_) e `||` (_or_):

- `&&` (_and_): produz true apenas se a expressão booleana à esquerda do operador e a da direita forem ambas true.
- `||` (_or_): produz true se a expressão à esquerda ou à direita do operador for true, ou se ambas forem true.

```kotlin
println(true && true) // imprime true
println(true && false) // imprime false
println(false && false) // imprime false
println(true || true) // imprime true
println(true || false) // imprime true
println(false || false) // imprime false
```
