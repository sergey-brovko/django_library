from django import forms

from mylib.models import Book


class BookModelForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
