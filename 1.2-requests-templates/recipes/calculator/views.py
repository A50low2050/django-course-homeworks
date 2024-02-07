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


def get_dish(request, recipe):
    servings = request.GET.get('servings')
    get_recipe = DATA.get(recipe)

    context = {
        'recipe': {

        }
    }

    if get_recipe:
        for ingredient, amount in get_recipe.items():
            if servings:
                context['recipe'][ingredient] = round(amount * int(servings), 2)
            else:
                context['recipe'][ingredient] = amount
        return render(request, 'calculator/index.html', context)
    else:
        return render(request, 'calculator/index.html', context)
