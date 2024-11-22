from django.shortcuts import render, reverse

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


def home_view(request):
    template_name = 'calculator/home.html'

    pages = {
        'Омлет': reverse('omlet'),
        'Паста': reverse('pasta'),
        'Бутерброд': reverse('butter')
    }

    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def omlet_view(request):
    template_name = 'calculator/index.html'
    num = int(request.GET.get('servings', 1))

    recipe = {
        'яйца, шт': DATA['omlet']['яйца, шт'] * num,
        'молоко, л': DATA['omlet']['молоко, л'] * num,
        'соль, ч.л.': DATA['omlet']['соль, ч.л.'] * num,
    }

    context = {
        'recipe': recipe,
        'name': 'Омлет'
    }

    return render(request, template_name, context)


def pasta_view(request):
    template_name = 'calculator/index.html'
    num = int(request.GET.get('servings', 1))

    recipe = {
        'макароны, г': DATA['pasta']['макароны, г'] * num,
        'сыр, г': DATA['pasta']['сыр, г'] * num,
    }

    context = {
        'recipe': recipe,
        'name': 'Паста'
    }

    return render(request, template_name, context)


def butterbrod_view(request):
    template_name = 'calculator/index.html'
    num = int(request.GET.get('servings', 1))

    recipe = {
        'хлеб, ломтик': DATA['buter']['хлеб, ломтик'] * num,
        'колбаса, ломтик': DATA['buter']['колбаса, ломтик'] * num,
        'сыр, ломтик': DATA['buter']['сыр, ломтик'] * num,
        'помидор, ломтик': DATA['buter']['помидор, ломтик'] * num,
    }

    context = {
        'recipe': recipe,
        'name': 'Паста'
    }

    return render(request, template_name, context)
