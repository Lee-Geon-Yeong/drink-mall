from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import forms

SEX_CHOICES = (
    (0, 'female'),
    (1, 'male')
)

class UserChangeForm_2(UserChangeForm):
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    age = forms.IntegerField(max_value=130)


class UserCreationForm_2(UserCreationForm):
    sex = forms.ChoiceField(choices=SEX_CHOICES)
    age = forms.IntegerField(max_value=130, required=True)