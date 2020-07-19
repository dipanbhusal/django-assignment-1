from django.contrib import admin
from .models import Author, Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','created_at')  
admin.site.register(Post, PostAdmin)
admin.site.register(Author, AuthorAdmin)  

