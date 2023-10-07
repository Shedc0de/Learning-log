from django.shortcuts import render
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect

# Create your views here.

def logout_view(request):
    """Log the user out"""
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('learning_logs:index'))
    else:
        """Register a user"""
        if request.method != 'POST':
            # display a blank form
            form = UserCreationForm()
        else:
            form = UserCreationForm(data=request.POST)
            if form.is_valid():
                new_user = form.save()
                # register user and redirect to the home page
                authenticated_user = authenticate(username=new_user.username, password=request.POST['password1'])
                login(request, authenticated_user)


                return HttpResponseRedirect(reverse('learning_logs:index'))
            
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    
    
