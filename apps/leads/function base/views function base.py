from django.shortcuts import render, redirect
from apps.leads.models import Lead, Agent
from apps.leads.forms import LeadForm, LeadModelForm
from django.views import generic


# Create your views here.
def index(request):
    return render(request, "index.html")


class IndexPageView(generic.TemplateView):
    template_name = "landing.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect("dashboard")
        return super().dispatch(request, *args, **kwargs)


def lead_list(request):
    leads = Lead.objects.all()
    context = {"leads": leads}
    return render(request, "leads/lead-list.html", context)


def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {"lead": lead}
    return render(request, "leads/lead-detail.html", context)


def create_lead(request):
    form = LeadModelForm()

    if request.method == "POST":
        form = LeadModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("leads:lead_list")
    context = {"form": form}
    return render(request, "leads/create-lead.html", context)


def update_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    form = LeadModelForm(instance=lead)
    if request.method == "POST":
        form = LeadModelForm(request.POST, instance=lead)
        if form.is_valid():
            form.save()
            return redirect("leads:lead_list")
    context = {"form": form, "lead": lead}
    return render(request, "leads/lead-update.html", context)


def delete_lead(request, pk):
    lead = Lead.objects.get(id=pk)
    lead.delete()
    return redirect("leads:lead_list")


# def update_lead(request, pk):
#     lead = Lead.objects.get(id=pk)
#     form = LeadForm()
#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()
#             lead.first_name = first_name
#             lead.last_name = last_name
#             lead.age = age
#             lead.save()
#             return redirect("leads:lead_list")
#     context = {"form": form, "lead": lead}
#     return render(request, "leads/lead-update.html", context)


# def create_lead(request):
#     form = LeadForm()

#     if request.method == "POST":
#         form = LeadForm(request.POST)
#         if form.is_valid():
#             first_name = form.cleaned_data["first_name"]
#             last_name = form.cleaned_data["last_name"]
#             age = form.cleaned_data["age"]
#             agent = Agent.objects.first()
#             Lead.objects.create(
#                 first_name=first_name, last_name=last_name, age=age, agent=agent
#             )
#             return redirect("leads:lead_list")
#     context = {"form": form}
#     return render(request, "leads/create-lead.html", context)
