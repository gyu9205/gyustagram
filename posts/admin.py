from django.contrib import admin

# Register your models here.

from .models import Post #admin 관리에 추가적으로 app을 추가하는 법

admin.site.register(Post)
