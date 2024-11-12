from django.shortcuts import render
from django.http import HttpResponse
from django.http import *
from django.http import HttpResponse, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.template.response import TemplateResponse
from .forms import UserForm
from .models import Person
from django.db.models import F
from .models import Image
from .forms import ImageForm
from django.shortcuts import redirect
from .models import File 
from .forms import FileForm 
from .models import VideoFile 
from .forms import VideoForm
from .models import AudioFile 
from .forms import AudioForm  


# person = Person.objects.get(id=2)
# person.delete()
# Person.objects.filter(id=4).delete()
def form_up_img(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    my_text = 'Загруженные изображения'
    my_img = Image.obj_img.all()
    form = ImageForm()
    context = {'my_text': my_text, "my_img": my_img, "form": form}
    return render(request, 'firstapp/form_up_img.html', context)
    
def delete_img(request, id):
    try:
        img = Image.obj_img.get(id=id)
        img.delete()
        return redirect('form_up_img')
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Объект не найден</h2>")
    
# загрузка файлов pdf 
def form_up_pdf(request): 
    if request.method == 'POST': 
        form = FileForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
        
    my_text = 'Загруженные файлы' 
    form = FileForm() 
    file_obj = File.objects.all() 
    context = {'my_text': my_text, "file_obj": file_obj, "form": form} 
    return render(request, 'firstapp/form_up_pdf.html', context)
    
# удаление файлов из БД 
def delete_pdf(request, id): 
    try: 
        pdf = File.objects.get(id=id) 
        pdf.delete() 
        return redirect('form_up_pdf') 
    except Person.DoesNotExist: 
        return HttpResponseNotFound("<h2>Объект не найден</h2>") 

# загрузка видео файлов 
def form_up_video(request): 
    if request.method == 'POST': 
        form = VideoForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save()
    my_text = 'Загруженные видео файлы' 
    form = VideoForm() 
    file_obj = VideoFile.obj_video.all() 
    context = {'my_text': my_text, "file_obj": file_obj, "form": form} 
    return render(request, 'firstapp/form_up_video.html', context)

# загрузка аудио файлов 
def form_up_audio(request): 
    if request.method == 'POST': 
        form = AudioForm(request.POST, request.FILES) 
        if form.is_valid(): 
            form.save() 
    my_text = 'Загруженные аудио файлы' 
    form = AudioForm() 
    file_obj = AudioFile.obj_audio.all() 
    context = {'my_text': my_text, "file_obj": file_obj, "form": form} 
    return render(request, 'firstapp/form_up_audio.html', context)  

# удаление аудио файлов из БД 
def delete_audio(request, id): 
    try: 
        audio = AudioFile.obj_audio.get(id=id) 
        audio.delete() 
        return redirect('form_up_audio') 
    except Person.DoesNotExist: 
        return HttpResponseNotFound("<h2>Объект не найден</h2>")      

# удаление видео файлов из БД 
def delete_video(request, id): 
    try: 
        video = VideoFile.obj_video.get(id=id) 
        video.delete() 
        return redirect('form_up_video') 
    except Person.DoesNotExist: 
        return HttpResponseNotFound("<h2>Объект не найден</h2>") 

def edit_form(request, id):
        # Логика для редактирования формы
        return render(request, 'your_template.html', {'id': id})


def products(request, productid):
    category = request.GET.get("cat", "")
    output = "<h2>Продукт № {0} Категория: {1}</h2>" .format(productid, category)
    return HttpResponse(output)

def users(request):
    id = request.GET.get("id", 1)
    name = request.GET.get("name", "Максим")
    output = "<h2>Пользователь</h2><h3>id: {0} Имя: {1}</h3 >" .format(id, name)
    return HttpResponse(output)

def index(request):
    my_text = 'Изучаем формы Django'
    context = {'my_text': my_text}
    return render(request, "firstapp/index.html", context)

def about(request):
 return render(request, "firstapp/about.html")

def my_form(request):
    if request.method == "POST":
        userform = UserForm(request.POST)
        if userform.is_valid():
            name = request.POST.get("name") # получить значение поля Имя
            age = request.POST.get("age") # получить значение поля Возраст
            output = "<h2>Пользователь</h2><h3>Имя - {0}," \
             " Возраст – {1} </h3 >".format(name, age)
            return HttpResponse(output)
    userform = UserForm()
    return render(request, "firstapp/my_form.html", {"form": userform})



def contact(request):
    my_kv = ['I квартал ->', 'II квартал ->', 'III квартал->',
    'IV квартал->']
    my_month = ['Январь', 'Февраль', 'Март',
    'Апрель', 'Май', 'Июнь',
    'Июль', 'Август', 'Сентябрь',
    'Октябрь', 'Ноябрь', 'Декабрь']
    context = {'my_month': my_month, 'my_kv': my_kv}
    return render(request, "firstapp/contact.html", context)

def details(request):
    return HttpResponsePermanentRedirect("/")

def create(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.age = request.POST.get("age")
        klient.save()
    return HttpResponseRedirect("/")

def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")

def delete(request, id):
    try:
        person = Person.objects.get(id=id)
        person.delete()
        return HttpResponseRedirect("/")
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")