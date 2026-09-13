**정규 표현식(regular expression)**은 텍스트를 기술하는 작은 패턴 언어입니다. Python은 표준 `re` 모듈을 통해 이를 제공합니다:
```python
import re
```

`re.search(pattern, text)`는 패턴을 텍스트 어디에서나 찾습니다. 무언가를 찾으면 **매치 객체(match object)**를 반환하고, 찾지 못하면 `None`을 반환합니다. `match.group()`은 매치된 텍스트 조각을 되돌려줍니다:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

여기서는 패턴의 두 요소가 역할을 합니다. `\d`는 *임의의 숫자 하나*를 의미하고, `+`는 *앞 항목이 하나 이상*을 의미하므로, `\d+`는 "하나 이상의 숫자"로 읽습니다. 그 밖의 유용한 축약 표현으로는 `\w`(문자, 숫자 또는 밑줄)와 `\s`(공백, 탭 또는 줄바꿈)가 있습니다.

패턴은 따옴표 앞에 `r`을 붙인 **로우 문자열(raw string)**로 작성합니다. 일반 Python 문자열에서는 백슬래시가 이스케이프 시퀀스를 시작하므로, `"\d"`는 언젠가 문제가 될 경고이고 `"\n"`은 정규 표현식 엔진이 기대하는 두 문자가 아니라 실제 줄바꿈이 되어버립니다. `r` 접두사는 백슬래시를 다시 평범한 문자로 되돌리므로, `r"\d"`는 엔진이 받는 문자 그대로입니다. 패턴에는 항상 `r"..."`를 사용하세요.

---

`re.search`는 텍스트 전체를 훑지만, `re.match`는 패턴을 **맨 앞**에서만 시도합니다:
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

둘 다 매치되는 것이 없으면 `None`을 반환하고, 매치 객체는 언제나 참으로 평가되므로, "매치되었는가?"를 묻는 일반적인 방법은 단순한 `if`입니다:
```python
if re.search(r"\d", text):
    print("there is a digit")
```
실제 `True`나 `False`가 필요할 때는 `is not None`과 비교하거나 호출을 `bool(...)`로 감싸세요.

---

세 번째 진입점인 `re.fullmatch`는 패턴이 첫 문자부터 마지막 문자까지 텍스트 **전체**를 덮을 때만 성공합니다. 검증에 알맞은 도구입니다:
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

즉, 세 함수는 패턴이 위치할 수 있는 곳만 다릅니다: `re.match`는 텍스트의 시작, `re.search`는 텍스트 어디든, `re.fullmatch`는 텍스트 전체입니다.

---

매치 객체는 매치된 텍스트 이상의 정보를 담고 있습니다. `.group()` 외에도 원본 문자열 안에서 매치의 위치를 알려줍니다:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()`는 매치된 첫 문자의 인덱스, `.end()`는 마지막 문자 바로 다음 인덱스이고, `.span()`은 둘을 튜플로 반환합니다. 즉, `text[match.start():match.end()]`는 항상 `match.group()`과 같습니다.

`re.search`는 `None`을 반환할 수 있으므로, 매치되지 않았을 때 `.group()`을 바로 읽으면 `AttributeError`가 발생합니다. 먼저 결과를 확인하세요.

---

패턴 안의 둥근 괄호는 **캡처 그룹(capture group)**을 만듭니다. 캡처 그룹은 매치의 일부로, 따로따로 읽어올 수 있습니다. 그룹은 `1`부터 시작해 왼쪽에서 오른쪽으로 번호가 매겨집니다:
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)`은 `match.group()`과 똑같이 전체 매치이고, `match.groups()`는 모든 그룹을 튜플로 반환합니다. 존재하지 않는 그룹 번호를 요청하면 `IndexError`가 발생합니다.

---

괄호를 세어 그룹 `3`을 찾는 일은 금방 지겨워집니다. 그룹에는 `(?P<name>...)`로 이름을 붙일 수 있고, 이름 붙은 그룹은 `match.group("name")`으로 읽을 수 있습니다:
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()`는 이름 붙은 모든 그룹을 딕셔너리로 반환합니다. 이름 붙은 그룹도 번호를 그대로 유지하므로 `match.group(1)`은 여전히 동작합니다.

이 예제는 중괄호를 사용하는 **수량자(quantifier)**도 씁니다: `\d{2}`는 정확히 두 개의 숫자, `\d{2,4}`는 두 개에서 네 개 사이, `\d{2,}`는 두 개 이상을 의미합니다. 이들은 `+`(하나 이상), `*`(0개 이상), `?`(0개 또는 하나)의 정밀한 버전입니다.

---

대괄호는 **문자 클래스(character class)**를 정의합니다. 문자 클래스는 문자들의 집합으로, 해당 위치에서 그중 무엇이든 하나가 받아들여집니다. `[aeiou]`는 모음 하나, `[0-9]`는 숫자 하나, `[a-z]`는 소문자 하나와 일치합니다. 여는 괄호 바로 뒤에 `^`이 오면 의미가 뒤집혀, `[^0-9]`는 숫자가 *아닌* 것과 일치합니다.

클래스 밖에서 `^`와 `$`는 **앵커(anchor)**입니다. `^`는 패턴을 텍스트의 시작에 묶고 `$`는 끝에 묶습니다. `re.fullmatch`에서는 앵커가 암묵적이기 때문에 검증이 더 자연스럽게 읽힙니다:
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search`는 첫 번째 매치에서 멈춥니다. 대신 `re.findall(pattern, text)`는 **모든** 매치를 수집하여 문자열의 리스트로 반환합니다:
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
매치되는 것이 없으면 리스트는 비어 있으므로 확인할 `None`이 없습니다. 바로 반복하거나 `len(...)`으로 개수를 셀 수 있습니다. `findall`은 매치 객체가 아니라 평범한 문자열을 반환하므로 위치는 구할 수 없다는 점에 유의하세요.

