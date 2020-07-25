from django import forms

class upload_photo(forms.Form):
    photo = forms.ImageField(label="photo")