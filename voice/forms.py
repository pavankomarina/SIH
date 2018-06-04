from django import forms
from django.contrib.auth.models import User

from .models import *

class UserdetailsForm(forms.ModelForm):

    class Meta:
        model = Userdetails
        fields = ['audio_file']
