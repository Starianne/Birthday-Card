from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World! I'm Home.")

def about(request):
    return HttpResponse("My About Page.")