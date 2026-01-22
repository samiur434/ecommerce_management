from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from .forms import *
from django.http import Http404
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode,urlsafe_base64_encode
from .utils import *
from django.utils.encoding import force_bytes,force_str,DjangoUnicodeDecodeError
from django.core.mail import EmailMessage
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.forms import AuthenticationForm





def Signup(request):
    if request.method =='POST':
       form=SignUpForm(request.POST)
       if form.is_valid():
           user = form.save()
           
        
           user.save()
           
        #    uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        #    token = generate_token.make_token(user)
        #    url = reverse('activate', kwargs={'uidb64': uidb64, 'token': token})
        #    activation_link = request.build_absolute_uri(url)
        #    email_subject="activate your account"
        #    message=render_to_string("activation_email.html",{
        #        "user":user,
               
        #        "domain":'127.0.0.1:8000',
        #        "uidb64":uidb64,
        #        "token":token,
        #    })
        #    print("email sent properly")
        #    email_message=EmailMessage(email_subject,message,settings.EMAIL_HOST_USER,)
        #    email_message.send()
        #    messages.success(request,"activate your account by clicking the link in your gmail")
           
           return redirect("/")
    else:
       
     form=SignUpForm()
    return render(request, 'signup.html',{'form':form})

def Login(request):
    if request.method == 'POST':
        form = loginForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')  # Redirect to a success page
            else:
                messages.info(request, "Invalid username or password")
                return render(request, 'login.html',{'form':form})
                
    else:
        form = loginForm()
    return render(request, 'login.html', {'form': form})

def Logout(request):
    logout(request)
    return redirect('/')



def update(request,pk):
    try:
        user_instance = User.objects.get(pk=pk)
    except User.DoesNotExist:
        raise Http404("User does not exist")

    if request.method == 'POST':
        form = SignUpForm(request.POST, instance=user_instance)  # Pass instance=user_instance here
        if form.is_valid():
            form.save()
            messages.success(request, "Updated successfully")
            return redirect('index')
    else:
        form = SignUpForm(instance=user_instance)  # Pass instance=user_instance here

    context = {"form": form}
    return render(request, 'update.html', context=context)

# class activate(View):
#     def get(self,request,uidb64,token):
#         try:
#             uid = force_str(urlsafe_base64_decode(uidb64))
#             user = User.objects.get(pk=uid)
#         except Exception as identifier:
#             user = None
#         if user is not None and generate_token.check_token(user, token):
#             user.is_active = True
#             user.save()
#             messages.success(request, "account activated")
#             return redirect('/')
#         return render(request,'login.html')

