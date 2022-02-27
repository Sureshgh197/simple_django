from . forms import ProfileForm,AccountCreationForm,LoginForm
from . models import Account


from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate
from django.contrib.auth import login as auth_log

from django.http import HttpResponse

from django.shortcuts import render,redirect

def index(request):
    return render(request, "accounts/index.html")

def signup(request):
    user_form = AccountCreationForm()
    profile_form = ProfileForm()

    if request.method == 'POST':
        user_form = AccountCreationForm(request.POST) 
        profile_form = ProfileForm(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            username = user_form.cleaned_data.get('username')
            password = user_form.cleaned_data.get('password1')
            profile_image = profile_form.cleaned_data.get('profile_image')

            user = User(username=username)
            user.set_password(password)
            user.save()
            profile = Account(user=user,profile_image=profile_image)
            profile.save()


            return HttpResponse('<h1>Account created</h1>')

        else:
            return HttpResponse('<p>Form are not valid')
    return render(request,'accounts/signup.html',{'profile_form':profile_form,'user_form':user_form})
            


def login(request):
    login_form = LoginForm()

    if request.method == 'POST':
        login_form = LoginForm(request.POST) 
        
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
        
            if user is not None:

                auth_log(request, user)

                return redirect('/')
            else:
                return HttpResponse('<h1>Incorrect credentials</h1>')
            
        else:
            return HttpResponse(login_form.errors)
    return render(request,'accounts/login.html',{'login_form':login_form})

def logout_view(request):
    logout(request)
    return redirect('/')