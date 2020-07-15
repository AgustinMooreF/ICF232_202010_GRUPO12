from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Curso, CursoFactory
from django.contrib.auth.mixins import LoginRequiredMixin

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

class HomeCursorView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        cursoFactory=CursoFactory()
        return render(request, 'cursos.html', {'cursos': cursoFactory.obtenerCursos()})
        
class DetalleCursoView(LoginRequiredMixin, TemplateView):
    def get(self, request, **kwargs):
        cursoFactory=CursoFactory()
        sigla=kwargs["sigla"]
        return render(request, 'curso.html', {'curso': cursoFactory.getCurso(sigla)})
