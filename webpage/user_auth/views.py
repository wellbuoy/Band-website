from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login
from .forms import UserRegistrationForm

def index(request):

    # Render the index.html page
    return render(request, 'user/index.html')

#Handles login functionality.
def login_view(request):
    if request.method == 'POST':

        # Check if form data is valid
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():

             # Get the valid user
            user = form.get_user()

            # Log in the user
            login(request, user)

            # Redirect to index page
            return redirect('home')
        
    else:

        # Create an empty form for GET requests
        form = AuthenticationForm()

    # Render the login page with the form
    return render(request, 'user/login.html', {'form': form})

def register(request):

    # If request method is POST
    if request.method == 'POST':

        # Initialize form with POST data
        form = UserRegistrationForm(request.POST)

        # Check if form data is valid
        if form.is_valid():

            # Save form data
            form.save()

            # Redirect to login page
            return redirect('login')
        
    # If request method is not POST
    else:

        # Initialize empty form
        form = UserRegistrationForm()

    # Render registration page with form
    return render(request, 'user/register.html', {'form': form})