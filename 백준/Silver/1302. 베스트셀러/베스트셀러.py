N = int(input())
books = {}

for i in range(N):
    book = input()
    books[book] = books.get(book, 0) + 1
# 입력 받으면서 딕셔너리에 저장
newbooks = sorted(books.items(), key = lambda x : (-x[1], x[0]))
print(newbooks[0][0])
