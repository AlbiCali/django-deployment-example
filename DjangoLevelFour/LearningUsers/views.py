from django.shortcuts import render
from LearningUsers.forms import UserForm
from LearningUsers.forms import UserProfileInfoClassForm

from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from LearningTemplates.views import index


# Create your views here.
def  Register(request):
    #create a context dictionary
    #return render(request,'UserIndex.html')
    registered=False
    if request.method=='POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoClassForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():

            user=user_form.save() #save the user to the DB
            user.set_password(user.password) # Hashing the password
            user.save() #save the changes to the users

            profile=profile_form.save(commit=False)#stop the saving on the db to avoid colllisions
            profile.user = user # set up the one to one relationship with the user

            if 'profile_pic' in request.FILES:
                profile.profile_pic = request.FILES['profile_pic']

            profile.save()

            registered=True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form=UserProfileInfoClassForm()

    return render(request,'Registration.html',
                  {'user_form':user_form,
                  'profile_form':profile_form,
                  'registered':registered                  
                  })


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('LearningTemplates:index'))


def  user_login(request):
    #create a context dictionary
    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('LearningTemplates:index'))
            else:
                return HttpResponse("account not active")
        else:
            print("someone tried to log in and failed")
            print("Username: {} and password {}".format(username,password))
            return HttpResponse("Invalid login details supplied")
    else:
        return render(request,'LogIn.html')