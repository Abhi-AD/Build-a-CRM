from django.urls import path
from apps.leads.views import (
    IndexPageView,
    LeadListView,
    LeadDetailView,
    LeadCreateView,
    LeadUpdateView,
    LeadDeleteView,
    AssignAgentView,
)

app_name = "leads"
urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("lead/", LeadListView.as_view(), name="lead_list"),
    path("lead/<int:pk>/", LeadDetailView.as_view(), name="lead_detail"),
    path("lead/<int:pk>/update/", LeadUpdateView.as_view(), name="update_lead"),
    path("lead/<int:pk>/delete/", LeadDeleteView.as_view(), name="delete_lead"),
    path("lead/create/", LeadCreateView.as_view(), name="create_lead"),
    path("lead/<int:pk>/assign-agent/", AssignAgentView.as_view(), name="assign_agent"),
]
