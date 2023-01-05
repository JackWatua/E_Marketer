from django  import forms
from authenticator.models import User

class SingUpForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email","password", ]
        widgets = {
            "first_name" : forms.TextInput(attrs={"class" : "form-control", "type" : "text"}),
            "last_name" : forms.TextInput(attrs={"class" : "form-control", "type" : "text"}),
            "email" : forms.EmailInput(attrs={"class" : "form-control", "type": "email"}),
            "password" : forms.PasswordInput(attrs={"class" : "form-control", "type" : "password"}),
        }


    #clean form

    def clean (self, *arg, **kwargs):
        cleaned_data = super().clean()
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        #email = cleaned_data.get("email")
        password = cleaned_data.get("password")


        #clean first and last name
        if not first_name.isalpha():
            self.add_error("first_name", "name must have alphabets only!")

        if not last_name.isalpha():
            self.add_error("last_name", "name must have alphabets only!")
        
        if len(password) < 8:
            self.add_error("password", "password too short!")

        if password.isalpha():
            self.add_error("password", "password too weak!")





class SignInForm (forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "password"]
        widgets = {
            "email" : forms.EmailInput(attrs={"class" : "form-control", "type": "email"}),
            "password" : forms.PasswordInput(attrs={"class" : "form-control", "type" : "password"}),
        }