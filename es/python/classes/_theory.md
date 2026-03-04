Python es un lenguaje de programación orientado a objetos, lo que significa que manipula construcciones de programación llamadas objetos.
Puedes pensar en un objeto como una única estructura de datos que contiene datos así como funciones; las funciones de un objeto se llaman sus métodos.
Por ejemplo, cuando llamas:
```python
dict_name.items()
```
Python verifica si `my_dict` tiene un método `items()` (que todos los diccionarios tienen) y ejecuta ese método si lo encuentra.

---

Una clase básica consiste solo en la palabra clave `class` y el nombre de la clase, por ejemplo:
```python
class ClassName:
    pass
```

---

Reemplacemos `pass` con algo más.
El método `__init__()` es requerido para las clases, y se usa para __inicializar__ los objetos que crea.
`__init__()` siempre toma al menos un argumento, `self`, que se refiere al objeto que se está creando.
Puedes pensar en `__init__()` como el método que arranca cada objeto que crea la clase.

---

Por supuesto, el método `__init__()` puede usar más parámetros que `self`

---

El primer argumento `__init__()` se usa para referirse al objeto de instancia, y por convención, ese argumento se llama `self`.
Si agregas argumentos adicionales (por ejemplo, un `gender` y `legs` para tu animal) configurando cada uno igual a `self.gender` y `self.legs` en el cuerpo de `__init__()` hará que cuando crees un objeto de instancia de tu clase `Animal`, necesites dar a cada instancia un género y patas, y esas se asociarán con la instancia particular que crees

---

Definir una clase no crea un objeto.
Para hacer eso, necesitamos crear una __instancia__ de una clase

---

Cuando una clase tiene sus propias funciones, esas funciones se llaman __métodos__. Ya has visto un método: `__init__()`.
¡Pero también puedes definir tus propios métodos!
