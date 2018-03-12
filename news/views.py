from django.views.generic import ListView, DetailView, View
from news.models import News
from .forms import CommentForm
from django.http import JsonResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

class IndexView(ListView):
    template_name = 'news.html'
    model = News

    def get_queryset(self):
        news_list = News.objects.all()
        pagination = Paginator(news_list, 3)
        try:
            result = pagination.page(self.request.GET.get('page'))
        except PageNotAnInteger:
            result = pagination.page(1)
        except EmptyPage:
            result = pagination.page(pagination.num_pages)
        return result


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
