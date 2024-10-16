from django.shortcuts import render,redirect
from django.contrib.auth.models import User 
# Create your views here.

def signup(request):
    if request.method == 'POST':
        username=request.POST['username']
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        password=request.POST['password']

        x=User.objects.create_user(username=username, first_name=firstname, last_name=lastname, password=password)
        x.save()
        print('User Created')
        return redirect('/')



    else:
        return render(request,'x.html')