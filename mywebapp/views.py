from django.shortcuts import render

# Create your views here.
def aboutview(request):
    return render(request, 'mywebapp/about.html', {})
def projectview(request):
    return render(request, 'mywebapp/project.html', {})