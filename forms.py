from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from food.models import Resto , item

class RegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class RestoForm(forms.ModelForm):
    class Meta:
        model = Resto
        fields = ['resto_name', 'resto_location', 'resto_image']

class ItemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ['item_name', 'item_desc', 'item_price', 'item_image']

