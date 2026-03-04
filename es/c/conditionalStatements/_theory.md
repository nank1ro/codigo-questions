La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple una cierta condición.
Supongamos que queremos jugar afuera solo si el clima es agradable.
En programación, podemos guardar una variable booleana `nice_weather` y realizar la acción de jugar afuera `if` esta variable es `true`, como:
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

Continuemos con el ejemplo anterior.
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```
Hemos visto que la sentencia `if` ejecuta el bloque de código solo si la condición es `true`.
Otra cosa importante a considerar está representada por los **corchetes** `{}` que indican un bloque de código.

---

Acabamos de ver cómo ejecutar un bloque de código si se cumple una condición, ahora veamos cómo ejecutar otro bloque de código si la primera condición falla.
Vamos a jugar afuera si el clima es agradable; de lo contrario, nos quedamos en casa.
En C podemos usar la sentencia `else`, como:
```c
bool nice_weather = false;
if (nice_weather) {
    // play outside
} else {
    // stay home
}
```

---

Supongamos que tenemos otra condición a verificar, como en este ejemplo:
```c
int num = 3;
if (num == 2) {
    printf("the number is 2\n");
} else if (num == 3) {
    printf("the number is 3\n");
} else {
    printf("do something else\n");
}
```
y el resultado de este código es `the number is 3`.
Primero, verifiquemos si el número es igual a 2, esto es falso.
Entonces, continuemos con la segunda sentencia y verifiquemos si `num` es igual a 3, siendo verdadero, ejecutamos el siguiente bloque de código imprimiendo `the number is 3`

---

Podemos añadir tantas sentencias `else if` como queramos, no hay límites
```c
int num = 4;
if (num == 2) {
    printf("the number is 2");
} else if (num == 3) {
    printf("the number is 3");
} else if (num == 4) {
    printf("the number is 4");
} else if (num == 5) {
    printf("the number is 5");
} else if (num == 6) {
    printf("the number is 6");
}
```
y el resultado de este código es `the number is 4`.

---

También podemos anidar una sentencia condicional (`if`, `else if` o `else`) dentro de otra sentencia condicional, para crear una estructura más compleja.
```c
int num = 4;
if (num < 3) {
    printf("the number is lower than 3\n");
} else {
    if (num == 3) {
        printf("the number is 3\n");
  } else if (num == 4) {
        printf("the number is 4\n");
  } else {
        printf("the number is greather than 4\n");
  }
}
```
y el resultado de este código es `the number is 4`.

---

La sentencia `if` es la base de las sentencias condicionales en C. Nos permite ejecutar un bloque de código solo si una condición es `true`. La sintaxis básica es:
```c
if (condición) {
    // código a ejecutar si la condición es true
}
```

---

Las condiciones booleanas utilizan valores `true` o `false`. En C, podemos usar estos valores directamente en una sentencia `if`. Cuando la condición es `true`, el bloque de código se ejecuta; cuando es `false`, se omite.

---

Así como podemos ejecutar código cuando una condición es `true`, también podemos prevenir que se ejecute cuando queremos que la condición sea `false`. Esto es útil para controlar el flujo del programa en diferentes escenarios.

---

Cuando queremos ejecutar código sin importar el estado de una condición, simplemente creamos una sentencia `if` con una condición que siempre es `true`. Esto garantiza que el bloque de código se ejecutará cada vez.

---

Ahora que conocemos la estructura básica de una sentencia condicional `if`, vamos a aprender a identificar sus componentes. La palabra clave `if` es fundamental para crear una sentencia condicional.

---

Es importante entender cómo se comporta el código cuando la condición es `true`. Cuando la condición se evalúa como `true`, el bloque de código dentro de la sentencia `if` se ejecuta.

---

De manera similar, cuando la condición es `false`, el bloque de código dentro de la sentencia `if` se omite y la ejecución continúa después de la sentencia condicional.

---

Las condiciones son valores booleanos que pueden ser `true` o `false`. Estos valores son los que determinan si un bloque de código debe ejecutarse o no.

---

Ahora practicaremos escribiendo una sentencia `if` completa. Necesitamos la palabra clave `if`, seguida de una condición entre paréntesis, y luego el bloque de código entre llaves.

---

La condición en una sentencia `if` debe estar siempre entre paréntesis redondos `()`. Esta es una parte esencial de la sintaxis en C.

---

Cuando queremos prevenir que un bloque de código se ejecute, podemos usar una condición `false`. Esto es útil para entender el flujo condicional del programa.

---

Practiquemos más con la sintaxis completa de una sentencia `if`. Recuerda que necesitas la palabra clave `if`, paréntesis alrededor de la condición, y llaves para delimitar el bloque de código.

---

Un bloque de código puede contener múltiples líneas de instrucciones. Todas las líneas dentro de las llaves se ejecutarán si la condición es `true`.

---

Las variables booleanas pueden usarse directamente como condiciones en una sentencia `if`. Si la variable tiene el valor `true`, el bloque se ejecuta; si tiene `false`, se omite.

---

Para asegurar que un bloque de código NO se ejecute, necesitamos que la variable booleana tenga el valor `false`. Esto nos permite controlar el flujo del programa según el estado de nuestras variables.

---

Es importante entender que solo el código dentro de las llaves de la sentencia `if` está condicionado. El código fuera de las llaves siempre se ejecuta, sin importar la condición.

---

Un bloque de código dentro de una sentencia `if` puede contener tantas líneas como sea necesario. No hay límite en la cantidad de instrucciones que puedes incluir entre las llaves.

---

Ahora que comprendemos cómo funcionan los bloques de código y las variables booleanas, veamos cómo se comporta el programa cuando una variable tiene el valor `true`.

---

De manera similar, cuando una variable booleana tiene el valor `false`, el bloque de código dentro de la sentencia `if` se omite completamente.
