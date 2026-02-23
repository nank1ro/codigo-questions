Variables are containers for storing data values.
Every variable in Kotlin is an object.
To create a variable, we need to give it a __name__ keeping in mind that it must not contain spaces.
A variable is created the moment you first assign a value to it.
In Kotlin you declare constants with the `val` (short for _value_) keyword and variables with the `var` (short for _variable_) keyword.
The value of a constant can't be changed once it's set, whereas a variable can be set to a different value in the future.
An example of a variable creation named `x` is:
```kotlin
var x = 1
```
In this way we have assigned the value `1` to the variable named `x`.
If we print the variable `x` we get back the number `1`:
```kotlin
println(x) // prints 1
```

---

Variables are called in this way because the value they store can change.
We can update `x` by using `=` and giving it a new value.
```kotlin
var x = 1
println(x) // prints 1
x = 2
println(x) // prints 2
```

---

Tambem podemos dar as variaveis os valores de outras variaveis. Aqui, podemos dar a variavel `y` o valor de `x`
```kotlin
var x = 5
var y = x
println(y) // imprime 5
```

---

Quando atualizamos uma variavel, ela esquece seu valor anterior. Aqui podemos exibir a variavel `x` duas vezes e ver como seu valor e atualizado.
```kotlin
var x = 5
println(x) // imprime 5
x = 10
println(x) // imprime 10
```
