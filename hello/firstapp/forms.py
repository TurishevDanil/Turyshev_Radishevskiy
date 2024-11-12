from django import forms
from .models import Image 
from .models import File
from .models import VideoFile
from .models import AudioFile

class FileForm(forms.ModelForm): 
    class Meta: 
        model = File 
        fields = '__all__' 

class VideoForm(forms.ModelForm): 
    class Meta: 
        model = VideoFile 
        fields = '__all__' 

class AudioForm(forms.ModelForm): 
    class Meta: 
        model = AudioFile 
        fields = '__all__' 

# class UserForm(forms.Form):
#  combo_text = forms.ComboField(label='Введите данные',
#  fields=[
#  forms.CharField(max_length=20),
#  forms.EmailField()])

# class UserForm(forms.Form):
#  combo_text = forms.MultiValueField(label='Комплексное поле',
#  fields=(
#  forms.CharField(max_length=20),
#  forms.EmailField()))

# class UserForm(forms.Form):
#  date_time = forms.SplitDateTimeField(label="Введите дату и время")

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя")
#  age = forms.IntegerField(label="Возраст")
#  comment = forms.CharField(label="Комментарий")

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя")
#  age = forms.IntegerField(label="Возраст")
#  comment = forms.CharField(label="Комментарий",
#  widget=forms.Textarea)

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя", initial="Введите ФИО")
#  age = forms.IntegerField(label="Возраст", initial=18)
#  comment = forms.CharField(label="Комментарий",
#  widget=forms.Textarea) 

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя", initial="Введите ФИО")
#  age = forms.IntegerField(label="Возраст", initial=18)
#  field_order = ["age", "name"]
 
# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя", initial="Введите ФИО")
#  age = forms.IntegerField(label="Возраст", initial=18) 

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя", help_text="Введите ФИО")
#  age = forms.IntegerField(label="Возраст", help_text="Введите возраст")

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя")
#  age = forms.IntegerField(label="Возраст")
#  email = forms.EmailField(label="Электронный адрес")
#  reklama = forms.BooleanField(label="Согласны получать рекламу")

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя")
 
# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента")
#  age = forms.IntegerField(label="Возраст клиента")

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента")
#  age = forms.IntegerField(label="Возраст клиента") 

# class UserForm(forms.Form):
#  name = forms.CharField(label="Имя клиента", min_length=3,
#  help_text='Не менее 3-х символов')
#  age = forms.IntegerField(label="Возраст клиента",
#  min_value=1, max_value=120,
#  help_text='От 1 до 120 лет')
#  required_css_class = "field"
#  error_css_class = "error"
 
class UserForm(forms.Form):
 name = forms.CharField(label="Имя клиента",
 widget=forms.TextInput(attrs={"class": "myfield"}))
 age = forms.IntegerField(label="Возраст клиента",
 widget=forms.NumberInput(attrs={"class": "myfield"}))

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = '__all__'
        # fields = ['title', 'image']