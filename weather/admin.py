from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(DomesticCurrent)
admin.site.register(GlobalCurrent)
admin.site.register(GlobalPredict)

