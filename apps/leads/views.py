from django.shortcuts import render, redirect, reverse
from apps.leads.models import Lead, Agent
from apps.leads.forms import LeadForm, LeadModelForm
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class IndexPageView(generic.TemplateView):
    template_name = "index.html"


class LeadListView(generic.ListView):
    template_name = "leads/lead-list.html"
    queryset = Lead.objects.all()
    context_object_name = "leads"


class LeadDetailView(generic.DetailView):
    template_name = "leads/lead-detail.html"
    queryset = Lead.objects.all()
    context_object_name = "lead"


class LeadCreateView(generic.CreateView):
    template_name = "leads/create-lead.html"
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")


class LeadUpdateView(generic.UpdateView):
    template_name = "leads/lead-update.html"
    queryset = Lead.objects.all()
    form_class = LeadModelForm

    def get_success_url(self):
        return reverse("leads:lead_list")


class LeadDeleteView(generic.DeleteView):
    template_name = "leads/lead-delete.html"
    queryset = Lead.objects.all()
    

    def get_success_url(self):
        return reverse("leads:lead_list")
