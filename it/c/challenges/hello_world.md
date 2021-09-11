---
language: c
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ è il primo programma tradizionale per iniziare a programmare in un nuovo linguaggio o ambiente.

# --instructions--

Scrivi una funzione che restituisce "Hello, World!".

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
