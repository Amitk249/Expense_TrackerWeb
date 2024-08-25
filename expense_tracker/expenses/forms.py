from django import forms
from .models import Category, Expenses

class Expensesform(forms.ModelForm):
    class Meta:
        model = Expenses
        fields = ['amount','category', 'description', 'date']

class Categoryform(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']