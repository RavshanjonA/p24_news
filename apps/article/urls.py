from django.urls import path

from apps.article.views import HomeView, CategoryView

app_name = 'article'
urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('category/<pk>/', CategoryView.as_view(), name="category")
]
