from django.http import HttpResponse

def home(request):
    return HttpResponse(request,"<h1>Hello World</h1>")