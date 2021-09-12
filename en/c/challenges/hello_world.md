---
language: c
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ is the traditional first program for beginning programming in a new language or environment.

# --instructions--

Write a function that returns the string "Hello, World!".

# --seed--

```c
char* hello() {
  
}
```

# --before-asserts--

```c
#include <stdio.h>
#include <string.h>
#include <assert.h>

int main() {
```

# --asserts--

The function should return "Hello, World!".

```c
  assert((strcmp(hello(), "Hello, World!") == 0) && "--err-t1--");
```

# --after-asserts--

```c
  return 0;
}
```

# --solutions--

```c
char* hello() {
  return "Hello, World!";
}
```
