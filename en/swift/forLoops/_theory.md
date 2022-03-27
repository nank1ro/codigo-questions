We know how to repeat code using a `while` loop.
Like this program repeating statements to display `hello`
```swift
var counter = 0

while counter < 5 {
	print("hello")
	counter += 1;
}
```
But we can do the same with `for` loops:
```swift
for i in 0..<5 {
	print("hello")
}
```

---

In a `for` loop we can specify how many times we'd like our loop to run

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

In Swift we have also the `forEach` loop.
In fact, `forEach` calls the given closure on each element in the sequence in the same order as a `for-in` loop:
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
