from .form import SingUpForm
from django.http import JsonResponse
from django.views.generic import ListView, DeleteView, View
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
from django.template import Context
from django.template.loader import get_template
from c9_django.settings import EMAIL_HOST_USER
from .token import account_activation_token
from c9_django.settings import SITE_URL
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
            'domain': SITE_URL
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
            return JsonResponse({"success": 1, "message": []})
        else:
            return JsonResponse({"success": 0, "message": user})
