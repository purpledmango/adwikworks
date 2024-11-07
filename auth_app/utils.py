from django.conf import settings
from django.core.mail import send_mail

def send_otp_email(user):
    otp = user.generate_otp()
    subject  = "OTP: Account Registeration"
    body = f" Please use the OTP - <b> {otp} <b/> to succefully complete the regiseration process for AdwikWorks.com"
    email_from = settings.EMAIL_HOST_USER
    recepient_list = [user.email]
    send_mail(subject, body, email_from, recepient_list, fail_silently=False)
    
    

