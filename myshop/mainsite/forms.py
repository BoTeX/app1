from django import forms

from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('title', 'text','photo' ,'price' ,'category', 'name', 'number', 'email',)