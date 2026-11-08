from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import ProfileForm, RegisterForm


def auth_page(request):
    if request.user.is_authenticated:
        return redirect("accounts:profile")
    return render(request, "accounts/auth.html", {
        "login_form": AuthenticationForm(request),
        "register_form": RegisterForm(),
    })


def login_view(request):
    if request.method != "POST":
        return redirect("accounts:login")
    form = AuthenticationForm(request, data=request.POST)
    if form.is_valid():
        login(request, form.get_user())
        return redirect("accounts:profile")
    return render(request, "accounts/auth.html", {
        "login_form": form,
        "register_form": RegisterForm(),
    })


def register_view(request):
    if request.method != "POST":
        return redirect("accounts:login")
    form = RegisterForm(request.POST, request.FILES)
    if form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "حساب شما با موفقیت ساخته شد.")
        return redirect("accounts:profile")
    return render(request, "accounts/auth.html", {
        "login_form": AuthenticationForm(request),
        "register_form": form,
        "show_register": True,
    })


@login_required
def profile_view(request):
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "پروفایل شما ذخیره شد.")
            return redirect("accounts:profile")
    else:
        form = ProfileForm(instance=request.user)
    return render(request, "accounts/profile.html", {"form": form})
