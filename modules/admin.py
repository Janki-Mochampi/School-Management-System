from django.contrib import admin
from .models import module, comment, Tag

# Register your models here.
admin.site.register(module)
admin.site.register(comment)
admin.site.register(Tag)

