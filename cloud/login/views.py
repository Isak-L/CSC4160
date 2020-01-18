import time
from django.shortcuts           import render
from django.shortcuts           import render, redirect
from django.contrib.auth        import logout
from django.contrib.auth.models import User, auth
from django.http                import HttpResponseRedirect, HttpResponse
from django.contrib             import messages
from .models                    import Doctor

def register(request):
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname  = request.POST['lastname']
        username  = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email     = request.POST['email']

        global User

        if username != "":                                                      #check if user provide account name
            if User.objects.filter(username=username).exists() == False:        #check if the account had existed
                if password1 == password2:                                      #check if the two passwords are differents 
                    doctorID = "d" + time.strftime("%Y%m%d%H%M%S", time.localtime())
                    #print(dID)
                    Doc  = Doctor.objects.create(dID=doctorID, dAccount=username, dPassword=password1)
                    User = User.objects.create_user(username=username, password=password1)
                    return redirect('login')                                                      
                else:
                    message = "Your passwords does not match, please try again."
            else:
                message = "The account is already exist!"
        else:
            message = "Please enter Your account name!"

        '''
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'Email is taken!')
                return redirect('register')
            else:   
                user = User.objects.create_user(username=username, password=password1,email=email, first_name = firstname, last_name = lastname)
                user.save()
                print("User created!")
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')
        '''

    else:
        return render(request, 'register.html')


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        User = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request, User)
            Doc = Doctor.objects.get(dAccount=username)
            return redirect('../../home/%s' %Doc.dID)
        else:
            messages.info(request, "Username does not exist.or incorrect password!")
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect('login')
