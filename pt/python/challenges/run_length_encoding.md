---
language: python
exerciseType: 1
difficulty: 2
title: Codificação run-length
---

# --description--

A codificação run-length é um dos truques de compressão mais antigos que existem: em vez de escrever o mesmo caractere repetidas vezes, você escreve quantas vezes ele se repete e, em seguida, o próprio caractere.

Uma máquina de fax que digitaliza uma página quase inteira em branco encontra longos trechos de pixels idênticos, de modo que uma fileira de doze `W` percorre a linha como o `12W`, bem mais curto. Quando um caractere aparece apenas uma vez, não há nada a ganhar ao contá-lo, então ele é copiado sozinho.

# --instructions--

Escreva uma função `encode_run` que recebe uma string `text` e retorna a sua codificação em run-length.

Cada sequência do mesmo caractere repetido duas ou mais vezes se torna o comprimento da sequência escrito em decimal, seguido desse caractere. Uma sequência de comprimento um é copiada como o único caractere, sem nenhum número na frente.

Exemplos:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- O texto contém apenas letras maiúsculas de `A` a `Z` e espaços.
- Uma sequência com mais de nove caracteres usa sua contagem decimal completa, de modo que doze `W` se tornam `12W` e nunca `9W3W`.
- Espaços são caracteres comuns: eles são contados e codificados exatamente como as letras.
- A string vazia é codificada como a string vazia.

# --seed--

```python
def encode_run(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

A string vazia é codificada como a string vazia

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

Um único caractere é copiado como ele mesmo

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

Uma string sem repetições passa inalterada

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

Uma sequência de dois se torna a contagem seguida do caractere

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

O exemplo misto "AABCCCDEEEE" se torna "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

Uma sequência de doze usa sua contagem decimal completa, então o resultado começa com "12W"

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

Sequências de espaços são codificadas exatamente como sequências de letras

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

Uma sequência de dez é escrita como "10A", nunca como duas sequências menores

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

Caracteres únicos alternados são todos copiados como eles mesmos

```python
    def test9(self):
        self.assertEqual(encode_run("ABABAB"), "ABABAB", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def encode_run(text):
    result = ""
    i = 0

    while i < len(text):
        run = 1
        while i + run < len(text) and text[i + run] == text[i]:
            run += 1
        if run > 1:
            result += str(run)
        result += text[i]
        i += run

    return result
```
