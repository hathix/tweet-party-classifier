from django import forms

class TextForm(forms.Form):
	raw_text = forms.CharField(label="Tweet text", max_length=140)