Kotlin tem um tipo Booleano básico, chamado `Boolean`.
Os valores Booleanos são referidos como lógicos, porque só podem ser verdadeiros ou falsos.
Você pode avaliar qualquer expressão em Kotlin e obter uma de duas respostas, `true` ou `false`.

---

Podemos armazenar o valor booleano `true` em uma variável assim como um número ou uma string.

---

O valor oposto de `true` é `false`

---

Os valores Booleanos também podem ser negados usando o `!` antes deles, por exemplo:
```kotlin
println(!true) // prints false
println(!false) // prints true
```

---

Também podemos criar expressões booleanas usando o `&&` (_and_) e `||` (_or_):

- `&&` (_and_): produz true apenas se a expressão Booleana à esquerda do operador e a à direita forem ambas true.
- `||` (_or_): Produz true se a expressão à esquerda ou à direita do operador for true, ou se ambas forem true.

```kotlin
println(true && true) // prints true
println(true && false) // prints false
println(false && false) // prints false
println(true || true) // prints true
println(true || false) // prints true
println(false || false) // prints false
```
