from django import forms


class LoginForm(forms.Form):
    u_name = forms.CharField(max_length=8)
    u_password = forms.CharField(max_length=16)

    def clean_u_name(self):
        name = self.cleaned_data.get('u_name')
        if type(name) is not str:
            raise forms.ValidationError('用户名类型错误')
        return name

    def clean_u_password(self):
        password = self.cleaned_data.get('u_password')
        if len(password) > 16:
            raise forms.ValidationError('密码格式错误')
        return password
