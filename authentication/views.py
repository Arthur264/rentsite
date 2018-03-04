from .form import SingUpForm
from django.http import JsonResponse
from django.views.generic import ListView, DeleteView, View
from django.contrib.auth import authenticate, login
from django.core.mail import EmailMessage
# Create your views here.


class SingUp(View):

    def post(self, request):
        form = SingUpForm(request.POST)
        if form.is_valid():
            email = EmailMessage('title', 'body', to=[form.data["email"]])
            email.send()
            form.save()
            return JsonResponse({"success": 1, "message": []})
        else:
            return JsonResponse({"success": 0, "message": form.errors})


class SingIn(View):

    def post(self, request):
        user = authenticate(username=request.POST["username"], password=request.POST["password"])
        if user is not None:
            login(request, user)
            return JsonResponse({"success": 1, "message": []})
        else:
            return JsonResponse({"success": 0, "message": user})
