from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout, update_session_auth_hash
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from .forms import UserForm

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        if request.user.is_authenticated:
            return redirect('articles:index')
        form = UserCreationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/form.html', context)

def login(request):
    if request.method == 'POST':
        # AuthenticationForm은 ModelForm이 아닌 Form 상속
        # 별도로 정의된 Model이 없다는 뜻
        # 그래서 넘겨주는 인자가 달라진다.
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인은 DB에 뭔가 작성하는 것은 동일하지만, 연결된 모델이 있는 것은 아니다.
            # 그럼 무엇을 확인해야 하나?
            # 세션과 유저 정보
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        if request.user.is_authenticated:
            return redirect('articles:index')
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/form.html', context)

@login_required
def logout(request):
    auth_logout(request)
    return redirect('articles:index')

@login_required
@require_POST
def delete(request):
    if request.method == "POST":
        request.user.delete()
    return redirect('articles:index')

@login_required
def update(request):
    if request.method == "POST":
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = request.user.password
            user.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = UserForm(instance=request.user)
    context = {
        'form':form
    }
    return render(request, 'accounts/form.html', context)

@login_required
def password(request):
    if request.method == "POST":
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/form.html', context)