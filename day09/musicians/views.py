from django.shortcuts import render, redirect
from .forms import MusicianForm
from .models import Musician

# Create your views here.
def index(request):
    # .all()로 조회하면 QuerySet
    # QuerySet은 list처럼 사용 가능
    musicians = Musician.objects.all()
    context = {
        'musicians' : musicians
    }
    return render(request, "musicians/index.html", context)

def create(request):
    if request.method == "POST" :
        # 사용자의  요청 정보를 담아준다.
        form = MusicianForm(request.POST)
        # forms를 상속받았기 때문에 사용가능
        if form.is_valid():
            # Musician가 models에게 받은 메서드
            # ModelForm을 정의할 때 class Meta : Musician을 담아줬다.
            musician = form.save()
            return redirect('musicians:index')
    else :
        # MusicianForm 불러오기
        # form은 MusicianForm 인스턴스
        # MusicianForm이 가진 정보를 가짐.
        # MusicianForm은 Musician의 정보를 들고 있음
        # template에서 보여줄 tag 정보도 갖고 있다 => modelForm이 하는 일
        form = MusicianForm()
    context = {
        'form' : form
    }
    return render(request, "musicians/create.html", context)

# 함수이름(urls에 작성한 변수명)
def detail(request, musician_pk):
    musician = Musician.objects.get(pk=musician_pk)
    context = {
        'musician' : musician
    }
    return render(request, 'musicians/detail.html', context)

def edit(request, pk):
    musician = Musician.objects.get(pk=pk)
    if request.method == "POST" :
        form = MusicianForm(request.POST, instance=musician)
        if form.is_valid():
            form.save()
            return redirect('musicians:detail', musician.pk)
    else :
        form = MusicianForm(instance=musician)
    context= {
        'form' : form
    }
    return render(request, 'musicians/edit.html', context)

def delete(request, pk):
    Musician.objects.get(pk=pk).delete()
    return redirect('musicians:index')