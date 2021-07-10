from django.contrib import admin
from .models import User,Books,Genre,Author

class BookAdmin(admin.ModelAdmin):
    # fields = ['name','price']
    fieldsets = [
        ('Basic Info', {'fields':['name','price','pic']}),
        ('publication_info',{'fields':['pub_date','author','genre']})
    ]
    list_display = ['name','is_available','price']
    search_fields = ['name']
    list_filter = ['pub_date','author']

class BookInline(admin.TabularInline):
# class BookInline(admin.StackedInline):
    model = Books
    extra = 2

class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

# Register your models here.
admin.site.register(Books,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
admin.site.register(User)