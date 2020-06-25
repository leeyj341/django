from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm
from IPython import embed
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.
def index(request):
    # embed()
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    # 1은 N을 보장할 수 없기 때문에 QuerySet(comment_set)형태로 조회해야 한다.
    comments = article.comment_set.all()
    comment_form = CommentForm()
    context = {
        'article': article,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'articles/detail.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user_id = request.user.pk
            article.save()
            messages.success(request, '게시물 작성 완료')
            return redirect('articles:detail', article.pk)
        else:
            messages.error(request, '잘못된 데이터') # 잘못된 항목을 넣었다
    else:
        form = ArticleForm()
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.user == request.user:
        if request.method == 'POST':
            form = ArticleForm(request.POST, request.FILES, instance=article)
            if form.is_valid():
                article = form.save()
                return redirect('articles:detail', article.pk)
            else:
                return redirect('articles:detail', article.pk)
        else:
            form = ArticleForm(instance=article)
    context = {
        'form': form
    }
    return render(request, 'articles/form.html', context)

@login_required
@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if article.user == request.user:
        article.delete()
    else:
        pass
    return redirect('articles:index')

@login_required
@require_POST
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = CommentForm(request.POST)
    if form.is_valid() :
        comment = form.save(commit=False)
        comment.article_id = article_pk
        comment.user = request.user
        comment.save()
        return redirect('articles:detail', article_pk)
    else:
        context = {
            'form' : form,
            'article' : article
        }
    return redirect('article:detail', context)

@login_required
@require_POST
def comment_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)

@login_required
def like(request, article_pk):
    # 특정 게시물에 대한 정보
    article = get_object_or_404(Article, pk=article_pk)
    # 좋아요를 누른 유저에 대한 정보
    user = request.user

    # 사용자가 게시글의 좋아요 목록에 있으면
    if user in article.like_users.all():
        article.like_users.remove(user)
    else:
        article.like_users.add(user)

    return redirect('articles:index')

@login_required
def recommend(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user

    if user in article.recommenders.all():
        article.recommenders.remove(user)
    else:
        article.recommenders.add(user)

    return redirect('articles:index')
