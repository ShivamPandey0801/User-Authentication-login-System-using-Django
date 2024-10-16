from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.decorators import login_required
from app2.models import employee
from .forms import UploadFileForm
from .models import UploadedFile 
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            auth_login(request, user)
            return redirect('dashboard')  
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    
    return render(request, 'login.html')

@login_required
def dashboard(request):
    data = employee.objects.all()
    uploaded_files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'dashboard.html', {
        'data': data,
        'uploaded_files': uploaded_files,
    })

@login_required
def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_file = form.save(commit=False)  # Do not save yet
            uploaded_file.user = request.user  # Set the user
            uploaded_file.save()  # Now save it
            return redirect('upload_success')  # Redirect after successful upload
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

@login_required
def upload_success(request):
    return render(request, 'upload_success.html')  

@login_required
def delete_file(request, file_id):
    uploaded_file = get_object_or_404(UploadedFile, id=file_id, user=request.user)
    uploaded_file.delete() 
    return HttpResponseRedirect(reverse('dashboard')) 



#def upload_file(request):
    #if request.method == 'POST':
        #form = UploadFileForm(request.POST, request.FILES)
        #if form.is_valid():
           # uploaded_file = form.save(commit=False)
           # uploaded_file.user = request.user
           # uploaded_file.save()
           # return redirect('upload_success')  
   # else:
       # form = UploadFileForm()
    #return render(request, 'upload.html', {'form': form})


