from django import forms
from django.forms import fields
from .models import Author, Books, Genre, User

class BookForm(forms.ModelForm):
    #name=forms.CharField(max_length=50)
    class Meta:
        model = Books
  #      fields = ['name','price']
        fields = '__all__'

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