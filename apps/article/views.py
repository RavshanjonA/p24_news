from django.shortcuts import render, get_object_or_404
from django.views import View

from apps.article.models import Article, Category, Tag


class HomeView(View):
    def get(self, request):
        articles = Article.published.order_by('-published_at')
        first = articles[0]
        articles = articles[1:]
        tags = Tag.objects.all()
        context = {
            "article": first,
            "articles": articles,
            "tags": tags
        }
        return render(request, "article/index.html", context=context)




class CategoryView(View):
    def get(self, request, pk):
        # category =Category.objects.get(id=pk)
        # articles = Article.objects.filter(category=category)
        articles = Article.objects.filter(category__id=pk)
        context = {
            "articles": articles,
            # "tags": tags
        }
        return render(request, "article/page.html", context=context)


class ArticleDetialView(View):
    def get(self, request, slug):
        article = get_object_or_404(Article, slug=slug)
        return render(request, "article/article.html", {"article": article})
