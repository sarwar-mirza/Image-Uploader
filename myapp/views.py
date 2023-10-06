from django.shortcuts import render
from .models import Image
from .forms import ImageForm
# Create your views here.
def home(request):
    if request.method == 'POST':
        fm = ImageForm(request.POST, request.FILES)      # request.FILES
        
        if fm.is_valid():
            fm.save()
    else:
        fm = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html', {'img':img, 'form':fm})
