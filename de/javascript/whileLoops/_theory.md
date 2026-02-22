Often in programming, we need to repeat a block of code, for example:
```javascript
console.log("2 seconds");
console.log("3 seconds");
console.log("4 seconds");
console.log("5 seconds");
```
This produces the following output:
```javascript
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviously, for long statements we would spend a lot of time writing the code, but fortunately, we can use loops.
Let's learn the `while` loop, getting the same output above.
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
So we created a variable `count` assigning `2`, the initial value.
Then we have used the `while` statement that will run the block of code until the condition `count <= 5` is `true`.
Inside the block of code, we should **NOT** miss to add the line `count += 1`.
It increments the `count` value, otherwise, our loop will be infinite

---

To control the times a `while` loop repeats, we start with a variable set to a number.
We call this variable a counter variable

---

Then, we use a comparison in the condition to compare the `counter` variable to a number.

---

Inside the block of code, in order to stop the `while` loop, we increment the `counter` variable.

---

The order you write code affects the output.

---

In JavaScript we also have the **do-while** variation of the `while` loop.
It performs a single pass through the loop block first, _before_ considering the loop's condition.
It then continues to repeat the loop until the condition is `false`.
