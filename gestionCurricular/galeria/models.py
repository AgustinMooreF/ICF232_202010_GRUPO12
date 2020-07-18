from django.db import models

# Create your models here
class Product(models.Model):
    sku = models.SlugField(max_length=30, unique=True)
    name = models.CharField(max_length=255, unique=True)
    def __str__(self):
        return self.name
    

# class productFactory:
#     def __init__(self):
#         self.cursos=[]
#         self.cursos.append(Curso("ICF232", "Ingenieria de Software I",6))
#         self.cursos.append(Curso("ICF121", "Introduccion a Ing. Civil Informatica ",6))
    
#     def obtenerCursos(self):
#         return self.cursos

#     def getCurso(self,sigla):
#         for curso in self.cursos:
#             if curso.sigla==sigla:
#                 return curso
#         return None