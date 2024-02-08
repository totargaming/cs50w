from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "hello/index.html")
def greet(request):
    name = request.GET.get('name', 'World')  # Use 'World' as a default value
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
