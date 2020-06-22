# 장고에서 미리 정의해둔 forms 받아오기
from django import forms
from .models import Musician, Album

# 클래스 정의
class MusicianForm(forms.ModelForm):
    # 쿨래스에 대한 클래스
    class Meta:
        # 어떤 모델? Musician에 정의된 것
        model = Musician
        # 모델에 있는 모든 필드 불러오기...
        fields = '__all__'

class AlbumForm(forms.ModelForm):
    class Meta:
        model = Album
        exclude = ['musician']

