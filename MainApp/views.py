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
   {"id": 1, "name": "Кроссовки abibas"},
   {"id": 2, "name": "Куртка кожаная"},
   {"id": 3, "name": "Coca-cola 1 литр"},
   {"id": 4, "name": "Картофель фри"},
   {"id": 5, "name": "Кепка"},
]


def home(request):
    return render(request, "index.html", {
        'name': 'Petrov ivan',
        'mail': 'petrov@mail.ru'
    })

def about(request):
    res = f'''
        Имя: <b>{autor['name']}</b><br>
        Отчество:<b>{autor['mid']}</b><br>
        Фамилия:<b>{autor['sur']}</b><br>
        Телефон:<b>{autor['phone']}</b><br>
        email: <b>{autor['email']}</b><br>
    '''  

    return HttpResponse(res)

def get_item(request, id):
    for item in items:
        
        if item['id'] == id:
            res = f"""
                <h2>Имя: {item['name']}</h2>
                <a href='/items'>Назад</a>
            """
            return HttpResponse(res)
    return HttpResponse('Товар не найден')

def items_list(request):

    return render(request, "items_list.html", {
        "items": items
    })

