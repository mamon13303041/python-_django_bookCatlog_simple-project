from django import forms
from .models import List_book
#DataFlair
class BookCreate(forms.ModelForm):
    class Meta:
        model = List_book
        fields = '__all__'