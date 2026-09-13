A **higher-order method** is a method that takes a function as an argument. Dart collections offer many of them, and the function you pass is usually an anonymous function written with the arrow syntax `(x) => ...`.

`map` is the most common one: it calls the function on every element and produces the results, one for each element, leaving the original collection untouched:

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

Notice the **round brackets** in the output. `map` does not return a `List`: it returns an `Iterable`, a sequence you can walk through. To get a real list back, call **`toList()`** on it:

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

Square brackets in the output are the sign that you are looking at a `List`, round brackets that you are looking at a plain `Iterable`.

---

`where` takes a function that returns a `bool`, called a **predicate**, and keeps only the elements for which it answers `true`. The order of the surviving elements never changes:

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

Like `map`, `where` returns an `Iterable` and never modifies the original collection, so `toList()` is again what turns the result into a `List`.

In other languages this method is called `filter`; in Dart it is `where`.

---

The function given to `map` does not have to return the same type as the elements it receives. Mapping a list of strings to their lengths turns a `List<String>` into an `Iterable<int>`, which `toList()` then makes a `List<int>`:

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

The result always has **exactly as many elements as the original**, in the same order: `map` transforms elements, it never adds or removes any.

---

Some higher-order methods answer a question about the collection instead of building a new one. They take a predicate and return a `bool`:

- `any` is `true` when **at least one** element satisfies the predicate
- `every` is `true` when **all** the elements satisfy it

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

Both stop as soon as the answer is certain: `any` at the first element that matches, `every` at the first that does not.

On an empty collection `any` is `false` and `every` is `true`: there is no element to prove the first, and none to break the second.

---

`map` and `where` are **lazy**: calling them runs nothing. They return an `Iterable` that remembers the source and the function, and the function is only called while something walks through the result, one element at a time.

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // nothing computed yet
print(doubled.first);                      // computes only 2
```

`toList()` is what **materialises** the sequence: it walks it from start to end and stores every result in a real `List`.

Laziness has two consequences worth remembering. A lazy `Iterable` is recomputed every time you iterate it, so materialising once with `toList()` is cheaper when you need the values more than once. And it keeps looking at the original collection, so changing that collection changes what the `Iterable` produces:

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` combines a whole collection into a **single value**. It takes two arguments: the starting value of the **accumulator**, and a function receiving the accumulator so far and the next element, and returning the new accumulator:

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

Here `acc` starts at `0`, then becomes `1`, `3`, `6` and finally `10`.

The accumulator does not have to be a number, nor the same type as the elements: starting from `''` and adding text builds a `String` out of a list of anything.

One detail to keep in mind: Dart works out the accumulator type from the starting value **and** from where the result is used. Inside `print(...)` the expected type is unknown, so store the result in a variable first (or write `fold<int>(...)`), otherwise the compiler complains that it cannot use `+` on the accumulator.

---

`reduce` is the shorter relative of `fold`. It takes no starting value: the **first element** is the starting accumulator, and the function runs for every remaining element:

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

Because there is no starting value, the result always has the **same type as the elements**, and calling `reduce` on an empty collection throws a `StateError`: there is no first element to start from. `fold` has no such problem, which is why it is the safer default.

`reduce` is at its best when you are looking for one element among many, such as the largest:

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` returns the **first** element matching a predicate, instead of all of them:

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

When nothing matches there is no element to return, so `firstWhere` throws a `StateError`. To give an answer instead of an error, pass the named argument **`orElse`**: a function taking no parameters that produces the fallback value.

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` is a function, not a plain value, so it is only called when the search fails. Writing `orElse: 'none'` does not compile.

---

When the function you give to `map` returns a collection for each element, you end up with a sequence of collections. **`expand`** does the same job but then joins all of them into one flat sequence:

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

The order is preserved: everything produced by the first element comes first, then everything produced by the second, and so on.

Because the returned collection can have any size, `expand` is also the way to produce **more or fewer** elements than you started with: returning an empty list for an element simply drops it.

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` keeps the **first** `n` elements and `skip(n)` throws them away. Neither takes a function, but both return a lazy `Iterable`, so they fit naturally between the other higher-order methods:

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

Asking for more elements than there are is not an error: you simply get what exists, or an empty result.

`takeWhile` and `skipWhile` are the versions with a predicate. They take or drop elements from the start **as long as** the predicate holds, and stop at the first element that fails it, even if later ones would match again:

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart has no `sorted` method. `sort` belongs to `List`, it reorders the list **in place** and returns nothing:

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

Because it returns `void`, you cannot use the result at all: `final sorted = numbers.sort();` gives a value the compiler refuses to let you read. The idiom for an ordered **copy** is `toList()` followed by the cascade `..sort()`: `toList()` makes the copy, and `..` runs `sort` on it while still handing back the copy itself.

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], untouched
```

`sort` also accepts a **comparator**: a function of two elements returning a negative number when the first comes before the second, `0` when they are equal, and a positive number otherwise. `compareTo` produces exactly that, so ordering by any key is a one-liner:

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` and `reduce` look alike, and choosing between them comes down to two questions: can the collection be empty, and does the result have the same type as the elements?

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String from Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int from Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` can only ever give back an element type, because it starts from an element. `fold` starts from a value you choose, so the accumulator can be an `int` counting, a `String` growing, or even a `List` being built up. And since that starting value already exists, an empty collection is simply the answer `fold` returns unchanged, while `reduce` has nothing to return and throws.

---

Every one of these methods returns an `Iterable`, and every `Iterable` has the same methods again. That is what lets them be **chained**: a whole computation reads as a pipeline from left to right, each step working on what the previous one produced.

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

Only the last step needs `toList()`: calling it in the middle would build a list nobody keeps.

The type changes along the chain, and so does what the next function receives: after `where` on a `List<String>` you still have strings, but after `map((w) => w.length)` the next step sees numbers.

Because each step is lazy, the order matters for the work done, not only for the result: filtering first with `where` means `map` is called on fewer elements.

---

Nothing about these methods is special: they simply have a **function as a parameter**, and your own functions can do the same. The type of a function parameter is written as the return type, then `Function`, then the parameter types in brackets:

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

The caller decides **what** happens, the function decides **on what**. Note how `operation` is handed straight to `map`: a function value can be passed on like any other value.

The argument can be an anonymous function, or the **name** of an existing one, written without brackets. Adding the brackets would call it instead of passing it:

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

A function can also **return** a function. The return type is written exactly like a function parameter type, and the value returned is usually an anonymous function:

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` does not multiply anything: it builds and gives back a new function that multiplies by `3`. That function is then stored, called, or passed to `map` like any other:

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

The returned function still remembers `factor` after `multiplier` has finished. A function that keeps the variables of the scope where it was created is called a **closure**, and it is what makes function factories like this one possible.

---

Put together, these methods replace most hand-written loops. A pipeline usually reads in three stages: **select** the elements with `where`, **transform** them with `map`, then **combine** them with `fold`:

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

Because `fold` chooses its own starting value, it can also end a chain with a type that has nothing to do with the elements, such as a `String` grown one piece at a time:

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

Each stage stays short and says what it does, which is the real reason to prefer them over a loop that does all three at once.
