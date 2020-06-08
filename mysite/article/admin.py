from django.contrib import admin
from .models import Article
#admin.site.register(Article)


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','likes',)
    list_filter = ('title','pub_date','likes',)
    search_fields = ('title','body','pub_date','likes',)
