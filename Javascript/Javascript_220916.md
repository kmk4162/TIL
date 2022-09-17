# 9/16

## 🟨 EMCA Script

### ✅ 코딩 스타일 가이드

- 코딩 스타일의 핵심은 합의된 원칙과 일관성
- 코딩 스타일은 코드의 품질에 직결되는 중요한 요소

  - 코드의 가독성, 유지보수 또는 팀원과의 커뮤니케이션 등 개발 과정 전체에 영향을 끼침

- 참고 : 다양한 자바스크립트 코딩 스타일 가이드
  - [GitHub - airbnb/javascript: JavaScript Style Guide](https://github.com/airbnb/javascript)
  - [Google JavaScript Style Guide](https://google.github.io/styleguide/jsguide.html)

<br>

### ✅ 변수와 식별자

- 식별자(identifier)는 변수를 구분할 수 있는 변수명을 말함
- 식별자는 반드시 문자, 달러($) 또는 밑줄(\_)로 시작
- 대소문자를 구분하며, `클래스명 외에는 모두 소문자로 시작`
- 예약어 사용 불가능
  - for, if, function 등등

<br>

### ✅ 선언, 할당, 초기화

- 선언 (Declaration)

  - 변수를 생성하는 행위 또는 시점

- 할당 (Assignment)

  - 선언된 변수에 값을 저장하는 행위 또는 시점

- 초기화 (Initialization)
  - 선언된 변수에 처음으로 값을 저장하는 행위 또는 시점

```javascript
# 선언
let foo
console.log(foo)
>>> undefined

# 할당
foo = 11
console.log(foo)
>>> 11

# 선언 + 할당
let bar = 0
console.log(bar)
>>> 0
```

<br>

### ✅ let, const

> let은 재할당 가능하지만 const는 재할당이 불가능
>
> 그런데 둘 다 `재선언`은 불가능!

- 선언은 var, const, let 키워드로 `자바스크립트 엔진에 변수의 존재를 알리는 것`

- 블록 스코프 (block scope)
  - if, for, 함수 등 중괄호
  - 블록 스코프를 가지는 변수는 블록 바깥에서 접근 불가능

```javascript
let x = 1;

if (x === 1) {
  let x = 2;
  console.log(x); // 2
}
console.log(x); // 1
```

> 블록 스코프 안에서 선언한 x와 밖에서 선언한 x는 다름. 블록 스코프 안에서 선언하면 그 변수는 저 블록 안에서만 종속되기 때문에, 외부에서 접근이 불가능함
>
> 그렇기 때문에 블록 안의 조건문 지난 후 console.log(x)를 하면 2가 아닌 1이 나옴

<br>

### ✅ var

- var는 재선언 및 재할당이 모두 가능
- ES6 이전에 변수 선언 시 사용하던 키워드
- 호이스팅 특성 가짐
  - 따라서 ES6 이후부터는 var 대신 const와 let을 사용하는 것을 권장
- 함수 스코프를 가짐
  - 함수의 중괄호 내부
  - 함수 스코프를 가지는 변수는 함수 바깥에서 접근이 불가능

> 스코프에 전역 스코프와 지역 스코프가 있고, 지역 스코프에 함수 스코프와 블록 스코프가 존재

<br>

### ✅ 호이스팅 (hoisting)

- 변수를 선언 이전에 참조할 수 있는 현상
- 변수 선언 이전의 위치에서 접근 시 undefined를 반환
- `자바스크립트는 모든 선언을 호이스팅한다!!`
- 즉, var, let, const 모두 호이스팅이 발생하지만, var는 선언과 초기화가 동시에 발생하여 일시적 사각지대가 존재하지 않음!

<br>

## 🟨 데이터 타입

### ✅ 데이터 타입

- 모든 값은 특정한 데이터 타입을 가짐
- 크게 원시 타입(Primitive type)과 참조 타입(Reference type)으로 분류됨

<br>

#### ✔️ 참조 타입(Reference type)

- 객체 (object) 타입의 자료형
- 변수에 해당 객체의 참조 값이 담김
- 다른 변수에 복사할 때 참조 값이 복사됨

#### ✔️ 원시 타입(Primitive type)

- 객체가 아닌 기본 타입
- 변수에 해당 타입의 값이 담김
- 다른 변수에 복사할 때 실제 값이 복사됨

<br>

##### 1. 숫자(Number) 타입

- 정수, 실수 구분 없는 하나의 숫자 타입
- 부동 소수점 형식을 따름
- `NaN(Not A Number)` : 계산 불가능한 경우 반환되는 값

<br>

##### 2. 문자열(String) 타입

- 텍스트 데이터를 나타내는 타입
- 16비트 유니코드 문자의 집합
- 작은따옴표 또는 큰따옴표 모두 가능
- 템플릿 리터럴 (Template Literal)
  - ES6부터 지원
  - 따옴표 대신 backtick()으로 표현
  - ${ expression } 형태로 표현식 삽입 가능 (파이썬에서 f-string과 유사)

```javascript
const firstName = "Kevin";
const lastName = "Durant";
const fullName = `${firstName} ${lastName}`;
console.log(fullName); // Kevin Durant
```

<br>

##### 3. undefined

- 변수의 값이 없음을 나타내는 데이터 타입
- 변수 선언 이후 직접 값을 할당하지 않으면, 자동으로 undefined가 할당됨

```javascript
let firstName;
console.log(firstName); // undefined
```

<br>

##### 4. null

- 변수의 값이 없음을 의도적으로 표현할 때 사용하는 데이터 타입

```javascript
let firstName = null;
console.log(firstName); // null
```

<br>

##### 5. Boolean 타입

- 논리적 참 또는 거짓을 나타내는 타입
- true / false
- 조건문 또는 반복문에서 유용하게 사용

```javascript
let isAdmin = true;
console.log(isAdmin); // true
```

<br>

## 🟨 연산자

### ✅ 할당 연산자

- 오른쪽에 있는 피연산자의 평가 결과를 왼쪽 피연산자에 할당하는 연산자
- =, +=, -=, \*=, /= 가능

<br>

### ✅ 비교 연산자

- 피연산자를 비교하고 결과값을 boolean으로 반환하는 연산자
- 문자열은 `유니코드` 값을 사용하며 표준 사전 순서를 기반으로 비교
- 예시) 알파벳끼리 비교할 경우
  - 알파벳 순서상 후순위가 더 크다
  - 소문자가 대문자보다 더 크다

<br>

### ✅ 동등 비교 연산자 (==)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 비교할 때 `암묵적 타입 변환`을 통해 타입을 일치시킨 후 같은 값인지 비교

  - 1004 == '1004' // true
  - 1004 + '1004' // 10041004 이런 느낌

- 예상치 못한 결과가 발생할 수 있으므로 특별한 경우를 제외하고 사용하지 않음

<br>

### ✅ 일치 비교 연산자 (===)

- 두 피연산자가 같은 값으로 평가되는지 비교 후 boolean 값을 반환
- 엄격한 비교가 이뤄지며 `암묵적 타입 변환이 발생하지 않음`
  - 엄격한 비교: 두 비교 대상의 `타입과 값 모두 같은지` 비교

```javascript
const a = 1004;
const b = "1004";
console.log(a === b); // false

const c = 1;
const d = true;
console.log(c === d); // false
```

<br>

### ✅ 논리 연산자

- 세 가지 논리 연산자로 구성

  - and 연산은 `&&`연산자를 이용
  - or 연산은 `||` 연산자를 이용
  - not 연산은 `!` 연산자를 이용

- 단축 평가 지원
  - false && true => false
  - true || false => true

<br>

### ✅ 삼항 연산자

- 세 개의 피연산자를 사용하여 조건에 따라 값을 반환하는 연산자
- 가장 왼쪽의 조건식이 참이면 콜론(:) 앞의 값을 사용하고 그렇지 않으면 콜론(:) 뒤의 값을 사용
- 삼항 연산자의 결과 값이기 때문에 변수에 할당 가능

```javascript
console.log(true ? 1 : 2); // 1
console.log(false ? 1 : 2); // 2
const result = Math.PI > 4 ? "Yes" : "No";
console.log(result); // No
```

<br>

## 🟨 조건문

### ✅ 조건문의 종류와 특징

- `if` statement
  - 조건 표현식의 결과값을 Boolean 타입으로 변환 후 참/거짓을 판단
  - 조건은 소괄호(condition) 안에 작성
  - 실행할 코드는 중괄호{} 안에 작성
  - 블록 스코프 생성

```javascript
if (condition) {
  // do something
} else if (condition) {
  // do something
} else {
  // do something
}
```

<br>

- `switch` statement
  - 조건 표현식의 결과값이 어느 값(case)에 해당하는지 판별
  - 조건이 많아질 경우 if문보다 가독성이 나을 수 있음
  - 표현식의 결과값과 case문의 오른쪽 값을 비교
  - 단, case문 표현이 `상수`만 가능!
  - break 및 default 문은 선택적으로 사용 가능
  - break문을 만나거나 default를 실행할 때 까지 다음 조건문 실행

```javascript
const numOne = 5;
const numTwo = 10;
let operator = "+";

switch (operator) {
  case "+": {
    console.log(numOne + numTwo);
    break;
  }
  case "-": {
    console.log(numOne - numTwo);
    break;
  }
  case "*": {
    console.log(numOne * numTwo);
    break;
  }
  case "/": {
    console.log(numOne / numTwo);
    break;
  }
  default: {
    console.log("유효하지 않은 연산자입니다.");
  }
}
```

> operator가 +, -, \*, / 일때마다 만족하는 각 case문이 실행되고 break가 있기 때문에 바로 종료됨
>
> 저 4가지 연산자가 아닐 경우에는 default가 실행되고 종료됨
>
> 만약 operator가 '+'인데 case문 마다 break가 없었다면 👉 위에서부터 아래로 break나 default를 만날때까지 계속 실행됐을 것!

<br>

## 🟨 반복문

### ✅ 반복문

#### ✔️ while

- 조건문이 참인 동안 반복 시행
- 조건은 소괄호 안에 작성
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
let i = 0;
while (i < 6) {
  console.log(i); // 0, 1, 2, 3, 4, 5
  i += 1;
}
```

<br>

#### ✔️ for

- 세미콜론으로 구분되는 세 부분으로 구성
- initialization : 최초 반복문 진입 시 1회만 실행되는 부분
- condition : 매 반복 시행 전 평가되는 부분
- expression : 매 반복 시행 이후 평가되는 부분
- 블록 스코프 생성

```javascript
for (let i = 0; i < 6; i++) {
  console.log(i); // 0, 1, 2, 3, 4, 5
}
// 1. 반복문 진입 및 변수 i 선언
// 2. 조건문 평가 후 코드 블럭 실행
// 3. 코드 블럭 실행 이후 i 값 증가
```

<br>

#### ✔️ for ... in

- 객체(object)의 속성(key)들을 순회할 때 사용
- `배열도 순회 가능하지만 권장하지 않음`
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
// object(객체) => key-value로 이루어진 자료구조
const capitals = {
  korea: "seoul",
  france: "paris",
  USA: "washington D.C.",
};
for (let capital in capitas) {
  console.log(capital); // korea, france, USA
}
```

> key-value 쌍에서 value가 아닌 key를 순회

<br>

#### ✔️ for ... of

- 반복 가능한 객체를 순회하면서 값을 꺼낼 때 사용
- 실행할 코드는 중괄호 안에 작성
- 블록 스코프 생성

```javascript
const fruits = ["딸기", "바나나", "메론"];
for (let fruit of fruits) {
  fruit = fruit + "!";
  console.log(fruit);
}
```

<br>

#### ✔️ for ... in과 for ... of 비교

- for in은 `객체 순회`에 적합하고
- for of는 `배열 순회`에 적합

<br>

## 🟨 함수

### ✅ 함수 in JS

- 참조 타입 중 하나로써 function 타입에 속함
- Javascript에서 함수를 정의하는 방법은 주로 2가지로 구분
  - 함수 선언식
  - 함수 표현식

<br>

### ✅ 함수의 정의

- 함수의 이름과 함께 정의하는 방식
- 3가지 부분으로 구성
  - 함수의 이름
  - 매개변수
  - 함수 body

```javascript
function add(num1, num2) {
  return num1 + num2;
}
add(1, 2);
```

<br>

### ✅ 함수 표현식

- 함수를 표현식 내에서 정의하는 방식
- 함수의 이름을 생략하고 익명 함수로 정의 가능
- 3가지 부분으로 구성
  - 함수의 이름 (생략 가능)
  - 매개변수
  - 몸통

```javascript
const add = function (num1, num2) {
  return num1 + num2;
};
add(1, 2);
```

<br>

### ✅ 기본 인자

- 인자 작성 시 '=' 문자 뒤 기본 인자 선언 가능

```javascript
const greeting = function (name = "Anonymous") {
  return `Hi ${name}`;
};
greeting(); // Hi Anonymous
```

<br>

### ✅ 매개변수와 인자의 개수 불일치 허용

- 매개변수보다 인자의 개수가 많을 경우

```javascript
const noArgs = function () {
  return 0;
};
noArgs(1, 2, 3); // 0

const twoArgs = function (arg1, arg2) {
  return [arg1, arg2];
};
twoArgs(1, 2, 3); // [1, 2], 뒤의 3은 무시됨
```

<br>

- 매개변수보다 인자의 개수가 적을 경우

```javascript
const threeArgs = function (arg1, arg2, arg3) {
  return [arg1, arg2, arg3];
};
threeArgs(); // [undefined, undefined, undefined]
threeArgs(1); // [1, undefined, undefined]
threeArgs(1, 2); // [1, 2, undefined]
```

> 부족한 인자는 undefined로 처리됨

<br>

### ✅ Rest Parameter

- rest parameter (`...`)를 사용하면 함수가 `정해지지 않은 수의 매개변수`를 배열로 받음

  👉 python의 \*args와 유사

- 만약 매개변수 인자가 넘어오지 않는다면 빈 배열로 처리

```javascript
const restOpr = function (arg1, arg2, ...restArgs) {
  return [arg1, arg2, restArgs];
};
restArgs(1, 2, 3, 4, 5); // [1, 2, [3, 4, 5]]
restArgs(1, 2); // [1, 2, []]
```

<br>

### ✅ Spread Operator

- spread operator(`…`)를 사용하면 배열 인자를 전개하여 전달 가능.

```javascript
const spreadOpr = function (arg1, arg2, arg3) {
  return arg1 + arg2 + arg3;
};
const numbers = [1, 2, 3];
spreadOpr(...numbers); // 6
```

<br>

### ✅ 함수의 타입

- 선언식 함수와 표현식 함수 모두 타입은 function으로 동일

```javascript
// 함수 표현식
const add = function (args) {};

// 함수 선언식
function sub(args) {}

console.log(typeof add); // function
console.log(typeof sub); // function
```

<br>

### ✅ 호이스팅(hoisting) - 함수 선언식

- 함수 선언식으로 선언한 함수는 var로 정의한 변수처럼 hoisting 발생
- 함수 호출 이후에 선언 해도 동작

```javascript
add(2, 7) // 9

function add (numl, num2) {
	return numl 十 num2
}
```

<br>

### ✅ 호이스팅(hoisting) - 함수 표현식

- 반면 함수 표현식으로 선언한 함수는 함수 정의 전에 호출 시 에러 발생
- 함수 표현식으로 정의된 함수는 변수로 평가되어 변수의 scope 규칙을 따름

```javascript
sub(7, 2); // Uncaught ReferenceError: Cannot access 'sub' before initialization

const sub = function (numl, num2) {
  return numl - num2;
};
```

<br>

## 🟨 Arrow Function

### ✅ 화살표 함수 (Arrow Function)

- 함수를 비교적 간결하게 정의할 수 있는 문법
- function 키워드 생략 가능
- 함수의 매개변수가 단 하나 뿐이라면, ‘( )’ 도 생략 가능
- 함수 몸통이 표현식 하나라면 ‘{ }’과 return도 생략 가능

```javascript
const arrow1 = function (name) {
  return `hello, ${name}`;
};

// 1. function 키워드 삭제
const arrow2 = (name) => {
  return `hello, ${name}`;
};

// 2. 매개변수가 1개일 경우에만 ( ) 생략 가능
const arrow3 = (name) => {
  return `hello, ${name}`;
};

// 3. 함수 바디가 return을 포함한 표현식 1개일 경우에 { } & return 삭제
가능;
const arrow4 = (name) => `hello, ${name}`;
```

<br>

## 🟨 문자열(String)

### ✅ 문자열 관련 주요 메서드 목록

#### ✔️ includes

- 특정 문자열의 존재여부를 참/거짓으로 반환

```javascript
const str = 'a santa at nasa’

str.includes('santa') // true
str.includes('asan') // false
```

<br>

#### ✔️ split

- 문자열을 토큰 기준으로 나눈 배열 반환

```javascript
const str = 'a cup’

str.split() // ['a cup’]
str.split('') // ['a', ' ', 'c', 'u', 'p']
str.split(' ') // ['a', 'cup']
```

> value가 없을 겨우, 기존 문자열을 배열에 담아 반환
>
> value가 빈 문자열일 경우, 각 문자로 나눈 배열을 반환
>
> value가 기타 문자열일 경우, 해당 문자열로 나눈 배열을 반환

<br>

#### ✔️ replace

- 해당 문자열 1개를 대상 문자열로 교체해서 반환

- `replaceAll`은 전부 반환

```javascript
const str = "a b c d";

str.replace(" ", "-"); // 'a-b c d' 1개반 바뀜
str.replaceAll(" ", "-"); // 'a-b-c-d'
```

<br>

#### ✔️ trim

- 공백문자(스페이스, 탭, 엔터 등)를 제거한 문자열 반환

- `trimStart`는 문자열 시작, `trimEnd`는 문자열 끝의 공백을 제거한 문자열 반환

```javascript
const str = " hello ";

str.trim(); // 'hello'
str.trimStart(); // 'hello '
str.trimEnd(); // ' hello'
```

<br>

## 🟨 배열(Arrays)

### ✅ 배열의 정의와 특징

- 키와 속성들을 담고 있는 참조 타입의 객체(object)
- 순서를 보장하는 특징이 있음
- 주로 대괄호를 이용하여 생성하고, 0을 포함한 양의 정수 인덱스로 특정 값에 접근 가능
- 배열의 길이는 `array.length` 형태로 접근 가능

```javascript
const numbers = [1, 2, 3, 4, 5];

console.log(numbers[0]); // 1
console.log(numbers[-l]); // undefined
console.log(numbers.length); // 5
```

<br>

### ✅ 배열 관련 주요 메서드 목록

#### ✔️ reverse

- 원본 배열의 요소들의 순서를 반대로 정렬

```javascript
const numbers = [1, 2, 3, 4, 5];
numbers.reverse();
console.log(numbers); // [5, 4, 3, 2, 1]
```

<br>

#### ✔️ push & pop

- 배열의 맨 뒤에 요소를 추가하거나 제거

```javascript
const numbers = [1, 2, 3, 4, 5];
numbers.push(100);
console.log(numbers); // [1, 2, 3, 4, 5, 100]

numbers.pop();
console.log(numbers); // [1, 2, 3, 4, 5]
```

<br>

#### ✔️ unshift & shift

- 배열의 맨 앞에 요소를 추가하거나 제거

```javascript
const numbers = [1, 2, 3, 4, 5];
numbers.unshift(100);
console.log(numbers); // [100, 1, 2, 3, 4, 5]

numbers.shift();
console.log(numbers); // [1, 2, 3, 4, 5]
```

<br>

#### ✔️ includes

- 배열에 특정 값이 존재하는지 판별 후 참 또는 거짓 반환

```javascript
const numbers = [1, 2, 3, 4, 5];
console.log(numbers.includes(l)); // true
console.log(numbers.includes(l00)); // false
```

<br>

#### ✔️ indexOf

- 배열에 특정 값이 존재하는지 확인 후 가장 첫번째로 찾은 요소의 인덱스 반환

- 값이 없을 경우 -1 반환

```javascript
const numbers = [1, 2, 3, 4, 5];
let result;

result = numbers.indexOf(3); // 2
console.log(result);

result = numbers.indexOf(100); // -1
console.log(result);
```

<br>

#### ✔️ join

- 배열의 모든 요소를`연결해서 반환`
- separator(구분자)는 선택적으로 지정 가능
- 생략 시 쉼표가 기본값

```javascript
const numbers = [1, 2, 3, 4, 5];
let result;

result = numbers.join();
console.log(result); // 1, 2, 3, 4, 5

result = numbers.join("");
console.log(result); // 12345

result = numbers.join(" ");
console.log(result); // 1 2 3 4 5

result = numbers.join("-");
console.log(result); // 1-2-3-4-5
```

<br>

#### ✔️ Spread operator(...)

- 배열 내부에서 배열 전개 가능

```javascript
const array = [1, 2, 3];
const newArray = [0, ...array, 4];

console.log(newArray); // [0, 1, 2, 3, 4]
```

<br>

#### ✔️ forEach

- `array.forEach(callback(element[,index[,array]]))`의 형식
- 배열의 각 요소에 대해 콜백 함수를 한 번씩 실행
- 콜백 함수는 3가지 매개변수로 구성
  - element: 배열의 요소
  - index: 배열 요소의 인덱스
  - array: 배열 자체
- 반환 값(return)이 없는 메서드

```javascript
const fruits = ['딸기', '수박', '사과', '체리']

fruits.forEach((fruit, index) => {
	console.log(fruit, index)
	// 딸기 0
	// 수박 1
	// 사과 2
	// 체리 3
})
```

.<br>

#### ✔️ map

- `array.map(callback(element[,index[,array]]))`의 형식
- 콜백 함수의 반환 값을 요소로 하는 새로운 배열 반환
- 기존 배열 전체를 다른 형태로 바꿀 때 유용

```javascript
const numbers = [1, 2, 3, 4, 5]

const doubleNums = numbers.map((num) => {
	return num * 2
})
conso1e.log(doubleNums) // [2, 4, 6, 8, 10]
```

<br>

#### ✔ filter

- `array.filter(callback(element[,index[,array]]))`의 형식
- 콜백 함수의 반환 값이 참인 요소들만 모아서 새로운 배열을 반환
- 기존 배열의 요소들을 필터링 할 때 유용

```javascript
const numbers = [1, 2, 3, 4, 5]

const oddNums = numbers.filter((num, index){
    return num % 2
})
conso1e.log(oddNums) // 1, 3, 5
```

<br>

#### ✔ reduce

- `array.reduce(callback(acc,element[,index[,array]]))`의 형식
- 콜백 함수의 반환 값들을 하나의 값(acc)에 누적 후 반환
- reduce 메서드의 주요 매개변수
  - acc : 이전 callback 함수의 반환 값이 누적되는 변수
  - initialValue(선택) : 최초 callback 함수 호출 시 acc에 해당하는 값, default는 배열의 첫번째 값
- (참고) 빈 배열의 경우 initialValue를 제공하지 않으면 에러 발생

```javascript
const numbers = [1, 2, 3, 4, 5]

const result = numbers.reduce((acc, num) => {
    return acc + num
}, 0)

conso1e.log(result) // 15
```

<br>

#### ✔ find

- `array.find(callback(element[,index[,array]]))`의 형식
- 콜백 함수의 반환 값이 참이면, 조건을 만족하는 첫번째 요소를 반환
- 찾는 값이 배열에 없으면 undefined 반환

```javascript
const avengers = [
    {name: 'Tony Stark', age: 45},
    {name: 'Steve Rogers', age: 32},
    {name: 'Thor', age: 40},
]

const result = avengers.find((avenger) ==> {
	return avenger.name === 'Tony Stark'        
})

console.log(result) // {name: "Tony Stark", age: 45}
```

<br>

#### ✔ some

- `array.some(callback(element[,index[,array]]))`의 형식
- 배열의 요소 중 하나라도 주어진 판별 함수를 통과하면 참을 반환
- 모든 요소가 통과하지 못하면 거짓 반환
- 빈 배열은 항상 거짓 반환

```javascript
const numbers = [1, 3, 5, 7, 9]

const hasEvenNumber = numbers.some((num) => {
	return num % 2 === 0
})
console.log(hasEvenNumber) // false

const hasOddNumber = numbers.some((num) => {
	return num % 2
})
console.log(hasOddNumber) // true
```

<br>

#### ✔ every

- `array.every(callback(element[,index[,array]]))`의 형식
- 배열의 모든 요소가 판별 함수를 통과하면 참을 반환
- 하나의 요소라도 통과하지 못하면 거짓 반환
- 빈 배열은 항상 참 반환

```javascript
const numbers = [2, 4, 6, 8, 10]

const isEveryNumberEven = numbers.every((num) => {
	return num % 2 === 0
})
console.log(isEveryNumberEven) // true

const isEveryNumberOdd = numbers.every((num) => {
	return num % 2
})
console.log(isEveryNumberOdd) // false
```

<br>

## 🟨 객체(Objects)

### ✅ 객체의 정의와 특징

- 객체는 속성(property)의 집합이며,  중괄호 내부에 key와 value의 쌍으로 표현
- key는 문자열 타입만 가능
  - key 이름에 띄어쓰기 등의 구분자가 있으면 따옴표로 묶어서 표현
- value는 모든 타입(함수포함) 가능
- 객체 요소 접근은 점 또는 대괄호로 가능
  - key 이름에 띄어쓰기 같은 구분자가 있으면 대괄호 접근만 가능

```javascript
const me = {
	name: 'jack',
	phoneNumber: '01012345678',
	'samsung products': {
	buds: 'Galaxy Buds pro',
	galaxy: 'Galaxy s20’,
	},
}
console.log(me.name) // jack
console.log(me.phoneNumber) // 01012345678
console.log(me['samsung products']) 	
console.log(me['samsung products'].buds) // Galaxy Buds pro
```

>  key 이름에 띄어쓰기 등의 구분자가 있으므로 key는 따옴표로 묶어서 표현하고, key 이름에 구분자가 있기 때문에 대괄호 접근만 가능

- 메서드는 객체의 속성이 참조하는 함수
- 객체.메서드명() 으로 호출 가능
- 메서드 내부에서는 this 키워드가 객체를 의미함

```javascript
const me = {
	firstName: 'John',
	lastName: 'Doe’,
	getFullName: function () {
		return this.firstName + this.lastName	
	}
}
```

<br>

### ✅ JSON

- JavaScript Object Notation
- key-value 쌍의 형태로 데이터를 표기하는 언어 독립적 표준 포맷
- 자바스크립트의 객체와 유사하게 생겼으나 실제로는 문자열 타입
  - 따라서 JS의 객체로써 조작하기 위해서는 구문 분석(parsing)이 필수
- 자바스크립트에서는 JSON을 조작하기 위한 두 가지 내장 메서드를 제공
  - JSON.parse()
    - JSON => 자바스크립트 객체
  - JSON.stringify()
    - 자바스크립트 객체 => JSON

---

## 🟨 실습
