---
language: javascript
exerciseType: 1
difficulty: 1
title: 해밍 거리
---

# --description--

DNA는 각각 한 글자인 뉴클레오터드 가닥으로 표기합니다: `A`, `C`, `G` 또는 `T`. 같은 길이의 두 가닥을 나란히 놓으면 어떤 위치에는 같은 뉴클레오터드가 있고 어떤 위치에는 다른 뉴클레오터드가 있습니다.

두 가닥이 서로 다른 위치의 개수를 해밍 거리라고 하며, 생물학자들은 이를 이용해 두 가닥이 얼마나 멀어졌는지 측정합니다. `GAGCCTACTAACGGGAT`를 `CATCGTAATGACGGCCT`와 나란히 놓으면 서로 다른 위치가 7개이므로 두 가닥의 해밍 거리는 7입니다.

# --instructions--

같은 길이의 두 DNA 가닥을 받아 서로 다른 위치의 개수를 반환하는 함수 `hammingDistance`를 작성하세요.

예시:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 두 가닥은 항상 길이가 같으므로 길이가 다른 가닥을 처리할 필요는 없습니다.
- 두 빈 가닥은 어디에서도 다르지 않으므로 거리는 0입니다.

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function hammingDistance(left, right) {
  
}
```

# --asserts--

두 빈 가닥은 어디에서도 다르지 않습니다

```javascript
tryCatch(hammingDistance("", "") === 0);
```

같은 뉴클레오터드 하나를 가진 두 가닥에는 차이가 없습니다

```javascript
tryCatch(hammingDistance("A", "A") === 0);
```

다른 뉴클레오터드 하나를 가진 두 가닥은 한 위치에서 다릅니다

```javascript
tryCatch(hammingDistance("A", "G") === 1);
```

모든 위치에서 다른 두 짧은 가닥

```javascript
tryCatch(hammingDistance("AG", "CT") === 2);
```

첫 번째 위치에서만 다른 두 짧은 가닥

```javascript
tryCatch(hammingDistance("AT", "CT") === 1);
```

가닥 중간에 하나의 다른 뉴클레오터드

```javascript
tryCatch(hammingDistance("GGACG", "GGTCG") === 1);
```

위치가 다른 같은 뉴클레오터드도 차이로 계산됩니다

```javascript
tryCatch(hammingDistance("TAG", "GAT") === 2);
```

네 군데가 다른 더 긴 가닥 쌍

```javascript
tryCatch(hammingDistance("GATACA", "GCATAA") === 4);
```

가닥을 한 칸 밀면 거의 모든 위치가 달라집니다

```javascript
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") === 9);
```

설명에 나온 두 가닥의 거리는 7입니다

```javascript
tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") === 7);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function hammingDistance(left, right) {
  let distance = 0;

  for (let i = 0; i < left.length; i++) {
    if (left[i] !== right[i]) {
      distance++;
    }
  }

  return distance;
}
```
