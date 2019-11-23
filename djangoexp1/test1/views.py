from django.shortcuts import render,redirect
from .forms import Form1
from .models import Signup
import datetime

# Create your views here.
def one(request):
    dt = datetime.datetime.now()
    return render(request, 'index.html',{'date' : dt})

def sum(request):
    c=""
    if request.method == 'POST':
        a = request.POST.get('num1')
        b = request.POST.get('num2')
        c = int(a) + int(b)

    return render(request,'sum.html',{'result' : c})

def two(request):
    msg = ""
    form = Form1(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            msg = "Data inserted"

    return render(request, 'hello.html',{'form' : form,'msg' : msg,'name': 'Pranav'})

def step(request):
     data = Signup.objects.all()
     return render(request, 'step.html',{'data':data})

#def three(request):

 #   return render(request, 'step.html')

def delete(request, id):
    abc = Signup.objects.get(id=id)
    abc.delete()
    return redirect(step)

def four(request):
    return render(request, 'index.html')



