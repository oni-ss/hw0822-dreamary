from django.shortcuts import render, redirect
from .models import Designer

# Create your views here.
def home(request):
    return render(request, 'home.html')

def introduce(request):
    return render(request, 'introduce.html')


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

def update(request, designer_id):
    get_object_or_404(Designer, pk = designer_id)

    if request.method == 'POST':
        if 'image' in request.FILES:
            post.image = request.FILES['image']
        post.name = request.POST['name']
        post.address = request.POST['address']
        post.description = request.POST['description']

        post.save()

        return redirect('detail', post.id)
    else:
        return render(request, 'update.html', {'designer' : post})