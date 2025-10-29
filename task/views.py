from django.shortcuts import render,redirect
from .models import Task
from .forms import TaskForm
from django.shortcuts import get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required







@login_required # <-- require login
def home(request):
    tasks=Task.objects.filter(user=request.user) # only current user's tasks
    form=TaskForm()

    if request.method=='POST': #this checks if the user submitted the form^^.
        form=TaskForm(request.POST)# this fills the form with submitted data.
        if form.is_valid(): # if its valid then save it./ runs Djangos build in validation^^.
            task=form.save(commit=False) # don't save to DB yet
            task.user= request.user  # assign logged-in user
            task.save()  # now save
            return redirect('home')
    context={'tasks':tasks, 'form':form} 
    return render(request, 'task/index.html', context)
@login_required 
def updateTask(request,pk):#pk stand for primary taks, and identifies which task is being edited^^
    task=get_object_or_404(Task, id=pk, user=request.user)#safely retrieves the task (returns 404 if not found).
    form=TaskForm(instance=task)#pre-fills the form with that task’s current data.
    if request.method=='POST': #this checks if the user submitted the form^^.
        form=TaskForm(request.POST, instance=task)# this fills the form with submitted data.
        if form.is_valid(): # if its valid then save it./ runs Djangos build in validation^^.
            form.save()# saves a new task in the database.
            return redirect('home')#On POST, it saves the changes and redirects home.
        
    context={'form':form}
    return render(request, 'task/updateTask.html', context)
@login_required
def deleteTask(request, pk):
    task=get_object_or_404(Task, id=pk, user=request.user)  # only current user's task
    if request.method=='POST':
        task.delete()
        return redirect('home')
    
    context={'task':task}
    return render(request, 'task/deleteTask.html', context)

def signup(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST) #UserCreationForm is Django’s built-in registration form.
        if form.is_valid():
            user=form.save()
            login(request, user)# logs the user in right after signup
            return redirect('home')
        
    else:
        form=UserCreationForm()
    return render(request, 'task/signup.html', {'form':form})
        

def login_view(request):
    if request.method=='POST':
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request, user)
            return redirect('home')
    else: 
        form=AuthenticationForm()       
    return render(request, 'task/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('login')# send them back to login page



