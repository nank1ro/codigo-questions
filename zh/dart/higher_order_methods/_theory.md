**高阶方法**是把函数当作参数接收的方法。Dart 的集合提供了很多这样的方法，而你传入的函数通常是用箭头语法 `(x) => ...` 写成的匿名函数。

`map` 是其中最常见的一个：它对每个元素调用该函数，并为每个元素产出一个结果，同时保持原集合不变：

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

注意输出里的**圆括号**。`map` 并不返回 `List`：它返回一个 `Iterable`，也就是一个你可以逐个遍历的序列。要拿回真正的列表，就在它上面调用 **`toList()`**：

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

输出里的方括号说明你看到的是 `List`，圆括号说明你看到的是普通的 `Iterable`。

---

`where` 接收一个返回 `bool` 的函数，即**谓词**，只保留让它返回 `true` 的元素。保留下来的元素顺序永远不变：

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

和 `map` 一样，`where` 返回一个 `Iterable`，也从不修改原集合，所以同样要用 `toList()` 把结果变成 `List`。

在其他语言里这个方法叫 `filter`；在 Dart 里它叫 `where`。

---

传给 `map` 的函数不必返回与它接收的元素相同的类型。把一个字符串列表映射成它们的长度，会把 `List<String>` 变成 `Iterable<int>`，再用 `toList()` 变成 `List<int>`：

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

结果的元素个数**总是和原来完全一样**，顺序也一样：`map` 只转换元素，从不增加或删除元素。

---

有些高阶方法回答的是关于集合的问题，而不是构建一个新集合。它们接收一个谓词并返回 `bool`：

- 当**至少有一个**元素满足谓词时 `any` 为 `true`
- 当**所有**元素都满足谓词时 `every` 为 `true`

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

两者都会在答案确定时立刻停止：`any` 停在第一个匹配的元素，`every` 停在第一个不匹配的元素。

对空集合来说 `any` 是 `false`，`every` 是 `true`：没有元素能证明前者，也没有元素能推翻后者。

---

`map` 和 `where` 是**惰性**的：调用它们什么也不会执行。它们返回一个记住了数据源和函数的 `Iterable`，只有当某段代码遍历结果时，函数才会被逐个元素地调用。

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // nothing computed yet
print(doubled.first);                      // computes only 2
```

`toList()` 才是**物化**这个序列的操作：它从头到尾遍历一遍，把每个结果存进一个真正的 `List`。

惰性有两个值得记住的后果。惰性的 `Iterable` 每次遍历都会重新计算，所以当你需要多次使用这些值时，用 `toList()` 物化一次更划算。而且它一直看着原集合，所以改变那个集合就会改变 `Iterable` 产出的内容：

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` 把整个集合合并成**单个值**。它接收两个参数：**累加器**的初始值，以及一个接收当前累加器和下一个元素、返回新累加器的函数：

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

这里 `acc` 从 `0` 开始，然后依次变成 `1`、`3`、`6`，最后是 `10`。

累加器不一定是数字，也不一定和元素同类型：从 `''` 开始不断拼接文本，就能用任意元素的列表构建出一个 `String`。

有一个细节要记住：Dart 会根据初始值**以及**结果的使用位置来推断累加器的类型。在 `print(...)` 里期望的类型是未知的，所以要先把结果存进一个变量（或者写成 `fold<int>(...)`），否则编译器会抱怨无法在累加器上使用 `+`。

---

`reduce` 是 `fold` 的简短版本。它不接收初始值：**第一个元素**就是初始累加器，函数对剩下的每个元素运行一次：

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

因为没有初始值，结果的类型**总是和元素相同**，而且对空集合调用 `reduce` 会抛出 `StateError`：没有第一个元素可以作为起点。`fold` 没有这个问题，所以它是更安全的默认选择。

当你要在很多元素中找出某一个时，比如最大的那个，`reduce` 最为合适：

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` 返回匹配谓词的**第一个**元素，而不是全部：

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

当没有元素匹配时就没有东西可返回，于是 `firstWhere` 会抛出 `StateError`。要给出一个答案而不是错误，就传入命名参数 **`orElse`**：一个不带参数、产出后备值的函数。

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` 是一个函数，而不是普通的值，所以只有在查找失败时才会被调用。写成 `orElse: 'none'` 无法通过编译。

---

