from django.shortcuts import render


def todo_list(request):
    return render(request, 'frontend/list.html',)
