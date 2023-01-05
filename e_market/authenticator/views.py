from django.shortcuts import render
from .forms import SingUpForm,SignInForm

# Create your views here.
def signUp (request):
    if request.method == "POST":
        form = SingUpForm(request.POST)
    else:
        form = SingUpForm()

    context = {
        "form" : form,
        "method": "post",
        "option" : "Sign Up",
    }
    return render(request, "auth.html", context = context)


def signIn (request):
    if request.method == "GET":
        form = SignInForm(request.GET)
    else:
        form = SignInForm()

    context = {
        "form" : form,
        "method" : "get",
        "option" : "Sign In"
    }
    return render(request, "auth.html", context = context)