---

모든 매치의 위치나 그룹이 필요할 때는 `re.finditer(pattern, text)`가 알맞은 선택입니다. 텍스트를 훑으면서 매치마다 **매치 객체**를 하나씩 내어 줍니다:
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer`는 리스트가 아니라 이터레이터를 만들므로 `for` 반복문이나 컴프리헨션에서 쓸 수 있습니다. `findall`이 텍스트만 주는 반면, `finditer`는 매치 객체가 아는 모든 것을 줍니다.

---

패턴에 캡처 그룹이 들어 있으면 `findall`은 태도를 바꿉니다. 그룹이 정확히 하나면 전체 매치 대신 그 그룹의 내용을 반환하고, 둘 이상이면 매치마다 그룹들의 튜플을 반환합니다:
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
이 점은 기억해 둘 만합니다. 단지 묶기 위해 패턴에 괄호를 추가하면 `findall`이 반환하는 것이 조용히 바뀝니다. `re.finditer`는 절대 이렇게 동작하지 않는데, 매치 객체는 언제나 전체 매치와 그룹을 모두 가지고 있기 때문입니다.

---

`re.sub(pattern, replacement, text)`는 모든 매치가 치환된 새 문자열을 반환합니다. 문자열은 불변이므로 원래 텍스트는 그대로 남습니다:
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

치환 문자열에서는 `\1`, `\2`, ... (이름 붙은 그룹은 `\g<name>`)로 캡처 그룹을 되짚어 참조할 수 있어서 텍스트 재배치가 한 줄이면 끝납니다. 치환 문자열도 같은 백슬래시 이유로 raw 문자열로 씁니다:
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
`count` 인자는 치환할 매치의 개수를 제한합니다. `re.sub(r"\d", "#", "1 2 3", count=1)`은 `# 2 3`을 줍니다.

---

`re.sub`에 주는 치환 값은 **함수**일 수도 있습니다. 이 함수는 매치마다 한 번씩 호출되어 매치 객체를 받고, 그 자리에 넣을 문자열을 반환해야 합니다. 이렇게 하면 치환 결과가 매치된 내용에 따라 달라질 수 있습니다:
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
함수는 괄호 없이 이름으로 전달합니다. `shout(match)`라고 쓰면 `re.sub`에 건네주는 대신 즉시 호출해 버립니다.

---

`str.split`은 고정된 구분자로만 자를 수 있습니다. `re.split(pattern, text)`는 패턴이 설명하는 무엇으로든 자를 수 있는데, 지저분한 입력에는 보통 이런 것이 필요합니다:
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
구분자를 `[,;\s]+`로 쓰면 쉼표, 세미콜론, 공백이 연달아 나오는 묶음 전체가 한 번의 자르기로 취급되어, 그 사이에 빈 문자열이 남지 않습니다.

`maxsplit` 인자는 정해진 횟수만큼 자른 뒤 멈추고 나머지 텍스트를 마지막 요소에 남깁니다. `re.split(r"\s+", "a b c", maxsplit=1)`은 `['a', 'b c']`를 줍니다.

---

`re.search`나 `re.findall`을 호출할 때마다 내부 캐시에서 패턴 문자열을 먼저 찾아봐야 합니다. `re.compile(pattern)`은 그 조회를 건너뛰고 같은 메서드들을 가진 **패턴 객체**를 반환합니다:
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
패턴은 이미 객체 안에 들어 있으므로 남는 인자는 텍스트뿐입니다. 같은 패턴을 여러 번, 예를 들어 반복문 안에서 쓸 때 컴파일이 이득이 되고, 패턴에 무엇과 일치하는지 설명하는 이름을 붙여 주기도 합니다.

---

**플래그(flag)**는 패턴이 적용되는 방식을 바꿉니다. `re`의 모든 함수는 플래그를 `flags` 인자로 받고, `re.compile`은 플래그를 패턴 객체에 저장합니다:
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
가장 많이 쓰이는 둘은 글자가 대소문자 구분 없이 일치하게 하는 `re.IGNORECASE`와, `^`와 `$`가 텍스트 전체가 아니라 각 줄의 시작과 끝에서 일치하게 하는 `re.MULTILINE`입니다. 여러 플래그는 `re.IGNORECASE | re.MULTILINE`처럼 `|`로 결합합니다.

플래그는 일치 규칙만 바꿉니다. 반환되는 텍스트는 언제나 실제로 거기 있던 텍스트이며 원래의 대소문자를 그대로 유지합니다.
