from django.shortcuts import render, redirect
from django.views.generic import View, UpdateView
from django.contrib import messages
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import (
    authenticate,
    login,
    logout,
    get_user_model,
)

from django.contrib.auth.views import LoginView, LogoutView

from accounts.forms import CustomUserCreationForm, UserProfileForm

# Create your views here.

User = get_user_model()


class UserProfileView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    template_name = "accounts/user_profile.html"
    extra_context = {"page_title": "Profile"}
    form_class = UserProfileForm
    success_message = "Successfully saved the profile details."
    success_url = reverse_lazy("accounts:user_profile_view")

    def get_object(self):
        return self.request.user


class CustomLoginView(SuccessMessageMixin, LoginView):
    template_name = "accounts/login.html"
    extra_context = {"page_title": "Login"}
    success_message = "Welcome to the Website."

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(request.META.get("HTTP_REFERER") or "core:home_view")
        return super().get(request, *args, **kwargs)


class RegisterView(SuccessMessageMixin, View):
    template_name = "accounts/register.html"
    form_class = CustomUserCreationForm
    extra_context = {"page_title": "User Registration"}
    success_message = "Successfully registered, You can go ahead and login now."
    success_url = reverse_lazy("accounts:login_view")

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect(request.META.get("HTTP_REFERER") or "core:home_view")
        context = {"form": self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect(self.success_url)

        context = {"form": form}
        return render(request, self.template_name, context)


class CustomLogoutView(SuccessMessageMixin, LogoutView):
    success_message = "We hope to see you back soon."

    def post(self, request, *args, **kwargs):
        # is user is not authenticated
        logout(request)
        return redirect(self.next_page)
