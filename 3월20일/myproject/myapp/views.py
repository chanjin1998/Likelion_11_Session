from django.shortcuts import render

# Create your views here.
# request 요청을 받았을 때 home.html을 보여줘라.

def home(request):
    return render(request, 'home.html')
def base(request):
    return render(request,'base.html')