# 9/15

# 🌇 오전

## 🕓 9:00 ~ 12:00

### 🟨 Javascript

#### ✅ Javascript의 필요성

- 브라우저 화면을 `동적`으로 만들기 위함
- 브라우저를 조작할 수 있는 유일한 언어

<br>

#### ✅ Vanilla Javascript

- 크로스 브라우징, 간편한 활용 등을 위해 많은 라이브러리 등장 (jQuery 등)
- ES6 이후, 다양한 도구의 등장으로 순수 자바스크립트 활용이 증가함
- 일단 아무것도 다운받지 않아도 되니 가볍고 빠름
- 프론트에서 리액트, 뷰, 앵귤러 등의 프레임워크가 자바스크립트의 es-6의 문법을 사용하면서 JS의 중요성이 더욱 높아짐!

<br>

### 🟨 DOM (Document Object Model)

#### ✅ 브라우저에서 할 수 있는 일

- DOM 조작
  - 문서(HTML) 조작

- BOM 조작
  - navigator, screen, location, frames, history, XHR

- JavaScript Core (ECMAScript) 
  - Data Structure(Object, Array), Conditional Expression, Iteration


<br>

#### ✅ DOM 이란?

- HTML, XML과 같은 문서를 다루기 위한 문서 프로그래밍 인터페이스
- 문서를 구조화하고 구조화된 구성 요소를 하나의 객체로 취급하여 다루는 논리적 트리 모델
- 문서가 구조화되어 있으며 각 요소는 객체(object)로 취급
- 단순한 속성 접근, 메서드 활용뿐만 아니라 프로그래밍 언어적 특성을 활용한 조작 가능
- 주요 객체
  - window : DOM을 표현하는 창. 가장 최상위 객체 (작성 시 생략 가능)
  - document : 페이지 컨텐츠의 Entry Point 역할을 하며,  등과 같은 수많은 다른 요소들을 포함
  - navigator, location, history, screen


<br>

#### ✅ BOM 이란?

- Browser Object Model
- 자바스크립트가 브라우저와 소통하기 위한 모델
- 브라우저의 창이나 프레임을 추상화해서 프로그래밍 적으로 제어할 수 있도록 제공하는 수단
  - 버튼, URL 입력창, 타이틀 바 등 브라우저 윈도우 및 웹 페이지 일부분을 제어 가능


- window 객체는 모든 브라우저로부터 지원받으며 브라우저의 창(window)를 지칭

![img](https://velog.velcdn.com/images%2Fwiostz98kr%2Fpost%2F4e7f320a-7fa9-4f21-8bb2-2aeb074f7e2f%2Fimage.png)

<br>

### 🟨 DOM 조작

#### ✅ DOM 조작 - 개념

- Document는 문서 한 장에 해당하고 이를 조작
- 선택 후 변경의 순서!

<br>

#### ✅ DOM 객체의 상속 구조

- EventTarget
  - Event Listener를 가질 수 있는 객체가 구현하는 DOM 

- Node
  - 여러가지 DOM 타입들이 상속하는 인터페이스
- Element
  - Document 안의 모든 객체가 상속하는 가장 범용적인 인터페이스
  - 부모인 Node와 그 부모인 EventTarget의 속성을 상속
- Document
  - 브라우저가 불러온 웹 페이지를 나타냄
  - DOM 트리의 진입점(entry point) 역할을 수행
- HTMLElement
  - 모든 종류의 HTML 요소
  - 부모 element의 속성 상속

![img](https://velog.velcdn.com/images%2Fss3152psy%2Fpost%2Fb10b742b-bd7a-4382-84c4-020b3cc17f72%2Fimage.png)

<br>

#### ✅ DOM 선택 - 선택 관련 메서드

- `document.querySelector(selector)`

  - 제공한 선택자와 일치하는 element 하나 선택

  - 제공한 CSS selector를 만족하는 `첫 번째` element 객체를 반환 (없다면 null)

    👉 단일 element 형식으로 반환

- `document.querySelectorAll(selector)`

  - 제공한 선택자와 일치하는 `여러 element`를 선택

  - 매칭 할 하나 이상의 셀렉터를 포함하는 유효한 CSS selector를 인자(문자열)로 받음

    👉 지정된 셀렉터에 일치하는 NodeList를 반환

- `getElementById(id)`

- `getElementsByTagName(name)`

- `getElementsByClassName(names)` 등이 있음

> 우리는 querySelector(), querySelectorAll()를 더 사용함
>
> 👉 id, class, tag 선택자 등을 모두 사용가능 하므로, 더 구체적이고 유연하게 선택이 가능!
>
> 예시) document.querySelector('#id’), document.querySelectAll(‘.class') 과 같이 좀 더 세밀한 선택이 가능

<br>

#### ✅ DOM 변경 - 변경 관련 메서드 (Creation)

- `document.createElement()`
  - 작성한 태그 명의 HTML 요소를 생성하여 반환
- `Element.append()`
  - 특정 부모 Node의 자식 NodeList 중 마지막 자식 다음에 Node 객체나 DOMString을 삽입
  - 여러 개의 Node 객체, DOMString을 추가 할 수 있음
  - 반환 값이 없음
- `Node.appendChild()`
  - 한 Node를 특정 부모 Node의 자식 NodeList 중 마지막 자식으로 삽입 (Node만 추가 가능)
  - 한번에 오직 하나의 Node만 추가할 수 있음
  - 만약 주어진 Node가 이미 문서에 존재하는 다른 Node를 참조한다면 새로운 위치로 이동

<br>

#### ✅ DOM 변경 - 변경 관련 속성 (property)

- `Node.innerText`
  - Node 객체와 그 자손의 텍스트 컨텐츠(DOMString)를 표현 (해당 요소 내부의 raw text) (사람이 읽을 수 있는 요소만 남김)
  - 즉, 줄 바꿈을 인식하고 숨겨진 내용을 무시하는 등 최종적으로 스타일링이 적용된 모습으로 표현
- `Element.innerHTML`
  - 요소(element) 내에 포함된 HTML 마크업을 반환
  - [참고] XSS 공격에 취약하므로 사용 시 주의

<br>

#### ✅ DOM 삭제 - 삭제 관련 메서드

- `ChildNode.remove()`
  - Node가 속한 트리에서 해당 Node를 제거
- `Node.removeChild()`
  - DOM에서 자식 Node를 제거하고 제거된 Node를 반환
  - Node는 인자로 들어가는 자식 Node의 부모 Node

<br>

#### ✅ DOM 속성 - 속성 관련 메서드

- `Element.setAttribute(name, value)`
  - 지정된 요소의 값을 설정
  - 속성이 이미 존재하면 값을 갱신, 존재하지 않으면 지정된 이름과 값으로 새 속성을 추가
- `Element.getAttribute(attributeName)`
  - 해당 요소의 지정된 값(문자열)을 반환
  - 인자(attributeName)는 값을 얻고자 하는 속성의 이름

<br>

# 🌆 오후

## 🕓 1:00 ~ 6:00

### 🟨 실습



