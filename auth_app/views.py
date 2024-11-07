from django.shortcuts import render
from .forms import RegistrationUserForm
from .utils import send_otp_email

def home_view(request):
    return render(request, "index.html")

def register_user(request):
    if request.method == 'POST':
        form = RegistrationUserForm(request.POST)
        if form.is_valid():
            
            user = form.save(commit=False)
           
            user.set_password(form.cleaned_data['password'])
            print("generating OTP")
            user.generate_otp()
            send_otp_email(user)
            
            # user.save()
            # return redirect('login')  # Redirect to login page after successful registration
    else:
        form = RegistrationUserForm()

    return render(request, "signup.html", {"form": form})


def login_user(request):
    pass

def logout_user(request, user):
    pass

