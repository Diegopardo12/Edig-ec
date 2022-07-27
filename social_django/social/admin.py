from atexit import register
import re
from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Relationship)
admin.site.register(Estudiante)
admin.site.register(Instructor)
admin.site.register(Cursos)