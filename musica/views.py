from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Artista, EstadoAnimo
from django.urls import reverse_lazy
# Create your views here.


# --------- ARTISTA -------

class artistaPageView(ListView):
    template_name = 'artista.html'
    model = Artista
    context_object_name = 'Todo_Artista'


class artistaPageDetail(DetailView):
    template_name = 'artista_detalle.html'
    model = Artista
    context_object_name = 'Todo_Artista'


class artistaPageCreate(CreateView):
    template_name = 'artista_nuevo.html'
    model = Artista
    fields = "__all__"


class artistaPageUpdate(UpdateView):
    template_name = 'artista_editar.html'
    model = Artista
    fields = ['Generos', 'Ultimo_lanzamiento', 'Popular_semana']


class artistaPageDelete(DeleteView):
    template_name = 'artista_eliminar.html'
    model = Artista
    fields = "_all_"
    success_url = reverse_lazy('artista')

# -------------------- ESTADO DE ANIMO ---------------------


class estadoAnimPageView(ListView):
    template_name = 'estado_animo.html'
    model = EstadoAnimo
    context_object_name = 'Todo_EstadoAnim'


class estadoAnimPageDetail(DetailView):
    template_name = 'estado_animo_detalle.html'
    model = EstadoAnimo
    context_object_name = 'Todo_EstadoAnim'


class estadoAnimPageCreate(CreateView):
    template_name = 'estado_animo_nuevo.html'
    model = EstadoAnimo
    fields = "__all__"


class estadoAnimPageUpdate(UpdateView):
    template_name = 'estado_animo_editar.html'
    model = EstadoAnimo
    fields = ['Canciones', 'Artista_Esc']


class estadoAnimPageDelete(DeleteView):
    template_name = 'estado_animo_eliminar.html'
    model = EstadoAnimo
    fields = "_all_"
    success_url = reverse_lazy('estado_animo')

# --------------- LISTAS ----------------


class listasPageview(TemplateView):
    template_name = 'listas.html'
