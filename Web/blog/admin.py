from django.contrib import admin
from .models import Blike, Beditor, LikeComment

admin.site.register(Blike)
admin.site.register(Beditor)
admin.site.register(LikeComment)

# Register your models here.