from django.views.generic import TemplateView
from .models import Servico, Funcionario

class indexView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self, **kwargs):
        context = super(indexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.all()
        context['funcionarios']= Funcionario.objects.all()
        return context

