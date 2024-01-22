
from django.contrib import admin

from finalapp.models import Country, field, City, Person, login

# Register your models here.
admin.site.register(field)
admin.site.register(login)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Person)
