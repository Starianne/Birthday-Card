from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            login(request, form.save())
            return redirect("cards:list")
    else:
        form = UserCreationForm()
    
    return render(request,'userLogin/register.html', { "form":form })

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            login(request, form.get_user())
            #if logged in from new card, redirects to new card straight away like url suggests, if not, go to cards list
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect("cards:list")
    else:
        form = AuthenticationForm()
    return render(request,'userLogin/login.html', { "form":form })

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("cards:list")