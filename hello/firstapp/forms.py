from django import forms

# class UserForm(forms.Form):
#  file = forms.FileField(label="Файл")

# class UserForm(forms.Form):
#  file_path = forms.FilePathField(label="Выберите файл",
#  path="C:/my_doc/")

# class UserForm(forms.Form):
#  file_path = forms.FilePathField(label="Выберите файл",
#  path="C:/my_doc/",
#  allow_files="True",
#  allow_folders="True")

# class UserForm(forms.Form):
#  num = forms.FloatField(label="Введите число")

# class UserForm(forms.Form):
#  ip_adres = forms.GenericIPAddressField(label="IP адрес",
#  help_text=" Пример формата 192.0.2.0")

# class UserForm(forms.Form):
#  file = forms.ImageField(label="Изображение")

# class UserForm(forms.Form):
#  num = forms.IntegerField(label="Введите целое число")

# class UserForm(forms.Form):
#  num = forms.JSONField(label="Данные формата JSON")

# class UserForm(forms.Form):
#  country = forms.MultipleChoiceField(label="Выберите страны",
#  choices=((1, "Англия"),
#           (2, "Германия"),
#           (3, "Испания"),
#           (4, "Россия")))
 
# class UserForm(forms.Form):
#  vyb = forms.NullBooleanField(label="Вы поедете в Сочи этим летом?")

# class UserForm(forms.Form):
#  reg_text = forms.RegexField(label="Текст", regex="^[0-9][A-F][0-9]$")

# class UserForm(forms.Form):
#  slug_text = forms.SlugField(label="Введите текст")

# class UserForm(forms.Form):
#  time = forms.DateField(label="Введите время")

# class UserForm(forms.Form):
#  city = forms.TypedMultipleChoiceField(label="Выберите город",
#  empty_value=None,
#  choices=((1, "Москва"),
#           (2, "Воронеж"),
#           (3, "Курск"),
#           (4, "Томск")))

# class UserForm(forms.Form):
#  url_text = forms.URLField(label="Введите URL",
#  help_text="Например http://www.yandex.ru")

class UserForm(forms.Form):
 uuid_text = forms.UUIDField(label="Введите UUID",
 help_text="Формат xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx")