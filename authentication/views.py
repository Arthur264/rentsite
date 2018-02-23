from django.shortcuts import render
from .form import SingUpForm
# Create your views here.
def singin(request):
     if request.method == 'POST':
         print ("POST")
     return True