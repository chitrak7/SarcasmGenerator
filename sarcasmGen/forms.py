from django import forms

class SearchQuery(forms.Form):
    query = forms.CharField(label='query', max_length=100)