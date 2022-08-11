# 8/8

# 🌇 오전

## 🕓 9:00 ~ 12:00

### ✅ 완전탐색 (Exhaustive Search)

#### 💻 1. 무식하게 풀기 (Brute-force)

- 모든 경우의 수를 탐색하여 문제를 해결하는 방식
- 가장 단순한 기법 (단순 조건문 + 반복문)
- 복잡한 알고리즘 보다는, 아이디어를 어떻게 코드를 구현할 것인지가 중요

<br>



#### 💻 2. 델타 탐색 (Delta Search)

- 각 지점에서 상하좌우에 위치한 다른 지점을 조회하거나 이동하는 방식
- 이차원 리스트의 인덱스를 조작
- 이때 행과 열의 변량인 -1, +1 을 `델타(delta)값`이라고 함!
- 상하좌우 이동 후 `범위를 벗어나지 않는지 확인 및 갱신하기`
- 상하좌우 + 대각선도 마찬가지
- 각각의 인덱스를 직접 써보고 하나씩 해보자.. 처음엔 헷갈리니까
- 따라서 델타 설정 👉 델타 순회 👉 경계값 설정

<br>




# 🌆 오후

## 🕓 1:00 ~ 6:00

- 