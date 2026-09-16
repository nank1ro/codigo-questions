---
language: javascript
exerciseType: 1
difficulty: 1
title: ハミング距離
---

# --description--

DNAはヌクレオチドがつながったストランドとして書かれ、各ヌクレオチドは`A`、`C`、`G`、`T`のいずれか1文字で表されます。同じ長さの2本のストランドを横に並べると、同じヌクレオチドがくる位置もあれば、異なるヌクレオチドがくる位置もあります。

2本のストランドが異なる位置の数はハミング距離と呼ばれ、生物学者は2本のストランドがどれほど離れているかを測るためにこれを使います。`GAGCCTACTAACGGGAT`と`CATCGTAATGACGGCCT`を並べると7つの位置が異なるので、この2つのハミング距離は7です。

# --instructions--

同じ長さの2本のDNAストランドを受け取り、異なる位置の数を返す`hammingDistance`という関数を書いてください。

例:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 2本のストランドは常に同じ長さなので、異なる長さのストランドを扱う必要はありません。
- 2本の空のストランドはどこも異ならないため、その距離は0です。

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

2本の空のストランドはどこも異なりません

```javascript
tryCatch(hammingDistance("", "") === 0);
```

同じ1文字のヌクレオチドからなる2本のストランドには違いがありません

```javascript
tryCatch(hammingDistance("A", "A") === 0);
```

異なる1文字のヌクレオチドからなる2本のストランドは1つの位置で異なります

```javascript
tryCatch(hammingDistance("A", "G") === 1);
```

すべての位置で異なる2本の短いストランド

```javascript
tryCatch(hammingDistance("AG", "CT") === 2);
```

最初の位置だけが異なる2本の短いストランド

```javascript
tryCatch(hammingDistance("AT", "CT") === 1);
```

ストランドの途中にある1つの異なるヌクレオチド

```javascript
tryCatch(hammingDistance("GGACG", "GGTCG") === 1);
```

同じヌクレオチドでも位置が異なれば違いとして数えられます

```javascript
tryCatch(hammingDistance("TAG", "GAT") === 2);
```

4つの違いがある少し長いストランドのペア

```javascript
tryCatch(hammingDistance("GATACA", "GCATAA") === 4);
```

ストランドを1つ位置ずらすと、ほぼすべての位置が異なります

```javascript
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") === 9);
```

説明にある2本のストランドの距離は7です

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
