Comparison operators compare two values and return a **boolean**, `True` or `False`: `==` equal, `!=` not equal, `<` less than, `>` greater than, `<=` less than or equal, `>=` greater than or equal:
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
The result can be stored in a variable or printed directly. A single `=` is an assignment, not a comparison.

---

Comparison operators are not limited to numbers. Strings are compared character by character using their code points, so `"apple" < "banana"` is `True` and, because every uppercase letter comes before the lowercase ones, `"Zoo" < "apple"` is also `True`. Lists and tuples are compared element by element in the same way:
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
A comparison is an expression, so a function can `return a < b` directly instead of wrapping it in an `if`.

---

Comparisons can be **chained**: `1 < x < 10` checks that `x` is greater than `1` **and** less than `10`, exactly like `1 < x and x < 10`, but `x` is evaluated only once:
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
Any comparison operators can be chained and each one applies to its two neighbours: `a < b == c` means `a < b and b == c`. Reading a chain as a range, `low < x < high`, is the most common use.

---

Logical operators combine booleans. `and` is `True` only when both sides are `True`, `or` when at least one side is, and `not` flips a single value:
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
Comparisons bind tighter than logical operators, so `age >= 18 and member` needs no parentheses. Parentheses are needed to group an `or` inside an `and`: `a and (b or c)`.

---

When `not`, `and` and `or` appear in one expression, Python applies `not` first, then `and`, then `or`. So `a or b and c` means `a or (b and c)`, and `not a == b` means `not (a == b)`:
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
When a different grouping is intended, add parentheses; they also make the expression easier to read.

---

Every value has a **truth value**. `bool(value)` returns `False` for `0`, `0.0`, `None`, the empty string `""` and empty containers such as `[]`, `{}` and `set()`; every other value is truthy, including `"0"` and `[0]`:
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`, `while`, `and`, `or` and `not` use this rule, so `if items:` checks that the list is not empty and `not name` checks that the string is empty; there is no need to write `len(items) > 0` or `name == ""`.

---

Because `if value:` already applies the truth value, comparing with `== True` or `== False` is unnecessary and can even be wrong: `2 == True` is `False`, yet `2` is truthy. Test the value itself:
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` and `or` do not always return `True` or `False`: they return one of their **operands**. `a and b` returns `a` if it is falsy, otherwise `b`; `a or b` returns `a` if it is truthy, otherwise `b`:
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
The result is truthy or falsy exactly when the whole expression is, which is why `if a and b:` still works. A common use is a default value: `name = user_input or "guest"`.

---

Logical operators are **short-circuit**: `and` stops as soon as one operand is falsy and `or` as soon as one is truthy, because the result is already known. The remaining operands are never evaluated, so if they are function calls they do not run:
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` compares **values**; `is` compares **identity**, that is, whether both names refer to the very same object. Two equal lists built separately are `==` but not `is`:
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` is meant for singletons such as `None`, `True` and `False`: write `value is None` or `value is not None`, never `value == None`, because a class can define `==` to return anything. Using `is` with numbers or strings is unreliable and Python warns about it.

---

Short-circuit evaluation is a safe way to **guard** an operation that would fail on some values. In `word is not None and len(word) < 4`, `len(word)` runs only when `word` is not `None`, so the call never raises. The guard must come first:
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
Keep in mind that `and` returns an operand: `word and len(word) < 4` gives `None` for `None` and `""` for the empty string, not `False`. Guard with a real comparison when a boolean is required.

---

The `in` operator checks **membership**: whether an element is in a list, tuple or set, whether a substring is in a string, or whether a key is in a dictionary. `not in` is its negation:
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
Both return a boolean and read like English, which makes them the preferred way to test membership instead of writing a loop.
