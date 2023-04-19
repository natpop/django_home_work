from django.http import HttpResponse
from django.shortcuts import render
from . models import Item

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

items_bd = Item.objects.all()

def home(request):
    return render(request, "index.html", {
        'name': 'Petrov ivan',
        'mail': 'petrov@mail.ru',
        "title": "Главная страница",        
    })

def about(request):
    return render(request, "about.html", {
        "title": "Описание",
        "sur": "Попов",
        "name": "Никита",
        "midd": "Евгеньевич",
        "email": "popov@mail.ru",
        "title": "About"
    })

def get_item(request, id):
        
        item = Item.objects.get(id=id)
                
        return render(request, "item.html", {
                "item": item,
            })

def items_list(request):
    
    return render(request, "items_list.html", {
        "items_bd": items_bd,
        "title": "Список товаров",
    })

