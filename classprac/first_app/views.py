from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from first_app import models
from django.urls import reverse_lazy
# def index_test(request):
#     dic={}
#     return HttpResponse('Hello World!')

class indexView(TemplateView):
    template_name = 'first_app/index1.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['s1'] = 'sameple text 1'
        context['s2'] = 'sample text 2'
        return context

class indexView2(ListView):
    context_object_name = 'Fighter_list'
    model = models.Fighter
    template_name = 'first_app/index1.html'

class FighterDetail(DetailView):
    context_object_name = 'fighter'
    model = models.Fighter
    template_name = 'first_app/fighter_details.html'

class AddFighter(CreateView):
    fields = ('first_name','last_name','style')
    model = models.Fighter
    template_name = 'first_app/fighter_form.html'
class UpdateFighter(UpdateView):
    fields = ('first_name','last_name','style')
    model = models.Fighter
    template_name = 'first_app/update_fighter.html'

class DeleteFighter(DeleteView):
    context_object_name = 'fighter'
    model = models.Fighter
    success_url = reverse_lazy("first_app:index")
    template_name = 'first_app/delete_fighter.html'
