from django.shortcuts import render


def platform(request):
    return render(request, 'third_task/platform.html')


def games(request):
    games_list = {
        "Atomic Heart": "#",
        "Cyberpunk 2077": "#",
        "PayDay2": "#"
    }
    return render(request, 'third_task/games.html', {'games': games_list})


def cart(request):
    return render(request, 'third_task/cart.html')

