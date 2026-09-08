An **enumeration** (or *enum*) defines a common type for a group of related, fixed values, like the days of the week or the colors of a traffic light.
Instead of passing around loose strings or numbers, you give each value a **name**, so the code is more readable and typos become errors.
In Python you create an enum by importing `Enum` from the `enum` module and declaring a class that inherits from it.
Each class attribute is a **member** of the enum, with a name and a value:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
By convention member names are written in upper case. You access a member through the class, and printing it shows the class and member names:
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

Every member of an enum has two attributes: `name`, the identifier you wrote in the class, and `value`, the value you assigned to it:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
The value can be any type, not only an integer: strings, tuples and floats are common choices.
A member is a normal object, so you can store it in a variable and read its attributes later:
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

Each enum member exists **only once**: every time you write `Color.RED` you get the very same object.
For this reason you can compare members with `is` (identity) as well as with `==`, and both give the same result:
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
A member is **not** equal to its raw value, because a member and a plain number are different things:
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
This is what makes enums safe: a `1` coming from somewhere else in the program cannot be mistaken for `Color.RED`.

---

An enum class is **iterable**: a `for` loop over the class visits every member, in the order they were declared:
```python
for color in Color:
    print(color.name, color.value)
```
`len()` returns how many members the enum has, and `list(Color)` builds a list of them:
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
Inside a list, members are shown with their `repr()`, which includes the value between angle brackets.

---

You can obtain a member starting from its **value** by calling the class like a function, or from its **name** using square brackets:
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
Both are handy when the value or the name comes from outside the program, like a file or user input.
If nothing matches, `Color(9)` raises a `ValueError` and `Color["PINK"]` raises a `KeyError`.

---

Often the exact values do not matter: you only need the members to be distinct.
In that case you can let Python pick the values with `auto()`, also imported from the `enum` module.
It assigns `1` to the first member and then counts up:
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

A plain `Enum` member cannot be compared with `<` or added to a number.
When the members represent **levels** that need ordering, inherit from `IntEnum` instead: its members are also integers, so they support comparisons, arithmetic and sorting:
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.LOW + 1)              # 2
print(int(Priority.MEDIUM))          # 2
```
An `IntEnum` member is also equal to its integer value: `Priority.LOW == 1` is `True`.

---

`StrEnum` (available since Python 3.11) is the string counterpart of `IntEnum`: its members are also strings, equal to their value.
This makes them convenient wherever plain strings are expected, like configuration keys or API parameters:
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
Unlike a plain `Enum`, converting a `StrEnum` member to text with `str()` or inside an f-string gives its **value**, not `Mode.DARK`.

---

An enum is a class, so it can have **methods** and **properties** like any other class.
Inside them, `self` is the member the method was called on, so you can look at `self.name`, `self.value` or compare `self` with other members:
```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2

    def can_go(self):
        return self is Light.GREEN

    @property
    def label(self):
        return self.name.lower()

print(Light.GREEN.can_go())  # True
print(Light.RED.label)       # red
```
Any plain value assigned in the class body becomes a member, while functions and properties never do, no matter where they appear.

---

If two members share the same value, the second one is not a new member but an **alias** of the first:
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
Aliases are skipped when iterating and are not counted by `len()`.
Usually a duplicated value is a mistake. The `unique` decorator, imported from `enum`, makes Python raise a `ValueError` as soon as an enum with aliases is declared:
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

A `Flag` is an enum whose members can be **combined**: a value can hold several members at once, like a set of options.
Declare its members with `auto()`, which for a `Flag` assigns powers of two (`1`, `2`, `4`, ...), so every combination has a distinct value:
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
Use `|` to combine members, `in` to check whether a member is part of a combination and `value` to see the resulting number:
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

Enums pair naturally with the `match` statement (available since Python 3.10), which compares a value against a series of `case` patterns and runs the first one that matches:
```python
def action(light):
    match light:
        case Light.RED:
            return "Stop"
        case Light.GREEN:
            return "Go"
        case _:
            return "Slow down"
```
Always write the member with its class, like `Light.RED`: a bare name such as `case RED:` would not compare anything, it would just capture the value into a new variable `RED` and match everything.
The wildcard `case _:` is the default and must come last, because any pattern after it could never be reached.

---

Enum members are **hashable**, so they can be used as dictionary keys and as set elements.
A dictionary keyed by an enum is a clean way to attach data to each member, and looking it up with a member is safer than using a raw string that could be misspelled:
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
Since members can appear in any collection, everything you know about lists, sets and comprehensions works with them too:
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

A member value can be a **tuple**, which lets you attach several pieces of data to each member.
If the enum defines an `__init__` method, Python calls it once per member, unpacking the tuple into its parameters, so you can save each piece in its own attribute:
```python
from enum import Enum

class Planet(Enum):
    EARTH = (5.97, 6371)
    MARS = (0.64, 3390)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

print(Planet.MARS.radius)  # 3390
print(Planet.MARS.value)   # (0.64, 3390)
```
The `value` of the member stays the whole tuple.

---

Iterating over the class and looking members up by name work well together when you process data coming from outside, like log lines or a file.
A dictionary comprehension over the class prepares one entry per member, then `Level[name]` converts each incoming string to the matching member:
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
Because the enum keeps the declaration order, iterating over `counts` afterwards gives the members in that same order.

---

Besides regular methods, an enum can define **class methods** with `@classmethod`. They receive the enum class itself as `cls`, so they are the right place for alternative ways of finding a member:
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
Together with `auto()`, methods, properties and lookups, this lets you build enums that carry their own behaviour.
