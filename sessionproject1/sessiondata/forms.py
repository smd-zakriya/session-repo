from django import forms

class AddItem(forms.Form):
    item=forms.CharField()
    quantity=forms.IntegerField()
    