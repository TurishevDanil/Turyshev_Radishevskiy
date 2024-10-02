from django.db import models
from django.urls import reverse

# Типичный класс, определяющий модель, производный от класса Model
class MyModelName(models.Model):

    # Поле (или множество полей)
    my_field_name = models.CharField(max_length=20, help_text="Не более 20 символов")

    # Метаданные
    class Meta:
        ordering = ["-my_field_name"]

    # Методы
def get_absolute_url(self):
        # Возвращает url-адрес для доступа к экземпляру MyModelName
    return reverse('model-detail-view', args=[str(self.id)])

def __str__(self):
        # Строка для представления объекта MyModelName в Admin site
    return self.field_name

