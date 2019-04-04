from django import forms
from .models import Review

class ReviewForm(forms.ModelForm):

	class Meta:
		model = Review
		fields = ['sku','rating','title', 'author', 'text','source']