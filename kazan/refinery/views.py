from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'kazan/index.html')

def about(request):
    return render(request, 'kazan/about.html')

def quality(request):
    return render(request, 'kazan/quality.html')
