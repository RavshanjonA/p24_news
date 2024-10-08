from threading import activeCount

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from apps.account.forms import SubscribeForm, FeedForm, LoginForm
from apps.account.models import Account
from apps.article.models import Article


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


class FeedView(LoginRequiredMixin, View):
    def get(self, request):
        form = FeedForm()
        return render(request, "account/contact.html", {"form": form})

    def post(self, request):
        form = FeedForm(data=request.POST)
        if form.is_valid():
            form.save(user=request.user)
            messages.info(request, "You feed successfully created ")
        else:
            return render(request, "account/contact.html", {"form": form})


class LoginView(View):
    def get(self, request):
        form = LoginForm()
        context = {
            "form": form
        }
        return render(request, "account/login.html", context=context)

    def post(self, request):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data["username"], password=form.cleaned_data["password"])

            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {user.username}.")
                return redirect("article:home")
            else:
                messages.warning(request, "With given data user not found")
                return redirect("article:home")


class LogoutView(LoginRequiredMixin, View):
    def get(self, request):
        logout(request)
        return redirect("article:home")


class ActivateView(View):
    def get(self, request, token):
        account = get_object_or_404(Account, password=token)
        account.is_active=True
        account.save()
        messages.success(request, f"Your account successfully activated {account.username}")
        return redirect("article:home")