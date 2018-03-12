from django.contrib import admin
from .models import News, NewsImage
# Register your models here.
class NewsImageInline(admin.StackedInline):
    model = NewsImage
    extra = 3
    can_delete = False
    fk_name = 'news'

class NewsAdmin(admin.ModelAdmin):
    model = News
    inlines = (NewsImageInline, )
    fields = ('title', 'subtitle', 'text', 'user')

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

admin.site.register(News, NewsAdmin)