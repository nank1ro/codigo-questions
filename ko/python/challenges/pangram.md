---
language: python
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

팬그램은 영어 알파벳의 모든 문자를 적어도 한 번씩 사용하는 문장입니다. 가장 잘 알려진 예는 "the quick brown fox jumps over the lazy dog"이며, 26개의 문자를 모두 아홉 개의 짧은 단어에 담고 있습니다.

이 검사는 대소문자를 구분하지 않으므로 `A`와 `a`는 같은 문자로 셉니다. 숫자, 문장 부호, 공백은 무시됩니다. 이들은 문자가 아니지만, 문장을 거부할 이유도 되지 않습니다.

# --instructions--

문장을 받아 그 문장이 팬그램이면 `True`를, 그렇지 않으면 `False`를 반환하는 함수 `is_pangram`를 작성하세요.

예시:
```
is_pangram("the quick brown fox jumps over the lazy dog") ➞ True
is_pangram("the five boxing wizards jump quickly") ➞ True
is_pangram("a quick movement of the enemy will jeopardize five gunboats") ➞ False
```

- 빈 문장은 팬그램이 아닙니다.
- `a`부터 `z`까지의 26개 문자만 셉니다.

# --seed--

```python
def is_pangram(sentence):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

빈 문장은 팬그램이 아니다

```python
    def test1(self):
        self.assertEqual(is_pangram(""), False, "--err-t1--")
```

고전적인 문장 "the quick brown fox jumps over the lazy dog"는 팬그램이다

```python
    def test2(self):
        self.assertEqual(is_pangram("the quick brown fox jumps over the lazy dog"), True, "--err-t2--")
```

문자 `x`가 빠진 문장은 팬그램이 아니다

```python
    def test3(self):
        self.assertEqual(is_pangram("a quick movement of the enemy will jeopardize five gunboats"), False, "--err-t3--")
```

문장 "the five boxing wizards jump quickly"는 팬그램이다

```python
    def test4(self):
        self.assertEqual(is_pangram("the five boxing wizards jump quickly"), True, "--err-t4--")
```

밑줄은 무시되므로 그 문장은 여전히 팬그램이다

```python
    def test5(self):
        self.assertEqual(is_pangram("the_quick_brown_fox_jumps_over_the_lazy_dog"), True, "--err-t5--")
```

숫자는 무시되므로 그 문장은 여전히 팬그램이다

```python
    def test6(self):
        self.assertEqual(is_pangram("the 1 quick brown fox jumps over the 2 lazy dogs"), True, "--err-t6--")
```

숫자는 문자 `e`, `i`, `t`를 대신하지 않는다

```python
    def test7(self):
        self.assertEqual(is_pangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog"), False, "--err-t7--")
```

대문자로 된 문장도 팬그램이다

```python
    def test8(self):
        self.assertEqual(is_pangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG"), True, "--err-t8--")
```

알파벳의 같은 절반의 대소문자를 섞는 것만으로는 충분하지 않다

```python
    def test9(self):
        self.assertEqual(is_pangram("abcdefghijklm ABCDEFGHIJKLM"), False, "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_pangram(sentence):
    letters = set()

    for char in sentence.lower():
        if "a" <= char <= "z":
            letters.add(char)

    return len(letters) == 26
```
