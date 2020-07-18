# Create your views here.
from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from galeria.models import *

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        products_list = Product.objects.all()
        context = {
            'products': products_list,
        }
        return render(request, 'index.html', context=context)


# class HomeCursorView(LoginRequiredMixin, TemplateView):
#     def get(self, request, **kwargs):
#         cursoFactory=CursoFactory()
#         return render(request, '', {'': cursoFactory.obtenerCursos()})

    # def product_list(self, request,LoginRequiredMixin, TemplateView):
    #     products_list = Product.all()
    #     context = {
    #         'products': products_list,
    #     }
    #     return render(request, 'index.html', context)