from django.shortcuts import render
import random
import requests

# Create your views here.
def index(request) :
    return render(request, 'pages/index.html')

def loop(request) :
    nums = []
    for data in range(10) :
        nums.append(data)
    context = {
        'nums' : nums
    }
    return render(request, 'pages/loop.html', context)

def throw(request) :
    return render(request, 'pages/throw.html')

def catch(request) :
    data = request.GET.get('message')
    context = {
        'data' : data
    }
    return render(request, 'pages/catch.html', context)

def food(request, name) :
    menu = ['김밥', '떡볶이', '순대', '튀김']
    pick = random.choice(menu)
    context = {
        'name' : name,
        'pick' : pick
    }
    return render(request, 'pages/food.html', context)

def getCount(request) :
    return render(request, 'pages/getCount.html')

def lotto(request) :
    count = int(request.GET['count'])
    lotto = []
    for i in range(count) :
        lotto.append(sorted(random.sample(range(1, 46), 6)))
    context = {
        'count' : count,
        'lotto' : lotto
    }
    return render(request, 'pages/lotto.html', context)

def artii(request) :
    return render(request, 'pages/artii.html')

def result(request) :
    message = request.GET.get('message')
    result = requests.get(f'http://artii.herokuapp.com/make?text={message}').text
    context = {
        'result' : result
    }
    return render(request, 'pages/result.html', context)