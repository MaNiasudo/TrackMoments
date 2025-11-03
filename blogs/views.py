from django.shortcuts import render
from django.urls import reverse_lazy
from scraper import goodreadscraper,traktscraper
from django.views.generic import CreateView , ListView , DeleteView , UpdateView
from .forms import IntegrationForm
from .models import Integration , Activity
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
# We get urls first and then pass them to scraper and save them in activity 
class IntegrationViewList(LoginRequiredMixin, ListView):
    model = Integration
    template_name = 'integration.html'
    context_object_name = 'integrations'
    # We use this context so only display specific User detail

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['integrations'] = context['integrations'].filter(user=self.request.user)
        return context
    
    # We made a form class with choices and we gonna get user webfor scrape and their url
class IntegrationAddView(LoginRequiredMixin, CreateView):
    model = Integration
    form_class = IntegrationForm
    template_name = 'add-integration.html'
    success_url = reverse_lazy('integ-list')

    def form_valid(self, form):
        integration.save()
        integration = form.save(commit=False)
        integration.user = self.request.user  # set current user
        integration.save()
        return super().form_valid(form)

class IntegrationUpdateView(LoginRequiredMixin, UpdateView):
    model = Integration
    form_class = IntegrationForm
    template_name = 'add-integration.html'
    success_url = reverse_lazy('integ-list')


class IntegrationDeleteView(LoginRequiredMixin, DeleteView):
    model = Integration
    template_name = 'delete-integration.html'
    success_url = reverse_lazy('integ-list')