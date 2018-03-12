from django.views.generic import TemplateView
# Create your views here.

class ContactView(TemplateView):
    print("trg")
    template_name = "contact.html"

