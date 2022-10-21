from django.urls import path
from .views import artistaPageView, artistaPageDetail, artistaPageCreate, artistaPageUpdate, artistaPageDelete
from .views import estadoAnimPageView, estadoAnimPageDetail, estadoAnimPageCreate, estadoAnimPageUpdate, estadoAnimPageDelete, listasPageview
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('artista/', artistaPageView.as_view(), name='artista'),
    path('artista/<int:pk>', artistaPageDetail.as_view(), name='artista_detalle'),
    path('artista/nuevo', artistaPageCreate.as_view(), name='artista_nuevo'),
    path('artista/<int:pk>/editar/',
         artistaPageUpdate.as_view(), name='artista_editar'),
    path('artista/<int:pk>/eliminar/',
         artistaPageDelete.as_view(), name='artista_eliminar'),
    path('estado_animo', estadoAnimPageView.as_view(), name='estado_animo'),
    path('estado_animo/<int:pk>', estadoAnimPageDetail.as_view(),
         name='estado_animo_detalle'),
    path('estado_animo/nuevo', estadoAnimPageCreate.as_view(),
         name='estado_animo_nuevo'),
    path('estado_animo/<int:pk>/editar/',
         estadoAnimPageUpdate.as_view(), name='estado_animo_editar'),
    path('estado_animo/<int:pk>/eliminar/',
         estadoAnimPageDelete.as_view(), name='estado_animo_eliminar'),
    path('listas', listasPageview.as_view(), name='listas'),

]
