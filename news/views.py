from django.views.generic import ListView, DetailView, View
from news.models import News
from .forms import CommentForm
from django.http import JsonResponse


# Create your views here.

class IndexView(ListView):
    template_name = 'news.html'
    model = News

    def get_queryset(self):
        return News.objects.all()


class DetailsView(DetailView):
    template_name = 'newsdetails.html'
    model = News

    def get_context_data(self, **kwargs):
        content = super(DetailsView, self).get_context_data(**kwargs)
        return content


class CommentView(View):
    def post(self, request):
        comment = CommentForm(request.POST)
        news = News.objects.get(id=comment.data['news'])
        print(news.id)
        comment.news = news
        if comment.is_valid():
            comment.save()
            return JsonResponse({'success': 1})
        else:
            return JsonResponse({'success': 0})
