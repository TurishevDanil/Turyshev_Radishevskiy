from django import forms

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента")
#  age = forms.IntegerField(label="Возраст клиента")


# class UserForm(forms.Form):
#    basket = forms.BooleanField(label="Положить товар в корзину", required=False)

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента")

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента", max_length=15,
#  help_text="ФИО не более 15 символов")

# class UserForm(forms.Form):
#  ling = forms.ChoiceField(label="Выберите язык",
#  choices=(
#  (1, "Английский"),
#  (2, "Немецкий"),
#  (3, "Французский")))

# class UserForm(forms.Form):
#  date = forms.DateField(label="Введите дату")

# class UserForm(forms.Form):
#  date_time = forms.DateTimeField(label="Введите дату и время")

# class UserForm(forms.Form):
#  num = forms.DecimalField(label="Введите десятичное число")

# class UserForm(forms.Form):
#  num = forms.DecimalField(label="Введите десятичное число",
#  decimal_places=2)

# class UserForm(forms.Form):
#  time_delta = forms.DurationField(label="Введите промежуток времени")

class UserForm(forms.Form):
 email = forms.EmailField(label="Электронный адрес",
 help_text="Обязательный символ - @")
