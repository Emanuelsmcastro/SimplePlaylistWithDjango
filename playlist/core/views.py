from django.forms.models import BaseModelForm
from django.http import HttpResponse, HttpRequest
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from core.models import Music

class HomeView(ListView):
    template_name= 'core/index.html'
    model = Music
    paginate_by = 5

class CreateMusicView(CreateView):
    template_name= 'core/form.html'
    model = Music
    fields = ['title', 'image', 'music']
    context_object_name = 'form'
    success_url = reverse_lazy('core:home')
    
    def form_valid(self, form):
        print('tst')
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        print('tsti')
        return super().form_invalid(form)
    
    