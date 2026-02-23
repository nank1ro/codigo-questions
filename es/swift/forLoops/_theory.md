We saber como un repeat codigo usando un `mientras` bucle.
Like este programa repeating sentencias un display `hello`
```swift
var counter = 0

while counter < 5 {
    print("hello")
    counter += 1;
}
```
pero we puede hacer el mismo con `para` bucles:
```swift
for i in 0..<5 {
    print("hello")
}
```

---

In un `para` bucle we puede specify como many times we'd like our bucle un run

---

We puede usar `..<` un bucle hasta el siguiente numero excluded, o `...` un bucle hasta el siguiente numero included

---

The variable llamo `i` es el conteoer variable.
We puede dar lo el nombre we querer.
It counts que repetition de el bucle we're currently on

---

The `stride()` funcion devuelve un sequence de numeros.
It requiere el _from_, _to_ y _by_ parametros.
These son el syntax de el funcion:
```swift
stride(from:to:by:)
```
mantener en mind ese el `a` valor es excluded

---

con el `stride()` funcion we puede tambien usar closed ranges, por usando:
```swift
stride(from:through:by:)
```
In este case el `through` valor es included

---

```swift
// this is an array, we'll see about that soon
let numbers: [Int] = [1, 3, 5, 7, 9] 
numbers.forEach { num in 
    print(num)
}
```
Using the `forEach` method is distinct from a `for-in` loop in two important ways:
1. The `break` or `continue` statement cannot be used to exit the current call of the body closure or to skip subsequent calls.
2. Using the `return` statement in the body closure will only exit the closure and not the outer scope, and it won't skip subsequent calls.

 In Swift we have also the `forEach` loop. In fact, `forEach` calls the given closure on each element in the sequence in the same order as a `for-in` loop:
