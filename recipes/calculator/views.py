import itertools

from django.http import HttpResponse, HttpResponseNotFound
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


# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
def get_recipe(request, recipe_name):
    context = dict(recipe_name=recipe_name, servings=1)
    try:
        recipe = DATA[recipe_name.lower()].copy()
        servings = request.GET.get('servings')
        if servings and servings.isalnum():
            context['servings'] = int(servings)
            for key in recipe:
                recipe[key] *= context['servings']
        context['recipe'] = recipe
    finally:
        return render(request, 'calculator/index.html', context)
