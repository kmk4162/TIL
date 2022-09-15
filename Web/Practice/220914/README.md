# 프로젝트 07 - 부트스트랩을 활용한 영화 사이트 웹 구현



## 과정
- [목표](#목표)
- [준비 사항](#준비-사항)
- [요구사항](#요구-사항)
- [프로젝트 결과 완성본](#프로젝트-결과-완성본)
- [프로젝트 후기](#프로젝트-후기)



## 목표
- HTML를 통한 웹 페이지 마크업
- CSS를 통한 선택자 활용 및 속성 부여
- 시맨틱 태그를 활용한 기본 레이아웃 구성
- 영화 추천 사이트 메인 레이아웃 구성



## 준비 사항
1. **(필수)** HTML/CSS 환경 구성
2. **(필수)** Bootstrap
3. `images.zip` 폴더에 활용할 이미지 포함



## 요구 사항
> 01_nav_footer.html

![nav_footer.html 완성본 이미지](../../img/nav_footer.png)

- navbar 좌측에는 영화 로고가 배치됩니다.
- 항목은 Home, Community, Login로 구성되어 있습니다.
    - Home은 02_home.html으로 링크를 구성합니다.
    - Community는 03_community.html으로 링크를 구성합니다.
    - Login은 Modal이 팝업됩니다.
        
        ![nav_footer.html modal 이미지](../../img/nav_footer_modal.png)
        
- footer는 컨텐츠 최하단에 배치됩니다. 내용은 자유롭게 구성합니다.

> 02_home.html

![home.html 완성본 이미지](../../img/home.png)

- 01_nav_footer.html에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다.
- Carousel을 활용하여 이미지가 자동으로 전환될 수 있도록 합니다.
    - 이미지는 적절한 이미지를 찾아 변경 가능합니다.
- Boxoffice 문구는 `h2` 태그를 활용합니다.
- 영화 목록의 카드 배치는 반응형으로 합니다.
    - Viewport의 가로 크기가 576px 미만일 경우 한 행에 1개씩 표시됩니다.
        
        ![home.html의 boxoffice에서 1개 column 이미지](../../img/boxoffice_01.png)
        
    - Viewport의 가로 크기가 576px 이상일 경우 한 행에 2개 이상 표시됩니다.(자유롭게 설정 가능)
        
        ![home.html의 boxoffice에서 2개 column 이미지](../../img/boxoffice_02.png)
        
        ![home.html의 boxoffice에서 3개 column 이미지](../../img/boxoffice_03.png)


> 03_community.html

- 992px 이상일 때 게시판 

  ![](../../img/community_01.png)

- 992px 미만일 때 게시판 

  ![](../../img/community_02.png)

- 01_nav_footer.html에서 작성한 Navigation bar & Modal & Footer 코드를 적절한 위치에 사용합니다.
- Community 페이지는 크게 게시판 목록과 게시판으로 이루어져 있으며 반응형입니다.
- 게시판 목록(`aside`)은 클릭 가능하지만 연결된 링크는 없습니다.
    - Viewport의 가로 크기가 992px 미만일 경우 HTML main 요소 영역 전체만큼의 너비를 가집니다.
    - Viewport의 가로 크기가 992px 이상일 경우 HTML main 요소 영역 기준으로 좌측 1/6 만큼의 너비를 가집니다.
    - Viewport의 가로 크기 별 반응형 디자인은 스크린 샷 예시를 참고하여 일치하도록 합니다.
- Section (게시판)
    - 게시판은 Viewport의 가로 크기에 따라 전혀 다른 레이아웃으로 구성됩니다.
    - Viewport의 가로 크기가 992px 미만일 경우 게시판은 카드 형식으로 구성됩니다.
    - Viewport의 가로 크기가 992px 이상일 경우 테이블 형식으로 구성되며, HTML main 요소 영역 기준으로 우측 5/6 만큼의 너비를 가집니다.



## 프로젝트 결과 완성본
> 01_nav_footer.html

![](../../gif/nav_footer_animation.gif)

> 02_home.html

![](../../gif/home_animation.gif)

> 03_community.html

![](../../gif/community_animation.gif)



## 프로젝트 후기

> 페어프로그래밍/웹 개발 후기

오늘 두번째로 페어 프로그래밍을 진행하였다. 2인 1조로 조가 나뉘어졌고 한 명은 드라이버, 다른 한 명은 네비게이터가 되어 일정 파트 구현이 끝나면 역할을 계속 체인지해가면서 영화 사이트를 만들었다. 

가장 먼저 nav_footer 페이지를 구현했는데, 여기서는 내가 드라이버가 되고 조원분이 네비게이터가 되었다. 부트스트랩을 활용해 Navbar를 만드는 부분은 이미 이전에 여러번 실습해봤기 때문에 빠르게 구현할 수 있었다. Navbar에서 login 링크를 클릭했을 때 modal 팝업창을 띄워야 했는데, modal 파트는 나와 조원분 모두 활용해본 적이 없었기 때문에 쉽게 감을 잡진 못했다. 그래서 부트스트랩 문서 내 modal 코드를 차근차근 살펴보며 button 태그를 a 태그로 바꾸되 안에 일부 속성들만 그대로 옮겨주면 되지 않을까 아이디어를 냈고 적용한 결과 원하는 대로 잘 구현이 되었다. 다음으론 nav_footer 페이지에서 footer 태그를 만들었는데, 이 부분에서 상당히 애를 먹었다. position을 어떻게 줘야 할지 조원분과 상의해보고 여러 방식을 적용해 본 결과, fixed를 주는게 젤 깔금한 것 같아서 이렇게 position을 주고 따로 css 파일을 통해 배경색도 입혀줬다. 푸터의 배경색을 고민할 때 조원분께서 MS의 [PowerToys](https://docs.microsoft.com/ko-kr/windows/powertoys/)라는 유틸리티를 소개해주셔서 Color Picker 기능을 통해 [컬러 팔레트 사이트](https://mybrandnewlogo.com/ko/color-palette-generator)에서 다양한 컬러 중 하나를 선택해 rgb값을 확인하고 css에 작성했다. 

다음으로는 home 페이지를 구현했는데, 여기에서는 조원분이 드라이버가 되고 내가 네비게이터가 되었다. Carousel부분은 이전에 실습해본적이 있기 때문에 빠르게 작성했다. BoxOffice부분은 그리드 시스템을 활용해서 breakpoint에 따라 다르게 배치되게 반응형으로 구현하였다. 

마지막으로 community 페이지는 table까지는 조원분이 계속 이어서 드라이버 역할을 해주셨고, 그 이후부터는 내가 드라이버가 되어 카드를 구현했다. 내가 처음 구상할 땐 aside 부분을 button group을 사용해서 구현하면 되겠다고 생각했는데, 조원분께서 list group으로 구현하신 것 보고 그런 component도 있다는 것을 배우게 되어 감사했다. 마찬가지로 table 부분도 조원분과 함께 부트스트랩 문서를 읽어가며 table content에 대해서 더 알아갈 수 있었다.
community 페이지에서 aside 태그와 table 태그 card 태그들을 viewport에 따라 다르게 배치하면서 동시에 table과 card 둘 중 하나만 보이게 하는 부분이 가장 구현해내기 어려웠다. 노트에 그리드 시스템의 전체적인 구조를 적어가며 어떤 식으로 코드를 짜야할지 고심한 끝에, position도 viewport에 따라 none이나 block를 주면 될 것 같다는 생각을 했다. 상상한 대로 코드를 짜본 결과, 다행히 원하는 대로 잘 구현이 되었다. 

저번 페어 프로그래밍할 때도 느꼈지만, 다른 사람과 함께 하나의 페이지를 만드는 과정은 훨씬 시간 단축적이고 많은 것을 배울 수 있는 뜻 깊은 시간인 것 같다. '왜 이 태그에 마진을 줬는데 먹히지가 않는 걸까요?'라며 질문하고 같이 고민하고 해결해 나가면서 동지애도 느끼고 배로 뿌듯함을 느꼈던 감사한 시간이었다. 