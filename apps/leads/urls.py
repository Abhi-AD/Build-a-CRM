from django.urls import path
from apps.leads.views import (
    lead_list,
    lead_detail,
    create_lead,
    update_lead,
    delete_lead,
)

app_name = "leads"
urlpatterns = [
    path("lead/", lead_list, name="lead_list"),
    path("lead/<int:pk>/", lead_detail, name="lead_detail"),
    path("lead/<int:pk>/update/", update_lead, name="update_lead"),
    path("lead/<int:pk>/delete/", delete_lead, name="delete_lead"),
    path("lead/create/", create_lead, name="create_lead"),
]
