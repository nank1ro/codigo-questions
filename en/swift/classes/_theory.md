Swift is an object-oriented programming language, which means it manipulates programming constructs called objects.
You can think of an object as a single data structure that contains data as well as functions; the functions of an object are called its methods.
For example, when you call:
```swift
dictName.removeValue(forKey: "keyName")
```
Swift checks to see if `dictName` has a `removeValue()` method (which all dictionaries have) and executes that method if it finds it.

---

_Structures_ and _classes_ are general-purpose, flexible constructs that become the building blocks of your program's code.
A basic class|struct consists only of the `class` or `struct` keyword and its name, for example:
```swift
class ClassName {
	// class definition
}
struct ClassName {
	// structure definition
}
```

---

Let's put something inside our `Animal` class

---

Defining a class doesn't create an object.
In order to do that, we need to create an __instance__ of a class

---

When a class has its own functions, those functions are called __methods__.

---

Structures and classes in Swift have many things in common. Both can:
- Define properties to store values
- Define methods to provide functionality
- Define subscripts to provide access to their values using subscript syntax
- Define initializers to set up their initial state
- Be extended to expand their functionality beyond a default implementation
- Conform to protocols to provide standard functionality of a certain kind

But classes have additional capabilities that structures don't have:
- Inheritance enables one class to inherit the characteristics of another
- Type casting enables you to check and interpret the type of a class instance at runtime
- Deinitializers enable an instance of a class to free up any resources it has assigned
- Reference counting allows more than one reference to a class instance

---

You can access the properties of an instance using _dot syntax_.
In dot syntax, you write the property name immediately after the instance name, separated by a period `.`, without any spaces:
```swift
someInstance.someProperty
```
Using the same syntax we can also update the value of a property

---

One advantage of structures is that have an automatically generated memberwise initializer, which you can use to initialize the member properties of new structure instances.
Initial values for the properties of the new instance can be passed to the memberwise initializer by name
