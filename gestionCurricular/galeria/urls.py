from django.conf.urls import url, re_path
from django.urls import path, include
from galeria import views

urlpatterns =[
    url(r'^$',views.HomePageView.as_view(), name="index"),
    # url(r'cursos/', views.HomeCursorView.as_view(), name="cursos"),
    # re_path(r'curso/(?P<sigla>ICF[0-9]{3})/$', views.DetalleCursoView.as_view(),name="detalle"),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls'))
]