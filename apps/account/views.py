from django.shortcuts import render, redirect
from django.views import View

from apps.account.forms import SubscribeForm


class SubscribeView(View):
    def get(self, request):
        form = SubscribeForm()
        context = {
            "form": form
        }
        return render(request, "account/subscribe.html", context)

    def post(self, request):
        form = SubscribeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("article:home")
        else:
            context = {
                "form": form
            }
            return render(request, "account/subscribe.html", context)
