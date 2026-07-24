from django.http import HttpResponse
from django.shortcuts import render


DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}

def recipes_view(request, dish_name):
    recipe = DATA.get(dish_name)
    servings = request.GET.get('servings')
    result = {}
    if not recipe:
        return HttpResponse('Такого блюда нет')
    else:
        if servings:
            servings = int(servings)
        else:
            servings = 1
        for ingredient, amount in DATA[dish_name].items():
            result[ingredient] = servings * amount
    context = {
        'recipe': result
        }
    return render(request, 'calculator/index.html', context)

            
            
        


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
