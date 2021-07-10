from django import forms
from django.forms import fields
from django.contrib.auth.forms import UserCreationForm
from django.forms.formsets import MAX_NUM_FORM_COUNT
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    # mob = forms.IntegerField()
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )
        # labels = {'mob': 'Mobile Number',} # newly added
        # widgets = {
        #     'username':forms.TextInput(attrs={'class':'form-control','id':'usernameid'}),
        #     'password1':forms.PasswordInput(attrs={'type':"password" ,'class':"form-control",'id':'password1id'}),
        #     'password2':forms.PasswordInput(attrs={'class':'form-control','id':'password2id'}),
            # 'mob':forms.NumberInput(attrs={'class':'form-control','id':'mobid'}),
        # }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control','placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'class': 'form-control','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class': 'form-control','placeholder':'Password Confirmation'})