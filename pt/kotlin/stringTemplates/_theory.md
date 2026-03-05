Um _template_ de String é uma forma programática de gerar uma String.
Em Kotlin podemos usar o sinal `+` (concatenação) para exibir duas ou mais strings juntas, assim:
```kotlin
println("Hello " + "Kotlin!")
// imprime "Hello Kotlin!"
```

---

Mas usar o sinal `+` para adicionar um número como '10' a uma string como ` "friends"` produz um erro, pois são tipos diferentes de valores

---

Templates de string nos permitem exibir expressões como adicionar uma string a um número, sem nenhum erro.
Colocar uma expressão dentro de `${}` a avalia.
O valor de retorno é convertido para uma String e inserido na String resultante

---

Se você colocar um $ antes do nome de um identificador, o template de String inserirá o conteúdo desse identificador na String

---

Se o que segue o sinal `$` não é reconhecível como um identificador de programa, nada de especial acontece

---

Também podemos inserir variáveis após os sinais de dólar para mostrar seus valores

---

Podemos usar chaves para inserir valores quantas vezes quisermos dentro dos templates de string

---

Dentro de `${}` também podemos colocar condições, por exemplo:
```kotlin
println("${if (true) "Correct" else "Wrong"}")
// imprime Correct
```

---

Templates de string são mais usados em instruções de impressão, mas também podemos armazená-los em variáveis como strings normais.
