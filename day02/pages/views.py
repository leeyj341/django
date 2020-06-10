from django.shortcuts import render
import random
from datetime import datetime

# Create your views here.
def index(request) :
    return render(request, 'index.html')

def hello(request) :
    menu = ['닭갈비', '탕수육', '초밥', '스파게티돈까스']
    pick = random.choice(menu)
    return render(request, 'hello.html', {'pick' : pick})

def name(request) :
    my_name = '이영주'
    return render(request, 'name.html', {'my_name' : my_name})

def introduce(request) :
    my_info = ['이영주', '28']
    name = '이영주'
    age = 100
    github = 'https://github.com/leeyj341'
    movie = '어바웃 타임'
    company = 'Line Plus'
    mate = '김민정'
    context = {
        'name' : name,
        'age' : age,
        'github' : github,
        'movie' : movie,
        'company' : company,
        'mate' : mate
    }
    return render(request, 'introduce.html', context)

def pickStudent(request) :
    students = ['김민정', '윤소윤', '박누리', '문준우', '오성식']
    pick = random.choice(students)
    context = {
        'pick' : pick
    }
    return render(request, 'randompick.html', context)
    
def yourname(request, name) :
    name = name
    context = {
        'name' : name
    }
    return render(request, 'yourname.html', context)

def info(request, name, age) :
    context = {
        'name' : name,
        'age' : age
    }
    return render(request, 'info.html', context)

def multiple(request, num1, num2) :
    context = {
        'num1' : num1,
        'num2' : num2,
        'result' : num1 * num2
    }
    return render(request, 'multiple.html', context)

def gugu(request, num1, num2) :
    gu_list = list()
    for data in range(1, num1) :
        gu_list.append(num2 * data)
    context = {
        'gu_list' : gu_list
    }
    return render(request, 'gugu.html', context)

def pigeon(request, big, small) :
    result = []
    if big < small :
        big, small = small, big
    for num in range(1, small + 1) :
        result.append(big * num)
    context = {
        'result' : result
    }
    return render(request, 'pigeon.html', context)

def dtl(request) :
    my_list = ['짜장면', '차돌짬뽕', '탕수육', '콩국수']
    empty_list = []
    my_string = 'Life is short, You need Python'
    today = datetime.now()
    context = {
        'my_list' : my_list,
        'empty_list' : empty_list,
        'my_string' : my_string,
        'today' : today 
    }
    return render(request, 'dtl.html', context)

def forif(request, my_str) :
    my_list = [100, 50, 30, 20, 10]
    my_string = '간단한 문자열'
    data_a = '첫번째 데이터'
    data_b = '두번째 데이터'
    data_a, data_b = data_b, data_a
    context = {
        'my_list' : my_list,
        'my_string' : my_string,
        'data_a' : data_a,
        'data_b' : data_b,
        'my_str' : my_str
    }
    return render(request, 'forif.html', context)