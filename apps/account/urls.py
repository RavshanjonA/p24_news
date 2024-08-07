from django.urls import path

from apps.account.views import SubscribeView

app_name = "account"
urlpatterns = [
    path('subcribe/', SubscribeView.as_view(), name="subscribe")
]
