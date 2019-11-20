from django.shortcuts import render,redirect
from .forms import Form1
from .models import Signup

# Create your views here.
def one(request):
    return render(request, 'hello.html')

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

def three(request):

    return render(request, 'step.html')

def delete(request, id):
    abc = Signup.objects.get(id=id)
    abc.delete()

    return redirect(three)



