from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import RegistrationUserForm, LoginForm
from .utils import send_otp_email
from .models import CustomUser

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail  # To send the OTP email
from django.contrib import messages  # To display success/error messages

def register_user(request):
    if request.method == 'POST':
        # Retrieve data from the POST request
        email = request.POST.get("email")
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        contact_no = request.POST.get("contact_no")
        password = request.POST.get("password")
        
        # Basic validation (you can extend this as needed)
        if not email or not first_name or not password:
            messages.error(request, "All fields are required.")
            return render(request, "signup.html")

        try:
            # Create the user using the provided details
            user = CustomUser.objects.create_user(email=email, first_name=first_name, last_name = last_name, contact_no=contact_no,password=password)
            
            
            # Generate OTP and send email (assuming OTP method is implemented)
            print("Generating OTP")
              # You need to implement this method
            
            # Send OTP email (implement send_otp_email function)
            # send_otp_email(user, otp)  # Uncomment once implemented

            # Save user
            user.save()

            # Success message
            messages.success(request, "Registration successful! Please login")

            # Redirect to login page
            return redirect('login_user')

        except Exception as e:
            # Handle errors (e.g., if the email already exists)
            messages.error(request, f"An error occurred: {e}")
            return render(request, "signup.html")

    return render(request, "signup.html")


def login_user(request):
    if request.method == "POST":
        # Get the email and password from POST data directly
        email = request.POST.get("email")
        password = request.POST.get("password")

        print("Email->", email)
        print("password->", password)

        # Authenticate the user
        user = authenticate(request, email=email, password=password)

        if user is not None:
           
            login(request, user)
            return redirect("home")  # Redirect to the homepage or another page
        else:
            # If authentication fails, show an error message
            messages.error(request, "Invalid email or password")

    return render(request, "login.html")

def logout_user(request):
    logout(request)
    messages.success(request, "You have successfully logged out.")
    return redirect("home")  
