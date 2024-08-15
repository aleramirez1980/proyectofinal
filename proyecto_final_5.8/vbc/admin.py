from django.contrib import admin

from vbc.models import Electrica, Acustica, Amplificador, Efecto
# Register your models here. dd

admin.site.register(Electrica)
admin.site.register(Acustica)
admin.site.register(Amplificador)
admin.site.register(Efecto)

