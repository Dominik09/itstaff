from django.contrib import admin
from article.models import Article, Comments


class ArticleInLine(admin.StackedInline):
	model = Comments
	extra = 3


class ArticleAdmin(admin.ModelAdmin):
	fields = ['title', 'text', 'date']
	inlines = [ArticleInLine]
	list_filter = ['date']


admin.site.register(Article, ArticleAdmin)