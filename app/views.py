from django.shortcuts import render

# Create your views here.

def jyothi(request):
    d={'username':'Jyothi','country':'India'}
    return render(request,'jyothi.html',context=d)
