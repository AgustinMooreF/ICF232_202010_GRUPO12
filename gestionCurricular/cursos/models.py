from django.db import models 

class Curso:
    def __init__(self, sigla, nombre, creditos):
        self.sigla=sigla
        self.nombre=nombre
        self.creditos=creditos

class CursoFactory:
    def __init__(self):
        self.cursos=[]
        self.cursos.append(Curso("ICF232", "Ingenieria de Software I",6))
        self.cursos.append(Curso("ICF121", "Introduccion a Ing. Civil Informatica ",6))
    
    def obtenerCursos(self):
        return self.cursos

    def getCurso(self,sigla):
        for curso in self.cursos:
            if curso.sigla==sigla:
                return curso
        return None
