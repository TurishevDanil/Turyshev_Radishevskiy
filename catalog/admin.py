from django.contrib import admin
from.models import Author, Book, Genre, Language, Status, BookInstance

# Register your models here.
admin.site.register(Author) 
# admin.site.register(Book) 
admin.site.register(Genre) 
admin.site.register(Language) 
admin.site.register(Status) 


class BooksInstanceInline(admin.TabularInline):
 model = BookInstance
 

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
 list_display = ('title', 'genre', 'language', 'display_author')
 list_filter = ('genre', 'author')
 inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': ('book', 'imprint', 'inv_nom')
        }),
        ('Availability', {
            'fields': ('status', 'due_back', 'borrower')
        }),       
        )
    def borowwer(self):
        BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='2').order_by('due_back')





