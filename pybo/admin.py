from django.contrib import admin
from .models import Maincont,Comment,Similar

class MaincontAdmin(admin.ModelAdmin):
    search_fields = ['subject'] #제목으로 검색 하기

class CommentAdmin(admin.ModelAdmin):
    search_fields = ['comment'] #댓글로 검색하기

class SimilarAdmin(admin.ModelAdmin):
    search_fields = ['similar'] #유사도로 검색하기


admin.site.register(Maincont, MaincontAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Similar,SimilarAdmin)


# Register your models here.
