from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    user_id = forms.CharField(label="学号", max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="密码", max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class RegisterForm(forms.Form):
    user_name = forms.CharField(label="姓名", max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    user_id = forms.CharField(label="学号", min_length=8, max_length=8, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱",max_length=254,widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="密码", min_length=6, max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="确认密码", min_length=6, max_length=64, widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class SearchForm(forms.Form):
    keyword = forms.CharField(label="关键词", max_length=60,
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': '请输入关键词'}))

# firget.html中，用于验证邮箱格式和验证码
class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={'invalid':'验证码错误'})


# reset.html中，用于验证新设的密码长度是否达标
class ResetForm(forms.Form):
    newpwd1 = forms.CharField(required=True,min_length=6,error_messages={'required':'密码不能为空','min_length':'至少为6位'})
    newpwd2 = forms.CharField(required=True,min_length=6,error_messages={'required':'密码不能为空','min_length':'至少为6位'})