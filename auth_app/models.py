from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import random
from django.utils import timezone

class CustomUser(AbstractBaseUser):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=35)
    last_name = models.CharField(max_length=35)
    contact_no = models.CharField(unique=True, max_length=15)
    date_of_birth = models.DateField()
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    otp = models.CharField(max_length=6, blank=True, null=True)
    otp_expiry = models.DateTimeField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'contact_no', 'date_of_birth']

    def clean(self):
        super().clean()

        if CustomUser.objects.filter(email = self.email).exclude(pk = self.pk).exists():
            raise ValidationError({"email": _("This E-mail is already in use!")})
        
        if CustomUser.objects.filter(contact_no = self.contact_no).exclude(pk = self.pk).exists():
            raise ValidationError({"contact_no": _("The Phone number is already associated with a different account!")})



    def generate_otp(self):
        self.otp = f'{random.randint(100000, 999999)}'
        self.otp_expiry = timezone.now() + timezone.timedelta(minutes =10)
        self.save()

    def verify_otp(self, otp):
        if self.otp == otp and timezone.now() < self.otp_expiry:
            self.is_active = True
            self.otp = None
            self.otp_expiry=None
            self.save()
            return True
        return False
        
    def __str__(self):
        return self.first_name + " " + self.last_name

