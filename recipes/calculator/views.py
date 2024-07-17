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
}

def recieps_view(request):
    dish = request.path[1:-1]
    servings = int(request.GET.get("servings", 1))
    if servings < 1:
        servings = 1
    recipe = DATA[dish]
    recipe_serving = {key: round(float(value) * servings, 1) for key, value in recipe.items()}
    
    context = {
            "recipe": recipe_serving,
            "servings": servings,
        }
    return render(request, "index.html", context)
