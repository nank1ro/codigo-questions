Python es un lenguaje de programación orientado a objetos, lo que significa que manipula construcciones de programación llamadas objetos.
Puedes pensar en un objeto como una estructura de datos única que contiene datos así como funciones; las funciones de un objeto se llaman sus métodos.
Por ejemplo, cuando llamas:
```python
nombre_diccionario.items()
```
Python verifica si `mi_diccionario` tiene un método `items()` (todos los diccionarios tienen uno) y ejecuta ese método si lo encuentra.

---

Por supuesto, el método `__init__()` puede usar más parámetros que `self`

---

El primer argumento `__init__()` se usa para referirse al objeto de instancia, y por convención, ese argumento se llama `self`.
Si agregas argumentos adicionales (por ejemplo, un `genero` y `patas` para tu animal) establecer cada uno de ellos igual a `self.genero` y `self.patas` en el cuerpo de `__init__()` hará que cuando crees un objeto de instancia de tu clase `Animal`, necesites dar a cada instancia un genero y patas, y esos estarán asociados con la instancia particular que crees

---

Reemplacemos `pass` con algo más.
El método `__init__()` es obligatorio para las clases, y se usa para __inicializar__ los objetos que crea.
`__init__()` siempre toma al menos un argumento, `self`, que se refiere al objeto que se está creando.
Puedes pensar en `__init__()` como el método que inicia cada objeto que crea la clase.

---

Python es un lenguaje de programación orientado a objetos, lo que significa que manipula construcciones de programación llamadas objetos.
Puedes pensar en un objeto como una única estructura de datos que contiene datos así como funciones; las funciones de un objeto se llaman sus métodos.
Por ejemplo, cuando llamas:
```python
nombre_diccionario.items()
```
Python comprueba si `mi_diccionario` tiene un método `items()` (que todos los diccionarios tienen) y ejecuta ese método si lo encuentra.
