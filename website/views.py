from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
from .models import Record

# Create your views here.

def home(request):
    records = Record.objects.all()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('home')
        else:
            messages.error(request, 'Invalid username or password')
            return redirect('home')
    else:
        return render(request, 'home.html',{'records':records})


def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'Account created successfully')
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html',{'form':form})
    return render(request, 'register.html',{'form':form})

def logout_user(request):
    logout(request)
    messages.success(request, 'You are now logged out')
    return redirect('home') 

def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Record.objects.get(id=pk)
        return render(request, 'record.html',{'customer_record':customer_record})
    else:
        messages.error(request, 'Please login to view this page')
        return redirect('home')
    
def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_record = Record.objects.get(id=pk)
        delete_record.delete()
        messages.success(request, 'Record deleted successfully')
        return redirect('home')
    else:
        messages.error(request, 'Please login to view this page')
        return redirect('home')
    

def add_record(request):
    form = AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                add_record = form.save()
                messages.success(request,"Record Added Successfully")
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,'Please login to view this page')
        return redirect('home')
    
def update_record(requset,pk):
    if requset.user.is_authenticated:
        current_record = Record.objects.get(id=pk)
        form = AddRecordForm(requset.POST or None, instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(requset,"Record Has Been Updated")
            return redirect("home")
        return render(requset,'update_record.html',{'form':form})
    else:
        messages.success(request,'Please login to view this page')
        return redirect('home')