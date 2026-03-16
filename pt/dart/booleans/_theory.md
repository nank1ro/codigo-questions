Um __booleano__ é um tipo de dado que pode conter um dos dois valores: `true` ou `false`.
Em Dart, o tipo booleano é declarado com a palavra-chave `bool`.

```dart
bool isRaining = true;
```

A variável `isRaining` armazena o valor `true`, o que significa que está chovendo.
Os valores booleanos são sempre escritos em minúsculas: `true` e `false`.

---

Assim como qualquer outra variável, você pode imprimir um valor booleano com `print()`.
Quando você imprime um booleano, Dart exibe o texto `true` ou `false`.

```dart
bool isSunny = true;
print(isSunny); // true
```

---

Uma variável booleana também pode conter o valor `false`.
Use `false` quando algo não é o caso.

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

Assim como `true`, `false` deve ser escrito em minúsculas.

---

O __operador de negação__ `!` (também chamado de "não") inverte um valor booleano.
Aplicar `!` a `true` resulta em `false`, e aplicar `!` a `false` resulta em `true`.

```dart
bool isActive = true;
print(!isActive); // false
```

Isso é útil quando você quer verificar o oposto de uma condição.

---

Os booleanos são usados em toda a programação para representar condições e impulsionar decisões.
Sempre que seu programa precisa decidir entre duas possibilidades, um booleano está envolvido.

Exemplos:
- O usuário está conectado? (`isLoggedIn`)
- A porta está aberta? (`isDoorOpen`)
- O pedido foi enviado? (`isShipped`)
