from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    # 전체 가져와서 역순으로 조회
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

def create(request):
    # 제출 버튼을 눌러서 method가 POST 라면
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        # 유효성 검사를 진행 유효하면 저장하고 index 페이지로 redirect
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        # 버튼을 누른게 아니라면 초기 화면인 빈 상태
        # 그렇기 때문에 빈 form을 만들고 context로 넘겨준다
        article_form = ArticleForm()

    # 요청이 POST인데 유효성 검사에 실패를 하면 기존에 잘못 입력한 값들은
    # 그대로 유지하고 싶기 때문에 form에 넣어서 데이터를 넘겨줌
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk);
    context = {
        'article' : article, 
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk = pk);
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    # 일단 가져와서 바꿔줘야함
    article = Article.objects.get(pk = pk)
    # POST 요청과 유효함이 통과할 때만 바꿔서 저장
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance = article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)

    # POST 요청이 아닌 경우는 처음 페이지를 render 했을 때임
    # 그렇기 때문에 이전에 작성한 데이터를 그대로 제공
    else:
        article_form = ArticleForm(instance = article)
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/update.html', context)