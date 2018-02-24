from django.shortcuts import render, HttpResponse
from .form import SingUpForm
# Create your views here.
def singin(request):
     if request.method == 'POST':
         form = SingUpForm(request.POST)
         if form.is_valid():
             form.save()
             print ("POST", form)
         else:
             print ("false", form.data)

     return HttpResponse(   form.error_messages)