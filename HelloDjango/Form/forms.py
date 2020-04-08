from django import forms

from Form.models import User


class LoginForm(forms.Form):
    username = forms.CharField(label='User Name:', max_length=16)
    password = forms.CharField(label='Password:', widget=forms.PasswordInput)

    def clean_password(self):   # 服务端检验表单
        password = self.cleaned_data.get('password')
        if password != '123':
            raise forms.ValidationError('password wrong')
        return password


class UploadForm(forms.Form):
    file = forms.FileField(label='File:')
    # 由于文件不能单独上传，设置一个隐藏字段帮助正确识别文件字段
    assist = forms.Field(label='', widget=forms.HiddenInput, required=False)

    def clean_file(self):
        file = self.cleaned_data.get('file')
        ext = file.name.split('.')[-1].lower()
        if ext not in 'txt':
            raise forms.ValidationError('file must not none')
        return file


class RegisterForm(forms.Form):
    model = User    # 不能是User(),这样会调用实例化一个模型对象,没法查询
    u_id = forms.CharField(label='用户ID：', max_length=12)
    u_name = forms.CharField(label='用户名：')
    u_password = forms.CharField(label='密码：', widget=forms.PasswordInput)
    u_password2 = forms.CharField(label='确认密码：', widget=forms.PasswordInput)
    u_icon = forms.ImageField(label='头像：', required=False)

    def clean_u_id(self):
        id = self.cleaned_data.get('u_id')
        if self.model.objects.filter(u_id=id):  # 能够查询到这条记录,抛出异常
            raise forms.ValidationError('此ID已经存在')
        return id

    def clean_u_password2(self):
        password = self.cleaned_data.get('u_password')
        password2 = self.cleaned_data.get('u_password2')
        if password != password2:
            raise forms.ValidationError('两次密码不一致')
        return password2
