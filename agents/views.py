from django.views.generic import ListView, DetailView
from authentication.models import UserProfile, Role, UserPhone
from helpers.objects import filter_or_None


# Create your views here.
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