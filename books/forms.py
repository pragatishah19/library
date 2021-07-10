from django import forms
from django.forms import fields
from .models import Author, Books, Genre, User

class BookForm(forms.ModelForm):
    #name=forms.CharField(max_length=50)
    class Meta:
        model = Books
        fields = ['name','author','is_available','price','pub_date','genre','pic']
        # fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].widget.attrs.update({'class': 'form-control','placeholder':'Enter book name'})
    #     self.fields['author'].widget.attrs.update({'class': 'form-control','placeholder':'select author'})
    #     self.fields['is_available'].widget.attrs.update({'class': 'form-control',})
    #     self.fields['price'].widget.attrs.update({'class': 'form-control',})
    #     self.fields['pub_date'].widget.attrs.update({'class': 'form-control',})
    #     self.fields['genre'].widget.attrs.update({'class': 'form-control','placeholder':'selcet genre'})
    #     self.fields['pic'].widget.attrs.update({'class': 'form-control',})


class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = '__all__'

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'