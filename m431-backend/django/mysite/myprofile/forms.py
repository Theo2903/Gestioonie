# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from myprofile.models import UserProfile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class UserProfileEditForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [] #['exemple',]
