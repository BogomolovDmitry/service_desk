from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.order_by('-id')
    return render(request, 'main/index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance
            # return redirect('home')
            return render(request, 'main/create.html', {'form': form, 'img_obj': img_obj})
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'main/create.html', context)

#TODO: Добавить отображение в виде таблицы
