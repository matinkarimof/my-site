from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    # فیلد تله برای ربات‌ها؛ کاربر آن را نمی‌بیند
    website = forms.CharField(required=False, label="")

    class Meta:
        model = ContactMessage
        fields = ("name", "email", "message")
        labels = {"name": "نام", "email": "ایمیل", "message": "پیام"}
        widgets = {"message": forms.Textarea(attrs={"rows": 5})}

    def clean_message(self):
        message = self.cleaned_data["message"].strip()
        if len(message) < 5:
            raise forms.ValidationError("پیام باید حداقل ۵ کاراکتر باشد.")
        return message
