from django.shortcuts import render

# Create your views here.
def jinja(request):
    d={'name':'shahnaz','age':21}
    return render(request,'jinja.html',d)

