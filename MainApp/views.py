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
    return HttpResponse('''
        <h1>Привет, изучаем django</h1>
    ''')

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
            return HttpResponse(item['name'])
    return HttpResponse('Товар не найден')



def items_list(request):
    res = '<h2>Список товаров</h2>'
    for item in items:
        res += f'<li>{item["name"]}</li>'
    
    res += '</ol>'
    return HttpResponse(res)

