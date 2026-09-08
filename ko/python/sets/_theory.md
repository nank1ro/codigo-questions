**집합(set)**은 **고유한** 요소들의 컬렉션입니다: 같은 값을 아무리 여러 번 써도 한 번만 나타납니다.
집합은 또한 **순서가 없습니다**: 첫 번째나 마지막 요소라는 것이 없으므로, 인덱스로 요소를 읽을 수 없습니다.
집합은 값이 *몇 번* 나오는지, *어느 위치*에 있는지가 아니라 *어떤* 값이 있는지만 중요할 때 이상적입니다.
중괄호 `{...}` 사이에 요소를 작성하여 집합을 만듭니다:
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
중복된 `"red"`는 제거되므로, `len()`은 서로 다른 요소만 셉니다.

---

내장 함수 `set()`은 리스트나 문자열 같은 임의의 컬렉션으로부터 집합을 만듭니다.
집합은 각 값을 한 번만 유지하므로, 이는 **중복을 제거**하는 전형적인 방법입니다:
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
값이 존재하는지 확인하려면 `True` 또는 `False`를 반환하는 `in` 연산자를 사용하세요:
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
집합에 대한 멤버십 확인은 요소가 수천 개여도 매우 빠릅니다.

---

**빈 집합**을 만들 때는 함정이 있습니다.
중괄호는 딕셔너리의 문법이기도 해서, `{}`는 집합이 아니라 빈 **딕셔너리**를 만듭니다:
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
빈 집합을 얻으려면 인자 없이 `set()`을 호출해야 합니다:
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

집합은 **가변(mutable)**입니다: 만든 후에도 요소를 추가하고 제거할 수 있습니다.
`add(value)`는 값을 삽입합니다. 이미 존재하는 값을 추가해도 아무 변화가 없습니다:
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
요소를 제거하는 방법은 두 가지가 있습니다:
- `remove(value)`는 요소를 삭제하지만, 그 값이 집합에 없으면 `KeyError`를 발생시킵니다
- `discard(value)`는 값이 있으면 삭제하고, 없으면 에러 없이 **아무 일도 하지 않습니다**
```python
letters.remove("a")
letters.discard("z")  # "z" is not there, but no error
letters.remove("z")   # KeyError: 'z'
```

---

`pop()`은 집합에서 **임의의 요소**를 제거하고 그것을 반환합니다.
집합에는 순서가 없으므로 어떤 요소가 제거될지 선택할 수 없습니다. 빈 집합에서 `pop()`을 호출하면 `KeyError`가 발생합니다:
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()`는 **모든** 요소를 제거하여 빈 집합을 남깁니다:
```python
tickets.clear()
print(len(tickets))  # 0
```

---

리스트와 정확히 똑같이, `for`로 집합을 순회할 수 있습니다:
```python
for color in {"red", "blue"}:
    print(color)
```
집합은 순서가 없으므로 요소는 **어떤 순서로든** 나올 수 있으며, 그 순서는 실행할 때마다 바뀔 수도 있습니다.
예측 가능한 순서가 필요하면 집합을 `sorted()`에 전달하세요. 이는 요소를 정렬한 **리스트**를 반환합니다:
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

두 집합의 **합집합(union)**은 **둘 다**의 요소를 중복 없이 담은 새 집합입니다.
`|` 연산자나 `union()` 메서드를 사용하세요:
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
`a`도 `b`도 수정되지 않습니다: 집합 연산은 항상 새 집합을 반환합니다.

---

두 집합의 **교집합(intersection)**은 **둘 다**에 존재하는 요소만을 담습니다.
`&` 연산자나 `intersection()` 메서드를 사용하세요:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
두 집합에 공통 요소가 없으면 결과는 빈 집합입니다.

---

**차집합(difference)** `a - b`는 `a`의 요소 중 `b`에 **없는** 것들을 담습니다.
순서가 중요합니다: `a - b`와 `b - a`는 보통 다릅니다:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
**대칭차집합(symmetric difference)** `a ^ b`는 두 집합 중 **정확히 하나에만** 있는 요소들을 담습니다:
```python
print(a ^ b)  # {1, 4}
```
메서드 형태는 `difference()`와 `symmetric_difference()`입니다.

---

연산자와 메서드는 완전히 동등하지는 않습니다.
`|`, `&`, `-`, `^` 연산자는 **두** 피연산자가 모두 집합일 때만 작동합니다.
`union()`, `intersection()`, `difference()`, `symmetric_difference()` 메서드는 리스트나 문자열 같은 **모든 이터러블**을 받습니다:
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

집합끼리 **비교**할 수도 있습니다.
`a.issubset(b)` 또는 `a <= b`는 `a`의 모든 요소가 `b`에도 있을 때 `True`입니다.
`a.issuperset(b)` 또는 `a >= b`는 `a`가 `b`의 모든 요소를 포함할 때 `True`입니다.
`a.isdisjoint(b)`는 두 집합에 공통 요소가 **하나도 없을** 때 `True`입니다:
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

집합은 **해시 가능한** 요소, 즉 변경할 수 없는 값만 담을 수 있습니다: 숫자, 문자열, `True`/`False`, 그리고 **튜플**입니다.
리스트, 딕셔너리, 또는 다른 집합을 추가하려고 하면 `TypeError`가 발생합니다:
```python
points = set()
points.add((1, 2))  # ok, a tuple
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
튜플의 집합은 좌표나 (name, age) 같은 고유한 쌍을 관리하는 데 편리합니다:
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

**frozenset**은 **불변(immutable)** 집합입니다: 한 번 만들면 요소를 추가하거나 제거할 수 없습니다.
어떤 컬렉션으로부터든 `frozenset()`으로 만들 수 있습니다:
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
frozenset을 출력하면 `frozenset({'sat', 'sun'})`처럼 요소 주위에 타입 이름이 표시됩니다.
변경할 수 없으므로 frozenset은 해시 가능합니다: 일반 집합과 달리 다른 집합의 요소나 딕셔너리의 키가 될 수 있습니다.
읽기 전용 연산(`in`, `len()`, `|`, `&`, `-`, `^`, 비교)은 모두 평소처럼 동작합니다.

---

**집합 컴프리헨션(set comprehension)**은 리스트 컴프리헨션과 같은 문법이지만 중괄호를 사용해, 하나의 표현식으로 집합을 만듭니다:
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
선택적인 `if`로 요소를 걸러낼 수 있으며, 표현식으로 인해 생기는 중복은 자동으로 제거됩니다:
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

집합 연산은 새 집합을 반환하는 대신 집합을 **제자리에서(in place)** 수정할 수도 있습니다.
`update(iterable)`은 어떤 컬렉션의 모든 요소를 추가합니다. `add()`와 비슷하지만 한 번에 여러 값을 추가할 수 있습니다:
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
복합 대입 연산자도 제자리에서 동작합니다: `|=`는 다른 집합의 요소를 추가하고, `&=`는 공통 요소만 남기며, `-=`는 다른 집합의 요소를 제거합니다:
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

두 집합은 작성된 순서와 상관없이 같은 요소를 담고 있으면 **같습니다**:
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
컬렉션의 길이와 그 집합의 길이를 비교하는 것은 중복을 빠르게 발견하는 방법입니다: 집합이 **더 작다면**, 어떤 값이 두 번 이상 나온 것입니다:
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
리스트 메서드 `count(value)`는 어떤 값이 몇 번 나오는지 알려주므로, *어떤* 값이 중복되었는지 찾는 데 도움이 됩니다.
