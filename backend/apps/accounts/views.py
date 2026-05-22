from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from .forms import UserLoginForm
# Create your views here.

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redirect to a success page.
            return redirect("notes:home")
        else:
            # Return an 'invalid login' error message.
            return redirect("accounts:login")
    else:
        form = UserLoginForm()

    return render(request, "accounts/login.html", {"form": form})

