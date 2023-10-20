from django.shortcuts import render

# Create your views here.
def eval(request):
    return render(request,'templatesEva2Backend/index.html')