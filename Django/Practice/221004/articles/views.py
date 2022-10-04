from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def index(request):
    articles = Article.objects.all().order_by('-pk')
    context = {
        'articles' : articles,
    }
    return render(request, 'articles/index.html', context)

# def new(request):
#     # 인스턴스 생성
#     article_form = ArticleForm()
#     context = {
#         'article_form' : article_form,
#     }
#     return render(request, 'articles/new.html', context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    context = {
        'article_form' : article_form,
    }
    return render(request, 'articles/new.html', context)

def detail(request, pk):
    article = Article.objects.get(pk = pk)
    context = {
        'article' : article,
    }
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk = pk)
    article.delete()
    return redirect('articles:index')

def update(request, pk):
    # DB에서 pk 값이 같은 데이터를 가져옴
    article = Article.objects.get(pk = pk)

    if request.method == 'POST':
        # POST : input 값 가져와서, 검증하고, DB에 저장
        article_form = ArticleForm(request.POST, instance = article)

        # 유효성 검사 통과하면 저장하고 상세보기 페이지로
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk)

    # 통과 못하면 해당 pk의 인스턴스를 return한다.
    else:
        article_form = ArticleForm(instance = article)
    context = {
        'article' : article,
        'article_form' : article_form,
    }
    return render(request, 'articles/update.html', context)