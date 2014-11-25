#coding:utf-8
from django.contrib import admin
from models import Pessoa
from models import Acesso
from models import Local
from models import validar
# Register your models here.

class PessoaAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True

	
class AcessoAdmin(admin.ModelAdmin):
	list_display = ['Descricao']
	list_filter = ['Descricao']
	search_fields = ['Descricao']
	save_as = True
	
	
class LocalAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
class validarAdmin(admin.ModelAdmin):
	list_display = ['Nome']
	list_filter = ['Nome']
	search_fields = ['Nome']
	save_as = True
	
admin.site.register(Pessoa,PessoaAdmin)
admin.site.register(Acesso,AcessoAdmin)
admin.site.register(Local,LocalAdmin)
admin.site.register(validar,validarAdmin)

