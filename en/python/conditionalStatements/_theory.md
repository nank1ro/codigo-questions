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
