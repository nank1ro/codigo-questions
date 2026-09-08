**문자열(string)**은 텍스트의 한 조각으로, 따옴표로 둘러싸인 문자의 나열입니다.
Python은 작은따옴표 `'...'` 와 큰따옴표 `"..."` 를 모두 지원하며, 둘은 완전히 동일하게 동작합니다:
```python
name = 'Ada'
language = "Python"
```
텍스트 자체에 따옴표가 포함되어 있을 때는 어떤 것을 선택하는지가 중요해집니다.
작은따옴표 안에 아포스트로피가 있으면 문자열이 너무 일찍 끝나버리므로, 그런 텍스트는 큰따옴표로 감싸야 합니다:
```python
print("It's sunny")  # It's sunny
```

---

내장 함수 `len()`은 문자열의 **길이**, 즉 문자열이 포함하는 문자의 개수를 반환합니다.
공백과 문장부호도 문자로 취급됩니다:
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

문자열의 각 문자는 **인덱스(index)**라는 위치를 가집니다.
인덱스는 `1`이 아니라 `0`부터 시작합니다: 첫 번째 문자는 인덱스 `0`, 두 번째는 인덱스 `1`, 이런 식으로 이어집니다.
문자열 뒤에 대괄호로 인덱스를 적으면 문자 하나를 읽을 수 있습니다:
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
`word[6]`처럼 존재하지 않는 인덱스를 요청하면 `IndexError`가 발생합니다.

---

인덱스는 **음수**일 수도 있습니다: 이 경우 문자열의 끝에서부터 셉니다.
`-1`은 마지막 문자, `-2`는 그 앞의 문자, 이런 식으로 이어집니다:
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
이는 문자열의 길이를 몰라도 끝에 도달할 수 있어 편리합니다.

---

**슬라이스(slice)**는 문자열의 일부를 추출합니다.
대괄호 안에 `[start:end]`를 적으면, `start` 위치의 문자는 포함되고 `end` 위치의 문자는 **제외**됩니다:
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
`start`를 생략하면 처음부터, `end`를 생략하면 끝까지 슬라이스할 수 있습니다:
```python
print(word[:2])  # py
print(word[2:])  # thon
```
슬라이싱은 에러를 발생시키지 않습니다: `end`가 길이보다 크면 그냥 마지막 문자에서 멈춥니다.

---

`+`가 두 문자열을 연결(**concatenation**)한다는 것은 이미 알고 있습니다.
`*` 연산자는 문자열을 지정한 횟수만큼 **반복**합니다:
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
반복은 구분선이나 간단한 패턴을 빠르게 그리는 방법입니다.

---

`in` 연산자는 어떤 문자열이 다른 문자열을 **포함**하는지 확인합니다.
`True` 또는 `False`를 반환하므로 `if` 안에서 자연스럽게 사용할 수 있습니다:
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in`은 반대의 검사를 수행합니다.

---

문자열에는 많은 내장 **메서드(method)**가 있습니다: 문자열 뒤에 점을 찍어 호출하는 함수입니다.
`upper()`는 텍스트를 대문자로, `lower()`는 소문자로 반환합니다:
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
이 메서드들은 **새 문자열을 반환**한다는 점에 주의하세요: 원래의 `word`는 변경되지 않습니다.
`lower()`는 대소문자를 무시하고 텍스트를 비교할 때 자주 사용됩니다: `"Yes".lower() == "yes"`.

---

문자열은 **불변(immutable)**입니다: 한 번 만들어지면 그 문자들을 바꿀 수 없습니다.
인덱스에 대입하면 `TypeError`가 발생합니다:
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
문자열을 "바꾸려면" 예를 들어 슬라이스와 연결을 사용해 새 문자열을 만들고, 그것을 변수에 저장해야 합니다:
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

사용자가 입력한 텍스트에는 앞뒤에 불필요한 공백이 붙어 있는 경우가 많습니다.
`strip()` 메서드는 **앞뒤 공백**(스페이스, 탭, 줄바꿈)이 제거된 문자열의 복사본을 반환합니다:
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
텍스트 중간의 공백은 그대로 유지됩니다.
`lstrip()`은 왼쪽만, `rstrip()`은 오른쪽만 제거합니다.

---

`split()`은 문자열을 조각들의 **리스트**로 나눕니다.
인자가 없으면 공백을 기준으로 나누고, 인자가 있으면 그 구분자를 기준으로 나눕니다:
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()`은 그 반대로, 리스트의 항목들을 하나의 문자열로 이어붙입니다.
이것은 **구분자**에 대해 호출되며, 리스트는 인자로 전달됩니다:
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)`는 `old`가 나타나는 **모든** 곳을 `new`로 바꾼 문자열의 복사본을 반환합니다:
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
문자열은 불변이므로, 결과를 유지하고 싶다면 반드시 저장해야 한다는 점을 기억하세요.

---

`find(sub)`는 `sub`가 처음 나타나는 위치의 **인덱스**를 반환하며, 찾지 못하면 `-1`을 반환합니다:
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)`는 `sub`가 **몇 번** 나타나는지를 반환합니다:
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)`와 `endswith(suffix)`는 문자열이 어떻게 시작하고 끝나는지에 따라 `True` 또는 `False`를 반환합니다:
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
이들은 파일 확장자, 프로토콜, 접두사를 확인하는 일반적인 방법입니다.

---

일부 문자는 문자열 안에 직접 입력할 수 없습니다.
**이스케이프 시퀀스(escape sequence)**는 백슬래시 `\` 뒤에 문자나 기호가 이어져 특수 문자를 나타내는 것입니다:

- `\n` 줄바꿈
- `\t` 탭
- `\"` 큰따옴표 문자열 안의 큰따옴표
- `\'` 작은따옴표 문자열 안의 작은따옴표
- `\\` 백슬래시 문자 자체

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
다음과 같이 출력됩니다:
```
Line 1
Line 2
She said "hi"
```
각 이스케이프 시퀀스는 두 글자를 입력해도 **한** 글자로 취급됩니다.

---

**여러 줄**에 걸친 문자열은 **삼중 따옴표** `"""..."""`(또는 `'''...'''`)로 작성할 수 있습니다.
따옴표 안의 모든 줄바꿈은 문자열의 일부가 되므로 `\n`이 필요 없습니다:
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
다음과 같이 출력됩니다:
```
Roses are red,
Violets are blue
```
삼중 따옴표 문자열에는 작은따옴표와 큰따옴표를 자유롭게 포함할 수도 있습니다.

---

모든 문자열 메서드는 새 문자열을 반환하므로, 메서드를 차례로 **연결(chain)**할 수 있습니다.
각 호출은 이전 결과에 대해 동작합니다:
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
슬라이스는 세 번째 값인 **스텝(step)**도 받을 수 있습니다.
스텝 `-1`은 문자열을 거꾸로 훑는 것으로, 문자열을 뒤집는 대표적인 방법입니다:
```python
print("abc"[::-1])  # cba
```

---

**슬러그(slug)**는 제목을 URL에 적합한 형태로 만든 것입니다: 소문자로, 앞뒤 공백 없이, 단어는 대시로 구분됩니다. 예: `hello-world`.
슬러그를 만드는 것은 지금까지 배운 메서드 `strip()`, `lower()`, `replace()`를 연결하는 것일 뿐입니다.
