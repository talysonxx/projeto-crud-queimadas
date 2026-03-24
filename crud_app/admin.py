# arquivo apenas para poder visualizar os modelos (tabelas do banco) no painel administrativo nativo do django.

from django.contrib import admin
from . import models

admin.site.register(models.Usuario)
admin.site.register(models.Incendio)