当你传给 `map` 的函数为每个元素返回一个集合时，你得到的是一个由集合组成的序列。**`expand`** 做同样的事，但接着把它们全部连成一个扁平的序列：

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

顺序会被保留：第一个元素产出的内容全部排在前面，然后是第二个元素产出的内容，以此类推。

因为返回的集合可以是任意大小，所以 `expand` 也是产出**比原来更多或更少**元素的方式：为某个元素返回空列表就相当于把它丢弃。

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` 保留**前** `n` 个元素，`skip(n)` 把它们丢掉。两者都不接收函数，但都返回惰性的 `Iterable`，所以它们能自然地和其他高阶方法配合使用：

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

要求的元素比实际存在的多并不是错误：你只会得到已有的部分，或者一个空结果。

`takeWhile` 和 `skipWhile` 是带谓词的版本。它们从开头开始，**只要**谓词成立就一直取或一直丢，并在第一个不满足谓词的元素处停下，即使后面的元素又重新满足也不再继续：

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart 没有 `sorted` 方法。`sort` 属于 `List`，它**就地**重排列表并且不返回任何东西：

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

因为它返回 `void`，你根本无法使用它的结果：`final sorted = numbers.sort();` 得到的值编译器不允许你读取。得到一份排好序的**副本**的惯用写法是 `toList()` 后面接级联 `..sort()`：`toList()` 做出副本，而 `..` 在副本上执行 `sort`，同时仍然把副本本身交还给你。

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], untouched
```

`sort` 还接受一个**比较器**：一个接收两个元素的函数，当第一个排在第二个前面时返回负数，相等时返回 `0`，否则返回正数。`compareTo` 产出的正是这样的值，所以按任意键排序只要一行：

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` 和 `reduce` 看起来很像，在两者之间做选择归结为两个问题：集合可能为空吗，以及结果和元素是同一个类型吗？

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String from Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int from Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` 只能返回元素的类型，因为它从一个元素开始。`fold` 从你选择的值开始，所以累加器可以是计数的 `int`、不断增长的 `String`，甚至是正在构建的 `List`。而且既然那个初始值已经存在，对空集合来说它就是 `fold` 原样返回的答案，而 `reduce` 没有东西可返回，只能抛出异常。

---

这些方法每一个都返回 `Iterable`，而每个 `Iterable` 又都拥有这些方法。正是这一点让它们可以**链式调用**：整个计算从左到右读起来就像一条流水线，每一步都作用在上一步产出的结果上。

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

只有最后一步需要 `toList()`：在中间调用它只会构建一个没人保留的列表。

类型会沿着链条变化，下一个函数接收到的东西也随之变化：对 `List<String>` 执行 `where` 之后你拿到的仍然是字符串，但在 `map((w) => w.length)` 之后，下一步看到的就是数字了。

因为每一步都是惰性的，顺序影响的不只是结果，还有实际完成的工作量：先用 `where` 过滤意味着 `map` 只会在更少的元素上被调用。

---

这些方法并没有什么特别之处：它们只是有一个**函数类型的参数**，而你自己的函数也能这么做。函数参数的类型写法是：先写返回类型，然后是 `Function`，然后是括号里的参数类型：

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

调用方决定**做什么**，函数决定**对什么做**。注意 `operation` 是直接交给 `map` 的：函数值可以像任何其他值一样被传递下去。

参数可以是匿名函数，也可以是已有函数的**名字**，写的时候不加括号。加上括号就变成调用它，而不是把它传进去：

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

函数也可以**返回**一个函数。返回类型的写法和函数参数类型完全一样，返回的值通常是一个匿名函数：

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` 并不做任何乘法：它构建并返回一个把数字乘以 `3` 的新函数。之后这个函数就可以像其他函数一样被保存、调用或传给 `map`：

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

即使 `multiplier` 已经执行完毕，返回的函数仍然记得 `factor`。这种保留了自己被创建时所在作用域变量的函数叫作**闭包**，正是它让这样的函数工厂成为可能。

---

把这些方法组合起来，就能替代大多数手写的循环。一条流水线通常分三个阶段来读：用 `where` **筛选**元素，用 `map` **转换**它们，再用 `fold` **合并**它们：

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

因为 `fold` 自己选择初始值，它也能让一条链以一个与元素毫无关系的类型收尾，比如一点一点拼起来的 `String`：

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

每个阶段都很简短，而且清楚地说明了自己在做什么，这才是比起一个同时做完三件事的循环更应该选择它们的真正理由。
