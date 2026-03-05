Nous savons comment répéter du code en utilisant une boucle `while`.
Comme ce programme qui répète des instructions pour afficher `hello`
```swift
var counter = 0

while counter < 5 {
    print("hello")
    counter += 1;
}
```
Mais nous pouvons faire la même chose avec les boucles `for` :
```swift
for i in 0..<5 {
    print("hello")
}
```

---

Dans une boucle `for`, nous pouvons spécifier combien de fois nous aimerions que notre boucle s'exécute

---

We can use `..<` to loop until the next number excluded, or `...` to loop until the next number included

---

The variable called `i` is the counter variable.
We can give it the name we want.
It counts what repetition of the loop we're currently on

---

The `stride()` function returns a sequence of numbers.
It requires the _from_, _to_ and _by_ parameters.
These are the syntax of the function:
```swift
stride(from:to:by:)
```
Keep in mind that the `to` value is excluded

---

With the `stride()` function we can also use closed ranges, by using:
```swift
stride(from:through:by:)
```
In this case the `through` value is included

---

En Swift, nous avons aussi la boucle `forEach`.
En fait, `forEach` appelle la fermeture donnée sur chaque élément de la séquence dans le même ordre qu'une boucle `for-in` :
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
