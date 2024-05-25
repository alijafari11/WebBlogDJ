from django import forms
from .models import *


class AccountForm(forms.Form):
    SEX_CHOICES = (
        ('مرد', 'مرد'),
        ('زن', 'زن'),
    )
    phone = forms.CharField(max_length=11, required=True, label='شماره')
    f_name = forms.CharField(max_length=25, required=True, label='نام')
    l_name = forms.CharField(max_length=25, required=True, label='نام خانوادگی')
    sex = forms.ChoiceField(choices=SEX_CHOICES, widget=forms.RadioSelect, label='جنسیت')
    address = forms.CharField(max_length=255, widget=forms.Textarea, label='آدرس')
    age = forms.IntegerField(label='سن', required=True)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        if phone:
            if not phone.isnumeric():
                raise forms.ValidationError('شماره همراه باید عددی باشد')
            else:
                return phone

    def clean_age(self):
        age = self.cleaned_data['age']
        if age:
            if age < 0:
                raise forms.ValidationError('سن نباید منفی باشد ')
            else:
                return age


class ContactUsForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, required=True, label='پیام')
    name = forms.CharField(max_length=245,required=True, label='نام و نام خانوادگی')
    email = forms.EmailField(required=True, label='ایمیل')
    subject = forms.CharField(required=True, label='موضوع')
    phone = forms.CharField(max_length=11, required=False, label='شماره همراه')


class ShareForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'class': 'sp-text'}), required=True, label='پیام')
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'sp-name'}), max_length=245,required=True, label='نام و نام خانوادگی')
    to = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'sp-email'}),required=True, label='گیرنده')


# class MyForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['slug']
#         fields = '__all__'
#         widgets = {
#             'slug': forms.TextInput(attrs={'class': 'sp-name'})
#         }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'cm-name'}),
            'body': forms.Textarea(attrs={'class': 'cm-body'})
        }
