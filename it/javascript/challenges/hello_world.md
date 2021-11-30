---
language: javascript
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ è il primo programma tradizionale per iniziare a programmare in un nuovo linguaggio o ambiente.

# --instructions--

Scrivi una funzione che restituisce `"Hello, World!"`.

# --seed--

```javascript
function hello() {
  
}
```

# --asserts--

La funzione deve restituire "Hello, World!".

```javascript
  console.assert(hello() == "Hello, World!", "--err-t1--");
```

# --solutions--

```javascript
function hello() {
  return "Hello, World!"
}
```
