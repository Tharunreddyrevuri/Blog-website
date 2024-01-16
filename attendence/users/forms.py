from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()    # if required= False then field isnot not mandatory , but by default it's 
    

    class Meta:
        model = User
        fields = ['username', 'email','password1','password2']

    """ this class meta gives us the nested name space for the configuration and keeps the configurations in one place/
     and with in the configuration we are saying , model that effected is User.
     i.e  when form.save() is performed it save  to User model.
     

     and the fields that have is , fields we want in form and what order.
    """

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email'] 

   
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']