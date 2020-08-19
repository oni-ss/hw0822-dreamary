from django.shortcuts import render, redirect
from .models import Designer

# Create your views here.
def home(request):
    blogs = Designer.objects
    return render(request, 'home.html', {'blogs':blogs})
    
def create(request):
    if request.method == 'POST':
        designer = Designer()
        designer.image = request.FILES['p']
        designer.name = request.POST['n']
        designer.address = request.POST['a']
        designer.description = request.POST['d']
        designer.save()
        return redirect('home')
    else:
        return render(request, 'new.html')