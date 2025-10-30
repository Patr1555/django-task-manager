from django.shortcuts import render, redirect,get_object_or_404
from .models import BlogPost
from .forms import BlogPostForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm  # built-in Django form for user registration
from django.contrib.auth import login       
from django.contrib import messages
            



@login_required
def blog_home(request):
    posts=BlogPost.objects.filter(author=request.user)
    form=BlogPostForm()

    if request.method=='POST':# checks if user submitted a form
        form=BlogPostForm(request.POST)# fill form with submitted data
        if form.is_valid():
            post=form.save(commit=False)# create object but don’t save yet
            post.author= request.user# assign logged-in user as author
            post.save()
            messages.success(request, 'Your post was created successfully!')
            return redirect('blog_home')
    context={'posts':posts, 'form':form}
    # send posts and form to template
    return render(request, 'blog/blog_home.html', context)


# Update view – edit a post
@login_required
def blog_update(request, pk):
    post= get_object_or_404(BlogPost, id=pk, author=request.user)# get post by ID and make sure it belongs to current user
    form=BlogPostForm(instance=post)# pre-fill form with post’s current data
    if request.method== 'POST':
        form=BlogPostForm(request.POST, instance=post)#Update form with submitted data.
        if form.is_valid():
            form.save()
            messages.success(request, 'Your post was Updated successfully!')
            return redirect('blog_home')
    return render(request, 'blog/blog_update.html', {'form':form} )



# Delete view – confirm and delete a post
@login_required#protects all actions
def blog_delete(request, pk):
    post=get_object_or_404(BlogPost, id=pk, author=request.user)
# only allow deleting posts owned by current user

    if request.method=='POST': # if user confirms deletion
      post.delete()
      messages.success(request,'Your post was deleted successfully!')
      return redirect('blog_home')

    return render(request, 'blog/blog_delete.html', {'post':post})


def login_view(request):
    if request.method== 'POST':
        form=AuthenticationForm(request, data=request.POST)# Fill the built-in AuthenticationForm with the data the user typed
        if form.is_valid():
            user=form.get_user() # If the form passes validation, get the actual user object
            login(request, user)# Create a session for that user (so Django knows they’re logged in)
            return redirect('blog_home')
    else:
            form=AuthenticationForm()# If GET request (first time visiting), show a blank form
    return render(request, 'blog/login.html', {'form':form})      

def logout_view(request):
    logout(request)

    
    # End the user session (removes authentication info)
    

# Show a simple logout confirmation page
    return render(request, 'blog/logout.html')



def signup_view(request):
    if request.method=='POST':# If user submitted the form (via POST), we fill the form with their input data
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save()
            messages.success(request, f"Welcome, {user.username}! Your account was created.")
            login(request, user)# After signup, automatically log the user in so they don't need to re-enter credentials
            return redirect('blog_home')
    else:
        form=UserCreationForm()# If the page is loaded for the first time (GET request), we show a blank sign-up form

    return render(request,  'blog/signup.html', {'form':form})
# Finally, render the signup page and pass the form object to the HTML template