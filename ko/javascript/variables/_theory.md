변수는 데이터 값을 저장하는 컨테이너입니다.
JavaScript에서 모든 변수는 객체입니다.
변수를 만들려면 공백을 포함하지 않는 **이름**을 지정해야 합니다.
변수는 처음으로 값을 할당하는 순간 생성됩니다.
JavaScript에서는 `let` 또는 `const` 키워드로 상수를 선언하고, `var` 키워드로 변수를 선언합니다.
상수의 값은 한 번 설정하면 변경할 수 없지만, 변수는 나중에 다른 값으로 설정할 수 있습니다.
`x`라는 이름의 변수를 생성하는 예시는 다음과 같습니다:
```javascript
var x = 1;
```
이렇게 하면 `x`라는 이름의 변수에 값 `1`을 할당한 것입니다.
변수 `x`를 출력하면 숫자 `1`을 돌려받습니다:
```javascript
console.log(x);
// prints 1
```

---

변수는 저장된 값이 변경될 수 있기 때문에 이렇게 불립니다.
`=`를 사용하여 `x`에 새로운 값을 할당할 수 있습니다.
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

다른 변수의 값을 변수에 할당할 수도 있습니다.
여기서 `y` 변수에 `x`의 값을 할당할 수 있습니다.
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

변수를 업데이트하면 이전 값은 사라집니다.
여기서 `x` 변수를 두 번 출력하여 값이 어떻게 업데이트되는지 확인할 수 있습니다.
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

JavaScript에서 문자열 변수는 큰따옴표와 작은따옴표 모두를 사용하여 선언할 수 있습니다:
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

여러 단어로 된 변수 이름을 만들려면 **카멜 케이스(camelCase)**를 사용합니다.
이것은 구문 중간에 있는 각 단어의 첫 글자를 대문자로 쓰는 방식입니다.
