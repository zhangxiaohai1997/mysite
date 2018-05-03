from django import forms

class ContactForm(forms.Form):  #建立表单
    subject=forms.CharField(min_length=10)    #括号可设置相关参数
    email=forms.EmailField(required=False,label="your email address")  #将email设为选填,其他默认必填
    message=forms.CharField(widget=forms.Textarea)  #widget设置表单表现逻辑

    def clean_message(self):   #Django 的表单系统会自动查找名称以 clean_ 开头、以字段名结尾的方法。
        message=self.cleaned_data['message']
        num_words=len(message.split())   #存储message的单词数
        if num_words<4:
            raise forms.ValidationError('Not enough words!')
        return message
