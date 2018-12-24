from django.shortcuts import render

from .models import Course

def index(request):
    courses = Course.objects.order_by('-id')[:5]
    context = {'courses': courses, 'title' : 'No existen cursos que mostrar por ahora!'}

    return render(request, 'index.html', context)
