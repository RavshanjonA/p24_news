from django.core.exceptions import ValidationError
from django.forms import Form, ModelForm, CharField, PasswordInput

from apps.account.models import Account


class SubscribeForm(ModelForm):
    password = CharField(widget=PasswordInput)
    confirm_password = CharField(widget=PasswordInput)

    def clean(self):
        if self.cleaned_data["password"] != self.cleaned_data["confirm_password"]:
            raise ValidationError("Passwords must be match")
        return super().clean()

    def save(self, commit=True):
        user: Account = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        user.is_subscribe = True
        user.save()
        return user

    class Meta:
        model = Account
        fields = ("first_name", "last_name", "username", "email", "password", "confirm_password",)
