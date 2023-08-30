from django import forms
import re

class UserformComment(forms.Form):
    name=forms.CharField(max_length=10)
    email=forms.EmailField(required=False)
    com=forms.CharField(widget=forms.Textarea)

class UserformErrors(forms.Form):
    name = forms.CharField(error_messages={'required':'надо заполнить'})
    num = forms.IntegerField(error_messages={'invalid':'целое число'})
    agree = forms.BooleanField(error_messages={'required':'поставь галочку'})


from django.core.validators import ValidationError, RegexValidator
def p1(value):
    if value[0]!='A':
        raise forms.ValidationError('начинается на заглавную А')
    pass

def p2(value):
    if value[-1]!='Z':
        raise forms.ValidationError('заканчивается на заглавную Z')
    pass

class UserformValidator(forms.Form):
    name=forms.CharField()
    code=forms.CharField(validators=[p1,p2])
    tel=forms.CharField(validators=[RegexValidator('[+7][0-9]{9}',message='no tel')])





def p5(value):
    if not value.isalpha():
        raise forms.ValidationError('Может содержать только буквы.')
def p3(value):
    if not value[0].isupper():
        raise forms.ValidationError('Введите строку, начинающуюся с заглавной буквы.')
def p4(value):
    if not re.match(r'[a-zA-Z0-9]', value):
        raise forms.ValidationError('Должно содержать буквы и цифры.')
def p6(value):
    if any(char in '.,!?;:"\'()[]{}<>+=-_~`@#$%^&*|\\/ ' for char in value):
        raise forms.ValidationError('Не используйте знаки препинания.')

from django.core.validators import ValidationError, RegexValidator

class UserformWater(forms.Form):
    name=forms.CharField(label='Введите имя', validators=[p3, p5, p6])
    sname=forms.CharField(label='Введите фамилию', validators=[p3, p5, p6])
    email=forms.EmailField(label='Введите почту')
    tel = forms.CharField(validators=[RegexValidator('[+7][0-9]{9}',message='Не верный формат телефона')],label='Введите телефон')
    adres=forms.CharField(label='Введите адрес', validators=[p4])
    vibor = (('Один месяц', 'Один месяц'), ('Три месяца', 'Три месяца'), ('Шесть месяцев', 'Шесть месяцев'), ('Двенадцать месяцев', 'Двенадцать месяцев'))
    dost=forms.TypedChoiceField(label='Выберите частоту доставки', choices=vibor)
    vibor1 = (('Пять литров', 'Пять литров'), ('Десять литров', 'Десять литров'), ('Пятнадцать литров', 'Пятнадцать литров'))
    litr=forms.TypedChoiceField(label='Выберите количество литров', choices=vibor1)
