from django.shortcuts import render, redirect
from django.views.generic import View
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)

from django.contrib.auth.views import LogoutView

from accounts.forms import CustomUserCreationForm

# Create your views here.

User = get_user_model()


class RegisterView(View):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    extra_context = {"page_title": "User Registration"}
    success_message = "Welcome to the website."
    success_url = reverse_lazy("accounts:login_view")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(request.META.get("HTTP_REFERER"))
        context = {"form": self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        context = {"form": form}
        return render(request, self.template_name, context)


class CustomLogoutView(LogoutView):
    def post(self, request, *args, **kwargs):
        # is user is not authenticated
        logout(request)
        return redirect(self.next_page)
