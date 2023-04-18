from django.http import HttpResponse
from django.shortcuts import render

autor = {
    "name": "Иван",
    "mid": "Иванович",
    "sur": "Иванов",
    "phone": "89236000102",
    "email": "vasya@mail.ru",
}


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 3, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 4, "name": "Картофель фри" ,"quantity":0},
   {"id": 5, "name": "Кепка" ,"quantity":124},
]



def home(request):
    return render(request, "index.html", {
        'name': 'Petrov ivan',
        'mail': 'petrov@mail.ru'
        
    })

def about(request):
    return render(request, "about.html", {
        "title": "Описание",
        "sur": "Попов",
        "name": "Никита",
        "midd": "Евгеньевич",
        "email": "popov@mail.ru"
    })

def get_item(request, id):
    for item in items:
        if item['id'] == id:
            return render(request, "item.html", {
                    "item": item,
                })

    return HttpResponse('Товар не найден')

def items_list(request):

    return render(request, "items_list.html", {
        "items": items
    })

