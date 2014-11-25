#coding:utf-8
from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

SEXO_PESSOA = [
     ('M','MASCULINO'),
     ('F','FEMININO')
]

class Pessoa (models.Model):
	Nome = models.CharField('Nome',max_length=100,null=True)
	CPF = models.CharField('CPF',max_length=11,null=True)
	Endereco = models.CharField('Endereco',max_length=100,null=True)
	Telefone = models.CharField('Telefone',max_length=10,null=True)
	sexo = models.CharField('Sexo',max_length=1,choices=SEXO_PESSOA,null=True)
	Descricao = models.ForeignKey(Acesso,verbose_name="Tipo de Acesso",null=True)

	
	def __unicode__(self):
		return "%s - %s" % (self.Nome,self.Descricao.Descricao)


class Acesso (models.Model):
	Descricao = models.CharField('Tipo de Acesso',max_length=100,null=True)
	
	def __unicode__(self):
		return self.Descricao


class Local (models.Model):
	Nome = models.CharField('Local',max_length=100,null=True)
	Descricao = models.ManyToManyField(Acesso,verbose_name="Tipo de Acesso",null=True)
	
	def __unicode__(self):
		return self.Nome
		
class validar (models.Model):
	Nome = models.ForeignKey(Pessoa,verbose_name="Pessoa",null=True)
	Descricao = models.ForeignKey(Lugar,verbose_name="Local",null=True)
	Entrada = models.TimeField(auto_now=False,null=True)
	Saida = models.TimeField(auto_now=False,null=True)
	
	def clean(self):
		q = validacao.objects.filter(Nome=self.Descricao,Descricao=self.Descricao)
		
		if not q:
			raise ValidationError("Pessoa não tem acesso a esta area")
			
	def clean(self):
		q = validar.objects.filter(Entrada=self.Saida)
		
		if not q:
			raise ValidationError("Horario Estourado")
		
	class Meta:
		unique_together = ("Nome","Descricao")