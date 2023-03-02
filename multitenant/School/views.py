from django.shortcuts import render
from .models import Students

# Create your views here.
def get_Students(request):
    students = Students.objects.all()
    context = {
        'students': students
    }
    return render(request, 'index.html', context)