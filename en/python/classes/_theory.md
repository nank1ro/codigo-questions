Python is an object-oriented programming language, which means it manipulates programming constructs called objects.
You can think of an object as a single data structure that contains data as well as functions; the functions of an object are called its methods.
For example, when you call:
```python
dict_name.items()
```
Python checks to see if `my_dict` has an `items()` method (which all dictionaries have) and executes that method if it finds it.

---

A basic class consists only of the `class` keyword and the name of the class, for example:
```python
class ClassName:
    pass
```

---

Let's replace `pass` with something else.
The method `__init__()` is required for classes, and it's used to __initialize__ the objects it creates.
`__init__()` always takes at least one argument, `self`, that refers to the object being created.
You can think of `__init__()` as the method that boots up each object the class creates.

---

Of course, the `__init__()` method can use more parameters than `self`

---

The first argument `__init__()` is used to refer to the instance object, and by convention, that argument is called `self`.
If you add additional arguments (for instance, a `gender` and `legs` for your animal) setting each of those equal to `self.gender` and `self.legs` in the body of `__init__()` will make it so that when you create an instance object of your `Animal` class, you need to give each instance a gender and legs, and those will be associated with the particular instance you create

---

Defining a class doesn't create an object.
In order to do that, we need to create an __instance__ of a class

---

When a class has its own functions, those functions are called __methods__. You've already seen one such method: `__init__()`.
But you can also define your own methods!
