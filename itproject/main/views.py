from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    data = {
        'title': 'Это главная страница',
        'achievement': {
            'car': None,
            'home': None,
        },
        'disclaimer': 'Данная информация на сайте не проверина chat-ом gpt, поэтому мы не имеем ответсчтвенности к данной информации и вообще я хз что пишут во всех дисклеймерах'
    }
    return render(request, 'main/index.html', data)

def about(request):
    data = {
        'value': ['ChatGPT', 'Помогает', 'создавать', 'сайт '],
    }
    return render(request, 'main/about.html', data)


