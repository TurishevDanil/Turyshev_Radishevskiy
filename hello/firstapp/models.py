from django.db import models
from django.db.models import F
# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    objects = models.Manager()
    DoesNotExist = models.Manager

class Company(models.Model):
        name = models.CharField(max_length=30)

class Product(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    price = models.IntegerField()

class Course(models.Model):
    name = models.CharField(max_length=30)

class Student(models.Model):
    name = models.CharField(max_length=30)
    courses = models.ManyToManyField(Course)

class User(models.Model):
    name = models.CharField(max_length=20)

class Account(models.Model):
    login = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

class Image(models.Model):
    title = models.CharField(max_length=100, null=False,
                    verbose_name="Описание изображения",)
    image = models.ImageField(upload_to='images',
                    verbose_name="Файл с изображением",
                    null=True, blank=True)
    obj_img = models.Manager()
    def __str__(self):
        return self.title    

# igor = Person (nаmе="Игорь", age=23)
# igor.save()

# klientl = Person.objects.get(narne="Bиктop") 
# klient2 = Person.objects.get(age=25)
# klientЗ = Person.objects.get(name="Bacилий", age=23)

# bob, created = Person.objects.get_or_create(name="Bob", age=24)
# print(bob.name)
# print(bob.age)

# people = Person.objects.exclude(age=23)

# people = Person.objects.filter(age=23)
# people2 = Person.objects.filter(name="Tom", age=23)

# people = Person.objects.exclude(age=23)
# people = Person.objects.filter(name="Tom").exclude(age=23)

# people = Person.objects.in_bulk()
# for id in people:
#     print(people[id].name)
#     print(people[id].age)

# people2 = Person.objects.in_bulk([1,3])
# for id in people2:
#     print(people2[id].name)
#     print(people2[id].age)

# nic = Person.objects.get(id=2)
# nic.name = "Николай Петров"
# nic.save()

# nic = Person.objects.get(id=2)
# nic.name = "Николай Петров"
# nic.save(update_fields=["name"])
# Person.objects.filter(id=2).update(name="Михаил")

# Person.objects.all(id=2).update(age = F("age") + 1)

# Person.objects.all().update(name="Михайил")
# Person.objects.all().update(age = F("age") + 1)

# values_for_update = {"name":"Михаил", "age": 31}
# bob, created = Person.objects.update_or_create(id=2,
#                                             defaults = values_for_update)

people = Person.objects.filter(name="Tom").exclude(age=34)
print(people.query)