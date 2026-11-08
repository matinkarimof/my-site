from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from .models import User


class RegisterForm(forms.ModelForm):
    password1 = forms.CharField(label="رمز عبور", widget=forms.PasswordInput)
    password2 = forms.CharField(label="تکرار رمز عبور", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("first_name", "phone", "avatar")
        labels = {"first_name": "نام", "avatar": "تصویر پروفایل"}

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        if User.objects.filter(phone=phone).exists():
            raise forms.ValidationError("این شماره قبلاً ثبت شده است.")
        return phone

    def clean(self):
        cleaned = super().clean()
        p1 = cleaned.get("password1")
        p2 = cleaned.get("password2")
        if p1 and len(p1) < 6:
            self.add_error("password1", "رمز عبور باید حداقل ۶ کاراکتر باشد.")
        if p1 and p2 and p1 != p2:
            self.add_error("password2", "رمز عبور و تکرار آن یکسان نیستند.")
        return cleaned

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "avatar")
        labels = {"first_name": "نام", "last_name": "نام خانوادگی", "avatar": "تصویر پروفایل"}


class AdminChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(
        label="رمز عبور",
        help_text="رمز عبور به‌صورت رمزنگاری‌شده ذخیره می‌شود و مستقیم قابل مشاهده نیست.",
    )

    class Meta:
        model = User
        fields = "__all__"

    def clean_password(self):
        return self.initial["password"]
