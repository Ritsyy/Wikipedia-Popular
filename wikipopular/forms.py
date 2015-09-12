from django import forms

from .models import wikiTitle

class WikiTitleForm(forms.ModelForm):
		class Meta:
			model = wikiTitle
			fields = '__all__'