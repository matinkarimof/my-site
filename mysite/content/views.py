from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse

from .forms import ContactForm
from .models import Article
from .resume import RESUME


def home(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            if not form.cleaned_data.get("website"):
                form.save()
                messages.success(request, "پیام شما ارسال شد. به زودی پاسخ می‌دهم.")
            return redirect(reverse("home") + "#contact")
    else:
        form = ContactForm()

    articles = Article.objects.filter(published=True)
    return render(request, "home.html", {
        "resume": RESUME,
        "articles": articles,
        "contact_form": form,
    })


def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk, published=True)
    return render(request, "article_detail.html", {"article": article})
