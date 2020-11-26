from django.contrib import admin
from .models import Like
from .models import Recommend
from .models import Editor
from .models import Seoul, Incheon, Busan, Gwanggu, Daejon, Gangwon

admin.site.register(Like)
admin.site.register(Recommend)
admin.site.register(Editor)
admin.site.register(Seoul)
admin.site.register(Incheon)
admin.site.register(Busan)
admin.site.register(Gwanggu)
admin.site.register(Daejon)
admin.site.register(Gangwon)

# Register your models here.
