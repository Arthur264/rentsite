from django.views.generic import ListView, DetailView, View
from authentication.models import UserProfile, Role, UserPhone
from helpers.objects import filter_or_None
from django.http import JsonResponse
from .form import ContactForm
from django.template import Context
from django.core.mail import EmailMessage
from django.template.loader import get_template
from c9_django.settings import EMAIL_HOST_USER, SITE_URL
from datetime import datetime

class IndexView(ListView):
    template_name = "agent.html"

    def get_queryset(self):
        agents = filter_or_None(UserProfile, user_role=Role.objects.get(name="Agent").pk)
        for item in agents:
            item.phone = UserPhone.objects.filter(user=item.user.pk)
        return agents


class DetailsViews(DetailView):
    template_name = "agentDetails.html"
    model = UserProfile

    def get_context_data(self, **kwargs):
        content = super(DetailsViews, self).get_context_data(**kwargs)
        print(content)
        print(type(content))
        content["userprofile"].phone = UserPhone.objects.filter(user=content["userprofile"].user.pk)
        return content


class ContactView(View):
    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            ContactView.sendEmail(self, form.data)
            return JsonResponse({"success": 1, "message": []})
        else:
            return JsonResponse({"success": 0, "message": form.errors})

    def sendEmail(self, form):
        print(form)
        subject = "Message from user"
        to = [form['email_user']]
        from_email = EMAIL_HOST_USER
        ctx = {
            'message': 'Follow the link to confirm your registration',
            'domain': SITE_URL,
            'user': form,
            'year': datetime.today().year
        }
        message = get_template('email/contact.html').render(Context(ctx))
        msg = EmailMessage(subject, message, to=to, from_email=from_email)
        msg.content_subtype = "html"
        msg.send()
