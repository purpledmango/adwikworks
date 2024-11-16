from django.conf import settings
from django.core.mail import send_mail

from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self.create_user(email, password, **extra_fields)
    
    
def send_otp_email(user):
    # Generate the OTP and make sure it is returned from `generate_otp`
    otp = user.generate_otp()
    
    # Define email content
    subject = "OTP: Account Registration"
    body = f"Please use the OTP - {otp} to successfully complete the registration process for AdwikWorks.com"
    
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user.email]

    # Send the email
    send_mail(
        subject,
        body,
        email_from,
        recipient_list,
        fail_silently=False,
        html_message=f"<p>Please use the OTP - <b>{otp}</b> to successfully complete the registration process for AdwikWorks.com</p>"
    )