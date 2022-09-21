from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.template.defaulttags import url
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from django.contrib.auth.decorators import login_required

from .models import Customer
from .tokens import account_activation_token

# AIRDROP profile/game/etc

"""
def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == "POST":
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)

"""


def login_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == "POST":
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username or Password is incorrect')

        context = {}
        return render(request, 'login.html', context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.is_active = False
                user.save()

                customer = Customer.objects.create(
                    user=user,
                    name=user.username,
                )
                customer.save()
                current_site = get_current_site(request)
                mail_subject = 'Activate your blog account.'
                message = render_to_string('activate.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': account_activation_token.make_token(user),
                })
                to_email = form.cleaned_data.get('email')
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                # Added username after video because of error returning customer name if not added

                messages.info(request, 'Please confirm your email address to complete the registration')
                # return HttpResponse('Please confirm your email address to complete the registration')
        else:
            form = CreateUserForm()
        return render(request, 'register.html', {'form': form})


def logOutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def home_page(request):
    # print(request.user.customer)
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    profile_pic = "../../static/" + str(customer.profile_pic) # IMG_20220329_0007.jpg
    # "https://www.pngarts.com/files/5/LeBron-James-PNG-Image-Background.png"hh
    context = {'form': form, 'profile_pic': profile_pic, 'overall': 98}
    """if request.method == "POST":
        form = UploadFileForm()
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')"""
    return render(request, 'home.html', context)


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        context = {}
        return render(request, 'thx.html', context)
    else:
        return HttpResponse('Activation link is invalid!')
