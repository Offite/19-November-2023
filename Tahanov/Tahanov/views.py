from django.shortcuts import render

def home(request):
    context = {
        'name': 'ваше имя',
        'age': 'ваш возраст',
        'interests': 'ваши интересы',
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        'from': 'место, откуда приехали',
        'academic_achievements': 'успеваемость в школе',
        'studying': 'любите/не любите учиться',
    }
    return render(request, 'about.html', context)

def contacts(request):
    context = {
        'github': 'ваш GitHub',
    }
    return render(request, 'contacts.html', context)
