from django.contrib import admin
from .models import *

admin.site.register(Nauczyciel)
admin.site.register(Kurs)
admin.site.register(Uczen)
admin.site.register(Dzien)
admin.site.register(Rodzaj)
admin.site.register(Nauczyciel_Rodzaj)