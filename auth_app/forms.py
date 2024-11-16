from django import forms
from .models import CustomUser

class RegistrationUserForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ["email", "first_name", "last_name", "contact_no", "password", "confirm_password"]

    def clean_confirm_password(self):
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        
        return confirm_password
    

class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ["email", "password"]
        widgets = {
            "password": forms.PasswordInput(),
        }