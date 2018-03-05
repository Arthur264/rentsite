from .form import SingUpForm
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.generic import View
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import redirect
from django.template.loader import get_template
from c9_django.settings import EMAIL_HOST_USER
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from .token import account_activation_token
from c9_django.settings import SITE_URL
from datetime import datetime
from django.core.urlresolvers import reverse


# Create your views here.

class SingUp(View):
    def post(self, request):
        form = SingUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            SingUp.sendEmail(self, user)
            return JsonResponse({"success": 1, "message": []})
        else:
            return JsonResponse({"success": 0, "message": form.errors})

    def sendEmail(self, user):
        print(user)
        subject = "Confirm email"
        to = [user.email]
        from_email = EMAIL_HOST_USER
        ctx = {
            'message': 'Follow the link to confirm your registration',
            'token': account_activation_token.make_token(user),
            'domain': SITE_URL,
            'userId': urlsafe_base64_encode(force_bytes(user.pk)),
            'year': datetime.today().year
        }
        message = get_template('email/login.html').render(Context(ctx))
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = "html"
        msg.send()


class SingIn(View):
    def post(self, request):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return JsonResponse({"success": 1, "message": ""})
        else:
            return JsonResponse({"success": 0, "message": user})


class Activate(View):
    def get(self, request, userId, token):
        try:
            uid = force_text(urlsafe_base64_decode(userId))
            user = User.objects.get(pk=uid)
        except:
            user = None
        if user is not None:
            account_activation_token.check_token(user, token)
            user.backend = 'django.contrib.auth.backends.ModelBackend'
            user.is_active = True
            user.save()
            login(request, user)
            return redirect("house:index")
        else:
            return HttpResponse("Invalid token")


class Reset(View):
    def post(self):
        pass


class Logout(View):
    def get(self, request):
        logout(request)
        return redirect("house:index")
