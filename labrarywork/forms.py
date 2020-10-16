from django import  forms
from .models import *


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        exclude = ('book_id',)


class BookCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'