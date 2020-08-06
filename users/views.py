from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegistrationForm, userupdateform , profileupdateform
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created, plese login')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request,'users/register.html', {'form': form}) 

@login_required # @ adds functionality to an existing function
def profile(request):
    if request.method == 'POST':
        u_form = userupdateform(request.POST, instance=request.user) #instance to fill the username field by logged in persons username
        P_form = profileupdateform(request.POST,
         request.FILES, 
         instance=request.user.profile)

        if u_form.is_valid() and P_form.is_valid():
            u_form.save()
            P_form.save()
            messages.success(request, f'Your account has been updated:')
            return redirect('profile')
    else:
        u_form = userupdateform(instance=request.user) #instance to fill the username field by logged in persons username
        P_form = profileupdateform(instance=request.user.profile)


    context = {
      
        'u_form': u_form,
        'p_form': P_form
    }
    return render(request, 'users/profile.html',context)
