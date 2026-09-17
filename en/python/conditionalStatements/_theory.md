Decision making is required when we want to execute code only if a certain condition is satisfied.
Let's assume we want to play outside only if the weather is nice.
In programming, we can save a boolean variable `nice_weather` and perform the action of playing outside `if` this variable is `True`, like:
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

Let's continue with the previous example.
```python
nice_weather = True
if (nice_weather):
    # play outside
```
We've seen that the `if` statement executes the block of code only if the condition is `True`.
Another important thing to consider is represented by the **colons** `:` and the **indentation**, which indicate a code block start.
Indentation refers to the spaces at the beginning of a code line.
Where in other programming languages the indentation in code is for readability only, the indentation in Python is essential.
You can use your favorite number of spaces (2, 4, 6, 8), noting that the preferred is 4.
Here in the app, we suggest using the **TAB** key to indent your line of codes

---

We just saw how to execute a block of code if a condition occurs, now let's see how to execute another block of code if the first condition fails.
We go to play outside if the weather is nice; otherwise, we stay home.
In Python we can use the `else` statement, like:
```python
nice_weather = True
if (nice_weather):
    # play outside
else:
    # stay home
```

---

Let's assume we have another condition to check, like in this example:
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
and the output of this code is `the number is 3`.
First of all, let's check if the number is equal to 2, this is false.
So let's move on to the second statement and check if `num` is equal to 3, being true we execute the following block of code by printing `the number is 3`

---

We can add as many `elif` statements as we want, there are no limits
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
and the output of this code is `the number is 4`.

---

We can also nest a conditional statement (`if`, `elif` or `else`) inside another conditional statement, to create a more complex structure.
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
and the output of this code is `the number is 4`.

---

Every conditional statement needs the `if` keyword to introduce it. It's what tells Python that the block below only runs when a condition holds.

---

A condition doesn't have to be a comparison — a boolean value like `True` on its own works too, and the block runs whenever that value is `True`.

---

The same statement can be made to skip its block just by changing the condition: whenever it evaluates to `False`, Python jumps straight past the indented code.

---

An `if` line in Python is built from three parts: the `if` keyword, a condition, and the colon that closes the line. Everything indented after that colon is the block.

---

Since the condition here is `True`, Python runs the indented line beneath it and prints `Hello!`.

---

A `False` condition means Python never enters the indented block, so nothing gets printed at all.

---

The value that decides whether a block runs is called a condition, and it always has to evaluate to a boolean, `True` or `False`.

---

The block under an `if` can never be empty: Python raises an `IndentationError` when no indented line follows the colon. `pass` is the usual placeholder when there's nothing to run yet.

---

The colon belongs to the `if` line rather than to the block: it marks the end of the condition and announces that the indented lines below are part of the statement.

---

When a condition is `False`, Python skips the whole indented block and carries on at the next line that isn't indented under the `if`.

---

Python doesn't require parentheses around a condition — `if True:` is a complete statement on its own. Parentheses here are ordinary grouping, the same kind used in arithmetic, and they leave the value unchanged.

---

A code block can hold more than one line, and the lines run in the order they are written — a statement added above an existing one prints first.

---

A boolean variable can be used as a condition all by itself — there's no need to compare it to `True` or `False` first.

---

When the condition is a variable, `if` reads whatever that variable holds at that moment. Changing the assignment above is enough to switch the block off, without touching the `if` line at all.

---

The indented lines that belong to a conditional statement are called its code block — indentation is what marks them as part of it.

---

A line that sits outside the `if`'s indentation runs no matter what the condition was, since it was never part of that block.

---

A code block isn't limited to one line — it can be as short or as long as the logic needs, as long as every line stays indented consistently.

---

With `online` set to `False`, the condition never holds, so the block is skipped and nothing is printed.

---

Only the indented `print` right after the `if` belongs to its block; a line written at the same indentation as the `if` itself does not.

---

A line placed after the `if` block but without any extra indentation is no longer part of it — it runs every time, whatever the condition was.

---

A block can hold any number of statements. They run from top to bottom, and each one has to be indented to the same level as the others.

---

Assigning `True` to the variable makes the condition it feeds into hold, so the block underneath runs.

---

Assigning `False` instead makes the condition fail, so the block underneath is skipped entirely.

---

The `if` keyword is what starts a conditional statement — together with its condition, it decides whether the block below executes.

---

`"False"` in quotes is a string, not a boolean, and a non-empty string always counts as true. Only the bare `False` keeps a block from running.
```python
print(bool("False"))  # True
```

---

Choosing `True` here runs both lines in the block, not just the first — everything indented under the `if` belongs to the same block.

---

The colon is the one piece an `if` line can't do without: it closes the condition and opens the block. Parentheses around the condition are optional in Python, so `if True:` and `if (True):` behave identically.

---

Statements like `if`, `elif` and `else`, which run or skip code based on a boolean value, are known collectively as conditional statements.

---

The `not` operator flips a boolean value: `not True` is `False`, and `not False` is `True`.
```python
is_online = False
print(not is_online)  # True
```

---

`not` builds a new boolean instead of modifying the one it reads, so after `is_afternoon = not is_morning` the variable `is_morning` still holds its original value.

---

A condition always sits between the `if` keyword and the colon that follows it, nowhere else in the line.

---

There's no hard limit on how many lines an `if` block can contain — what matters is that every line stays indented at the same level.

---

A boolean literal makes a perfectly good condition: `if True:` runs its block every time. Writing it as `if (True):` is the very same statement, since parentheses around a condition are optional in Python.

---

An `if` statement's code block is the group of indented lines beneath it, set apart from the rest of the program by that indentation.

---

A condition always reduces to one of two values, `True` or `False` — that's what makes it a boolean.
